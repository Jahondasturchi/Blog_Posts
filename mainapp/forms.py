from django import forms
from .models import Posts, Comments

class PostForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={"rows":"3"}))
    class Meta:
        model = Posts
        fields = ['title', 'content']

class CommentForm(forms.ModelForm):
    text = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Add comment', 'value': '', 'size': 90, 'style': 'font-size: 18px'}))
    class Meta:
        model = Comments
        fields = ['text']
        