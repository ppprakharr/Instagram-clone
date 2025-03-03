from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from post.models import Post, Tag, Follow, Stream
from post.forms import NewPostForm

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


def new_post(request):
    user=request.user
    if request.method=='POST':
        form=NewPostForm(request.POST,request.FILES)
        if form.is_valid():
            picture = form.cleaned_data.get('picture')
            caption = form.cleaned_data.get('caption')
            tags_obj=[]
            tags=form.cleaned_data.get('tag')
            tag_list=list(tags.split(','))

            for tag in tag_list:
                t,created  = Tag.objects.update_or_create(title=tag.strip(),defaults={'slug':slugify(tag.strip())})
                tags_obj.append(t)
            p,created=Post.objects.get_or_create(picture=picture,caption=caption,user=user)
            p.tag.set(tags_obj)
            p.save()
            return redirect('post:index')
    else:
        form=NewPostForm()
    context={'form':form}
    return render(request,'post/newpost.html',context)

# Create your views here.


