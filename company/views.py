from django.shortcuts import render, redirect

from .forms import CompanyForm
from .models import Company


def home_view(request):
    companies = Company.objects.all()
    return render(request, 'home/home.html', {'companies': companies})


def view_company(request, id):
    # companies = Company.objects.all()
    return render(request, 'home/view.html', {'ids': id})


def add_company(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = CompanyForm()

    return render(request, 'company/add-company.html', {'form': form})
