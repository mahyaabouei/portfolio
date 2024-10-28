from rest_framework import serializers
from django.contrib.auth import get_user_model
from . import models


class InformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Information
        fields = '__all__'


class HeroSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.HeroSection
        fields = '__all__'



class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Blog
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Project
        fields = '__all__'


class WorkExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.WorkExperience
        fields = '__all__'

