from rest_framework import serializers
from . import models


class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Posts
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comments
        fields = '__all__'
