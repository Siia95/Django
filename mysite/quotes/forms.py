from django import forms
from .models import Quote


class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ['text', 'author']

    def save(self, **kwargs):
        user = kwargs.pop('user')
        instance = super(QuoteForm, self).save(**kwargs)
        instance.user = user
        instance.save()
        return instance
