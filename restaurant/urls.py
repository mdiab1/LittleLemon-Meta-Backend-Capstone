from django.urls import path
#from .views import MenuItemView, SingleMenuItemView, BookingView, home, about, menu, book
from .views import MenuItemView, SingleMenuItemView, BookingView, home, about

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    #path('book/', book, name="book"),
    #path('menu/', menu, name="menu"),
    path('menu-items/', MenuItemView.as_view()),
    path('menu-items/<int:pk>', SingleMenuItemView.as_view()),
    path('bookings/', BookingView.as_view()),
]