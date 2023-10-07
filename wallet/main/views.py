from django.shortcuts import render
from .models import Assets, Transactions


def index(request):
    return render(request, 'main/index.html')


def wallet(request):
    assets = Assets.objects.all()
    transactions = Transactions.objects.all()
    return render(request, 'main/wallet.html', {
        'assets': assets,
        'transactions': transactions,
    })


def profile(request):
    return render(request, 'main/profile.html')


def analyst(request):
    return render(request, 'main/analyst.html')


def change(request):
    return render(request, 'main/change.html')


def deposit(request):
    return render(request, 'main/deposit.html')


def referral(request):
    return render(request, 'main/referral.html')


def achievement(request):
    return render(request, 'main/achievement.html')


def auth(request):
    return render(request, 'main/auth.html')


def recall(request):
    return render(request, 'main/recall.html')


def registration(request):
    return render(request, 'main/registration.html')
