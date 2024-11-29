from django.urls import path

from posts import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('detail', views.DetailView.as_view(), name='detail'),
    path('feed', views.FeedView.as_view(), name='feed'),
    path('topic', views.TopicView.as_view(), name='topic'),
    path('create-topic', views.CreateTopicView.as_view(), name='create-topic'),
    path('profile', views.ProfileView.as_view(), name='profile'),
    path('edit-profile', views.EditProfileView.as_view(), name='edit-profile'),
    path('profile-setting', views.ProfileSettingView.as_view(), name='profile-setting'),
]
