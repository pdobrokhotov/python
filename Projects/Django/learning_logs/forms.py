from django import forms
from .models import Topic, Entry
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
class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        # Include the widgets attribute. A widget is an HTML form element,
        # such as a single-line text box, multi-line text area, or drop-down list.
        # By including the widgets attribute you can override Django’s default 
        # widget choices. By telling Django to use a [forms.Textarea] element, 
        # we're customizing the input widget for the field 'text' so the text area
        # will be 80 columns wide instead of the default 40. This will give users
        # enough room to write a meaningful entry.
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}