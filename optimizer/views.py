from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Website, File, OptimizedFile, Log, Feedback, Report
from .forms import *

def Addwebsite(request):
    form = WebsiteForm()
    if request.method == 'POST':
        form = WebsiteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        messages.success(request, 'Website added successfully!')
        return redirect('dashboard')
    return render(request, 'addwebsite.html', {'form': form})


def viewwebsite(request, id):
    website = Website.objects.get(id=id)
    return render(request, 'viewwebsite.html', {'website': website})

def dashboard(request):
    websites = Website.objects.all()
    return render(request, 'dashboard.html', {'websites': websites})

def optimized(request, id):

    website = Website.objects.get(id=id)
    # files = File.objects.filter(website=website)
    # optimized_files = []
    # for file in files:
    #     optimized_file = OptimizedFile(file=file, optimization_result='Success')
    #     optimized_file.save()
    #     optimized_files.append(optimized_file)
    # return render(request, 'optimized.html', {'website': website, 'optimized_files': optimized_files})
    messages.success(request, 'Website optimized successfully!')
    return render(request, 'optimize.html', {'website': website})

def optimize(request):
    websites = Website.objects.all() #replace with your actual query
    return render(request, 'optimize.html', {'websites': websites})

def feedback(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        feedback = Feedback(name=name, email=email, message=message)
        feedback.save()
        return render(request, 'feedback.html', {'message': 'Feedback sent successfully!'})
    else:
        return render(request, 'feedback.html')
    
def report(request):
    reports = Report.objects.all()
    return render(request, 'report.html', {'reports': reports})

def viewlog(request):
    logs = Log.objects.all()
    return render(request, 'log_view.html', {'logs': logs})

def viewfile(request):
    files = File.objects.all()
    return render(request, 'file_view.html', {'files': files})

def viewoptimizedfile(request):
    optimizedfiles = OptimizedFile.objects.all()
    return render(request, 'optimizedfile_view.html', {'optimizedfiles': optimizedfiles})

def delete_website(request, id):
    website = Website.objects.get(id=id)
    website.delete()
    messages.success(request, 'Website deleted successfully!')
    return redirect('dashboard')


def add_website(request):
    # Code to add website...

    return redirect('optimized?success=true')