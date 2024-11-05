from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import FeedbackForm
from django.http import HttpResponse
from django.template import loader

def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('submit')
    else:
        form= FeedbackForm()
        
    return render(request, 'form.html',{'form': form})

def feedback1(request):
    template = loader.get_template("submit.html")
    return HttpResponse(template.render())

