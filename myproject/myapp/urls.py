from django.urls import path
from myapp import views
from . import views
urlpatterns = [
    path('', views.index),
    path('about',views.about),
    path('form/', views.form, name="form"),
     path('book-ticket/', views.book_ticket, name='book_ticket'),
    path('ticket-booked/', views.ticket_booked, name='ticket_booked'),
]