import datetime
from . import serializers
from . import models 
from rest_framework import status 
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponse, HttpResponseNotAllowed



class InformationViewset(APIView):
    def get (self,request, *args, **kwargs) :
        domain = request.query_params.get('domain', '').strip()
        if domain is None :
            return Response ({'message' : 'Invalid Domain'},status=status.HTTP_404_NOT_FOUND)
        domain = models.Domain.objects.filter(domain = domain).first()
        if not domain :
            return Response ({'message' : 'Domain not found'},status=status.HTTP_404_NOT_FOUND)
        information = models.Information.objects.filter(domain = domain).first()
        if not information :
            return Response ({'message' : 'Information Not Found'},status=status.HTTP_400_BAD_REQUEST)
        serializer = serializers.InformationSerializer (information)
        return Response (serializer.data,status=status.HTTP_200_OK)
        
        
class HeroSectionViewset (APIView) :
    def get (self,request, *args, **kwargs) :
        domain = request.query_params.get('domain', '').strip()
        if domain is None :
            return Response ({'message' : 'Invalid Domain'},status=status.HTTP_404_NOT_FOUND)
        domain = models.Domain.objects.filter(domain = domain).first()
        if not domain :
            return Response ({'message' : 'Domain not found'},status=status.HTTP_404_NOT_FOUND)
        hero_section = models.HeroSection.objects.filter(domain = domain).first()
        if not hero_section :
            return Response ({'message' : 'hero_section Not Found'},status=status.HTTP_400_BAD_REQUEST)
        serializer = serializers.HeroSectionSerializer(hero_section)
        return Response (serializer.data,status=status.HTTP_200_OK)
        
        
class BlogViewset (APIView) :
    def get (self,request, *args, **kwargs) :
        domain = request.query_params.get('domain', '').strip()
        if domain is None :
            return Response ({'message' : 'Invalid Domain'},status=status.HTTP_404_NOT_FOUND)
        domain = models.Domain.objects.filter(domain = domain).first()
        if not domain :
            return Response ({'message' : 'Domain not found'},status=status.HTTP_404_NOT_FOUND)
        blog = models.Blog.objects.filter(domain = domain).first()
        if not blog :
            return Response ({'message' : 'blog Not Found'},status=status.HTTP_400_BAD_REQUEST)
        serializer = serializers.BlogSerializer(blog)
        return Response (serializer.data,status=status.HTTP_200_OK)
                
class ProjectViewset (APIView) :
    def get (self,request, *args, **kwargs) :
        domain = request.query_params.get('domain', '').strip()
        if domain is None :
            return Response ({'message' : 'Invalid Domain'},status=status.HTTP_404_NOT_FOUND)
        domain = models.Domain.objects.filter(domain = domain).first()
        if not domain :
            return Response ({'message' : 'Domain not found'},status=status.HTTP_404_NOT_FOUND)
        project = models.Project.objects.filter(domain = domain).first()
        if not project :
            return Response ({'message' : 'project Not Found'},status=status.HTTP_400_BAD_REQUEST)
        serializer = serializers.ProjectSerializer(project)
        return Response (serializer.data,status=status.HTTP_200_OK)
                      
class WorkExperienceViewset (APIView) :
    def get (self,request, *args, **kwargs) :
        domain = request.query_params.get('domain', '').strip()
        if domain is None :
            return Response ({'message' : 'Invalid Domain'},status=status.HTTP_404_NOT_FOUND)
        domain = models.Domain.objects.filter(domain = domain).first()
        if not domain :
            return Response ({'message' : 'Domain not found'},status=status.HTTP_404_NOT_FOUND)
        work_experience = models.WorkExperience.objects.filter(domain = domain).first()
        if not work_experience :
            return Response ({'message' : 'work_experience Not Found'},status=status.HTTP_400_BAD_REQUEST)
        serializer = serializers.WorkExperienceSerializer(work_experience)
        return Response (serializer.data,status=status.HTTP_200_OK)
        
        