from django.shortcuts import render,redirect
from .forms import SignupForm, ExpenceForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from .models import Expence, CustomUser
# Create your views here.






def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        messages.success(request, "Registration successful.")
    else:
        form = SignupForm()
        messages.error(request, "Unsuccessful registration. Invalid information.")
    return render(request, 'App/signup.html', {'form': form})

def login_request(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'App/login.html')

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.")
	return redirect("login")

@login_required(login_url='login')
def showall(request):
    if request.user.is_Admin:
        # Get all expenses
        expence = Expence.objects.all()
    else:
        # Get expenses created by the current user
        nowuser = request.user
        expence = Expence.objects.filter(Created_by=nowuser)
    return render(request, 'App/showall.html', {'expence': expence})


def userall(request):
    customob = CustomUser.objects.all()
    context = {
        'customob': customob,

    }
    return render(request, 'App/Userall.html', context)

def save(request):
    name1 = request.POST.get('name')
    date1 = request.POST.get('dateofexpence')
    category1 = request.POST['category']
    description1 = request.POST['description']
    amount1 = request.POST['amount']
    created_by1 = request.user

    expense = Expence.objects.create(
        Name=name1,
        Date_of_Expense=date1,
        Category=category1,
        Description=description1,
        Amount=amount1,
        Created_by=created_by1
    )
    messages.success(request, "Your new expence is created.")
    return redirect('/')

def delete(request, id):
  expence = Expence.objects.filter(id=id).delete()

  return redirect('/')

def update(request, id):
    if request.method == 'POST':
        name1 = request.POST.get('name')
        date1 = request.POST.get('dateofexpence')
        category1 = request.POST['category']
        description1 = request.POST['description']
        amount1 = request.POST['amount']
        created_by1 = request.user

        expense = Expence(
            id= id,
            Name=name1,
            Date_of_Expense=date1,
            Category=category1,
            Description=description1,
            Amount=amount1,
            Created_by=created_by1
        )
        expense.save()
        messages.success(request, "Your new expence record is updated.")
    return redirect('/')