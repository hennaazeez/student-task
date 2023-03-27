from django import forms
from django.contrib.auth.forms import UserCreationForm

from st_app.models import Login, studentregister, Complaint, Notification


class Login_form(UserCreationForm):
    class Meta:
        model=Login
        fields = ("username","password1","password2")


class register_form1(forms.ModelForm):
    class Meta:
        model = studentregister
        fields ='__all__'
        exclude=('user',)


class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ('__all__')
        exclude = ('status','reply',)

class NotificationForm(forms.ModelForm):
    class Meta:
        model = Notification
        fields = ('__all__')
        exclude = ('reply',)