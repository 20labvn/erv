from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)
    industry = models.CharField(max_length=255)  # Lĩnh vực
    location = models.CharField(max_length=255)  # Vị trí
    employee_count = models.PositiveIntegerField()  # Số lượng nhân viên
    image = models.ImageField(upload_to='company_images/', null=True, blank=True)  # Hình ảnh
    rating = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)  # Ví dụ 4.5 sao

    created_at = models.DateTimeField(auto_now_add=True)  # thời gian tạo (chỉ set 1 lần)
    updated_at = models.DateTimeField(auto_now=True)      # thời gian cập nhật (tự update mỗi lần save)

    def __str__(self):
        return self.name
