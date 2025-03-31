from django.contrib import admin
from django.urls import path

from realestate import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('signup', views.signup),
    path('aboutus', views.aboutus),
    path('services',views.services),
    path('login', views.login),
    path('logout', views.logout, name='logout'),
    path('register', views.register),
    path('loginaction',views.loginaction),
    path('terms-and-conditions',views.terms_and_conditions),
    path('privacy-policy', views.privacy_policy),
    path('post-property', views.post_property, name='post_property'),
    path('invalid', views.invalid, name='invalid'),
    path('change-password', views.changepassword, name='changepassword'),
    path('forgot-password', views.forgotpassword, name='forgot_password'),
    path('forgotpass', views.forgotpass, name='forgotpass'),
    path('user-profile', views.profile, name='profile'),
    path('update-profile', views.updateprofile, name='updateprofile'),
    path('updatedprofile', views.updatedprofile, name='updatedprofile'),
]