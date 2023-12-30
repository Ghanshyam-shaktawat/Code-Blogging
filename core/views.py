from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Count
from django.http import Http404
from django.urls import reverse
from core.models import Post, Category
from django.db.models import Q
from core.forms import NewPostForm, CommentForm, EditPostForm
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

User = get_user_model()


def index(request):
    """
    Display a list of posts on the homepage.

    Returns:
        HttpResponse: Rendered HTML response with a list of posts.
    """
    posts = Post.objects.filter(status=1).order_by('-created_on')
    cats = Category.objects.order_by('cat')
    context = {'cats': cats, 'posts': posts}
    return render(request, 'core/index.html', context)


def about_us(request):
    """
    Display the 'About Us' page.

    Returns:
        HttpResponse: Rendered HTML response for the 'About Us' page.
    """
    return render(request, 'core/about.html')


def detail_post(request, author, slug):
    """
    Display details of a specific post.

    Returns:
        HttpResponse: Rendered HTML response with details of the post.
    """
    post = get_object_or_404(Post, author__username=author, slug__iexact=slug)
    context = {'post': post}
    return render(request, 'core/detail.html', context)


def comments(request, author, slug):
    """
    Handle comments for a specific post.

    Returns:
        HttpResponse: Rendered HTML response with comments for the post.
    """
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
    """
    Create a new post.

    Returns:
        HttpResponse: Rendered HTML response for creating a new post.
    """
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
    """
    Edit existing post.

    Returns:
        HttpResponse: Rendered HTML response for editing an existing post.
    """
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
    """
    Delete a post from the database and media too.

    Returns:
        HttpResponse: Redirects to the user's dashboard after deleting the post.
    """
    post = get_object_or_404(Post, author__username=author, slug=slug)
    if request.user != post.author:
        raise Http404

    if request.method == 'POST':
        if post.cover_image:
            post.cover_image.delete()
        post.delete()
        return redirect(reverse('core:dashboard'))
        
    return redirect(reverse('core:dashboard'))


def search(request):
    """
    Search a post with a matching title.

    Returns:
        HttpResponse: Rendered HTML response with search results.
    """
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
    """
    Display user profile and associated posts.

    Returns:
        HttpResponse: Rendered HTML response with user profile and posts.
    """
    user_profile = get_object_or_404(User, username=profile)
    posts = Post.objects.filter(
        author__username=profile, status=1).order_by('-created_on')
    context = {'profile': user_profile, 'posts': posts}
    return render(request, 'core/profile.html', context)


@login_required
def dashboard(request):
    """
    Display the user's dashboard with their posts, likes, and comments.

    Returns:
        HttpResponse: Rendered HTML response with the user's dashboard information.
    """
    posts = Post.objects.filter(author=request.user).order_by('-created_on').annotate(
        total_likes=Count('likes', distinct=True),
        total_comments=Count('comments', distinct=True)
    )

    context = {
        'post_count': posts.count(),
        'posts': posts,
        'total_likes_received': sum(post.total_likes for post in posts),
        'total_comments_received': sum(post.total_comments for post in posts),
    }

    return render(request, 'core/dashboard.html', context)


@login_required
def my_bookmarks(request):
    """
    Display posts bookmarked by the logged-in user.

    Returns:
        HttpResponse: Rendered HTML response with bookmarked posts.
    """
    user_bookmarks = Post.objects.filter(bookmarks=request.user)
    return render(request, 'core/bookmarks.html', {'bookmarks': user_bookmarks})


@login_required
def like_view(request, post_id):
    """
    Handle the like/unlike action for a post.

    Parameters:
        request (HttpRequest): The HTTP request object.
        post_id (int): The ID of the post to be liked/unliked.

    Returns:
        JsonResponse: A JSON response containing the updated like count and whether the user has liked the post.

    Raises:
        Http404: If the post with the specified ID does not exist.
    """
    post = get_object_or_404(Post, id=post_id)

    if request.user in post.likes.all():
        post.likes.remove(request.user)
        is_liked = False
    else:
        post.likes.add(request.user)
        is_liked = True

    like_count = post.likes.count()

    return JsonResponse({'like_count': like_count, 'is_liked': is_liked})


@login_required
def bookmark_view(request, post_id):
    """
    Handle the bookmark/unbookmark action for a post.

    Parameters:
        request (HttpRequest): The HTTP request object.
        post_id (int): The ID of the post to be liked/unliked.

    Returns:
        JsonResponse: A JSON response containing the updated bookmark count and whether the user has bookmared the post.

    Raises:
        Http404: If the post with the specified ID does not exist.
    """
    post = get_object_or_404(Post, id=post_id)
    
    if request.user in post.bookmarks.all():
        post.bookmarks.remove(request.user)
        is_bookmarked = False
    else:
        post.bookmarks.add(request.user)
        is_bookmarked = True
    bookmark_count = post.bookmarks.count()

    return JsonResponse({'bookmark_count': bookmark_count, 'is_bookmarked': is_bookmarked})


def category_view(request, cat):
    """
    Display posts of a specific category.

    Returns:
        HttpResponse: Rendered HTML response with posts of the specified category.
    """
    posts = Post.objects.filter(category__cat=cat.lower()).order_by('-created_on')
    return render(request, 'core/category.html', {'cat': cat, 'posts': posts})
