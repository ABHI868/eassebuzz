
from django import forms

from school.models import Student,Profile

class CreateStudentModelForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields ='__all__'

class CreateProfile(forms.ModelForm):
    class Meta:
        model=Profile
        fields='__all__'

class editProfileForm(forms.ModelForm):
    user_type=forms.CharField(disabled=True)
    user=forms.CharField(disabled=True)
    class Meta:
        model = Profile
        fields=('user','user_type','contact_no','address')
        # fields = ('full_name', 'active', 'admin','email','user_type')

    # def clean_password2(self):
    #     # Check that the two password entries match
    #     password1 = self.cleaned_data.get("password1")
    #     password2 = self.cleaned_data.get("password2")
    #     if password1 and password2 and password1 != password2:
    #         raise forms.ValidationError("Passwords don't match")
    #     return password2

    # def save(self, commit=True):
    #     # Save the provided password in hashed format
    #     user = super(ProfileForm, self).save(commit=False)
    #     user.set_password(self.cleaned_data["password1"])
    #     # user.active = False # send confirmation email
    #     if commit:
    #         user.save()
        # return user