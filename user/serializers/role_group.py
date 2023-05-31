from rest_framework import serializers
from user.models import Role_group

class RoleGroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Role_group
        fields = "__all__"
