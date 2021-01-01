from django.urls import path

from user import views

app_name = 'user'

urlpatterns = [
    path('auth/register/', views.CreateUserView.as_view(), name='create'),
    path('auth/token/', views.CreateTokenView.as_view(), name='token'),
    path('auth/login/', views.CreateTokenView.as_view(), name='login'),
    path('', views.ManageUserView.as_view(), name='me')
]
