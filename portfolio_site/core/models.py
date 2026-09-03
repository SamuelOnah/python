from django.db import models
from django.urls import reverse
from django.utils import timezone


class Tag(models.Model):
    name = models.CharField(max_length=40, unique=True)
    slug = models.SlugField(max_length=40, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Project(models.Model):
    STATUS_CHOICES = [
        ("live", "Live"),
        ("in_progress", "In progress"),
        ("archived", "Archived"),
    ]

    title = models.CharField(max_length=120)
    slug = models.SlugField(max_length=140, unique=True)
    role = models.CharField(max_length=120, blank=True, help_text="e.g. 'Design & development, solo'")
    year = models.CharField(max_length=9, blank=True, help_text="e.g. '2024' or '2023–24'")
    summary = models.CharField(max_length=240, help_text="One line, shown in the index.")
    body = models.TextField(help_text="Longer write-up. Plain paragraphs, one per line.")
    cover_alt = models.CharField(max_length=200, blank=True, help_text="Description used in place of an image.")
    cover_image = models.ImageField(upload_to="projects/", blank=True, null=True, help_text="Shown on the index and at the top of the project page.")
    link_url = models.URLField(blank=True)
    link_label = models.CharField(max_length=60, blank=True, default="View live")
    repo_url = models.URLField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="live")
    featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0, help_text="Lower numbers appear first.")
    tags = models.ManyToManyField(Tag, blank=True, related_name="projects")
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["order", "-year", "title"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("core:project_detail", args=[self.slug])

    def body_paragraphs(self):
        return [p.strip() for p in self.body.split("\n") if p.strip()]


class Post(models.Model):
    title = models.CharField(max_length=160)
    slug = models.SlugField(max_length=180, unique=True)
    dek = models.CharField(max_length=240, help_text="Standfirst / subheading shown under the title.")
    cover_image = models.ImageField(upload_to="posts/", blank=True, null=True, help_text="Shown on the index and at the top of the post.")
    body = models.TextField(help_text="Plain paragraphs, one per line. First paragraph gets a drop cap.")
    published = models.BooleanField(default=True)
    published_at = models.DateTimeField(default=timezone.now)
    reading_minutes = models.PositiveIntegerField(default=4)
    tags = models.ManyToManyField(Tag, blank=True, related_name="posts")

    class Meta:
        ordering = ["-published_at"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("core:post_detail", args=[self.slug])

    def body_paragraphs(self):
        return [p.strip() for p in self.body.split("\n") if p.strip()]


class Profile(models.Model):
    """Singleton — the one row here drives the masthead, hero, about page, and footer."""

    full_name = models.CharField(max_length=120, default="Onah Samuel Iyojeni")
    tagline = models.CharField(max_length=160, default="Software engineer · graphic designer · entrepreneur")
    hero_heading = models.CharField(max_length=120, blank=True, help_text="Leave blank to use your full name.")
    hero_text = models.TextField(
        default="I build software, design the visual identity around it, and start the ventures that need both.",
        help_text="Shown under your name on the home page.",
    )
    bio = models.TextField(
        blank=True,
        help_text="Your About page bio. Plain paragraphs, one per line.",
    )
    portrait = models.ImageField(upload_to="profile/", blank=True, null=True, help_text="Shown on the About page.")
    hero_image = models.ImageField(
        upload_to="profile/", blank=True, null=True,
        help_text="Optional. Shown behind the home page hero if set.",
    )
    email = models.EmailField(blank=True)
    github_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    location = models.CharField(max_length=120, blank=True)
    availability = models.CharField(max_length=160, blank=True, default="Open to internships, freelance work, and collaborations")

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profile"

    def __str__(self):
        return self.full_name

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj

    def bio_paragraphs(self):
        return [p.strip() for p in self.bio.split("\n") if p.strip()]


class ContactMessage(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} <{self.email}>"
