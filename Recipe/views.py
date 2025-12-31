from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
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