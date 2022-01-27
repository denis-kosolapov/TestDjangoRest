from rest_framework import serializers
from .models import Users

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'first_name', 'last_name', 'gender', 'age')

class UserDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault)

    class Meta:
        model = Users
        fields = '__all__'