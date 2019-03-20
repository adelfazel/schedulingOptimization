from django import forms
from django.core.exceptions import ValidationError
import xlrd


class uploadFileForm(forms.Form):

    uniqueIdentifier = forms.CharField(label='Unique Identifier', max_length=100)
    shiftFile = forms.FileField(label='Shifts file', allow_empty_file = False)
    employeeFile = forms.FileField(label='Employee names file', allow_empty_file = False)

class resultForm(forms.Form):
    uniqueIdentifier = forms.CharField(label='Unique Identifier')
