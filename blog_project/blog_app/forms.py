from django import forms
from django.db.models import fields
from django.forms import widgets
from blog_app.models import Post, Comments

class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ('author', 'title', 'text')

        # These class names in widgets are known by Django
        widgets = {
            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})

        }
class CommentForm(forms.ModelForm):

    class Meta():
        model = Comments
        fields = ('author','text')

        # These class names in widgets are known by Django
        widgets = {
            'author' : forms.TextInput(attrs={'class':'textinputclss'}),
            'text' : forms.Textarea(attrs={'class':'editable medium-editor-textarea'})
        }


