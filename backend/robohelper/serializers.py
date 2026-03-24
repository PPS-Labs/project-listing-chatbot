from rest_framework import serializers
from .models import Component, Project, ProjectComponent, ChatSession, ChatMessage


class ComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Component
        fields = ['id', 'name', 'category', 'description', 'keywords']


class ProjectComponentSerializer(serializers.ModelSerializer):
    component_name = serializers.CharField(source='component.name', read_only=True)

    class Meta:
        model = ProjectComponent
        fields = ['component_name', 'quantity']


class ProjectSerializer(serializers.ModelSerializer):
    components_list = ProjectComponentSerializer(
        source='projectcomponent_set', many=True, read_only=True
    )

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'difficulty', 'instructions', 'components_list']


class ChatMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatMessage
        fields = ['id', 'role', 'content', 'created_at']


class ChatInputSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=1000)
    session_id = serializers.IntegerField(required=False, allow_null=True)
