from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from calc_app.forms import CalcForm
from calc_app.models import Operation
from django.contrib import messages



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
                messages.error(request, "You can't divide by zero")
            if request.user.is_authenticated():
                try:
                    Operation.objects.create(user=request.user, a=a, b=b, operator=action, result=result)
                except (ZeroDivisionError, ValueError):
                    pass
    return render(request, 'index.html', {'form': CalcForm, 'result': result, 'a': a, 'b': b, 'action': action})

def create_user_view(request):
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("login_view"))
        else:
            return render(request, 'create_user.html', {"form": form})
    form = UserCreationForm()
    return render(request, 'create_user.html', {"form": form})


@login_required
def profile_view(request):
    calculations = {"calculations": Operation.objects.filter(user=request.user)}
    return render(request, 'profile.html', calculations)
