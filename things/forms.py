"""Forms of the project."""
from django import forms



# Create your forms here.
class ThingForm(forms.Form):
    name = forms.CharField(label = 'name')
    description = forms.Textarea(label = 'description')
    quantity = forms.IntegerField(label = 'quantity')