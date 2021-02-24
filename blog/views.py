from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .models import Blogpost,Comment
from django.core.paginator import Paginator
from next_prev import next_in_order, prev_in_order
from .forms import CommentForm
# Create your views here.
def bloghome(request):
    allposts=Blogpost.objects.all().order_by('-sno')
    paginator=Paginator(allposts,6)
    page=request.GET.get('page')
    allposts=paginator.get_page(page)
    threepost=Blogpost.objects.all().order_by('-sno')[0:3]
    context={'allposts':allposts,'threepost':threepost}
    return render(request,'blogt/bloghome.html',context)
def blogpost(request,slug):
    qs = Blogpost.objects.all().order_by('-sno')
    posts=Blogpost.objects.filter(slug=slug).first()
    next_post = next_in_order(posts, qs=qs)
    prev_post = prev_in_order(posts, qs=qs, loop=True)
    comment_form=CommentForm()
    context={'posts':posts,'postp':prev_post,'postn':next_post,'comment_form':comment_form}
    return render(request,'blogt/blogpost.html',context)
def post_detail(request,slug):
    template_name='blogt/blogpost.html'
    posts=get_object_or_404(Blogpost,slug=slug)
    comments=posts.comments.all()
    new_comment=None
    #Comment posted
    if request.method =='POST':
        comment_form=CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment=comment_form.save(commit=False)
            new_comment.post=posts
            new_comment.save()
        else:
            comment_form=CommentForm()
        return redirect('/blog/'+posts.slug)
                                             