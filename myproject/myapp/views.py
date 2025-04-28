from django.shortcuts import render, redirect
from django.http import HttpResponse
from myapp.models import Person
from .models import TicketBooking
from .forms import TicketBookingForm

# Create your views here.
def index(request):
    all_Person = Person.objects.all()
    return render(request,"index.html",{"all_person":all_Person})

def about(request):
    return render(request,"about.html")

def form(request):
    if request.method == "POST":
        #รับข้อมูลจากฟอร์ม
        name = request.POST.get("name")
        age = request.POST.get('age')

        #บันทึกข้อมูลลงฐานข้อมูล
        person = Person.objects.create(
            name=name,
            age=age
        )

        #เปลี่ยนเส้นทางไปหน้าแรก
        return redirect("/")
    else:

        #แสดงฟอร์ม
        return render(request, "form.html")
    

def book_ticket(request):
    if request.method == "POST":
        form = TicketBookingForm(request.POST)
        if form.is_valid():
            form.save()  # บันทึกข้อมูล
            return redirect('ticket_booked')  # ไปที่หน้าหลังจากการจอง
    else:
        form = TicketBookingForm()
    
    return render(request, 'book_ticket.html', {'form': form})

def ticket_booked(request):
    bookings = TicketBooking.objects.all()  # ดึงข้อมูลการจองทั้งหมด
    return render(request, 'ticket_booked.html', {'bookings': bookings})
    