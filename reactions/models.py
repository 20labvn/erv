from django.db import models

from reviews.models import Review


class Reaction(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name="reactions")
    like = models.PositiveIntegerField(default=0)
    dislike = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review {self.review.id} - Likes: {self.like}, Dislikes: {self.dislike}"
