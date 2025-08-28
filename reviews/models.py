from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Review(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="reviews"
    )
    content = models.TextField()
    image = models.ImageField(upload_to="static/image/", blank=True, null=True)
    tag = models.CharField(max_length=100, blank=True, null=True)
    favorite_count = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
