from django.db import models


class Review(models.Model):
    company = models.ForeignKey('company.Company', on_delete=models.CASCADE, related_name='reviews')
    author = models.CharField(max_length=255)
    content = models.TextField()
    rating = models.IntegerField(
        choices=[
            (5, "⭐️⭐️⭐️⭐️⭐️ (5 sao)"),
            (4, "⭐️⭐️⭐️⭐️ (4 sao)"),
            (3, "⭐️⭐️⭐️ (3 sao)"),
            (2, "⭐️⭐️ (2 sao)"),
            (1, "⭐️ (1 sao)"),
        ],
        default=5
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.author} for {self.company.name}"
