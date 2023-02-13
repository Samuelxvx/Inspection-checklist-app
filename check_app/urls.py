from django.urls import path
from .views import InspectionView, InspectionDetail, CreateInspection, InspectionUpdate ,DeleteInspection, AboutView

urlpatterns = [
    path('', InspectionView.as_view(), name='home'),
    path('list/<int:pk>/', InspectionDetail.as_view(), name='view'),
    path('create-list/', CreateInspection.as_view(), name='create-list'),
    path('update-list/<int:pk>/', InspectionUpdate.as_view(), name='update-list'),
    path('delete-list/<int:pk>/', DeleteInspection.as_view(), name='delete-list'),
    path('about/', AboutView.as_view(), name='about'),
]
