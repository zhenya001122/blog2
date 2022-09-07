import logging
from django.shortcuts import render, redirect

from posts.forms import PostForm
from posts.models import Post

logger = logging.getLogger(__name__)


def index(request):
    # for key, value in request.POST.items():
    #     logger.info(f"POST param: {key}={value}")

    # if request.method == "GET":
    #     value = request.GET.get("value")
    #     post_list = Address.objects.get(phone=value)
    #     return HttpResponse(post_list)
    posts = Post.objects.all()
    return render(request, "posts_list.html", {"posts": posts})

def add_posts(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            Post.objects.create(author=request.user, **form.cleaned_data)
            return redirect("/")
    else:
        form = PostForm()
    return render(request, "posts/add_post.html", {'form': form})