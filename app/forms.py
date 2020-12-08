from django import forms
from .models import *

class FailedDataEntryForm(forms.ModelForm):
	class Meta:
		model = Failed
		fields =('c','link','comment','high_level_resone','low_level_resone','issue_description','frequency','analysis','rca','action')
		widgets={
			'c' : forms.TextInput(attrs={'class':'form-control','required':'','type':'number'}),
			'high_level_resone' : forms.TextInput(attrs={'class':'form-control','required':'','type':'text'}),
			'low_level_resone' : forms.TextInput(attrs={'class':'form-control','required':'','type':'text'}),
			'frequency' : forms.TextInput(attrs={'class':'form-control','required':'','type':'number'})

		}


class DisabledDataEntryForm(forms.ModelForm):
	class Meta:
		model = Disabled
		fields =('c','link','comment','high_level_resone','low_level_resone','issue_description','frequency','analysis','rca','action')
		widgets={
			'c' : forms.TextInput(attrs={'class':'form-control','required':'','type':'number'}),
			'high_level_resone' : forms.TextInput(attrs={'class':'form-control','required':'','type':'text'}),
			'low_level_resone' : forms.TextInput(attrs={'class':'form-control','required':'','type':'text'}),
			'frequency' : forms.TextInput(attrs={'class':'form-control','required':'','type':'number'})

		}

















