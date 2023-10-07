from django.shortcuts import render, redirect
from .models import Assets, Transactions
from .forms import RegisterForm


def registration(request):
    error = ''

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('wallet')
        else:
            error = "Form not valid"

    form = RegisterForm()
    return render(request, 'main/registration.html', {
        'form': form,
        'error': error
    })


def index(request):
    return render(request, 'main/index.html')


def wallet(request):
    assets = Assets.objects.all()
    transactions = Transactions.objects.all()
    return render(request, 'main/layout/wallet.html', {
        'assets': assets,
        'transactions': transactions,
    })


def profile(request):
    return render(request, 'main/layout/profile.html')


def analyst(request):
    return render(request, 'main/layout/analyst.html')


def change(request):
    return render(request, 'main/layout/change.html')


def deposit(request, id):
    return render(request, 'main/layout/deposit.html', {
        'id': id
    })


def referral(request):
    return render(request, 'main/layout/referral.html')


def achievement(request):
    return render(request, 'main/layout/achievement.html')


def auth(request):
    return render(request, 'main/auth.html')


def recall(request):
    return render(request, 'main/recall.html')

