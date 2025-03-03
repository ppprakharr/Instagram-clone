from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from post.models import Post, Tag, Follow, Stream

def index(request):
    user = request.user
    posts = Stream.objects.filter(user=user)
    group_ids = []
    for post in posts:
        group_ids.append(post.post.id)
    post_items = Post.objects.filter(id__in=group_ids).all().order_by('-posted')
    context={
        'post_items':post_items
    }
    return render(request, 'post/index.html',context)

# Create your views here.
