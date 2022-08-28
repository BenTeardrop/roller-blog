from .models import Comment, Post, Review
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'featured_image', 'status')
        
class CreateReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('body',)

