from django import forms
from .models import *


class CreateSliderForm(forms.ModelForm):
    class Meta:
        model = Slider
        fields = (
            'title', 'image',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'rounded_list'}),
        }


class SliderUpdateForm(forms.ModelForm):
    class Meta:
        model = Slider
        fields = (
            'title', 'image',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'rounded_list'}),
        }


class CreateProductSliderForm(forms.ModelForm):
    class Meta:
        model = ProductSlider
        fields = (
            'title', 'image',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'rounded_list'}),
        }


class ProductSliderUpdateForm(forms.ModelForm):
    class Meta:
        model = Slider
        fields = (
            'title', 'image',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'rounded_list'}),
        }


class CreateHomeAboutForm(forms.ModelForm):
    class Meta:
        model = HomeAbout
        fields = (
            'title', 'description', 'image',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'rounded_list'}),
        }


class DescriptionUpdateForm(forms.ModelForm):
    class Meta:
        model = HomeAbout
        fields = (
            'title', 'description', 'image',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'rounded_list'}),
        }


class CreateAboutDescriptionForm(forms.ModelForm):
    class Meta:
        model = About
        fields = (
            'title', 'description', 'image',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'rounded_list'}),
        }


class AboutDescriptionUpdateForm(forms.ModelForm):
    class Meta:
        model = About
        fields = (
            'title', 'description', 'image',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'rounded_list'}),
        }


class CreateGalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = (
            'title', 'image',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'rounded_list'}),
        }


class GalleryUpdateForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = (
            'title', 'image',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'rounded_list'}),
        }


class CreateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = (
            'title', 'category', 'image',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'rounded_list'}),
        }


class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = (
            'title', 'category', 'image',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'rounded_list'}),
        }