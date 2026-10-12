from rest_framework.serializers import ModelSerializer
from .models import Category, Job, Comment
from rest_framework import serializers
from django.contrib.auth.models import User

class CategorynameSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']

class CategorydetailSerializer(ModelSerializer):
    jobs = serializers.StringRelatedField(many=True)
    class Meta:
        model = Category
        fields = ['name', 'jobs']

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ['comment']

class JobSerializer(ModelSerializer):
    category = CategorynameSerializer(read_only=True)
    comment = CommentSerializer(many=True, read_only=True, source='comment_set')
    class Meta:
        model = Job
        fields = "__all__"

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)





    # students = serializers.StringRelatedField(many=True)
    # students = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # students = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name="talaba-detail")
    # students = serializers.SlugRelatedField(many=True, read_only=True, slug_field="full_name")
    # url = serializers.HyperlinkedIdentityField(view_name="course-detail")
























