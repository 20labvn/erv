from django.shortcuts import render, redirect
from .forms import CompanyForm

def add_company(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('')
    else:
        form = CompanyForm()

    return render(request, 'company/add-company.html', {'form': form})
