from django.shortcuts import render


def home_review(request):
    return render(request, 'home/home.html')


def create_review(request):
    return render(request, 'reviews/create-review.html')


def write_review(request):
    return render(request, 'reviews/write-review.html')
