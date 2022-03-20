from django import forms

class FeedbackForm(forms.Form):
    name = forms.CharField()
    rollno = forms.IntegerField()
    marks = forms.IntegerField()
    feedback = forms.CharField(widget=forms.Textarea)

    def clean(self):
        print('Total form validation by using single clean method...')
        total_cleaned_data = super().clean()
        inputname = total_cleaned_data['name']
        if inputname[0].lower()!='d':
            raise forms.ValidationError('Name should start with d|D')
        inputrollno = total_cleaned_data['rollno']
        if inputrollno<=0:
            raise forms.ValidationError('Rollno should be greater than zero')
