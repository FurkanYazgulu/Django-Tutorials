from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CustomRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, label="İsim")
    last_name = forms.CharField(max_length=30, required=True, label="Soyisim")
    student_class = forms.CharField(max_length=50, required=True, label="Sınıf")

    class Meta(UserCreationForm.Meta):
        model = User
        # Kayıt ekranında görünecek alanların sırası
        fields = ('username', 'first_name', 'last_name')
        labels = {
            'username': 'Kullanıcı Adı (Öğrenci No)',
        }