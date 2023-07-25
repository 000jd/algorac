from django.urls import path, include

from base.views import LatestNoticelistView, MentorView, NoticedetailView, LatestGallerylistView, ProjectView, MessagesView
from usermodel.views import APILogoutView
urlpatterns = [
    path('notices-latest/', LatestNoticelistView.as_view()),
    path('notices-detals/<slug:notice_slug>', NoticedetailView.as_view()),

    path('gallery-latest/', LatestGallerylistView.as_view()),

    path('projects/', ProjectView.as_view()),

    path('messages/', MessagesView.as_view()),

    path('mentor/',MentorView.as_view()),
    
    path('logout_token/', APILogoutView.as_view(), name='logout_token')
]
