# Create for main_site/core
from django.shortcuts import render

from posts.models import Post


def index(request):
    latest_post_list = Post.objects.order_by('-pub_date')[:5]
    context = {'latest_post_list': latest_post_list}
    return render(request, 'core/index.html', context)