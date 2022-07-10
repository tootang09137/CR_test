from django.shortcuts import render, redirect, get_object_or_404
from .forms import BlogForm
from django.utils import timezone
from .models import Post

# Create your views here.

def main(request):
    return render(request, 'main.html')

def write(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.pub_date = timezone.now()
            form.save()
            return redirect('main')
    else:
        form = BlogForm
        return render(request, 'write.html', {'form':form})

def read(request):
    blogs = Post.objects
    return render(request, 'read.html', {'blogs':blogs})

def detail(request, id):
    blog = get_object_or_404(Post, id=id)
    return render(request, 'detail.html', {'blog':blog})

def edit(request, id):
    blog = get_object_or_404(Post, id=id)
    if request.method == "POST":
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save(commit=False)
            form.save()
            return redirect('read')
    else:
        form = BlogForm(instance=blog)
        return render(request, 'edit.html', {'form':form})

def delete(request, id):
    blog = get_object_or_404(Post, id=id)
    blog.delete()
    return redirect('read')
