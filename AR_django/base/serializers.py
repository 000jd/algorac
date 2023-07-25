
from rest_framework import serializers

from .models import Gallery, Mentor, Notice, projects, messages
from django.contrib.auth.models import User


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = '__all__'


class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = (
            "id",
            "topic",
            "Slug",
            "description",
            "date_added"
        )


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = projects
        fields = '__all__'


class MessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = messages
        fields = '__all__'


class MentorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentor
        fields = '__all__'
