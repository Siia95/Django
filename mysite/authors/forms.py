from django import forms
from .models import Author

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'birth_date', 'bio']

    def save(self, **kwargs):
        user = kwargs.pop('user')
        instance = super(AuthorForm, self).save(**kwargs)
        instance.user = user
        instance.save()
        return instance
