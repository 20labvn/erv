from django import forms

from reviews.models import Review
from .models import Company


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'industry', 'location', 'employee_count', 'image', 'rating']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tên công ty'}),
            'industry': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Lĩnh vực'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Vị trí'}),
            'employee_count': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Số lượng nhân viên'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1', 'min': '0', 'max': '5',
                                               'placeholder': 'Đánh giá (0-5)'}),
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["author", "content", "rating"]
        widgets = {
            "author": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Người review"
            }),
            "content": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 4,
                "placeholder": "Nội dung review"
            }),
            "rating": forms.Select(
                attrs={"class": "form-select"},
                choices=[
                    ("", "-- Chọn số sao --"),
                    (5, "⭐️⭐️⭐️⭐️⭐️ (5 sao)"),
                    (4, "⭐️⭐️⭐️⭐️ (4 sao)"),
                    (3, "⭐️⭐️⭐️ (3 sao)"),
                    (2, "⭐️⭐️ (2 sao)"),
                    (1, "⭐️ (1 sao)"),
                ]
            )
        }
