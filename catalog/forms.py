# Listing 10.23
from django import forms
from datetime import date


class AuthorsForm(forms.Form):
    first_name = forms.CharField(label="Имя автора")
    last_name = forms.CharField(label="Фамилия автора")
    date_of_birth = forms.DateField(label="Дата рождения",
                                    initial=format(date.today()),
                                    widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    date_of_death = forms.DateField(label="Дата смерти",
                                    initial=format(date.today()),
                                    widget=forms.widgets.DateInput(attrs={'type': 'date'}))

# Listing 10.33
from django.forms import ModelForm
from .models import Book


class BookModelForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'genre', 'language', 'author', 'summary', 'isbn']

        # Listing 10.34
        #fields = [' summary', ]
        #labels = {' summary ': _('Аннотация'), }
        #help_texts = {' summary ': _('Не более 1000 символов'), }

