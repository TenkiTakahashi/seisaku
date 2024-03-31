from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .models import Tweet

# この関数を編集した


def index(request):
    tweet_list = Tweet.objects.all()
    return render(
        request,
        'a/index.html',
        {'tweet_list': tweet_list}
    )


def post(request):
    message = request.POST['message']
    point = request.POST['point']
    name = request.POST['name']
    tweet = Tweet(
        message=message,
        point=point,
        name=name
    )
    tweet.save()
    return HttpResponseRedirect(reverse('a:index'))
