from django.contrib import admin
from .models import Component, Project, ProjectComponent, ChatSession, ChatMessage


@admin.register(Component)
class ComponentAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'description')
    list_filter = ('category',)
    search_fields = ('name', 'keywords')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'difficulty')
    list_filter = ('difficulty',)
    search_fields = ('title', 'description')


@admin.register(ProjectComponent)
class ProjectComponentAdmin(admin.ModelAdmin):
    list_display = ('project', 'component', 'quantity')


@admin.register(ChatSession)
class ChatSessionAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at')


@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'session', 'role', 'created_at')
    list_filter = ('role',)
