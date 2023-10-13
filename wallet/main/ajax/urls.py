from django.urls import path
from . import sessions, index

urlpatterns = [
    path('login', sessions.LoginProc.as_view(), name='login_ajax'),
    path('logout', sessions.LogoutProc.as_view(), name='logout_ajax'),
    path('register', sessions.RegisterProc.as_view(), name='register_ajax'),
    path('index', index.IndexProc.as_view, name='index_ajax')
]
