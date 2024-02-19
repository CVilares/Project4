from .models import Comment, Post, UserProfile
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class PostForm(forms.ModelForm):
    """
    Form for posts
    """
    class Meta:
        model = Post
        fields = [
            'title',
            'author',
            'content',
            
            'featured_image',
        ]        

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'avatar']       