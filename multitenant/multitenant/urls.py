import debug_toolbar
from django.contrib import admin
from django.urls import path, include
from django.urls import path, re_path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Test API",
        default_version='v1',
        description="Welcome to the world",
        terms_of_service="https://www.test.org",
        contact=openapi.Contact(email="jason@test.org"),
        license=openapi.License(name="Awesome IP"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("__debug__/", include(debug_toolbar.urls)),
    re_path(r'^doc(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),  # <-- Here
    path('doc/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),  # <-- Here
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('', include('organisation.urls')),
    path('projects/', include('projects.urls')),

]
