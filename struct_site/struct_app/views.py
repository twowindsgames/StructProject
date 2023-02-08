from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from slugify import slugify


class GroupListView(APIView):
    def get(self, request):
        groups = Group.objects.root_nodes()
        serializer = GroupSerializer(groups, many=True)
        return Response(serializer.data)


class GroupDetailView(APIView):
    def get(self, request, tree_hierarchy):
        group_id = request.query_params.get('group_id', None)
        if group_id is None:
            category_slug = tree_hierarchy.split('/')
            parent = None
            root = Group.objects.all()
            for slug in category_slug[:-1]:
                parent = root.get(parent=parent, slug=slug)

            group = root.get(parent=parent, slug=category_slug[-1])

        else:
            group = Group.objects.get(group_id)

        serializer = GroupDetailSerializer(group)
        return Response(serializer.data)

    def post(self, request, tree_hierarchy):

        query = JSONParser().parse(request)

        query['slug'] = slugify(query['title'])
        serialize_data = GroupDetailSerializer(data=query)
        if serialize_data.is_valid():
            serialize_data.save()
            return Response("Added Successfully")
        else:
            return Response("Added Error")

    def put(self, request, tree_hierarchy):
        query = JSONParser().parse(request)
        query['slug'] = slugify(query['title'])
        group_id = query['id']
        group = Group.objects.get(id=group_id)
        serialize_data = GroupDetailSerializer(group, data=query)
        if serialize_data.is_valid():
            serialize_data.save()
            return Response("Added Successfully")
        else:
            return Response("Added Error")

    def delete(self, request, tree_hierarchy):
        group_id = request.query_params.get('group_id', None)
        group = Group.objects.get(id=group_id)
        group.delete()
        if Group.objects.filter(id=group_id) is None:
            return Response("Delete Successfully")
        else:
            return Response("Delete Error")


class EmployeeListView(APIView):
    def get(self, request):

        group_id = request.query_params.get('group_id', None)
        queryset = Employee.objects.filter(group=group_id)
        serializer = EmployeeSerializer(queryset, many=True, context={"request": request})
        return Response(serializer.data)

    def post(self, request):
        query = request.data
        if query['image'] == 'default':
            query = query.copy()
            del query['image']

        serialize_data = EmployeeSerializer(data=query)
        if serialize_data.is_valid():
            serialize_data.save()
            return Response("Added Successfully")
        else:
            return Response("Added Error")

    def put(self, request):
        query = JSONParser().parse(request)
        employee_id = query['id']
        employee = Employee.objects.get(id=employee_id)
        serialize_data = EmployeeSerializer(employee, data=query)
        if serialize_data.is_valid():
            serialize_data.save()
            return Response("Added Successfully")
        else:
            return Response("Added Error")

    def delete(self, request):
        employee_id = request.query_params.get('id', None)
        employee = Employee.objects.get(id=employee_id)
        employee.delete()
        if Group.objects.filter(id=employee_id) is None:
            return Response("Delete Successfully")
        else:
            return Response("Delete Error")
