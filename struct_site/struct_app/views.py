from django.http import Http404
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.viewsets import ReadOnlyModelViewSet

from .serializers import *
from slugify import slugify


class GroupListView(ReadOnlyModelViewSet):
    serializer_class = GroupSerializer
    queryset = Group.objects.root_nodes()


class GroupDetailView(APIView):
    def get( self, request, tree_hierarchy ):
        group_id = request.query_params.get('group_id', None)
        group = self.GetGroup(group_id, tree_hierarchy)
        serializer = GroupDetailSerializer(group)
        return Response(serializer.data)

    def post( self, request, tree_hierarchy ):
        query = JSONParser().parse(request)
        query[ 'slug' ] = slugify(query[ 'title' ])
        serialize_data = GroupDetailSerializer(data=query)
        return SaveData(serialize_data)

    def put( self, request, tree_hierarchy ):
        query = JSONParser().parse(request)
        query[ 'slug' ] = slugify(query[ 'title' ])
        group_id = query[ 'id' ]
        group = self.GetGroup(group_id, tree_hierarchy)
        serialize_data = GroupDetailSerializer(group, data=query)
        return SaveData(serialize_data)

    def delete( self, request, tree_hierarchy ):
        group_id = request.query_params.get('group_id', None)
        group = self.GetGroup(group_id, tree_hierarchy)
        group.delete()
        if Group.objects.filter(id=group_id).count() == 0:
            return Response(
                {'Успешно удалено'},
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {'Ошибка удаления'},
                status=status.HTTP_400_BAD_REQUEST
            )

    def GetGroup( self, group_id, tree_hierarchy ):
        try:
            if group_id is None:
                group = self.FindGroup(tree_hierarchy)
            else:
                group = Group.objects.get(id=group_id)
            return group
        except Group.DoesNotExist:
            raise Http404

    def FindGroup( self, tree_hierarchy ):
        category_slug = tree_hierarchy.split('/')
        parent = None
        root = Group.objects.all()
        for slug in category_slug[ :-1 ]:
            parent = root.get(parent=parent, slug=slug)
        group = root.get(parent=parent, slug=category_slug[ -1 ])
        return group


class EmployeeListView(APIView):
    def get( self, request ):
        group_id = request.query_params.get('group_id', None)
        queryset = self.GetEmployees(group_id)
        serializer = EmployeeSerializer(queryset, many=True, context={"request": request})
        return Response(serializer.data)

    def post( self, request ):
        query = self.CheckImage(request.data)
        serialize_data = EmployeeSerializer(data=query)
        return SaveData(serialize_data)

    def put( self, request ):
        query = self.CheckImage(request.data)
        employee_id = query[ 'id' ]
        employee = self.GetEmployee(employee_id)
        serialize_data = EmployeeSerializer(employee, data=query)
        return SaveData(serialize_data)

    def delete( self, request ):
        employee_id = request.query_params.get('id', None)
        employee = self.GetEmployee(employee_id)
        employee.delete()
        if Employee.objects.filter(id=employee_id).count() == 0:
            return Response(
                {'Успешно удалено'},
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {'Ошибка удаления'},
                status=status.HTTP_400_BAD_REQUEST
            )

    def CheckImage( self, query ):
        if query[ 'image' ] == 'default':
            query = query.copy()
            del query[ 'image' ]
        return query

    def GetEmployee( self, employee_id ):
        try:
            employee = Employee.objects.get(id=employee_id)
            return employee
        except Employee.DoesNotExist:
            raise Http404

    def GetEmployees( self, group_id ):
        try:
            queryset = Employee.objects.filter(group=group_id)
            return queryset
        except Employee.DoesNotExist:
            raise Http404


def SaveData( serialize_data ):
    if serialize_data.is_valid():
        serialize_data.save()
        return Response("Данные сохранены", status=status.HTTP_200_OK)
    else:
        return Response(
            serialize_data.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
