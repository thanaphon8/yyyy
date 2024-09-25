from django.urls import path
from . import views  # Import views from the same app
urlpatterns = [
    path('', views.homePage, name='home-page'),
    path('naveber', views.navebar, name='navebar'),
    path('register', views.registerPage, name='register'),
    path('contact', views.contactPage, name='contact'),
    path('login', views.loginPage, name='login'),
    path('event', views.eventPage, name='event'),
    path('product', views.productPage, name='product'),
]
