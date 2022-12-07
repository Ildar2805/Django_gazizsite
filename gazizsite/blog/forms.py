from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from captcha.fields import CaptchaField

from .models import *


class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = 'Категория не выбрана'

    class Meta:
        model = Post
        fields = ['title', 'slug', 'content', 'image', 'source', 'is_published', 'cat']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Введите заголовок'}),
            'slug': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Введите URL'}),
            'content': forms.Textarea(attrs={'class': 'form-input', 'placeholder': 'Введите содержание', 'rows': 10}),
            'source': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Введите источник'}),
        }

    #добавляем пользовательские валидаторы, которые действуют после стандартных is_valid and save()
    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError('Дина превышает 200 символов')
        return title


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class ContactForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=255, widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    content = forms.CharField(label='Содержание', widget=forms.Textarea(attrs={'cols': 60, 'rows': 10, 'class': 'form-input'}))
    captcha = CaptchaField(label='Проверка')


#Форма, не связанная с моделью
# class AddPostForm(forms.Form):
#     title = forms.CharField(max_length=255, label='Заголовок', widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Введите заголовок'}))
#     slug = forms.SlugField(max_length=255, label='URL', widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Введите URL'}))
#     content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10, 'class': 'form-input', 'placeholder': 'Введите содержание'}), label='Содержание')
#     source = forms.URLField(label='Источник', widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Введите источник'}))
#     is_published = forms.BooleanField(label='Публикация', required=False, initial=True)
#     cat = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория', empty_label='Категория не выбрана')