from django import forms
from .models import Post,TechPost
from ckeditor.widgets import CKEditorWidget

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'title_tag','title_subtitle','auther' 'body','image','date_time']
        widgets = {
            'body': CKEditorWidget(),
        }

class TechPostForm(forms.ModelForm):
    class Meta:
        model = TechPost
        fields = ['title', 'title_tag','title_subtitle','auther' 'body','image','date_time']
        widgets = {
            'body': CKEditorWidget(),
        }