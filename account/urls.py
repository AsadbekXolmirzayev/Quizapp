from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [

    path('register/', views.AccountRegisterView.as_view()),
    path('login/', views.LoginView.as_view()),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('my-account/', views.MyAccountAPIView.as_view()),
    path('retrieve-update/<int:pk>/', views.AccountRetrieveUpdateView.as_view()),

]
