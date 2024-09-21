from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,authenticate
from django.contrib import messages

from .models import Blog

from .forms import BlogModelForm
# Create your views here.
def home(request):
    #a=10/0
    return render(request,'home.html')

def user_login(request):
    if request.method=="POST":
        print("h1")
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            messages.success(request,"Login Successful")
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password")
    else:
        print("h3")
        form=AuthenticationForm()
    return render(request, 'user_login.html')

def user_signUp(request):
    print("h1")
    if request.method=="POST":
        print("h3")
        form=UserCreationForm(request.POST)
        print("h4")
        if form.is_valid():
            print("h5")
            form.save()
            return redirect('home')
        else:
            print("Form is not valid")
            for field in form:
                for error in field.errors:
                    messages.error(request, error)
            for error in form.non_field_errors():
                messages.error(request, error)
    else:
        print('h2')
        form=UserCreationForm()
    
    return render(request, 'user_signUp.html')

def create_post(request):
    if request.method == "POST":
        form = BlogModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Post has been created")
            return redirect('home')
    else:
        form = BlogModelForm()
        return render(request, 'createBlog.html', {'form': form})
    
def show_posts(request):
    posts = Blog.objects.all()
    return render(request, 'Blogs.html',{'posts':posts})

def update_post(request,id):
    blog = get_object_or_404(Blog, id=id)
    blog = get_object_or_404(Blog, id=id)
    
    if request.method == 'POST':
        form = BlogModelForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BlogModelForm(instance=blog)
    
    return render(request, 'updateBlog.html', {'form': form, 'blog': blog})
def delete_post(request,id):
    post = get_object_or_404(Blog, id=id)
    post.delete()
<<<<<<< HEAD
    messages.success(request,"Post has been deleted successfully")
=======
    print("Hello Gitmaster shivani")
    messages.success(request,"Post has been deleted")
>>>>>>> origin/main
        #return redirect('home')
    return render(request, 'home.html')
    



