from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from calc_app.forms import CalcForm
from calc_app.models import Operation


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
            #try:
            if action == '+':
                result = a + b
            elif action == '-':
                result = a - b
            elif action == '*':
                result = a * b
            elif action == '/':
                result = a / b
            #except (ZeroDivisionError, ValueError):
                #print("You can't divide by zero.")
                #reverse('index_view')
        if request.user.is_authenticated():
            Operation.objects.create(user=request.user, a=a, b=b, operator=action, result=result)
    return render(request, 'index.html', {'form': CalcForm, 'result': result, 'a': a, 'b': b, 'action': action})

def create_user_view(request):
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("index_view"))
        else:
            return render(request, 'create_user.html', {"form": form})
    form = UserCreationForm()
    return render(request, 'create_user.html', {"form": form})


@login_required
def profile_view(request):
    return render(request, 'profile.html')