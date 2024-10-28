from django.urls import path
from.views import InformationViewset , HeroSectionViewset,BlogViewset,ProjectViewset,WorkExperienceViewset

urlpatterns = [
    path('information/', InformationViewset.as_view(), name='information'),
    path('herosection/', HeroSectionViewset.as_view(), name='hero-section'),
    path('project/', ProjectViewset.as_view(), name='project'),
    path('blog/', BlogViewset.as_view(), name='blog'),
    path('work/experience/', WorkExperienceViewset.as_view(), name='work-experience'),
]