from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Hotel, Room, Employee
from rest_framework import viewsets
from .serializers import EmployeeSerializer

# Existing views for hotels, rooms, employees, and home page...
class HomePageView(TemplateView):
    template_name = 'hotel_app/home.html'

# ----- Hotel Views -----
class HotelListView(ListView):
    model = Hotel
    template_name = 'hotel_app/hotel_list.html'
    context_object_name = 'hotels'

class HotelCreateView(CreateView):
    model = Hotel
    fields = ['name', 'address', 'city', 'country', 'description']
    template_name = 'hotel_app/hotel_form.html'
    success_url = reverse_lazy('hotel_list')

class HotelUpdateView(UpdateView):
    model = Hotel
    fields = ['name', 'address', 'city', 'country', 'description']
    template_name = 'hotel_app/hotel_form.html'
    success_url = reverse_lazy('hotel_list')

class HotelDeleteView(DeleteView):
    model = Hotel
    template_name = 'hotel_app/hotel_confirm_delete.html'
    success_url = reverse_lazy('hotel_list')

# ----- Room Views -----
class RoomListView(ListView):
    model = Room
    template_name = 'hotel_app/room_list.html'
    context_object_name = 'rooms'

class RoomCreateView(CreateView):
    model = Room
    fields = ['hotel', 'room_number', 'room_type', 'price', 'is_available']
    template_name = 'hotel_app/room_form.html'
    success_url = reverse_lazy('room_list')

class RoomUpdateView(UpdateView):
    model = Room
    fields = ['hotel', 'room_number', 'room_type', 'price', 'is_available']
    template_name = 'hotel_app/room_form.html'
    success_url = reverse_lazy('room_list')

class RoomDeleteView(DeleteView):
    model = Room
    template_name = 'hotel_app/room_confirm_delete.html'
    success_url = reverse_lazy('room_list')

# ----- Employee Views (Web UI) -----
class EmployeeListView(ListView):
    model = Employee
    template_name = 'hotel_app/employee_list.html'
    context_object_name = 'employees'

class EmployeeCreateView(CreateView):
    model = Employee
    fields = ['first_name', 'last_name', 'department', 'salary']
    template_name = 'hotel_app/employee_form.html'
    success_url = reverse_lazy('employee_list')

class EmployeeUpdateView(UpdateView):
    model = Employee
    fields = ['first_name', 'last_name', 'department', 'salary']
    template_name = 'hotel_app/employee_form.html'
    success_url = reverse_lazy('employee_list')

class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = 'hotel_app/employee_confirm_delete.html'
    success_url = reverse_lazy('employee_list')

# ----- Employee API ViewSet -----
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
