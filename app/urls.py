from django.urls import path
from .views import JobFilterView, JobDetailView, JobCreateView, JobUpdateView, JobDeleteView


urlpatterns = [
    # 一覧画面
    path('',  JobFilterView.as_view(), name='index'),
    # 詳細画面
    path('detail/<int:pk>/', JobDetailView.as_view(), name='detail'),
    # 登録画面
    path('create/', JobCreateView.as_view(), name='create'),
    # 更新画面
    path('update/<int:pk>/', JobUpdateView.as_view(), name='update'),
    # 削除画面
    path('delete/<int:pk>/', JobDeleteView.as_view(), name='delete'),
]
