import json

from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, status
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from datamanagement.models import ChildData, Organisations
from datamanagement.serialisers import ChildDataSerialiser


class ChildViewSet(viewsets.ModelViewSet):
    queryset = ChildData.objects.all()
    serializer_class = ChildDataSerialiser

    @detail_route(methods=['get'])
    def add_to_school(self, request, pk):
        child = get_object_or_404(ChildData, pk=pk)
        organisation = get_object_or_404(Organisations, code=request.GET.get("school"))
        if organisation.type != "school":
            return Response(status=status.HTTP_400_BAD_REQUEST, data=f"{organisation.name}Not a school")
        if organisation.incharge != request.user:
            return Response(status=status.HTTP_400_BAD_REQUEST, data="Unauthorised request")
        child.school = organisation
        child.save()
        return Response(status=status.HTTP_200_OK)

