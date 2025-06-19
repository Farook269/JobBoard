# from django.shortcuts import render, get_object_or_404, redirect
# from .models import JobPosting
# from .forms import ApplicationForm
# from django.core.mail import send_mail
# # Create your views here.


# def job_detail(request, pk):
#     posting = get_object_or_404(JobPosting, pk=pk, is_active=True)
#     applications = posting.applications.all()
    
#     if request.method == "POST":
#         form = ApplicationForm(request.POST, request.FILES)
#         if form.is_valid():
#             app = form.save(commit=False)
#             app.job = posting
#             app.save()
#         send_mail(
#         subject="Job Application Received",
#         message=f"Thank you {app.name} for applying to {posting.title}.",
#         from_email="hr@example.com",
#         recipient_list=[app.email],
#         fail_silently=False,
#     )
#         return redirect("job-detail", pk=pk)
#     else:
#         form = ApplicationForm()
            
#     context = {
#         "posting": posting,
#         "form": form,
#         "applications": applications
#     }
#     return render(request, "job_board/detail.html", context)
from django.shortcuts import render, get_object_or_404, redirect
from .models import JobPosting
from .forms import ApplicationForm
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, authenticate
from django.contrib import messages
def landing_page(request):
    return render(request, 'job_board/landing.html')  # custom landing page


@login_required(login_url='login')
def index(request):
    active_postings = JobPosting.objects.filter(is_active=True)
    context = {
        "job_postings": active_postings
    }
    return render(request, "job_board/index.html", context)
def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
        messages.error(request, 'Please enter valid credentials.')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})



from django.contrib.auth import login




def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Signup successful! Please login to continue.')
            return redirect('login')  # Redirect to login after successful signup
    else:
        form = SignUpForm()

    return render(request, 'registration/signup.html', {'form': form})













# def signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)  # Log the user in immediately after signup
#             messages.success(request, 'Welcome! You are now logged in.')
#             return redirect('login')  # Redirect to your homepage URL name
#         else:
#             messages.error(request, 'Please correct the errors below.')
#     else:
#         form = SignUpForm()
#     return render(request, 'registration/signup.html', {'form': form})



@login_required
def job_detail(request, pk):
    posting = get_object_or_404(JobPosting, pk=pk, is_active=True)
    applications = posting.applications.all()
    
    if request.method == "POST":
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            app = form.save(commit=False)
            app.job = posting
            app.user = request.user  # Associate logged-in user
            app.save()
            messages.success(request, "Your application has been submitted successfully!")
            
            send_mail(
                subject="Job Application Received",
                message=f"Thank you {app.name} for applying to {posting.title}.",
                from_email="hr@example.com",
                recipient_list=[app.email],
                fail_silently=False,
            )
            return redirect("job-detail", pk=pk)
    else:
        form = ApplicationForm()
            
    context = {
        "posting": posting,
        "form": form,
        "applications": applications
    }
    return render(request, "job_board/detail.html", context)