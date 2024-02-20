from .models import Comment, Post, UserProfile
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        labels = {
            'body': 'Comment',  # Add label for the 'body' field
        }

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
        labels = {
            'title': 'Title',  # Add label for the 'title' field
            'author': 'Author',  # Add label for the 'author' field
            'content': 'Content',  # Add label for the 'content' field
            'featured_image': 'Featured Image',  # Add label for the 'featured_image' field
        }

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'avatar']
        labels = {
            'bio': 'Biography',  # Add label for the 'bio' field
            'avatar': 'Avatar',  # Add label for the 'avatar' field
        }
