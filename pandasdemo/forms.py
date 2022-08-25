from django import forms
from pandasdemo.models import Ethanol
from crispy_forms.helper import FormHelper
from django.urls import reverse_lazy
from crispy_forms.layout import Submit

class EthanolForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        #self.helper.form_action = reverse_lazy('ethanollist')
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Submit'))
        
    class Meta:
        model = Ethanol
        fields = "__all__"
        


        