from django.core.paginator import Paginator
from django.shortcuts import redirect, render,get_object_or_404
from django.views.generic import TemplateView,CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import Post,Group,User,Comments
from .forms import PostForm,CommentForm

from django.views.decorators.cache import cache_page #Кеширование


@cache_page(20)
@login_required
def index(request):
    template = 'post/index.html'
    
    keyword=request.GET.get("q",None)
    if keyword:
        posts = Post.objects.filter(text__contains=keyword).select_related('author').select_related('group')
    else:
        posts = Post.objects.all().order_by('-pub_date').select_related('author').select_related('group')
        
    paginator = Paginator(posts,10)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)
    
    context = {'page_obj':page_obj,'posts':posts,'keyword':keyword}
    return render(request, template, context)


def group_posts(request, slugs):
    template = 'post/group_post.html'
    group = get_object_or_404(Group,adress=slugs)
    posts=Post.objects.filter(group=group).order_by('-pub_date')[:10].select_related('author')
    title = 'Группы'
    
    paginator = Paginator(posts,10)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)

    context = {'title':title, 'group':group, 'posts':posts, 'page_obj':page_obj}
    return render(request, template, context)

def profile(request,username):
    name=get_object_or_404(User,username=username)
    posts=Post.objects.filter(author=name).select_related('author')
    post_count=posts.count
    
    context={'username':username,'posts':posts,'post_count':post_count}
    return render(request,'post/profile.html',context)


@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post,id=post_id)
    
    form = CommentForm(request.POST or None)
    if form.is_valid(): 
        comment = form.save(commit=False)
        comment.author = request.user
        comment.post = post
        comment.save()
    return redirect('post:post_detail', post_id=post_id) 


def post_detail(request,post_id):
    posts = get_object_or_404(Post,id=post_id)
    post_count = Post.objects.filter(author=posts.author).count 
    form = CommentForm(request.POST or None)
    comments = Comments.objects.filter(post=posts)
    comments_count=Comments.objects.filter(post=posts).count()
    
    context={'posts':posts,'post_count':post_count,'form':form,'comments':comments,'count':comments_count}
    return render(request,'post/post_detail.html',context)


@login_required
def post_create(request):
    form = PostForm(request.POST or None)
    if not form.is_valid():
        return render(request, 'post/create_post.html', {'form': form})
    post = form.save(commit=False)
    post.author = request.user
    post.save()
    return redirect("post:profile",request.user.username)




