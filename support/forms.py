from django import forms
from .models import Users, UsersIdentificationphotos, Events, Headbands
from django.contrib.auth.models import User


# class UserRegistrationForm(forms.ModelForm):
#     password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'Введите ваш пароль'}))
#     password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput(attrs={'placeholder': 'Введите ваш пароль повторно'}))
#
#     class Meta:
#         model = User
#         fields = ('username', 'first_name', 'email', 'last_name')
#         widgets = {
#             'email': forms.EmailInput(attrs={'placeholder': 'Введите вашу почту'}),
#             'first_name' : forms.TextInput(attrs={'placeholder': 'Введите ваше имя'}),
#             'last_name': forms.TextInput(attrs={'placeholder': 'Введите вашу фамилию'}),
#             'username': forms.TextInput(attrs={'placeholder': 'Введите ваш никнейм'}),
#         }
#
#     def clean_password2(self):
#         cd = self.cleaned_data
#         if cd['password'] != cd['password2']:
#             raise forms.ValidationError('Passwords don\'t match.')
#         return cd['password2']


class AddUserPhotoForm(forms.ModelForm):

    class Meta:
        model = UsersIdentificationphotos
        fields = ('identification_photo_1', 'identification_photo_2')
        widgets = {
            'identification_photo_1': forms.FileInput(attrs={'placeholder': 'Добавьте файл'}),
            'identification_photo_2': forms.FileInput(attrs={'placeholder': 'Добавьте файл'}),
        }


class ChangeUserPhotoForm(forms.ModelForm):

    class Meta:
        model = UsersIdentificationphotos
        fields = ('identification_photo_1', 'identification_photo_2')
        widgets = {
            'identification_photo_1': forms.FileInput(attrs={'placeholder': 'Добавьте файл'}),
            'identification_photo_2': forms.FileInput(attrs={'placeholder': 'Добавьте файл'}),
        }


class AddPreviewPhotoForm(forms.ModelForm):

    class Meta:
        model = Headbands
        fields = ('headband', )
        widgets = {
            'headband': forms.ClearableFileInput(attrs={'placeholder': 'Добавьте файл'}),
        }


class ChangePreviewPhotoForm(forms.ModelForm):

    class Meta:
        model = Headbands
        fields = ('headband', )
        widgets = {
            'headband': forms.ClearableFileInput(attrs={'placeholder': 'Добавьте файл'}),
        }


class ConfirmEventPasswordForm(forms.Form):
    password = forms.CharField(label='Пароль', widget=forms.TextInput(attrs={'placeholder': 'Введите пароль'}))


class AddEvent(forms.ModelForm):
    class Meta:
        model = Events
        fields = ['eventname', 'description', 'eventdate', 'location', 'file_archive', 'password', 'unique_link', 'private_mode']
        widgets = {
            'eventname': forms.TextInput(),
            'description': forms.Textarea(),
            'eventdate': forms.DateInput(),
            'location': forms.TextInput(),
            'file_archive': forms.FileInput(),
            'password': forms.TextInput(),
            'unique_link': forms.TextInput(),
            'private_mode': forms.CheckboxInput(),
        }


