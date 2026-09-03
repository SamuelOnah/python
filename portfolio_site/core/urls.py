from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
    path("", views.home, name="home"),
    path("work/", views.project_index, name="project_index"),
    path("work/<slug:slug>/", views.project_detail, name="project_detail"),
    path("journal/", views.post_index, name="post_index"),
    path("journal/<slug:slug>/", views.post_detail, name="post_detail"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
]
