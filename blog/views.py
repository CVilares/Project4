from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from django.views import generic, View
from .models import Post
from.forms import CommentForm

class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6


class PostDetail(View):

   def get(self, request, slug, *args, **kwargs):
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.filter(approved=True).order_by("-created_on")
    liked = False
    if post.likes.filter(id=self.request.user.id).exists():
        liked = True

    # Inicialize comment_form aqui
    comment_form = CommentForm()

    return render(
        request,
        "post_detail.html",
        {
            "post": post,
            "comments": comments,
            "commented": False,
            "liked": liked,
            "comment_form": comment_form
        },
    )



@login_required
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # Define o autor como o usuário atual
            post.save()
            return redirect('home')  # Redireciona para a página inicial após a adição do post
    else:
        form = PostForm()
    return render(request, 'add_post.html', {'form': form})