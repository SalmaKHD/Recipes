from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from rest_framework.views import APIView

from Recipe import serializers


# Create your views here.

class ListApiView(APIView):
    # specify what inputs to expect for methods that accept data
    serializer_class = serializers.ListSerializer

    def get(self, request, format=None):
        list = ['something']
        return Response({'list': list}) # return Json response

    def post(self, request):
        # needs a serializer to post
        # deserialize data
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hi {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        ''' replaces object with new object '''
        return Response({'method': 'put'})

    def patch(self, request, pk=None):
        ''' partial update to fields '''
        return Response({'method': 'patch'})

    def delete(self, request, pk=None):
        return Response({'method': 'delete'})


class BaseViewSet(viewsets.ViewSet):
    ''' for typical actions performed with APIs '''

    serializer_class = serializers.ListSerializer

    def list(self, request):
        list = ['something']
        return Response({'message': 'Hello'})

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response(message, status=HTTP_200_OK)
        else:
            return Response(serializer.errors, HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        return Response({'method': 'GET'})

    def update(self, request, pk=None):
        return Response({'method': 'PUT'})

    def partial_update(self, request, pk=None):
        return Response({'method': 'PATCH'})

    def destroy(self, request, pk=None):
        return Response({'method': 'DELETE'})
