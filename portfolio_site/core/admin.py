from django.contrib import admin
from django.utils.html import format_html
from .models import Project, Post, Tag, ContactMessage, Profile


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}


def thumb(obj, field="cover_image"):
    image = getattr(obj, field, None)
    if image:
        return format_html('<img src="{}" style="height:48px;width:48px;object-fit:cover;border-radius:4px;">', image.url)
    return "—"


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("cover_thumb", "title", "year", "status", "featured", "order")
    list_editable = ("order", "featured")
    prepopulated_fields = {"slug": ("title",)}
    filter_horizontal = ("tags",)
    list_filter = ("status", "featured", "tags")
    search_fields = ("title", "summary", "body")

    @admin.display(description="")
    def cover_thumb(self, obj):
        return thumb(obj)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("cover_thumb", "title", "published", "published_at", "reading_minutes")
    list_editable = ("published",)
    prepopulated_fields = {"slug": ("title",)}
    filter_horizontal = ("tags",)
    list_filter = ("published", "tags")
    search_fields = ("title", "dek", "body")
    date_hierarchy = "published_at"

    @admin.display(description="")
    def cover_thumb(self, obj):
        return thumb(obj)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Identity", {"fields": ("full_name", "tagline", "location")}),
        ("Home page", {"fields": ("hero_heading", "hero_text", "hero_image")}),
        ("About page", {"fields": ("portrait", "bio", "availability")}),
        ("Contact & links", {"fields": ("email", "github_url", "linkedin_url")}),
    )

    def has_add_permission(self, request):
        # Singleton: block "Add" once the one row exists.
        return not Profile.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False

    def changelist_view(self, request, extra_context=None):
        # Skip the list page — go straight to editing the single profile row.
        profile = Profile.load()
        from django.shortcuts import redirect
        return redirect("admin:core_profile_change", profile.pk)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "created_at")
    readonly_fields = ("name", "email", "message", "created_at")
    search_fields = ("name", "email", "message")
