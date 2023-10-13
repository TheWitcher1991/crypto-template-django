from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='home'),
    path('wallet/', views.wallet, name='wallet'),
    path('profile/', views.profile, name='profile'),
    path('analyst/', views.analyst, name='analyst'),
    path('change/', views.change, name='change'),
    path('deposit/<int:id>/', views.deposit, name='deposit'),
    path('referral/', views.referral, name='referral'),
    path('achievement/', views.achievement, name='achievement'),
    path('auth/', views.auth, name='auth'),
    path('recall/', views.recall, name='recall'),
    path('registration/', views.registration, name='registration'),
]
