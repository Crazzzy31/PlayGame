from django.contrib import admin
from django.urls import path
from django.urls import include
from .views import *


urlpatterns = [
    path('SignUp', SignupView.as_view(), name="signup"),
    path('Login', LoginView.as_view(), name="login"),
    path('Main', MainView.as_view(), name="main"),
    path('Start', StartView.as_view(), name="start"),
    path('Game/<int:pk>', GameView.as_view(), name="game"),
    path('Cart', CartView.as_view(), name="cart"),
    path('GameAdd', GameAddView.as_view(), name="gameadd"),
    path('GameUpdate/<int:pk>', GameUpdateView.as_view(), name="gameupdate"),
    path('SuccessBuy', SuccessBuyView.as_view(), name="successbuy"),
    path('GameDelete/<int:pk>', GameDeleteView.as_view(), name="gamedelete"),
    path('PublisherPage/<int:pk>', PublisherPageView.as_view(), name="publisherpage"),
    path('DeveloperPage', DeveloperPageView.as_view, name="developerpage"),
    path('Filter', FilterGameView.as_view(), name='filter'),
    path('UserLogout', user_logout, name='userlogout')
]