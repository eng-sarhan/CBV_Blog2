from django.db.models import Count, Q
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import PostForm, CommentForm
from .models import Post, Author, Category, PostView


def get_author(user):
    qs = Author.objects.filter(user=user)
    if qs.exists():
        return qs[0]
    return None


class SearchView(View):
    def get(self, request, *args, **kwargs):
        queryset = Post.objects.all()
        query = request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) |
                Q(categories__title__icontains=query)
                # |Q(author__username__icontains=query)
            ).order_by('-timestamp').distinct()
        context = {
            'queryset': queryset
        }
        return render(request, 'posts/search_results.html', context)


def get_category_count():
    queryset = Post \
        .objects \
        .values('categories__title') \
        .annotate(Count('categories__title'))
    return queryset


class PostListView(ListView):
    model = Post
    template_name = 'posts/blog.html'
    context_object_name = 'posts'
    cats = Category.objects.all()
    # byAuthor = User.objects.all()
    paginate_by = 4

    def get_context_data(self, **kwargs):
        category_count = get_category_count()
        most_recent = Post.objects.order_by('-timestamp')[:3]
        context = super().get_context_data(**kwargs)
        context['most_recent'] = most_recent
        context['page_request_var'] = "page"
        context['category_count'] = category_count
        return context


def CategoryView(request, cats):
    category_posts = Post.objects.filter(categories__title=cats.replace('-', ' '))
    return render(request, 'posts/categories.html',
                  {'cats': cats.replace('-', ' ').title(), 'category_posts': category_posts})


class UserPostListView(ListView):
    model = Post
    template_name = 'posts/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 4

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(id=self.request.user.id).order_by('-timestamp')


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post.html'
    context_object_name = 'post'
    form = CommentForm()

    def get_object(self):
        obj = super().get_object()
        if self.request.user.is_authenticated:
            PostView.objects.get_or_create(
                user=self.request.user,
                post=obj
            )
        return obj

    def get_context_data(self, **kwargs):
        category_count = get_category_count()
        most_recent = Post.objects.order_by('-timestamp')[:3]
        context = super().get_context_data(**kwargs)
        context['most_recent'] = most_recent
        context['page_request_var'] = "page"
        context['category_count'] = category_count
        context['form'] = self.form
        return context

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            post = self.get_object()
            form.instance.user = request.user
            form.instance.post = post
            form.save()
            return redirect(reverse("posts:post-detail", kwargs={
                'pk': post.pk
            }))


class PostCreateView(CreateView):
    model = Post
    template_name = 'posts/post_create.html'
    form_class = PostForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create'
        return context

    def form_valid(self, form):
        form.instance.author = get_author(self.request.user)
        form.save()
        return redirect(reverse("posts:post-detail", kwargs={
            'pk': form.instance.pk
        }))


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'posts/post_create.html'
    form_class = PostForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update'
        return context

    def form_valid(self, form):
        form.instance.author = get_author(self.request.user)
        form.save()
        return redirect(reverse("posts:post-detail", kwargs={
            'pk': form.instance.pk
        }))


class PostDeleteView(DeleteView):
    pass
    model = Post
    success_url = '/blog'
    template_name = 'posts/post_confirm_delete.html'


def about(request):
    return render(request, 'posts/about.html')
