from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from .views import ProfileView

urlpatterns = [
    path('', views.get_employees, name="index"),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("profile", ProfileView.as_view(), name="profile"),
    path("logout", views.logout_request, name="logout"),
    path("all", views.EmployeeListAPIView.as_view(), name="all"),
    path("projects/all", views.ProjectsListAPIView.as_view(), name="projects"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
