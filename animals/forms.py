from django import forms
from . import models


class AnimalForm(forms.ModelForm):
    kind_choices = list(models.Animal.KIND_CHOICES)
    name = forms.CharField(required=True)
    age = forms.IntegerField(required=True)
    breed = forms.CharField(required=True)
    description = forms.CharField(required=True, widget=forms.Textarea)
    image_url = forms.URLField(required=True)
    kind = forms.ChoiceField(choices=kind_choices, required=True)


    class Meta:
        model = Animal
        fields = ('kind_choices', 'name', 'age', 'breed', 'description', 'image_url', 'kind')