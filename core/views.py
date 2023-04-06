from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from core.models import Post
from django.db.models import Q
from core.forms import NewPostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from bloggingApp import settings

def index(request):
    posts = Post.objects.filter(status=1).order_by('-created_on')
    context = {'posts': posts}
    return render(request, 'core/index.html', context)


def detail_post(request, author, slug):
    post = get_object_or_404(Post, author__username=author, slug=slug)
    context = {
        'post': post
    }
    return render(request, 'core/detail.html', context)

@login_required
def new_post(request):    
    if request.method == 'POST':
        form = NewPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect(reverse('core:detail', args=[request.user.username, request.POST.get('slug')]))
    else:
        form = NewPostForm()
        context = {'form': form}
        return render(request, 'core/newpost.html', context)


def search(request):
    results = []
    if request.method == 'GET':
        query = request.GET.get('q')
        
    results = Post.objects.filter(Q(title__icontains=query), status=1).order_by('-created_on')
    return render(request, 'core/search.html', {'object_list': results, 'query': query})
        
        
def profile(request, profile):
    user_profile = get_object_or_404(User, username=profile)
    posts = Post.objects.filter(author__username=profile, status=1).order_by('-created_on')
    context = {
        'profile': user_profile,
        'posts': posts,
    }
    return render(request, 'core/profile.html', context)