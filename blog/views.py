from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from .models import Post, Comment
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse_lazy
from .forms import CommentForm, PostForm
from django.views.generic.edit import UpdateView
from .forms import UserProfileForm
from django.contrib.auth.decorators import login_required
from .models import UserProfile




class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6


class PostDetail(View):
    """
    Displays a single post
    """

    def get(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if (post.status == 0) and (post.author != request.user):
            raise Http404("Post not found.")
        comments = post.comments.filter(approved=True).order_by('-created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            'post_detail.html',
            {
                'post': post,
                'comments': comments,
                'commented': False,
                'liked': liked,
                'comment_form': CommentForm(),
            },
        )

    def post(self, request, slug, *args, **kwargs):

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )



class AddPost(LoginRequiredMixin, CreateView):
    """
    To add a post and get a feedback message.
    """
    model = Post
    template_name = 'add_post.html'
    form_class = PostForm
    success_message = 'Post added and waiting for approval!'

    def form_valid(self, form):
        if self.request.POST.get('status'):
            form.instance.status = int(self.request.POST.get('status'))
        form.instance.author = self.request.user
        # Salva o post
        response = super().form_valid(form)

        # Adiciona uma mensagem de sucesso
        messages.success(self.request, self.success_message)

        # Redireciona para a página inicial após adicionar o post
        return HttpResponseRedirect(reverse_lazy('home'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context



class DeletePostView(generic.DeleteView):
    """
    To delete author's own posts
    """
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
    

@login_required
def edit_profile(request):
    user_profile = request.user.userprofile
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=user_profile)
    return render(request, 'edit_profile.html', {'form': form})


class UserProfileView(View):
    def get(self, request, username):
        user = User.objects.get(username=username)
        
        userProfile = UserProfile.objects.get(user=user)
        return render(request, 'user_profile.html', {'user': user})


    
class PostLike(View):
    
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))