from django.shortcuts import render
from testapp.forms import FeedbackForm

# Create your views here.
def feedback_view(request):
    form = FeedbackForm()
    if request.method=='POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            print('Basic validation is done...')
            print('Name: ',form.cleaned_data['name'])
            print('Rollno: ',form.cleaned_data['rollno'])
            print('Marks: ',form.cleaned_data['marks'])
            print('Feedback: ',form.cleaned_data['feedback'])

    return render(request,'testapp/feedback.html',{'form':form})
