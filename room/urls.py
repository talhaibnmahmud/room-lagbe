from django.urls import path

from room import views

urlpatterns = [
    path('districts/', views.DistrictList.as_view(), name='get-districts'),
    path('hotels/', views.HotelList.as_view(), name='get-hotels'),
    path('rooms/', views.RoomView.as_view(), name='get-rooms'),
    path('reservation/', views.ReservationListView.as_view(), name='get-reservation'),
    path('make-reservation/', views.ReservationCreateView.as_view(), name='make-reservation'),
]
