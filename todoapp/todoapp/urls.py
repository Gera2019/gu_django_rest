"""todoapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from mainapp.views import ProjectModelViewSet, TodoNoteModelViewSet, TodoUserCustomViewSet, TodoUserModelView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view

# schema_view = get_schema_view(
#    openapi.Info(
#       title="ToDoNotes",
#       default_version='0.1',
#       description="Documentation to out project",
#       contact=openapi.Contact(email="admin@admin.local"),
#       license=openapi.License(name="MIT License"),
#    ),
#    public=True,
#    permission_classes=[permissions.AllowAny],
# )

router = DefaultRouter()
router.register('users', TodoUserCustomViewSet, basename='user')
router.register('projects', ProjectModelViewSet, basename='project')
router.register('notes', TodoNoteModelViewSet, basename='TodoNote')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('viewsets/', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
    # re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    # path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('openapi', get_schema_view(
            title="ToDo Note",
            description="API for all things …",
            version="0.1"
        ), name='openapi-schema'),
    path('swagger-ui/', TemplateView.as_view(
            template_name='swagger-ui.html',
            extra_context={'schema_url':'openapi-schema'}
        ), name='swagger-ui'),

    path('redoc/', TemplateView.as_view(
            template_name='redoc.html',
            extra_context={'schema_url':'openapi-schema'}
        ), name='redoc'),
]

