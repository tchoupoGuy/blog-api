from django.urls import path, include
from rest_framework.routers import DefaultRouter

from tag import views


router = DefaultRouter()
router.register('tags', views.TagViewSet)

app_name = 'tag'

urlpatterns = [
    path('', include(router.urls))

]
