from django.shortcuts import render
from django.views import View


class IndexView(View):
    def get(self, request):
        return render(request, 'home.html')


class DetailView(View):
    def get(self, request):
        return render(request, 'detail.html')


class FeedView(View):
    def get(self, request):
        return render(request, 'feed.html')


class TopicView(View):
    def get(self, request):
        return render(request, 'topic.html')

class CreateTopicView(View):
    def get(self, request):
        return render(request, 'create-topic.html')

class ProfileView(View):
    def get(self, request):
        return render(request, 'profile.html')

class EditProfileView(View):
    def get(self, request):
        return render(request, 'edit-profile.html')

class ProfileSettingView(View):
    def get(self, request):
        return render(request, 'profile-setting.html')
