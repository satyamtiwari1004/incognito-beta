from .models import Comment
from django import forms
class CommentForm(forms.ModelForm):
    name=forms.CharField()
    email=forms.EmailField()
    website=forms.URLField()
    Message=forms.Textarea()
    class Meta:
        model=Comment
        fields=('name','email','website','Message')