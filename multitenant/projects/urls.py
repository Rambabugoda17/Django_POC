from django.contrib import admin
from django.urls import path, include

from . import views
from .views import *

urlpatterns = [
    path("home/", views.emp_home),
    path("add-emp/", views.add_emp),
    path("delete-emp/<int:emp_id>", views.delete_emp),
    path("update-emp/<int:emp_id>", views.update_emp),
    path("email-emp/<int:emp_id>", SendMailView.as_view(), name="email form"),
    path("do-update-emp/<int:emp_id>", views.do_update_emp),
]
