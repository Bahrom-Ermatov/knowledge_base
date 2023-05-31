from rest_framework import serializers
from user.models import User_role

class UserRoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = User_role
        fields = "__all__"
