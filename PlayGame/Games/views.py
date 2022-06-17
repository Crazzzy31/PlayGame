from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from .models import *

class FilterView:
    def get_countries(self):
        return Country.objects.all()

    def get_developer(self):
        return Developer.objects.all()

    def get_category(self):
        return Category.objects.all()

    def get_publisher(self):
        return Publisher.objects.all()

    def get_localization(self):
        return Localization.objects.all()

    def get_age(self):
        return AgeRestrictions.objects.all()

    def get_game(self):
        return Game.objects.values("gamename").distinct()


class SignupView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('confirm')


class SignupConfirm(generic.ListView):
    model = Game
    template_name = 'gang.html'


class StartView(generic.View):
    template_name = ''


class LoginView(generic.View):
    template_name = ''
    model = User


class MainView(FilterView, generic.ListView):
    template_name = 'game_list.html'
    model = Game


class GameView(generic.DetailView):
    template_name = ''
    model = Game


class CartView(generic.ListView):
    template_name = ''


class GameAddView(FilterView, generic.CreateView):
    template_name = 'game_list.html'
    model = Game
    fields = ['GameName', 'AgeRestriction', 'Price',
                  'StatusId', 'PublisherId', 'CategoryId', 'DeveloperId',
                  'CountryId', 'LocalizationId']
    success_url = reverse_lazy('main')


class GameUpdateView(generic.UpdateView):
    template_name = ''
    model = Game


class SuccessBuyView(generic.View):
    template_name = ''


class GameDeleteView(generic.DeleteView):
    template_name = ''
    model = Game


class PublisherPageView(generic.ListView):
    template_name = ''


class DeveloperPageView(generic.ListView):
    template_name = ''





class FilterGameView(FilterView, generic.ListView):
    def get_queryset(self):
        queryset = Game.objects.all()
        if self.request.GET.getlist("Developer"):
            queryset = queryset.filter(Q(DeveloperId__in=self.request.GET.getlist("Developer")))
        if self.request.GET.getlist("Category"):
            queryset = queryset.filter(Q(CategoryId__in=self.request.GET.getlist("Category")))
        if self.request.GET.getlist("Age"):
            queryset = queryset.filter(Q(AgeRestriction__in=self.request.GET.getlist("Age")))
        if self.request.GET.getlist("Price"):
            queryset = queryset.filter(Q(Price__in=self.request.GET.getlist("Price")))
        if self.request.GET.getlist("Publisher"):
            queryset = queryset.filter(Q(PublisherId__in=self.request.GET.getlist("Publisher")))
        if self.request.GET.getlist("Country"):
            queryset = queryset.filter(Q(CountryId__in=self.request.GET.getlist("Country")))
        if self.request.GET.getlist("Localization"):
            queryset = queryset.filter(Q(LocalizationId__in=self.request.GET.getlist("Localization")))
        if self.request.GET.getlist("GameName"):
            queryset = queryset.filter(Q(GameName__istartswith=self.request.GET.getlist("GameName")[0]))
        return queryset.distinct()