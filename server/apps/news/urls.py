from django.urls import path

from apps.news.views import (NewsCreateAPIView, NewsListAPIView,
                             NewsRetrieveAPIView, NewsUpdateAPIView, NewsDestroyAPIView)

urlpatterns = [
    path('news/', NewsCreateAPIView.as_view(), name="news-create"),
    path('news/', NewsListAPIView.as_view(), name="news-list"),
    path('news/<int:pk>/', NewsRetrieveAPIView.as_view(), name="news-detail"),
    path('news/<int:pk>/', NewsUpdateAPIView.as_view(), name="news-update"),
    path('news/<int:pk>/', NewsDestroyAPIView.as_view(), name="news-delete"),
]
