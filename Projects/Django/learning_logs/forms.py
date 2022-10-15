from django import forms
from .models import Topic

#==================================================================
# define a class called TopicForm, which inherits from forms.ModelForm
'''
The simplest version of a ModelForm consists of a nested Meta class telling
Django which model to base the form on and which fields to include
in the form. We build a form from the Topic model and include only
the text field. The last line tells Django not to generate a label
for the text field.
'''
class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']     # = list with 1 element
        labels = {'text': ''} # = dictionary with 1 element

#==================================================================