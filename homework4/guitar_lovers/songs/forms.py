from django import forms


class AddSongForm(forms.Form):
    name = forms.CharField(max_length=64)
    date = forms.DateField(required=False)
    text = forms.CharField(max_length=1024, required=False)
    genre_id = forms.IntegerField(required=True)
    author_id = forms.IntegerField(required=True)
