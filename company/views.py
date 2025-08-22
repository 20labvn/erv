from django.shortcuts import render, redirect, get_object_or_404

from .forms import CompanyForm, ReviewForm
from .models import Company


def home_view(request):
    companies = Company.objects.all()
    return render(request, 'home/home.html', {'companies': companies})


def view_company(request, id):
    company = get_object_or_404(Company, id=id)
    reviews = company.reviews.all()

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.company_id = id
            review.save()
            return redirect("view_company", id=company.id)
    else:
        form = ReviewForm()

    return render(request, 'home/view.html', {'company': company, 'form': form, 'reviews': reviews, })


def add_company(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = CompanyForm()

    return render(request, 'company/add-company.html', {'form': form})
