from django.urls import path
from rest_framework import routers
from .views import UserViewSet, OrderViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)



router = routers.SimpleRouter()
router.register(r'users', UserViewSet)
router.register(r'orders', OrderViewSet, basename="orders")
urlpatterns = [
       path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] + router.urls
