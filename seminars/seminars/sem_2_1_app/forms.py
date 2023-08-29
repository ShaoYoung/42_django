from django import forms
from .models import Author
import datetime


class AuthorForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=100)
    surname = forms.CharField(label='Фамилия', max_length=100)
    email = forms.EmailField()
    biography = forms.CharField(label='Биография',widget=forms.Textarea)
    birthday = forms.DateField(label='День Рождения',initial=datetime.date.today, widget=forms.DateInput(attrs={'type':'date'}))


class ArticleForm(forms.Form):
    head = forms.CharField(label='Заголовок', max_length=200)
    content = forms.CharField(label='Содержание', widget=forms.TextInput)
    # выбор всех авторов из БД для выбора
    # author = forms.ChoiceField(label='Авторы', choices=[(author.id, str(author)) for author in Author.objects.all()])
    # аналогично (в Django уже есть реализация)
    author = forms.ModelChoiceField(label='Авторы', queryset=Author.objects.all())

    category = forms.CharField(label='Категория', max_length=100)

class CommentForm(forms.Form):
    author = forms.ModelChoiceField(label='Авторы', queryset=Author.objects.all())
    comment = forms.CharField(label='Комментарий',widget=forms.Textarea)
