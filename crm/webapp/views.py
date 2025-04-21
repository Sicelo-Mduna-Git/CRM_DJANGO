from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm

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
      # return redirect('login')

  context = {'form': form}
  return render(request, 'webapp/register.html', context = context)

  