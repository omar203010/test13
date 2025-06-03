from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, SubmissionForm
from .models import UserSubmission

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('gallery')
    else:
        form = RegisterForm()
    return render(request, 'coreuploads/register.html', {'form': form})

@login_required
def submit_view(request):
    if request.method == 'POST':
        form = SubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect('gallery')
    else:
        form = SubmissionForm()
    return render(request, 'coreuploads/submit.html', {'form': form})

def gallery_view(request):
    submissions = UserSubmission.objects.all().order_by('-created_at')
    return render(request, 'coreuploads/gallery.html', {'submissions': submissions})
