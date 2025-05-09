from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Customer_Table
# Home page / Landing page
def home(request):
  return render(request, 'webapp/index.html') 

# Register a User
def register(request):
  form = CreateUserForm()
  
  if request.method == "POST":
    form = CreateUserForm(request.POST)
    
    if form.is_valid():
      form.save()
      return redirect('login')

  context = {'form': form}
  return render(request, 'webapp/register.html', context = context)

#login a user

def login(request):
  form = LoginForm()
  if request.method == "POST":
    form = LoginForm(request, data = request.POST)
    
    if form.is_valid():
      username = request.POST.get('username')
      password = request.POST.get('password')
      
      user = authenticate(request, username=username, password=password)
      
      if user is not None:
        auth.login(request, user)
        return redirect('dashboard')
      else :
        form.add_error(None, 'Invalid username or password')
        
  context = {'form': form}
  return render(request, 'webapp/login.html', context = context)

# Create a dashboard for a login user
@login_required(login_url='login')
def dashboard(request):
  customer_table = Customer_Table.objects.all()
  context = {'customer_table': customer_table}
  return render(request, 'webapp/dashboard.html', context = context)



# logout a user

def logout(request):
  auth.logout(request)
  return redirect('login')

  