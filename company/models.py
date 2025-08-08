from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)
    industry = models.CharField(max_length=255)  # Lĩnh vực
    location = models.CharField(max_length=255)  # Vị trí
    employee_count = models.PositiveIntegerField()  # Số lượng nhân viên
    image = models.ImageField(upload_to='company_images/', null=True, blank=True)  # Hình ảnh

    def __str__(self):
        return self.name
