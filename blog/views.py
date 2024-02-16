from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect, Http404
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .models import Post, Comment
# MostLikedPosts
from .forms import CommentForm, PostForm

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



class AddPost(LoginRequiredMixin,
              generic.CreateView):
    """
    To add a post and get a feddback message.
    """
    model = Post
    template_name = 'add_post.html'
    form_class = PostForm
    success_message = 'Post added and waiting for approval!'

    def form_valid(self, form):
        if self.request.POST.get('status'):
            form.instance.status = int(self.request.POST.get('status'))
        form.instance.author = self.request.user
        messages.info(self.request, "Post added and waiting for approval")
        return super().form_valid(form)