from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, HttpResponse
from django.urls import reverse
from core.models import Post
from django.db.models import Q
from core.forms import NewPostForm
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

User = get_user_model()

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


@login_required
def edit_post(request, author, slug):
    """Edit post view in which we take post object and send it to the form instance."""
    
    post = get_object_or_404(Post, author__username=author, slug=slug)
    
    # Here, we are verifying if the author == logged in user, if yes then
    # send to edit post or else raise a 404 error.
    if author != request.user.username:
        raise Http404
        
    if request.method != 'POST':
        form = NewPostForm(instance=post)
    else:
        form = NewPostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('core:detail', args=[request.user.username, post.slug]))

    context = {'post': post, 'form': form}
    return render(request, 'core/edit.html', context)        


@login_required
def delete_post(request, author, slug):
    post = get_object_or_404(Post, author__username=author, slug=slug)
    if request.user != post.author:
        raise Http404
    
    if request.method == 'POST':
        post.delete()
        return redirect(reverse('core:index'))
    return render(request, 'core/delete.html', {'post': post})
        

def search(request):
    results = []
    if request.method == 'GET':
        query = request.GET.get('q')
        
    results = Post.objects.filter(Q(title__icontains=query) | Q(), status=1).order_by('-created_on')
    context = {
        'object_list': results, 'query': query
    }
    return render(request, 'core/search.html', context)
        
        
def profile(request, profile):
    user_profile = get_object_or_404(User, username=profile)
    posts = Post.objects.filter(author__username=profile, status=1).order_by('-created_on')
    context = {
        'profile': user_profile,
        'posts': posts,
    }
    return render(request, 'core/profile.html', context)
