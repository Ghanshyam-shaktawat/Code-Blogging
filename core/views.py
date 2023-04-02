from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from core.models import Post

# def index(request):
#     posts = Post.objects.order_by('-pub_date')
#     context = {'posts': posts}
#     return render(request, 'core/index.html', context)

# def post(request,slug):
#     post = Post.objects.get(slug=slug)
#     context = {
#         'post': post,
#     }
#     return render(request, 'post.html', context)

# def newPost(request):
#     post = Post()
#     if request.method == 'POST':
#         post.title = request.POST.get('title')
#         post.snippets = request.POST.get('snippets')
#         post.body = request.POST.get('body')
#         post.save()        
#         return render(request, 'core/create.html')

class IndexView(ListView):
    """Shows the list of post on the homepage."""
    model = Post
    template_name = 'core/index.html'
    context_object_name = 'posts'
    
    def get_queryset(self):
        return Post.objects.filter(status=1).order_by('-created_on')

class PostDetailView(DetailView):
    """Detail view of the post for readers."""
    model = Post
    template_name = 'core/detail.html'
    