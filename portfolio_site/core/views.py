from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from .forms import ContactForm
from .models import Project, Post


def home(request):
    featured_projects = Project.objects.filter(featured=True)[:3]
    if not featured_projects:
        featured_projects = Project.objects.all()[:3]
    latest_posts = Post.objects.filter(published=True)[:3]
    return render(
        request,
        "core/home.html",
        {
            "featured_projects": featured_projects,
            "latest_posts": latest_posts,
        },
    )


def project_index(request):
    projects = Project.objects.all()
    return render(request, "core/project_index.html", {"projects": projects})


def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    others = Project.objects.exclude(pk=project.pk)[:2]
    return render(request, "core/project_detail.html", {"project": project, "others": others})


def post_index(request):
    posts = Post.objects.filter(published=True)
    return render(request, "core/post_index.html", {"posts": posts})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, published=True)
    others = Post.objects.filter(published=True).exclude(pk=post.pk)[:2]
    return render(request, "core/post_detail.html", {"post": post, "others": others})


def about(request):
    return render(request, "core/about.html")


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Message sent — thanks for writing in. I'll reply soon.")
            return redirect("core:contact")
    else:
        form = ContactForm()
    return render(request, "core/contact.html", {"form": form})
