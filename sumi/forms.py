import datetime

from django import forms

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class BookForm(forms.Form):
    name = forms.CharField(help_text="Enter Your Name", required=True)
    email_address = forms.EmailField(help_text="Enter Email Address", required=True)
    phone_number = forms.CharField(help_text="Enter Phone Number", max_length=12, required=True)
    destination = forms.CharField(help_text="Enter Destination", max_length=40, required=True)
    start_date = forms.DateField(required=False)

    def clean_start_date(self):
        data = self.cleaned_data['start_date']

        # Check if a date is not in the past.
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - start date in past'))

        return data
    end_date= forms.DateField(required=False)
    
    def clean_end_date(self):
        data = self.cleaned_data['end_date']

        # Check if a date is not in the past.
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - start date in past'))

        return data
    number_of_people = forms.IntegerField(help_text="Enter Number of People Travelling", required=False)
    custome_request= forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":20}), help_text="Enter Special Request and Additional Details Here")
    

    