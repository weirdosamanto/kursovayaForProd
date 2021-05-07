from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Select


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['username', 'email', 'practice', 'date', 'adress']

        widgets = {
            "username": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя Фамилия',
            }),
            "email": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email',
            }),
            "practice": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Выберите занятие',
            }),
            "date": DateTimeInput(attrs={
                'type': 'date',
                'class': 'form-control',
                'placeholder': 'Выберите Дату',
            }),
            "adress": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Выберите Адрес',
            }),
        }