from django.urls import path, include
from rest_framework import routers
from .import views 

router = routers.DefaultRouter()
router.register('Industry', views.IndustryViewSet)
router.register('Company', views.CompanyViewSet)
router.register('Person', views.PersonViewSet)

  
urlpatterns = [  
    path('', include(router.urls)),
   
]