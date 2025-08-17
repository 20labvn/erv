from django.db import models

class Review(models.Model):
    company = models.ForeignKey('company.Company', on_delete=models.CASCADE, related_name='reviews')
    author = models.CharField(max_length=255)  # Người viết review
    content = models.TextField()  # Nội dung review
    created_at = models.DateTimeField(auto_now_add=True)  # Ngày viết

    def __str__(self):
        return f"Review by {self.author} for {self.company.name}"