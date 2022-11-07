from random import choices
from django import forms
from . models import Details
from . models import Register

class DatePickerInput(forms.DateInput):
    input_type = 'date'

class TimePickerInput(forms.TimeInput):
    input_type = 'time'

class DateTimePickerInput(forms.DateTimeInput):
    input_type = 'datetime'

roof_type_choices = ['Select here','Comp Shingle','Concrete','Metal','Spanish','Clay', 'Other']

CHOICES=[(True, 'Yes'), (False, 'No')]

like = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
class DetailsForm(forms.ModelForm):
    class Meta:
        model = Details
        fields = '__all__'
        # fields = ['name', 'roof_age', 'email', 'phone', 'address', 'monthly_bill', 'HOA', 'battery', 'foundation', 'roof_type', 'availability','bill']
        # HOA.widget.attrs.update({'class': 'rounded_list'})

        # widgets = {
        #     'HOA' : forms.BooleanField(attrs={'class': 'form-radio'})
        # }
        widgets = {
            'availability': DateTimePickerInput(),
            'HOA' : forms.BooleanField(widget= forms.RadioSelect(choices=[(True, 'Yes'), (False, 'No')]))
        }



class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        # fields = "__all__"
        fields = ['name', 'roof_age', 'email', 'phone', 'address', 'monthly_bill', 'HOA','battery', 'foundation','roof_type', 'availability','bill', 'questions', 'meter_picture', 'company_name']

        widgets = {
                'name': forms.TextInput(attrs={'class': 'form-control'}),
                'HOA' :forms.RadioSelect(attrs={'class': 'radio-item', 'id':'item'}),
                'battery' :forms.RadioSelect(attrs={'placeholder': 'Search'}),
                'foundation' :forms.RadioSelect(),
                'availability': forms.TextInput(attrs={'type':'date'})
        }