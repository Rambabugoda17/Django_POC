from django.forms import ModelForm

from .models import MailsForm


class EmailFormModelForm(ModelForm):
    class Meta:
        model = MailsForm
        fields = ["name", "email", "subject", "message"]
