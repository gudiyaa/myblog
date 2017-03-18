from django import forms
from .models import Post
	
class BlogForm(forms.ModelForm):
	class Meta:
		model=Post
		exclude = ['author', 'create_date']

	def clean_author(self):
		author = self.cleaned_data.get('author')
		return author

	def clean_title(self):
		title = self.cleaned_data.get('title')
		return title

	def clean_body(self):
		body = self.cleaned_data.get('body')
		return body
