from django.shortcuts import render
from calc_app.forms import CalcForm

# Create your views here.


def index_view(request):
    result = ''
    if request.POST:
        form = CalcForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['action'] == 'Add':
                result = form.cleaned_data['a'] + form.cleaned_data['b']
            elif form.cleaned_data['action'] == 'Subtract':
                result = form.cleaned_data['a'] - form.cleaned_data['b']
            elif form.cleaned_data['action'] == 'Multiply':
                result = form.cleaned_data['a'] * form.cleaned_data['b']
            elif form.cleaned_data['action'] == 'Divide':
                result = form.cleaned_data['a'] / form.cleaned_data['b']
    return render(request, 'index.html', {'form': CalcForm, 'result': result})
