from pyexpat import model
from .models import CountImage, Events
from django import forms


class EventsForms(forms.ModelForm):
    class Meta:
        model = Events
        fields = '__all__'

class CountForm(forms.ModelForm):
    class Meta:
        model = CountImage
        fields = ['image', 'Event_name'] 
    
    def clean_image(self):
        img = self.cleaned_data.get('image')
        if img.image.format in ['JPG', 'JPEG']:
            return img
        else:
            raise forms.ValidationError('Upload a jpg image.')
