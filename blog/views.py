from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.shortcuts import render, redirect
from django.utils.text import slugify
from user.utils import extractFirstName
from .forms import *
from .utils import *


def blog_home_view(request):
    blogs = BlogModel.objects.order_by('-date_posted')

    blog_search = request.GET.get('q')

    if blog_search is not None:
        blogs = BlogModel.objects.filter(Q(blog_title__icontains=blog_search)).order_by('-date_posted')
        add_to_blog_keyword(request.user, blog_search)
        add_to_keyword_model(blog_search)

    keywords = KeywordModel.objects.order_by('-total_count')[:3]

    paginator = Paginator(blogs, 5)
    page = request.GET.get('page', 1)
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)

    context = {
        'blogs': blogs,
        'keywords': keywords,
        'blog_search': blog_search,
        'util': datetime.now()
    }
    return render(request, 'blog/blog-home.html', context)


def trending_search_view(request, keyword):
    blogs = BlogModel.objects.order_by('-date_posted')

    if keyword is not None:
        blogs = BlogModel.objects.filter(Q(blog_title__icontains=keyword)).order_by('-date_posted')
        add_to_blog_keyword(request.user, keyword)
        add_to_keyword_model(keyword)

    keywords = KeywordModel.objects.order_by('-total_count')[:3]

    paginator = Paginator(blogs, 5)
    page = request.GET.get('page', 1)
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)

    context = {
        'blogs': blogs,
        'keywords': keywords,
        'blog_search': keyword,
        'util': datetime.now()
    }
    return render(request, 'blog/blog-home.html', context)


def blogs_view(request, pk):
    user = User.objects.get(id=pk)
    blogs = BlogModel.objects.filter(author=user).order_by('-date_posted')

    blog_search = request.GET.get('q')

    if blog_search is not None:
        blogs = BlogModel.objects.filter(Q(blog_title__icontains=blog_search)).order_by('-date_posted')

    paginator = Paginator(blogs, 5)
    page = request.GET.get('page', 1)
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)

    context = {
        'user': user,
        'blogs': blogs,
        'blog_search': blog_search,
        'util': datetime.now()
    }
    return render(request, 'blog/blogs.html', context)


def blog_details_view(request, slug):
    blog = BlogModel.objects.get(slug=slug)

    comment_form = NewCommentForm()
    if request.user.is_authenticated:
        if request.user != blog.author:
            increaseViewCount(request.user, blog)
        if request.method == 'POST':
            comment_form = NewCommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save()
                comment.author = request.user
                comment.blog_post = blog
                comment_form.save()
                return redirect('blog-details', blog.slug)
            else:
                return redirect('blog-details', blog.slug)

    comments = BlogCommentModel.objects.filter(blog_post=blog)
    context = {
        'blog': blog,
        'comment_form': comment_form,
        'comments': comments,
        'util': datetime.now()
    }
    return render(request, 'blog/blog-details.html', context)


@login_required(login_url='login')
def add_blog_view(request, util):
    task = "Add"
    name = extractFirstName(request.user.name)
    form = BlogForm()
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save()
            blog.author = request.user
            slug_str = "%s %s" % (blog.blog_title, blog.id)
            blog.slug = slugify(slug_str)
            form.save()
            send_email_notifications()
            return redirect('blog-home')
        else:
            context = {
                'task': task,
                'form': form,
                'name': name,
                'util': datetime.now()
            }
            return render(request, 'blog/add-edit-blog.html', context)

    context = {
        'task': task,
        'form': form,
        'name': name,
        'util': datetime.now()
    }
    return render(request, 'blog/add-edit-blog.html', context)


@login_required(login_url='login')
def edit_blog_view(request, slug):
    task = "Edit"
    name = extractFirstName(request.user.name)
    blog = BlogModel.objects.get(slug=slug)
    form = BlogForm(instance=blog)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            blog = form.save()
            slug_str = "%s %s" % (blog.blog_title, blog.id)
            blog.slug = slugify(slug_str)
            form.save()
            return redirect('blog-details', blog.slug)
        else:
            return redirect('edit-blog', request.BlogModel.slug)

    context = {
        'task': task,
        'form': form,
        'name': name,
        'util': datetime.now()
    }
    return render(request, 'blog/add-edit-blog.html', context)


@login_required(login_url='login')
def delete_blog_view(request, slug):
    name = extractFirstName(request.user.name)
    blog = BlogModel.objects.get(slug=slug)
    if request.method == 'POST':
        blog.delete()
        return redirect('blogs', request.user.id)

    context = {
        'item': blog,
        'name': name,
        'util': datetime.now()
    }
    return render(request, 'blog/delete-blog.html', context)


@login_required(login_url='login')
def edit_comment_view(request, pk):
    comment = BlogCommentModel.objects.get(id=pk)
    blog = BlogModel.objects.get(slug=comment.blog_post.slug)
    comments = BlogCommentModel.objects.filter(blog_post=blog)

    comment_form = NewCommentForm(instance=comment)
    if request.method == 'POST':
        comment_form = NewCommentForm(request.POST, instance=comment)
        if comment_form.is_valid():
            comment_form.save()
            return redirect('blog-details', blog.slug)
        else:
            return redirect('blog-details', blog.slug)

    context = {
        'comment_form': comment_form,
        'blog': blog,
        'comments': comments,
        'util': datetime.now()
    }
    return render(request, 'blog/blog-details.html', context)


@login_required(login_url='login')
def delete_comment_view(request, pk):
    name = extractFirstName(request.user.name)
    comment = BlogCommentModel.objects.get(id=pk)
    if request.method == 'POST':
        post_slug = comment.blog_post.slug
        comment.delete()
        return redirect('blog-details', post_slug)

    context = {
        'item': comment,
        'name': name,
        'util': datetime.now()
    }
    return render(request, 'blog/delete-comment.html', context)
