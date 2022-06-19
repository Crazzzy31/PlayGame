from django.contrib.auth import logout
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from .models import *
from django.shortcuts import *


class RolePermissonView():
    def get_permission(self, **kwargs):
        user = self.request.user
        siteuser = SiteUser.objects.filter(user=user)
        permission = Role.objects.filter(id=siteuser.values('RoleId')[0]['RoleId'])
        return permission[0]


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
    success_url = reverse_lazy('login')


class SignupConfirm(generic.ListView):
    model = Game
    template_name = ''


class StartView(generic.TemplateView):
    template_name = 'start.html'
    model = Game

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('Start')


class LoginView(generic.View):
    template_name = ''
    model = User


class MainView(FilterView, generic.ListView, RolePermissonView):
    template_name = 'game_list.html'
    model = Game


class GameView(generic.DetailView, RolePermissonView):
    template_name = 'gameview.html'
    model = Game


class CartView(generic.ListView, RolePermissonView):
    template_name = ''


class GameAddView(FilterView, generic.CreateView, RolePermissonView):
    template_name = 'gameadd.html'
    model = Game
    fields = ['GameName', 'AgeRestriction', 'Price',
                  'StatusId', 'PublisherId', 'CategoryId', 'DeveloperId',
                  'CountryId', 'LocalizationId']
    success_url = reverse_lazy('main')


class GameUpdateView(generic.UpdateView, RolePermissonView):
    template_name = 'update.html'
    model = Game
    fields = ['GameName', 'AgeRestriction', 'Price',
              'StatusId', 'PublisherId', 'CategoryId', 'DeveloperId',
              'CountryId', 'LocalizationId']
    def get_success_url(self):
        gameid = self.kwargs['pk']
        return reverse_lazy('game', kwargs={'pk': gameid})

class SuccessBuyView(generic.View, RolePermissonView):
    template_name = ''


class GameDeleteView(generic.DeleteView, RolePermissonView):
    model = Game
    def get_success_url(self):
        return reverse_lazy('main')


class PublisherPageView(generic.ListView, RolePermissonView):
    template_name = 'publisherpage.html'
    model = Publisher

    def get_publisher_games(self):
        publisherid = self.kwargs['pk']
        return Game.objects.filter(PublisherId=publisherid)

    def get_publisher_name(self):
        publisherid = self.kwargs['pk']
        return Publisher.objects.filter(Id=publisherid)


class DeveloperPageView(generic.ListView, RolePermissonView):
    template_name = ''


class FilterGameView(FilterView, generic.ListView, RolePermissonView):
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