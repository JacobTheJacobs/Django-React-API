from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from .views import MovieViewSet,RatingViewSet,UserViewSet


router=routers.DefaultRouter()

router.register('users', UserViewSet, 'users')
router.register('movies', MovieViewSet, 'movies')
router.register('ratings', RatingViewSet, 'ratings')


urlpatterns = [
    path('', include(router.urls)),
]
