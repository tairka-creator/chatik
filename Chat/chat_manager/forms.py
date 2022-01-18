from django import forms
from .models import File_table, Message


class Room_forms(forms.ModelForm):
    class Meta:
        model = File_table
        fields = ['files']

class Msg_form(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['value']