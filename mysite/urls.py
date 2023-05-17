from django.urls import include, path
from django.contrib import admin
from blog import views

urlpatterns = [
    # 其他URL模式...
    path('admin/', admin.site.urls),

    # URL模式：将根路径映射到post_list视图
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]
