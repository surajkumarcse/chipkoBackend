from django.urls import path
from . import views

urlpatterns = [
    path('', views.collectFeed, name='collectFeed'),
    path('organisationProfile', views.cauverycalling, name='organisationProfile'),
    path('organisationProfile2', views.teamtrees, name='organisationProfile2'),
    
 ]