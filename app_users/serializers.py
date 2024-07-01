from rest_framework import serializers
from .models import Users


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Users
        fields = ('username', 'password')

    def create(self, validated_data):
        user = Users.objects.create(
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
