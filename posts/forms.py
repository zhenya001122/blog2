from django import forms


class PostForm(forms.Form):
    # author = forms.CharField(max_length=20)
    title = forms.CharField(max_length=50)
    text = forms.CharField(max_length=1000)