from rest_framework import generics
from .serializer import UserListSerializer, UserDetailSerializer
from .models import Users

class UserCreateView(generics.CreateAPIView):
    serializer_class = UserDetailSerializer

class UsersListView(generics.ListAPIView):
    serializer_class = UserListSerializer
    queryset = Users.objects.all()

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserDetailSerializer
    queryset = Users.objects.all()
