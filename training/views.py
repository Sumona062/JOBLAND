from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib import messages


def training_home_view(request):

    context = {
    }
    return render(request, 'training/blog-home.html', context)


def course_details_view(request, pk):
    context = {
    }
    return render(request, 'training/blog-details.html', context)


def courses_view(request, pk):

    context = {
    }
    return render(request, 'training/blogs.html', context)
