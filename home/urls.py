from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),  # home
    path('about', views.AboutView.as_view(), name='about'),  # about
    # path('contact', views.ContactView.as_view(), name='contact'),  # contact
    path('contact', views.contact, name='contact'),  # contact
    path('gallery', views.GalleryView.as_view(), name='gallery'),  # gallery
    path('product', views.ProductView.as_view(), name='product'),  # product

    path('dashboard/gallery-create', views.create_gallery, name='gallery-create'),  # Gallery create
    path('dashboard/gallery-list', views.GalleryListView.as_view(), name='dash-gallery'),  # Gallery list
    path('dashboard/gallery-edit/<int:pk>', views.GalleryUpdateView.as_view(), name='gallery-edit'),  # Gallery edit
    path('dashboard/delete-gallery/<int:id>', views.delete_gallery, name='delete-gallery'),  # Gallery delete

    path('dashboard/product-create', views.create_product, name='product-create'),  # Product create
    path('dashboard/product-list', views.ProductListView.as_view(), name='dash-product'),  # Product list
    path('dashboard/product-edit/<int:pk>', views.ProductUpdateView.as_view(), name='product-edit'),  # Product edit
    path('dashboard/delete-product/<int:id>', views.delete_product, name='delete-product'),  # Product delete

    path('product/category', views.ProductCategoryView.as_view(), name='product-category'),  # Category list
    path('product/category2', views.ProductCategory2View.as_view(), name='product-category2'),  # Category list
    path('product/category3', views.ProductCategory3View.as_view(), name='product-category3'),  # Category list
    path('product/category4', views.ProductCategory4View.as_view(), name='product-category4'),  # Category list
    path('product/category5', views.ProductCategory5View.as_view(), name='product-category5'),  # Category list

    path('dashboard/slider-create', views.create_slider, name='slider-create'),  # Slider create
    path('dashboard/slider-list', views.SliderListView.as_view(), name='dash-slider'),  # Product list
    path('dashboard/slider-edit/<int:pk>', views.SliderUpdateView.as_view(), name='slider-edit'),  # Slider edit
    path('dashboard/delete-slider/<int:id>', views.delete_slider, name='delete-slider'),  # Slider delete

    path('dashboard/product-slider-create', views.create_product_slider, name='product-slider-create'),  # product Slider create
    path('dashboard/product-slider-list', views.ProductSliderListView.as_view(), name='dash-product-slider'),  # Product slider list
    path('dashboard/product-slider-edit/<int:pk>', views.ProductSliderUpdateView.as_view(), name='product-slider-edit'),  # Product Slider edit
    path('dashboard/delete-product-slider/<int:id>', views.delete_product_slider, name='delete-product-slider'),  # product Slider delete

    path('dashboard/create-home-description', views.add_home_about, name='home-description-create'),  # Home description create
    path('dashboard/home-description', views.ShowDescriptionView.as_view(), name='home-description'),  # home description
    path('dashboard/description-edit/<int:pk>', views.DescriptionUpdateView.as_view(), name='description-edit'),  # home description edit

    path('dashboard/about-description-edit/<int:pk>', views.AboutDescriptionUpdateView.as_view(), name='about-description-edit'),  # home description edit
    path('dashboard/create-about-description', views.add_about_description, name='about-description-create'),  # add about description
    path('dashboard/about-description', views.AboutDescriptionView.as_view(), name='about-description'),  # about description
]
