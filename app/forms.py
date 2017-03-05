from django.contrib.auth.models import User
from django import forms
from django.forms import HiddenInput
from .models import Item,Comment,Likes,Unlike

class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ('post', 'image')
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)
class LikesForm(forms.ModelForm):

    class Meta:
        model = Likes
        exclude = ('user','item',' created_date',)
class UnlikeForm(forms.ModelForm):

    class Meta:
        model = Unlike
        exclude = ('user','item',' created_date',)
        

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
