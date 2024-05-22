from django.urls import path
from .views import MenuItemView, SingleMenuItemView, BookingView

urlpatterns = [
    path('items/', MenuItemView.as_view()),
    path('items/<int:pk>', SingleMenuItemView.as_view()),
    path('tables', BookingView.as_view()),
]