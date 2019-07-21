from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from .models import Job


class JobForm(forms.ModelForm):

    class Meta:
        model = Job
        fields = ('name', 'support', 'memo', 'send_date', 'get_date')
        widgets = {
                    'name': forms.TextInput(attrs={'placeholder': '記入例：H2_01'}),
                    'support': forms.RadioSelect(),
                    'memo': forms.Textarea(attrs={'rows': 4}),
                    'send_date': AdminDateWidget(),
                    'get_date': AdminDateWidget(),
        }