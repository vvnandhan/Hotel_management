from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    HomePageView,
    HotelListView, HotelCreateView, HotelUpdateView, HotelDeleteView,
    RoomListView, RoomCreateView, RoomUpdateView, RoomDeleteView,
    EmployeeListView, EmployeeCreateView, EmployeeUpdateView, EmployeeDeleteView,
    EmployeeViewSet,
)

# Create a router and register our API viewset for employees
router = DefaultRouter()
router.register(r'api/employees', EmployeeViewSet, basename='employee-api')

urlpatterns = [
    # Web UI URLs
    path('home/', HomePageView.as_view(), name='home'),
    path('hotels/', HotelListView.as_view(), name='hotel_list'),
    path('hotels/create/', HotelCreateView.as_view(), name='hotel_create'),
    path('hotels/<int:pk>/update/', HotelUpdateView.as_view(), name='hotel_update'),
    path('hotels/<int:pk>/delete/', HotelDeleteView.as_view(), name='hotel_delete'),

    path('rooms/', RoomListView.as_view(), name='room_list'),
    path('rooms/create/', RoomCreateView.as_view(), name='room_create'),
    path('rooms/<int:pk>/update/', RoomUpdateView.as_view(), name='room_update'),
    path('rooms/<int:pk>/delete/', RoomDeleteView.as_view(), name='room_delete'),

    path('employees/', EmployeeListView.as_view(), name='employee_list'),
    path('employees/create/', EmployeeCreateView.as_view(), name='employee_create'),
    path('employees/<int:pk>/update/', EmployeeUpdateView.as_view(), name='employee_update'),
    path('employees/<int:pk>/delete/', EmployeeDeleteView.as_view(), name='employee_delete'),

    # API URLs
    path('', include(router.urls)),
]
