from django.conf.urls import url
from django.urls import path , re_path
from blog_app import views

urlpatterns = [
    path('', views.PostListView.as_view(), name = 'post_list'),
    path('about/', views.AboutView.as_view(), name='about'),
    re_path(r'^post/(?P<pk>\d+)$', views.PostDetailView.as_view(), name='post_detail'),
    path('post/new/', views.CreatePostView.as_view(), name = 'post_new'),
    re_path(r'^post/(?P<pk>\d+)/edit/$', views.PostUpdateView.as_view(), name='post_edit'),
    re_path(r'^post/(?P<pk>\d+)/remove/$', views.PostDeleteView.as_view(), name='post_delete'),
    path('drafts/', views.DraftListView.as_view(), name='post_draft_list'),
]

