from django import forms
from isaac.models import UserProfile, User


#user fields
class Userbase(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','email','password']


#extra fields
class UserForm(forms.ModelForm):
    picture = forms.ImageField(required=False)
    class Meta:
        model = UserProfile
        fields = ['portfolio','picture']


