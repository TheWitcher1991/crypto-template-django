from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseNotFound
from django.views.generic import TemplateView
from .models import Assets, Transactions
from .forms import RegisterForm, AuthForm
from .settings.functions import authorized


def registration(request):
    error = ''

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Ваш аккаунт создан: можно войти на сайт.')
            return redirect('auth')
        else:
            error = "Form not valid"
    else:
        form = RegisterForm()
    return render(request, 'main/registration.html', {
        'form': form,
        'error': error
    })


def auth(request):
    if request.method == "POST":
        form = AuthForm(request.POST)
    else:
        form = AuthForm()

    return render(request, 'main/auth.html', {
        'form': form
    })


@authorized
def wallet(request):
    id = request.session.get('id', False)
    assets = Assets.objects.filter(user=id).order_by('date')
    transactions = Transactions.objects.filter(user=id).order_by('date')
    return render(request, 'main/layout/wallet.html', {
        'assets': assets,
        'transactions': transactions,
    })


class Index(TemplateView):
    template_name = 'main/index.py.html'


@authorized
def profile(request):
    return render(request, 'main/layout/profile.html')


@authorized
def analyst(request):
    return render(request, 'main/layout/analyst.html')


@authorized
def change(request):
    return render(request, 'main/layout/change.html')


@authorized
def deposit(request, id):
    return render(request, 'main/layout/deposit.html', {
        'id': id
    })


@authorized
def referral(request):
    return render(request, 'main/layout/referral.html')


@authorized
def achievement(request):
    return render(request, 'main/layout/achievement.html')


@authorized
def recall(request):
    return render(request, 'main/recall.html')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>404 Page not found :(</h1>')
