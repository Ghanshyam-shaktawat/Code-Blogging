from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, HttpResponse
from django.urls import reverse
from core.models import Post, Comment, Bookmark
from django.db.models import Q
from core.forms import NewPostForm, CommentForm
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

User = get_user_model()

def index(request):
    posts = Post.objects.filter(status=1).order_by('-created_on')
    context = {
        'posts': posts,
        }
    return render(request, 'core/index.html', context)


def detail_post(request, author, slug):
    context = {}
    post = get_object_or_404(Post, author__username=author, slug=slug)
    total_likes = post.total_likes()
    context['post'] = post
    context['likes'] = total_likes

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect(reverse('core:detail', args=[post.author, post.slug]))
        
    else:
        form = CommentForm()
        context['form'] = form  
        return render(request, 'core/detail.html', context)


@login_required
def new_post(request):
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect(reverse('core:detail', args=[request.user.username, request.POST.get('slug')]))
        else:
            context = {'filledform': form, 'form':form}
            return render(request, 'core/newpost.html', context)
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
        form = NewPostForm(request.POST, request.FILES or None, instance=post)
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
        if post.cover_image:
            post.cover_image.delete()
        post.delete()
        return redirect(reverse('core:index'))
    return render(request, 'core/delete.html', {'post': post})
        

def search(request):
    if request.method == 'GET':
        query = request.GET.get('q')

    search_posts = Post.objects.filter(Q(title__icontains=query) | Q(), status=1).order_by('-created_on')

    search_user = User.objects.filter(Q(username__icontains=query) | Q(full_name__icontains=query))

    context = {
        'object_list': search_posts, 'users': search_user, 'query': query
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


@login_required
def my_bookmarks(request):
    user_bookmarks = Bookmark.objects.filter(bookmark_by=request.user)
    return render(request, 'core/bookmarks.html', {'bookmarks': user_bookmarks})