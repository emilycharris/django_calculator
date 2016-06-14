from django import forms


action = (
    ('+', '+'),
    ('-', '-'),
    ('*', '*'),
    ('/', '/'),
)

class CalcForm(forms.Form):
    a = forms.FloatField()
    action = forms.ChoiceField(action, required=True)
    b = forms.FloatField()


