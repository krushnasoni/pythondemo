from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import BlogForm

def blog_list(request):
    blog = Post.objects.all()
    return render(request,'blog/view_blog_list.html',{'blogs':blog})

def blog_new(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/blog_list')
    else:
        form = BlogForm()
    return render(request, 'blog/blog_edit.html', {'form': form})

def blog_edit(request, pk):
    person = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('/blog_list')
    else:
        form = BlogForm(instance=person)
    return render(request, 'blog/blog_edit.html', {'form': form})