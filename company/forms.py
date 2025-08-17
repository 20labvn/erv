from django import forms
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
            'rating': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1', 'min': '0', 'max': '5', 'placeholder': 'Đánh giá (0-5)'}),
        }
