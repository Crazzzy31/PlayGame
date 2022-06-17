from .models import *
from django.forms import *

class GameAddForm(ModelForm):
    class Meta:
        model = Game
        fields = ['GameName', 'AgeRestriction', 'Price',
                  'StatusId', 'PublisherId', 'CategoryId', 'DeveloperId',
                  'CountryId', 'LocalizationId']
        GameName = CharField(max_length=255)
        AgeChoice = ((i.id, i.age) for i in AgeRestrictions.objects.all())
        AgeRestriction = MultipleChoiceField(choices=AgeChoice)
        Price = IntegerField()
        StatusChoice = ((i.id, i.statusname) for i in Status.objects.all())
        Status = MultipleChoiceField(choices=StatusChoice)
        Publisher = ModelMultipleChoiceField(queryset=Publisher.objects.all(), vidget=CheckboxSelectMultiple)
        Category = ModelChoiceField(queryset=Category.objects.all(), vidget=CheckboxSelectMultiple)
        Developer = ModelMultipleChoiceField(queryset=Developer.objects.all(), vidget=CheckboxSelectMultiple)
        Country = ModelMultipleChoiceField(queryset=Country.objects.all(), vidget=CheckboxSelectMultiple)
        Localization = ModelMultipleChoiceField(queryset=Localization.objects.all(), vidget=CheckboxSelectMultiple)

