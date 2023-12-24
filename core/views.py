from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.urls import reverse
from core.models import Post, Category
from django.db.models import Q
from core.forms import NewPostForm, CommentForm, EditPostForm
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

User = get_user_model()


def index(request):
    """Display a list of posts on the homepage."""
    posts = Post.objects.filter(status=1).order_by('-created_on')
    cat = Category.objects.order_by('cat')
    context = {'cat': cat, 'posts': posts}
    return render(request, 'core/index.html', context)


def about_us(request):
    """Display the 'About Us' page."""
    return render(request, 'core/about.html')


def detail_post(request, author, slug):
    """Display details of a specific post."""
    post = get_object_or_404(Post, author__username=author, slug__iexact=slug)
    context = {'post': post}
    return render(request, 'core/detail.html', context)


def comments(request, author, slug):
    """Handle comments for a specific post."""
    post = get_object_or_404(Post, author__username=author, slug=slug)
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
        context = {'form': form}
        return render(request, 'core/detail.html', context)


@login_required
def new_post(request):
    """Create a new post."""
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect(reverse('core:detail', args=[request.user.username, post.slug]))
        else:
            context = {'filledform': form, 'form': form}
            return render(request, 'core/newpost.html', context)
    else:
        form = NewPostForm()
        context = {'form': form}
        return render(request, 'core/newpost.html', context)


@login_required
def edit_post(request, author, slug):
    """Edit existing post"""
    post = get_object_or_404(Post, author__username=author, slug=slug)

    # Ensure the logged-in user is the author of the post
    if author != request.user.username:
        raise Http404

    if request.method == 'POST':
        form = EditPostForm(request.POST, request.FILES or None, instance=post)
        if form.is_valid():
            form.save()
            return redirect(reverse('core:detail', args=[request.user.username, post.slug]))
    else:
        form = EditPostForm(instance=post)

    context = {'post': post, 'form': form}
    return render(request, 'core/edit.html', context)


@login_required
def delete_post(request, author, slug):
    """Delete a post from the database and media too."""
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
    """search a post with matching title."""
    if request.method == 'GET':
        query = request.GET.get('q')

    search_posts = Post.objects.filter(
        Q(title__icontains=query) | Q(), status=1).order_by('-created_on')

    # search_user = User.objects.filter(Q(username__icontains=query) | Q(full_name__icontains=query))

    context = {
        'object_list': search_posts, 'query': query
    }
    return render(request, 'core/search.html', context)


def profile(request, profile):
    """Display user profile and associated posts."""
    user_profile = get_object_or_404(User, username=profile)
    posts = Post.objects.filter(
        author__username=profile, status=1).order_by('-created_on')
    context = {'profile': user_profile, 'posts': posts}
    return render(request, 'core/profile.html', context)


@login_required
def dashboard(request):
    post = Post.objects.filter(author=request.user).order_by('-created_on')
    context = {'post_count': post.count(), 'posts': post}
    return render(request, 'core/dashboard.html', context)


@login_required
def my_bookmarks(request):
    """Display the post bookmarked by the logged-in user."""
    user_bookmarks = Post.objects.filter(bookmarks=request.user)
    return render(request, 'core/bookmarks.html', {'bookmarks': user_bookmarks})


@login_required
def like_view(request, author, slug):
    """Handle post likes."""
    post = get_object_or_404(Post, author__username=author, slug__iexact=slug)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect(reverse('core:detail', args=[post.author, post.slug]))


@login_required
def bookmark_view(request, author, slug):
    """Handle post bookmarks."""
    post = get_object_or_404(Post, author__username=author, slug__iexact=slug)
    if request.user in post.bookmarks.all():
        post.bookmarks.remove(request.user)
    else:
        post.bookmarks.add(request.user)
    return redirect(reverse('core:detail', args=[post.author, post.slug]))
