from email.policy import default
from django.db import models


# Create your models here.
class Emp(models.Model):
    name = models.CharField(max_length=200)
    emp_id = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    working = models.BooleanField(default=True)
    department = models.CharField(max_length=200)

    # class Meta:
    #     # Specify the database alias to use
    #     using = 'default'

    def __str__(self):
        return self.name


class MailsForm(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=64)
    subject = models.CharField(max_length=64)
    message = models.TextField()
    created_on = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "email_notifications"
        verbose_name = "email notification"
        verbose_name_plural = "email notifications"

    def __str__(self):
        return self.email
