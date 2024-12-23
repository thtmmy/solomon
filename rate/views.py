from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

# Create your views here.
from .models import *
from .forms import *

from .decorators import unauthenticated_user, allowed_users, admin_only

# Create your views here.
from .models import *

def index(request):
    context = {}
    return render (request, "rate/index.html", context)

def contact(request):
    context = {}
    return render (request, "rate/contact.html", context)

def support(request):
    context = {}
    return render (request, "rate/support.html", context)

def news(request):
    context = {}
    return render (request, "rate/news.html", context)

def about(request):
    context = {}
    return render (request, "rate/about.html", context)

def kyc(request):
    context = {}
    return render (request, "rate/kyc.html", context)

def info(request):
    context = {}
    return render (request, "rate/info.html", context)

def faq(request):
    context = {}
    return render (request, "rate/faq.html", context)


def education(request):
    context = {}
    return render (request, "rate/education.html", context)

def privacy_policy(request):
    context = {}
    return render (request, "rate/privacy_policy.html", context)

@login_required (login_url = "login")
def customer(request):
    context = {}
    return render (request, "rate/customer.html", context)

@login_required (login_url = "login")
def withdraw_history(request):
    user = request.user

    transaction = Transaction.objects.filter(user=user)

    context = {'transaction':transaction}
    return render (request, "rate/withdraw_history.html", context)


@login_required (login_url = "login")
def deposit(request):
    context = {}
    return render (request, "rate/deposit.html", context)

def privacy(request):
    context = {}
    return render (request, "rate/privacy.html", context)

def rbc(request):
    context = {}
    return render (request, "rate/rbc.html", context)

def wealth(request):
    context = {}
    return render (request, "rate/wealth.html", context)

def investment(request):
    context = {}
    return render (request, "rate/investment.html", context)

def logoutUser(request):
    logout (request)
    return redirect ('login')

def loginPage(request):
    if request.user.is_authenticated:
        return redirect ('customer')
    else:
        if request.method == 'POST':
            username = request.POST.get ('username')
            password = request.POST.get ('password')

            user = authenticate (request, username = username, password = password)

            if user is not None:
                login (request, user)
                return redirect ('customer')
            else:
                messages.info (request, 'Username OR password is incorrect')

        context = {}
    return render (request, "rate/login.html", context)



def platform(request):
    context = {}
    return render (request, "rate/platform.html", context)

@login_required (login_url = "login")
def referals(request):
    context = {}
    return render (request, "rate/referals.html", context)


@unauthenticated_user
def register(request):
    form = CreateUserForm ()
    if request.method == 'POST':
        form = CreateUserForm (request.POST)
        if form.is_valid ():
            user = form.save ()
            username = form.cleaned_data.get ('username')


            messages.success (request, 'Account was created for ' + username)

            return redirect ('details')

    context = {'form': form}
    return render (request, "rate/register.html", context)

def terms(request):
    context = {}
    return render (request, "rate/terms.html", context)

@login_required (login_url = "login")
def withdraw(request):
    user = request.user

    transaction = user.transaction_set.all()

    if request.method == 'POST':
        data = request.POST
        name = request.POST.getlist('name')
        wallet = request.POST.getlist('wallet')
        amount = request.POST.get('amount')
        time = request.POST.get('time')
        accountnumber = request.POST.get('accountnumber')
        status = request.POST.get('status')
        bank = request.POST.get('bank')
        cashapp = request.POST.get('cashapp')
        email = request.POST.get('email')


        transaction, created = Transaction.objects.get_or_create(
            user=user,
            name=name,
            wallet=wallet,
            amount=amount,
            time=time,
            accountnumber=accountnumber,
            status=status,
            bank=bank,
            cashapp=cashapp,
            email=email
            )

        return redirect('pin')

    context = {'transaction':transaction}
    return render (request, "rate/withdraw.html", context)

@login_required (login_url = "login")
def pin(request):
    context = {}
    return render (request, "rate/pin.html", context)


@login_required (login_url = "login")
def details(request):
    customer = request.user.customer
    form = CustomerForm (instance = customer)

    if request.method == 'POST':
        form = CustomerForm (request.POST, request.FILES, instance = customer)
        if form.is_valid ():
            form.save ()

    context = {'form': form}
    return render (request, "rate/details.html", context)

@login_required (login_url = "login")
def processing(request):
    context = {}
    return render (request, "rate/processing.html", context)