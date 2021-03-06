from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import *
from .forms import *
from django.views.generic import UpdateView, CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.core.mail import send_mail

# Create your views here.


# home view
class HomeView(View):
    def get(self, request):
        context = {
            'slider': Slider.objects.all(),
            'ps': ProductSlider.objects.all(),
            'description': HomeAbout.objects.all(),
            'title': "Index",
            'pageview': "Home"
        }
        return render(request, 'home/index.html', context)


# home description
class ShowDescriptionView(LoginRequiredMixin, View):
    def get(self, request):
        context = {
            'description': HomeAbout.objects.all(),
            'title': "Description",
            'pageview': "Home"
        }
        return render(request, 'home/home-description.html', context)


# add home description
@login_required
def add_home_about(request):
    template_name = 'home/create_home_about.html'
    message = ''

    if request.method == 'GET':
        home_form = CreateHomeAboutForm(request.GET or None)

    elif request.method == 'POST':
        home_form = CreateHomeAboutForm(request.POST, request.FILES)
        message = ''
        print(request.POST)

        if home_form.is_valid():
            obj = home_form.save(commit=False)

            obj.save()
            message = "Success"
            return redirect('home-description')

    return render(request, template_name,
                  {'home_form': home_form, 'message': message, 'title': "About", 'pageview': "Home"})


# edit-description
class DescriptionUpdateView(LoginRequiredMixin, UpdateView):
    model = HomeAbout
    form_class = DescriptionUpdateForm
    success_url = reverse_lazy('home-description')
    template_name = 'home/edit_description.html'

    success_message = "Description was updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        context["title"] = "Update Description"
        context["pageview"] = "Description"
        return context


# create slider
@login_required
def create_slider(request):
   if request.method == "POST":
    # form = CreateGalleryForm(request.POST)
    form = CreateSliderForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      img_obj = form.instance
      return render(request, 'home/create-slider.html', {'form': form, 'img_obj': img_obj})

   else:
      form = CreateSliderForm()
   return render(request, 'home/create-slider.html', {'form': form, 'title': "Create Slider", 'pageview': "Slider"})


# slider list
class SliderListView(LoginRequiredMixin, View):
    def get(self, request):
        context = {
            'slider': Slider.objects.all(),
            'title': "Slider List",
            'pageview': "Home"
        }
        return render(request, 'home/slider_list.html', context)


# edit-slider
class SliderUpdateView(LoginRequiredMixin, UpdateView):
    model = Slider
    form_class = SliderUpdateForm
    success_url = reverse_lazy('dash-slider')
    template_name = 'home/edit_slider.html'

    success_message = "Slider was updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        context["title"] = "Update Slider"
        context["pageview"] = "Slider"
        return context


