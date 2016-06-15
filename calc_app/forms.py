from django import forms
from calc_app.models import Operation


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

# class Auth_CalcForm(forms.ModelForm):
#     a = forms.FloatField()
#     b = forms.FloatField()
#     action = forms.ChoiceField(action, required=True)
#     result = forms.FloatField()
#
#     class Meta():
#         model = Operation
#         fields = ['a', 'b', 'action', 'result']
#


