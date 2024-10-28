from django.db import models
from django.utils.timezone import now
import datetime


class Domain(models.Model):
    name = models.CharField(max_length=255)
    domain = models.CharField(max_length=64, unique=True)
    createat = models.DateTimeField (auto_now_add=True)
    class Meta:
        verbose_name = "Domain"
        verbose_name_plural = "Domains "
    def __str__(self):
        return self.name+ '(' + self.domain+')'



class Information(models.Model):
    domain = models.ForeignKey(Domain ,  to_field='domain' , on_delete = models.CASCADE)
    name = models.CharField(max_length=250 , null= True , blank= True)
    logo = models.FileField(upload_to='static/images/logo')
    telephone = models.CharField (max_length=15 , null= True , blank= True)
    email = models.EmailField(null= True , blank= True)
    address = models.CharField(max_length=1000 , null= True , blank= True)
    social_media = models.JSONField(null=True, blank=True)
    
    class Meta:
        verbose_name = "Information"
        verbose_name_plural = "Information"
    def __str__(self):
        return str(self.domain)
class HeroSection(models.Model):
    domain = models.ForeignKey(Domain , to_field='domain' , on_delete=models.CASCADE)
    title = models.CharField(max_length=5000 , null= True , blank= True)
    text = models.CharField(max_length=5000 , null= True , blank= True)
    picture_3d = models.FileField(upload_to='static/images/3dmodel' , null= True , blank=True)
    class Meta:
        verbose_name = "HeroSection"
        verbose_name_plural = "HeroSection"
    def __str__(self):
        return str(self.domain)
class Blog (models.Model):
    domain = models.ForeignKey(Domain , to_field='domain' , on_delete=models.CASCADE)
    picture = models.FileField(upload_to='static/images/picture' , null= True , blank=True)
    title = models.CharField(max_length=5000 , null= True , blank= True)
    description = models.CharField(max_length=5000 , null= True , blank= True)
    
    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blog"
    def __str__(self):
        return str(self.domain)
    
class Project (models.Model) :
    domain = models.ForeignKey(Domain , to_field='domain' , on_delete=models.CASCADE)
    title = models.CharField(max_length=5000 , null= True , blank= True)
    logo = models.FileField(upload_to='static/images/logo' , null= True , blank=True)
    picture = models.FileField(upload_to='static/images/picture' , null= True , blank=True)
    video = models.FileField(upload_to='static/images/picture' , null= True , blank=True)
    link = models.CharField(max_length=5000 , null= True , blank= True)
    description = models.CharField(max_length=5000 , null= True , blank= True)
    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Project"
    def __str__(self):
        return str(self.domain)
class WorkExperience (models.Model):
    domain = models.ForeignKey(Domain , to_field='domain' , on_delete=models.CASCADE)
    picture = models.FileField(upload_to='static/images/picture' , null= True , blank=True)
    title = models.CharField(max_length=5000 , null= True , blank= True)
    description = models.CharField(max_length=5000 , null= True , blank= True)
    picture_3d = models.FileField(upload_to='static/images/3dmodel' , null= True , blank=True)
    date = models.DateTimeField(default=datetime.datetime.now())
    postion = models.CharField(max_length=200 , null= True , blank= True)
    
    class Meta:
        verbose_name = "WorkExperience"
        verbose_name_plural = "WorkExperience"
    def __str__(self):
        return str(self.domain)