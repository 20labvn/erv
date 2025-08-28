from django import forms

from .models import Review


class ReviewAddForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["title", "content", "image", "tag"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "input w-full", "placeholder": "Nhập tiêu đề"}),
            "image": forms.ClearableFileInput(attrs={"class": "file-input file-input-ghost w-full"}),
            "tag": forms.TextInput(attrs={"class": "input w-full", "placeholder": "Thêm tag"}),

            "content": forms.Textarea(
                attrs={"class": "textarea textarea-ghost w-full", "placeholder": "Nhập nội dung"}),
        }
