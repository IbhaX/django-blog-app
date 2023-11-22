from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description']

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter title'})
        self.fields['description'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter description'})


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['comment'].widget.attrs.update({'class': 'form-control shadow', 'placeholder': 'Comment', 'rows': 10, 'cols': 20})
        self.fields['comment'].label=''
