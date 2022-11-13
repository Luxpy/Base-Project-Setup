from django.urls import path

from apps.blogs.views import (BlogAssetsCreateAPIView, BlogCreateAPIView,
                              BlosListAPIView, BlogRetrieveAPIView, BlogUpdateAPIView, BlogDestroyAPIView)

urlpatterns = [
    path('blogs/assets/create/', BlogAssetsCreateAPIView.as_view(),
         name='blog-assets-create'),

    path('blogs/', BlogCreateAPIView.as_view(), name='blogs-create'),
    path('blogs/', BlosListAPIView.as_view(), name='blogs-list'),
    path('blogs/<int:pk>/', BlogRetrieveAPIView.as_view(), name='blogs-detail'),
    path('blogs/<int:pk>/', BlogUpdateAPIView.as_view(), name='blogs-update'),
    path('blogs/<int:pk>/', BlogDestroyAPIView.as_view(), name='blogs-delete'),
]
