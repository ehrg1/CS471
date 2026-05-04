from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'price', 'quantity', 'pubdate', 'rating']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter book title'}),
            'price': forms.NumberInput(attrs={'min': 0}),
            'quantity': forms.NumberInput(attrs={'min': 0}),
            'pubdate': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5}),
        }