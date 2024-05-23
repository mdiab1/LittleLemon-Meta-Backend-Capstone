from django.urls import path
from .views import MenuItemView, SingleMenuItemView, BookingView, index

urlpatterns = [
    path('menu/items/', MenuItemView.as_view()),
    path('menu/items/<int:pk>', SingleMenuItemView.as_view()),
    path('booking/tables', BookingView.as_view()),
    path('', index, name='home')
]