from django.urls import path, include
from rest_framework.routers import DefaultRouter

from my_blog import views


router = DefaultRouter()
router.register('tags', views.TagViewSet)

app_name = 'my_blog'

urlpatterns = [
    path('', include(router.urls))

]
