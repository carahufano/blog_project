from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .models import Post, Comment
from .forms import PostForm, CommentForm

# Create your views here.
def index(request):
	template    = 'list.html'
	posts       = Post.objects.all()

	context = {
		'posts':posts,
	}

	return render(request, template, context)

def add_post(request):
	template    = 'add_post.html'

	if request.method == "POST":
		form = PostForm(request.POST, initial={'author':'admin'})
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse_lazy('blog:index'))
	else:
		context = {
			'post_form':PostForm(),
		}

		return render(request, template, context)

def view_post(request, post_id):
	template    = 'view_post.html'

	post = Post.objects.get(id=int(post_id))
	comments = post.comments.all()
	new_comment = None

	if request.method == 'POST':
		comment_form = CommentForm(data=request.POST)
		if comment_form.is_valid():
			new_comment = comment_form.save(commit=False)
			new_comment.post = post
			new_comment.save()
	else:
		comment_form = CommentForm()

	context = {
		'post':post,
		'comments':comments,
		'new_comment':new_comment,
		'comment_form':comment_form
	}

	return render(request, template, context)

def delete_post(request,post_id):

	post=Post.objects.get(id=int(post_id))
	post.delete()
	return HttpResponseRedirect(reverse_lazy('blog:index'))

def delete_comment(request,comment_id):
	comment=Comment.objects.get(id=int(comment_id))
	post=comment.post_id
	comment.delete()
	url=reverse_lazy('blog:redirect') + str(post)
	return HttpResponseRedirect(url)

def update_post(request,post_id):
		template="update_post.html"
		post=Post.objects.get(id=int(post_id))

		if request.method == "POST":
			form = PostForm(request.POST, instance=post)
			if form.is_valid():
				form.save()
			return HttpResponseRedirect(reverse_lazy('blog:index'))
		else:
			context = {
				'post_form':PostForm(),
			}

			return render(request, template, context)
