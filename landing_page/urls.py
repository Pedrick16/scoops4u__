from django.urls import path
from landing_page import views


app_name = 'landing_page'
urlpatterns = [
    # login process
    path('', views.landing_page, name='landing_site'),
    path('sign-in/', views.loginView, name='login'),
    path('sign-out/', views.logoutView, name='logout'),

    #landing features
    path('inquiry/', views.inquiry_reseller, name='inquiry_reseller'),
    path('flavors/', views.flavors, name='flavors'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('reseller/', views.reseller, name='reseller'),

    path('send-email/', views.send_email, name='send_email'),
    path('reset-password/', views.reset_password, name='reset_password'),

]