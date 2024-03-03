from django.shortcuts import render, redirect
from .models import Posts, Comments
from django.contrib.auth.models import User
from .forms import PostForm, CommentForm
# Create your views here.
def home(request):
    return render(request, 'home.html')

def posts(request):
   
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('posts')
    else:
        form=PostForm()

    obj = Posts.objects.all().order_by('-created')
    data = {
        'obj': obj, 
        'form':form
    }
    return render(request, 'posts.html', data)

def edit(request, pk):
    obj = Posts.objects.get(pk=pk)
    if request.method == "POST":
        comm = CommentForm(request.POST)
        if comm.is_valid():
            instance = comm.save(commit=False)
            instance.author = request.user
            instance.post = obj
            instance.save()
            # return redirect('edit')
    else:
        comm=CommentForm()
    
    comments = Comments.objects.filter(post = obj.pk)
    son = len(comments)
    return render(request, 'edit.html', {'el':obj, 'comm':comm, 'comments':comments, 'son':son})