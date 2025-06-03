from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import UserSubmission

class RegisterForm(UserCreationForm):
    email = forms.EmailField(label="البريد الإلكتروني")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
            'username': 'اسم المستخدم',
            'email': 'البريد الإلكتروني',
            'password1': 'كلمة المرور',
            'password2': 'تأكيد كلمة المرور',
        }

class SubmissionForm(forms.ModelForm):
    class Meta:
        model = UserSubmission
        fields = ['title', 'description', 'image']
        labels = {
            'title': 'عنوان العمل',
            'description': 'وصف العمل',
            'image': 'صورة العمل',
        }

class ArabicLoginForm(AuthenticationForm):
    username = forms.CharField(label='اسم المستخدم')
    password = forms.CharField(label='كلمة المرور', widget=forms.PasswordInput)
    error_messages = {
        'invalid_login': "اسم المستخدم أو كلمة المرور غير صحيحة. تأكد من المدخلات.",
        'inactive': "هذا الحساب غير مفعل.",
    }
