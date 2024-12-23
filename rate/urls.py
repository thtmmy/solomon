from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path ('', views.index, name = "index"),
    path ('about/', views.about, name = "about"),
    path ('education/', views.education, name = "education"),
    path ('customer/', views.customer, name = "customer"),
    path ('faq/', views.faq, name = "faq"),
    path ('withdraw_history/', views.withdraw_history, name = "withdraw-history"),
    path ('deposit/', views.deposit, name = "deposit"),
    path ('privacy_policy/', views.privacy_policy, name = "privacy_policy"),
    path ('referals/', views.referals, name = "referals"),
    path ('investment/', views.investment, name = "investment"),
    path ('register/', views.register, name = "register"),
    path ('login/', views.loginPage, name = "login"),
    path ('logout/', views.logoutUser, name = "logout"),
    path ('privacy/', views.privacy, name = "privacy"),
    path ('withdraw/', views.withdraw, name = "withdraw"),
    path ('details/', views.details, name = "details"),
    path ('pin/', views.pin, name = "pin"),
    path ('support/', views.support, name = "support"),
    path ('news/', views.news, name = "news"),
    path ('processing/', views.processing, name = "processing"),
    path ('info/', views.info, name = "info"),
    path ('kyc/', views.kyc, name = "kyc"),
    path ('wealth/', views.wealth, name = "wealth"),
    path ('terms/', views.terms, name = "terms"),
    path ('contact/', views.contact, name = "contact"),
 ]