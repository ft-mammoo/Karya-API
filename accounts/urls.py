from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import SignupView

urlpatterns = [
    # Signup endpoint
    path('signup/', SignupView.as_view(), name='signup'),
    # Signin endpoint (Using SimpleJWT's inbuilt view)
    path('signin/', TokenObtainPairView.as_view(), name='signin'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]