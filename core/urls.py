"""
URL configuration for core project.
"""


from django.contrib import admin
from django.urls import path, re_path, include

from django.conf.urls.static import static
from django.conf import settings
from rest_framework.permissions import AllowAny

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title='Bizzbot API',
        default_version='v1',
        description='API Documentation for the Bizzbot Application',
        contact=openapi.Contact(email="support@bizzbot.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(AllowAny,)
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),

    # swagger/redoc
    re_path('^api/swagger(?P<format>\.json|\.yaml)', schema_view.without_ui(), name='schema-json'),
    re_path('^api/swagger/?$', schema_view.with_ui('swagger'), name='schema-swagger'),
    re_path('^api/redoc/?$', schema_view.with_ui('redoc'), name='schema-redoc'),

    *static(settings.STATIC_URL, document_root=settings.STATIC_ROOT),
]
