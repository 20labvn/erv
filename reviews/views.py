from django.shortcuts import render, redirect, get_object_or_404

from .forms import ReviewAddForm
from .models import Review


def home_review(request):
    reviews = Review.objects.all()
    return render(request, 'reviews/home-review.html', {'reviews': reviews})


def view_review(request, id):
    review = get_object_or_404(Review, id=id)
    comments = review.comments.all()
    reactions = review.reactions.all()

    return render(request, 'reviews/view-review.html', {'review': review, 'comments': comments, 'reactions': reactions})


def add_review(request):
    if request.method == 'POST':
        form = ReviewAddForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.save()
            return redirect('/')
    else:
        form = ReviewAddForm()

    return render(request, 'reviews/add-review.html', {'form': form})


def delete_review(request):
    return render(request, 'reviews/write-review.html')


def list_review(request):
    return render(request, 'reviews/write-review.html')
