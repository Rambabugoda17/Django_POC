from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_Employees, name="index"),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("profile", views.profile, name="profile"),
    path("logout", views.logout_request, name="logout"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)