import json

from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, status
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response

from datamanagement.models import ChildData, Organisations
from datamanagement.serialisers import ChildDataSerialiser


class ChildViewSet(viewsets.ModelViewSet):
    queryset = ChildData.objects.all()
    serializer_class = ChildDataSerialiser

    def create(self, request, *args, **kwargs):
        organisation = get_object_or_404(Organisations, pk=int(request.data.get("registered_by")))
        if organisation.type not in {"hospital", "anganwadi"}:
            return Response(status=status.HTTP_401_UNAUTHORIZED, data="Children can either be added by Hospitals or Anganwadis")
        if request.user != organisation.incharge:
            return Response(status=status.HTTP_401_UNAUTHORIZED, data="Unauthorised request")
        return super(ChildViewSet, self).create(request, *args, **kwargs)

    @detail_route(methods=['post'])
    def add_child(self, request, pk):
        child = get_object_or_404(ChildData, pk=pk)
        organisation = get_object_or_404(Organisations, code=request.data.get("organisation"))
        if organisation.type != request.data.get("to"):
            return Response(status=status.HTTP_400_BAD_REQUEST, data=f"{organisation.name} is not a {request.data.get('to')}")
        if organisation.incharge != request.user:
            return Response(status=status.HTTP_401_UNAUTHORIZED, data="Unauthorised request")
        if request.data.get("to") == "school":
            child.school = organisation
            child.enrolled_in_school = True
        elif request.data.get("to") == "orphanage":
            child.orphanage = organisation
            child.enrolled_in_orphanage = True
        child.save()
        return Response(status=status.HTTP_200_OK)

    @list_route(methods=["get"])
    def uneducated(self, request):
        data = ChildData.objects.filter(enrolled_in_school=False)
        serialised = ChildDataSerialiser(data, many=True)
        return Response(serialised.data)

    @list_route(methods=["get"])
    def unsheltered(self, request):
        data = ChildData.objects.filter(is_orphan=True, enrolled_in_orphanage=True)
        serialised = ChildDataSerialiser(data, many=True)
        return Response(serialised.data)

