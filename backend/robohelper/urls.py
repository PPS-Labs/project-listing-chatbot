from django.urls import path
from . import views

urlpatterns = [
    path('chat/', views.ChatView.as_view(), name='chat'),
    path('components/', views.ComponentListView.as_view(), name='components'),
    path('projects/', views.ProjectListView.as_view(), name='projects'),
    path('chat/history/<int:session_id>/', views.ChatHistoryView.as_view(), name='chat-history'),
]
