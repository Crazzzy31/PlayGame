from django.db.models import *
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


class Status(Model):
    StatusName = CharField(max_length=255)

    def __str__(self):
        return self.StatusName


class Publisher(Model):
    PublisherName = CharField(max_length=255)

    def __str__(self):
        return self.PublisherName


class Category(Model):
    CategoryName = CharField(max_length=255)

    def __str__(self):
        return self.CategoryName


class Developer(Model):
    DeveloperName = CharField(max_length=255)

    def __str__(self):
        return self.DeveloperName


class Comment(Model):
    CommentText = CharField(max_length=1023)

    def __str__(self):
        return self.CommentText


class Country(Model):
    CountryName = CharField(max_length=255)

    def __str__(self):
        return self.CountryName


class AgeRestrictions(Model):
    Age = CharField(max_length=255)

    def __str__(self):
        return self.Age


class Localization(Model):
    LocalizationName = CharField(max_length=255)

    def __str__(self):
        return self.LocalizationName


class Game(Model):
    GameName = CharField(default=None, max_length=255)
    AgeRestriction = ForeignKey(AgeRestrictions, on_delete=CASCADE, related_name="Ages")
    Price = IntegerField()
    StatusId = ForeignKey(Status, on_delete=CASCADE, related_name="Status")
    PublisherId = ForeignKey(Publisher, on_delete=CASCADE, related_name="Publisher")
    CategoryId = ManyToManyField(Category, default=None, related_name="Category")
    DeveloperId = ManyToManyField(Developer, default=None, related_name="Developer")
    CommentId = ManyToManyField(Comment, default=None, related_name="Comment")
    CountryId = ManyToManyField(Country, default=None, related_name="Country")
    LocalizationId = ManyToManyField(Localization, default=None, related_name="Localization")

    def __str__(self):
        return self.GameName


class Role(Model):
    RoleName = CharField(max_length=255)

    def __str__(self):
        return self.RoleName


class SiteUser(Model):
    user = OneToOneField(User, on_delete=CASCADE)
    RoleId = ForeignKey(Role, on_delete=CASCADE, default=3, null=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            SiteUser.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.siteuser.save()





# Create your models here.
