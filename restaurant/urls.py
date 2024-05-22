from django.urls import path
from .views import index, MenuItemView, SingleMenuItemView, BookingView

urlpatterns = [
    path('', index, name='index'),
    path('items/', MenuItemView.as_view()),
    path('items/<int:pk>', SingleMenuItemView.as_view()),
    path('tables', BookingView.as_view()),
]