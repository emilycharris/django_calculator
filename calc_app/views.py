from django.shortcuts import render
from calc_app.forms import CalcForm

# Create your views here.


def index_view(request):
    result = ''
    a = ''
    b = ''
    action = ''
    if request.POST:
        form = CalcForm(request.POST)
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            action = form.cleaned_data['action']
            try:
                if action == '+':
                    result = a + b
                elif action == '-':
                    result = a - b
                elif action == '*':
                    result = a * b
                elif action == '/':
                    result = a / b
            except ZeroDivisionError:
                result = "You can't divide by zero."
    return render(request, 'index.html', {'form': CalcForm(), 'result': result, 'a': a, 'b': b, 'action': action})
