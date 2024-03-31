from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Tweet


class IndexView(TemplateView):
    template_name = 'index.html'

def index(request):
    tweet_list = Tweet.objects.all()
    return render(
        request,
        'photo:index.html',
        {'tweet_list': tweet_list}
    )
