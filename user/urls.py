from django.urls import path

from user import views

from rest_framework_simplejwt import views as jwt_views

app_name = 'user'

urlpatterns = [
    path('auth/register/', views.CreateUserView.as_view(), name='create'),
    path('auth/token/obtain/',
         views.ObtainTokenPairWithUserView.as_view(), name='token_create'),
    path('auth/token/refresh/',
         jwt_views.TokenObtainPairView.as_view(), name='token_refresh'),
    path('auth/login/', views.CreateTokenView.as_view(), name='login'),
    path('', views.ManageUserView.as_view(), name='me')
]
