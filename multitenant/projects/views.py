from django.shortcuts import redirect, render
from django.views.generic import FormView

from .forms import EmailFormModelForm
from .models import Emp
from .tasks import send_email_task


def emp_home(request):
    emps = Emp.objects.all()
    return render(request, "home.html", {'emps': emps})


def add_emp(request):
    if request.method == "POST":
        emp_name = request.POST.get("emp_name")
        emp_id = request.POST.get("emp_id")
        emp_phone = request.POST.get("emp_phone")
        emp_address = request.POST.get("emp_address")
        emp_working = request.POST.get("emp_working")
        emp_department = request.POST.get("emp_department")
        e = Emp()
        e.name = emp_name
        e.emp_id = emp_id
        e.phone = emp_phone
        e.address = emp_address
        e.department = emp_department
        if emp_working is None:
            e.working = False
        else:
            e.working = True
        e.save()
        return redirect("/projects/home")
    return render(request, "add-emp.html", {})


def delete_emp(request, emp_id):
    emp = Emp.objects.get()
    emp.delete()
    return redirect("/projects/home")


def update_emp(request, emp_id):
    emp = Emp.objects.get()
    print("Yes Bhai")
    return render(request, "update_emp.html", {
        'emp': emp
    })


def email_emp(request, emp_id):
    emp = Emp.objects.get()
    return render(request, "send_email.html", {
        'email': emp.email
    })


def do_update_emp(request, emp_id):
    if request.method == "POST":
        emp_name = request.POST.get("emp_name")
        emp_id_temp = request.POST.get("emp_id")
        emp_phone = request.POST.get("emp_phone")
        emp_address = request.POST.get("emp_address")
        emp_working = request.POST.get("emp_working")
        emp_department = request.POST.get("emp_department")

        e = Emp.objects.get()

        e.name = emp_name
        e.emp_id = emp_id_temp
        e.phone = emp_phone
        e.address = emp_address
        e.department = emp_department
        if emp_working is None:
            e.working = False
        else:
            e.working = True
        e.save()
    return redirect("/projects/home")


class SendMailView(FormView):
    form_class = EmailFormModelForm
    template_name = "send_email.html"
    success_url = "/"

    def get_initial(self):
        """
        Returns the initial data to use for forms on this view.
        """
        initial = super().get_initial()
        emp_id = self.kwargs["emp_id"]
        emp = Emp.objects.get(id=emp_id)
        initial['email'] = emp.email
        return initial

    def form_valid(self, form):
        form.save()
        self.send_email(form.cleaned_data)

        return super().form_valid(form)

    def send_email(self, valid_data):
        email = valid_data["email"]
        subject = "Send email form sent from website"
        message = (
            f"You have received a contact form.\n"
            f"Email: {valid_data['email']}\n"
            f"Name: {valid_data['name']}\n"
            f"Subject: {valid_data['subject']}\n"
            f"{valid_data['message']}\n"
        )
        send_email_task.delay(
            email, subject, message,
        )

