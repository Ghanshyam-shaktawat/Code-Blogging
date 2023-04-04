from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from core.models import Post
from core.forms import NewPostForm

def index(request):
    posts = Post.objects.filter(status=0).order_by('-created_on')
    context = {'posts': posts}
    return render(request, 'core/index.html', context)

def detail_post(request,slug):
    post = Post.objects.get(slug=slug)
    context = {
        'post': post,
    }
    return render(request, 'core/detail.html', context)

def new_post(request):
    if request.method == 'POST':
        form = NewPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('detail', args=[request.POST.get('slug')]))
    else:
        form = NewPostForm()
        context = {'form': form}
        return render(request, 'core/newpost.html', context)
