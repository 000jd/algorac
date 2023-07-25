from django.http import Http404
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Gallery, Mentor, Notice, projects
from .serializers import GallerySerializer, MentorSerializer, NoticeSerializer, ProjectSerializer, MessagesSerializer
# Create your views here.


class LatestNoticelistView(APIView):
    def get(self, request, format=None):
        notices = list(Notice.objects.all()[0:3])
        if not notices:
            return Response({'message': 'No data found'})
        serializer = NoticeSerializer(notices, many=True)
        return Response(serializer.data)


class NoticedetailView(APIView):
    def get_object(self, notice_slug):
        try:
            return Notice.objects.get(slug=notice_slug)
        except Notice.DoesNotExist:
            raise Http404

    def get(self, notice_slug, format=None):
        Notices = self.get_object(notice_slug)
        serializer = NoticeSerializer(Notices)
        return Response(serializer.data)


class LatestGallerylistView(APIView):
    def get(self, request, format=None):
        Gallerys = Gallery.objects.all()[:3]
        if not Gallerys:
            return Response({'message': 'No data found'})
        serializer = GallerySerializer(Gallerys, many=True)
        return Response(serializer.data)


class FullGalleryView(APIView):
    def get_object(self, notice_slug):
        try:
            return Notice.objects.get(slug=notice_slug)
        except Notice.DoesNotExist:
            raise Http404

    def get(self, notice_slug, format=None):
        Notices = self.get_object(notice_slug)
        serializer = NoticeSerializer(Notices)
        return Response(serializer.data)


class ProjectView(APIView):
    def get(self, request, format=None):
        project = projects.objects.all()
        if not project:
            # Corrected variable name
            return Response({'message': 'No data found'})
        serializer = ProjectSerializer(project, many=True)
        return Response(serializer.data)


class MessagesView(APIView):
    def post(self, request, format=None):
        massages = MessagesSerializer(data=request.data)
        if massages.is_valid():
            massages.save()
            return Response(massages.data, status=status.HTTP_201_CREATED)
        return Response(massages.errors, status=status.HTTP_400_BAD_REQUEST)


class MentorView(APIView):
    def post(self, request, format = None):
        mentor = Mentor.objects.all()
        if not mentor:
            return Response({'message': 'No data found'})
        serializer = MentorSerializer(mentor, many = True)
        return Response(serializer.data)
