from django.urls import path, re_path
from posts import views
from posts.views import PostListView, PostCreateView, PostDetailView, PostUpdateView, PostDeleteView, \
    UserPostListView, SearchView, CategoryView

app_name = 'posts'
urlpatterns = [
    # path('', IndexView.as_view(), name='home'),
    # path('blog/', post_list, name='post-list'),
    path('', PostListView.as_view(), name='post-list'),

    re_path(r'^user/(?P<username>\w{0,50})/$', UserPostListView.as_view(), name='user-posts'),

    # path('user/<str:username>/', UserPostListView.as_view(), name="user-posts"),
    path('search/', SearchView.as_view(), name='search'),
    path('create/', PostCreateView.as_view(), name='post-create'),
    path('post/<pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name="blog-about"),

    # path('user/<str:username>/', AuthorPostView, name='post-author'),
    path('categories/<str:cats>/', CategoryView, name='categories'),

    # path('post', post_view, name='post_view'),
]
