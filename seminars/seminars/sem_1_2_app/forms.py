from django import forms


# форма с двумя полями
class ChoiceForm(forms.Form):

    # в кортежах первый элемент отправляется в форму, второй видит пользователь
    game = forms.ChoiceField(choices=[('d', 'Кубик'), ('r', 'Случайное число'), ('c', 'Монетка')])
    count = forms.IntegerField(min_value=1, max_value=64)




