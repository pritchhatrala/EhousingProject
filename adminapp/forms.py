from django import forms
from django.contrib.auth.models import User
from myapp.models import *

class updatesellForm(forms.ModelForm):
    class Meta:
        model = add_sellhouse
        fields = "__all__"


class updaterentForm(forms.ModelForm):
    class Meta:
        model = add_renthouse
        fields = "__all__"


class updateComplaintForm(forms.ModelForm):
    class Meta:
        model = complaint
        fields = "__all__"