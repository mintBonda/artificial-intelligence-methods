from django import forms
from django.forms import RadioSelect

from .models import User


class UserForm(forms.ModelForm):

    def save(self):
        new_user = User.objects.create(
            name=self.cleaned_data['name'],
            score=self.cleaned_data['score'],
            time=self.cleaned_data['time']
        )
        return new_user

    class Meta:
        model = User
        fields = ("name", "score", "time")
