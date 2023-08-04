from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from .dto import CustomResponse, CustomResponseSerializer
from .models import Employee

from .forms import NewUserForm
from .models import Employee, Technologies, Projects
from .serializers import EmployeeSerializer, ProjectsSerializer


# Create your views here.

def get_Employees(request):
    employees = Employee.objects.all()
    context = {
        'employees': employees
    }
    return render(request, 'index.html', context)


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("login")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="register.html", context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("profile")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("index")


# @login_required
# def profile(request):
#     logged_in_user = request.user.id
#     proj = Projects.objects.filter(projects__icontains='Titans', user_id=logged_in_user)
#     if request.method == 'POST':
#         p_form = NewUserForm(request.POST,
#                              request.FILES,
#                              instance=request.user.profile)
#
#         if p_form.is_valid():
#             p_form = Employee.objects.all()
#             p_form.save()
#             messages.success(request, f'Your account has been updated!')
#             return redirect('profile')
#
#     else:
#         p_form = None
#
#     context = {
#         'p_form': p_form,
#         'projects': list(proj)
#
#     }

# return render(request, 'profile.html', context)


#
class ProfileView(LoginRequiredMixin, View):
    serializer_class = EmployeeSerializer

    # @login_required
    def get(self, request):
        logged_in_user = request.user.id
        proj = Projects.objects.filter(projects__icontains='Titans', user_id=logged_in_user)
        context = {
            'p_form': None,
            'projects': list(proj)
        }
        return render(request, 'profile.html', context)

    def post(self, request):
        p_form = NewUserForm(request.POST, request.FILES, instance=request.user.profile)
        if p_form.is_valid():
            p_form = Employee.objects.all()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')


class EmployeePagination(PageNumberPagination):
    page_size = 2


#

class EmployeeListAPIView(ListAPIView):
    # throttle_scope = 'employees'
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    model = Employee
    pagination_class = EmployeePagination


class ProjectsListAPIView(ListAPIView):
    serializer_class = ProjectsSerializer
    model = Projects

    def get(self, request, **kwargs):
        data = Projects.objects.all()
        serializer = ProjectsSerializer(data, many=True)
        response = CustomResponse(serializer.data)
        # response_serializer = CustomResponseSerializer(response)
        return Response(data=response.data)
