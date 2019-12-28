from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions


class HelloApiView(APIView):
    """test API view"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
        'Uses HTTP methods as function (get, post, patch, delete)',
        'Is similar to a traditional Django View',
        'Gives you the most control over you application logic',
        'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apivew': an_apiview})

    def post(self, request):
        """Create Hello Message with my name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
             )

    def put(self, request, pk=None):
        """Handel updating an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handel a partial update of an object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """delete an object"""
        return Response({'method': 'DELETE'})



class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """return a hello message"""
        a_viewset = [
        'User actions (list, create,retrive,update, partial_update)',
        'automatically maps to URLs using Routers',
        'provide mor functioality with less code',
        ]

        return Response({'message': 'hello', 'a_viewset': a_viewset})

    def create(self, request):
        """create anew hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hallo {name}!'
            return Response({'message': message})
        else:
            return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )

    def retrive(self, request, pk=None):
        """handel getting an object by its ID"""
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """hendl updatting an object"""
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """hendel partioal updatting an object"""
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """hendel removing an object"""
        return Response({'http_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handel creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)
