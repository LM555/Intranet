
from django.forms import ModelForm
from django import forms
from pipa.addressbook.models import PipaProfile
from django.contrib.admin.widgets import AdminFileWidget

class ProfileForm(ModelForm):
	email = forms.EmailField()
	first_name = forms.CharField(max_length=30)
	last_name = forms.CharField(max_length=30)
	description = forms.CharField(widget=forms.Textarea(attrs={'cols':'32','rows':'10'}))
	sshpubkey = forms.CharField(widget=forms.Textarea(attrs={'cols':'32','rows':'10'}), required=False)
	image = forms.ImageField(widget=AdminFileWidget, required=False)
	
	class Meta:
		model = PipaProfile
		exclude = ('user',)
		# don't touch, this works in 1.1
		fields = tuple(['email', 'first_name', 'last_name'] + [f.name for f in model._meta.fields if f.__class__.__name__ != 'AutoField'])




class NewMemberForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    surname = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(max_length=100, required=True)
    phone = forms.CharField(max_length=100, label='Phone no.', required=True)
    username = forms.CharField(max_length=100, required=True)
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(), min_length=6, max_length=100, required=True)
    password2 = forms.CharField(label='Repeate pass.',widget=forms.PasswordInput(), min_length=6, max_length=100, required=True)
    dogbert_login = forms.BooleanField(required=False)
    jon_login = forms.BooleanField(required=False)
    intranet_login = forms.BooleanField(initial=True, required=False)
    create_email = forms.BooleanField(required=False)
    
    def clean(self):
		cleaned_data = self.cleaned_data
		passw1 = cleaned_data.get("password1")
		passw2 = cleaned_data.get("password2")
		
		if passw1 and passw2:
			if not passw1 == passw2:
				self._errors['password2'] = self.error_class(['Passwords were not equal.'])
				del cleaned_data['password1']
				del cleaned_data['password2']

		return cleaned_data


