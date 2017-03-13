from django import forms
from .models import Post

class ContactForm(forms.Form):
	email=forms.EmailField(required=True)
	full_name=forms.CharField(required=False)
	message=forms.CharField(required=True)

	
class BlogForm(forms.ModelForm):
	class Meta:
		model=Post
		fields = ['title', 'body']


#def clean_email(self):
		#email = self.cleaned_data.get('email')
		# return email

	# def clean_full_name(self):
		# full_name = self.cleaned_data.get('full_name')
		# return full_name

	# def clean_message(self):
		# message = self.cleaned_data.get('message')
		# return message

# class SignUpForm(forms.ModelForm):
# 	class Meta:
# 		model=SignUp
# 		fields=['full_name','email']

# 		def clean_email(self):
# 			email = self.cleaned_data.get('email')
# 			return email

# 		def clean_full_name(self):
# 			full_name = self.cleaned_data.get('full_name')
# 			return full_name
