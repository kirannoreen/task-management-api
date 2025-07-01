# backend/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from accounts.views import UserViewSet, CustomTokenObtainPairView  # Custom JWT view
from projects.views import ProjectViewSet, TaskViewSet
from rest_framework_simplejwt.views import TokenRefreshView

# Initialize the router for viewsets
router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')  # Register UserViewSet
router.register(r'projects', ProjectViewSet, basename='projects')  # Register ProjectViewSet
router.register(r'tasks', TaskViewSet, basename='tasks')  # Register TaskViewSet

# Define URL patterns
urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel URL
    path('api/', include(router.urls)),  # Include the viewset routes under /api/

    # JWT Authentication endpoints
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),  # Custom token obtain view
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Refresh token view
]
