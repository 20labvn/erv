from django.shortcuts import get_object_or_404, redirect

from reviews.models import Review
from .forms import CommentAddForm


def add_comment(request, review_id):
    review = get_object_or_404(Review, id=review_id)

    if request.method == "POST":
        form = CommentAddForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.review = review
            comment.author = request.user
            comment.save()
            return redirect(request.META.get("HTTP_REFERER", "/"))

        return redirect(request.META.get("HTTP_REFERER", "/"))