# delete slider
@login_required
def delete_slider(request, id):
    obj = get_object_or_404(Slider, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('dash-slider')
    context = {
        'obj': Slider.objects.get(id=id),
        'title': "Delete Slider",
        'pageview': "Slider"
    }

    return render(request, "home/delete_slider.html", context)


# create product slider
@login_required
def create_product_slider(request):
   if request.method == "POST":
    form = CreateProductSliderForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      img_obj = form.instance
      return render(request, 'home/create_product_slider.html', {'form': form, 'img_obj': img_obj})

   else:
      form = CreateProductSliderForm()
   return render(request, 'home/create_product_slider.html',
                 {'form': form, 'title': "Create Product Slider", 'pageview': "Slider"})


# product slider list
class ProductSliderListView(LoginRequiredMixin, View):
    def get(self, request):
        context = {
            'ps': ProductSlider.objects.all(),
            'title': " Product Slider List",
            'pageview': "Home"
        }
        return render(request, 'home/product_slider_list.html', context)


# edit product slider
class ProductSliderUpdateView(LoginRequiredMixin, UpdateView):
    model = ProductSlider
    form_class = ProductSliderUpdateForm
    success_url = reverse_lazy('dash-product-slider')
    template_name = 'home/edit_product_slider.html'

    success_message = "Product Slider was updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        context["title"] = "Update Product Slider"
        context["pageview"] = "Product Slider"
        return context


# delete product slider
@login_required
def delete_product_slider(request, id):
    obj = get_object_or_404(ProductSlider, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('dash-product-slider')
    context = {
        'obj': ProductSlider.objects.get(id=id),
        'title': "Delete Product Slider",
        'pageview': "Product Slider"
    }

    return render(request, "home/delete_product_slider.html", context)


# about view
class AboutView(View):
    def get(self, request):
        context = {
            'about': About.objects.all(),
            'title': "About",
            'pageview': "Home"
        }
        return render(request, 'home/about.html', context)


# about description
class AboutDescriptionView(LoginRequiredMixin, View):
    def get(self, request):
        context = {
            'description': About.objects.all(),
            'title': "Description",
            'pageview': "Home"
        }
        return render(request, 'home/about-description.html', context)


# about description
@login_required
def add_about_description(request):
    template_name = 'home/create_about_description.html'
    message = ''

    if request.method == 'GET':
        about_form = CreateAboutDescriptionForm(request.GET or None)

    elif request.method == 'POST':
        about_form = CreateAboutDescriptionForm(request.POST, request.FILES)
        message = ''
        print(request.POST)

        if about_form.is_valid():
            obj = about_form.save(commit=False)

            obj.save()
            message = "Success"
            return redirect('about-description')

    return render(request, template_name,
                  {'about_form': about_form, 'message': message, 'title': "About", 'pageview': "Home"})


# edit about description
class AboutDescriptionUpdateView(LoginRequiredMixin, UpdateView):
    model = About
    form_class = AboutDescriptionUpdateForm
    success_url = reverse_lazy('about-description')
    template_name = 'home/edit_about_description.html'

    success_message = "Description was updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        context["title"] = "Update Description"
        context["pageview"] = "Description"
        return context


# contact view
# class ContactView(View):
#     def get(self, request):
#         context = {
#
#             'title': "Contact",
#             'pageview': "Home"
#         }
#         return render(request, 'home/contact.html', context)


def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        address = request.POST['address']
        body = request.POST['body']
        phone = request.POST['phone']
        company = request.POST['company']
        sub = request.POST['select']

        send_mail(
            sub,
            body + "\n" + "Name: " + name + "\n" + "Email: " + email + "\n" + "Phone: " + phone + "\n" + "Company: " + company + "\n" + "Address: " + address,
            'enamul@stchaque.com',
            ['enamul@stchaque.com'],
        )
        print(name, email, body)

        return render(request, 'home/contact.html', {'name': name, 'title': "Contact", 'pageview': "Home"})

    else:
        return render(request, 'home/contact.html', {})


# gallery view
class GalleryView(View):
    def get(self, request):
        context = {
            'gallery': Gallery.objects.all(),
            'title': "Gallery",
            'pageview': "Home"
        }
        return render(request, 'home/gallery.html', context)


# gallery list
class GalleryListView(LoginRequiredMixin, View):
    def get(self, request):
        context = {
            'gallery': Gallery.objects.all(),
            'title': "Gallery List",
            'pageview': "Gallery"
        }
        return render(request, 'home/gallery_list.html', context)


# create gallery
@login_required
def create_gallery(request):
   if request.method == "POST":
    # form = CreateGalleryForm(request.POST)
    form = CreateGalleryForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      img_obj = form.instance
      return render(request, 'home/create_gallery.html', {'form': form, 'img_obj': img_obj})

   else:
      form = CreateGalleryForm()
   return render(request, 'home/create_gallery.html', {'form': form, 'title': "Create Gallery", 'pageview': "Gallery"})


# edit-gallery
class GalleryUpdateView(LoginRequiredMixin, UpdateView):
    model = Gallery
    form_class = GalleryUpdateForm
    success_url = reverse_lazy('dash-gallery')
    template_name = 'home/edit_gallery.html'

    success_message = "gallery was updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        context["title"] = "Update Gallery"
        context["pageview"] = "Gallery"
        return context


# delete Gallery
@login_required
def delete_gallery(request, id):
    obj = get_object_or_404(Gallery, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('dash-gallery')
    context = {
        'obj': Gallery.objects.get(id=id),
        'title': "Delete Gallery",
        'pageview': "Gallery"
    }

    return render(request, "home/delete_gallery.html", context)


# product view
class ProductView(View):
    def get(self, request):
        context = {
            'product': Product.objects.all(),
            'title': "Product",
            'pageview': "Home"
        }
        return render(request, 'home/product.html', context)


# category view
class ProductCategoryView(View):
    def get(self, request):
        context = {
            'product': Product.objects.filter(category='Rotary Nickel Screen'),
            'title': "Product",
            'pageview': "Home"
        }
        return render(request, 'home/product.html', context)


class ProductCategory2View(View):
    def get(self, request):
        context = {
            'product': Product.objects.filter(category='Flat Bed Screen'),
            'title': "Product",
            'pageview': "Home"
        }
        return render(request, 'home/product.html', context)


class ProductCategory3View(View):
    def get(self, request):
        context = {
            'product': Product.objects.filter(category='Reactive Dyes'),
            'title': "Product",
            'pageview': "Home"
        }
        return render(request, 'home/product.html', context)


class ProductCategory4View(View):
    def get(self, request):
        context = {
            'product': Product.objects.filter(category='Auxiliaries'),
            'title': "Product",
            'pageview': "Home"
        }
        return render(request, 'home/product.html', context)


class ProductCategory5View(View):
    def get(self, request):
        context = {
            'product': Product.objects.filter(category='Others'),
            'title': "Product",
            'pageview': "Home"
        }
        return render(request, 'home/product.html', context)


# create product
@login_required
def create_product(request):
   if request.method == "POST":
    # form = CreateGalleryForm(request.POST)
    form = CreateProductForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      img_obj = form.instance
      return render(request, 'home/create_product.html', {'form': form, 'img_obj': img_obj})

   else:
      form = CreateProductForm()
   return render(request, 'home/create_product.html', {'form': form, 'title': "Create Product", 'pageview': "Product"})


# product list
class ProductListView(LoginRequiredMixin, View):
    def get(self, request):
        context = {
            'product': Product.objects.all(),
            'title': "Product List",
            'pageview': "Product"
        }
        return render(request, 'home/product_list.html', context)


# edit-product
class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductUpdateForm
    success_url = reverse_lazy('dash-product')
    template_name = 'home/edit-product.html'

    success_message = "Product was updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        context["title"] = "Update Product"
        context["pageview"] = "Product"
        return context


# delete product
@login_required
def delete_product(request, id):
    obj = get_object_or_404(Product, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('dash-product')
    context = {
        'obj': Product.objects.get(id=id),
        'title': "Delete Product",
        'pageview': "Product"
    }

    return render(request, "home/delete_product.html", context)
