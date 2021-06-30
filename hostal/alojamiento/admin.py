from django.contrib import admin 
from .models import Profile, Room, Type, Employee, Guest, Post, Comment, Booking_Client, Ticket, Proovider, Dishes, Order, Answer , Product

# Register your models here.
admin.site.register(Profile)
admin.site.register(Room)
admin.site.register(Type)
admin.site.register(Employee)
admin.site.register(Guest)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Answer)
admin.site.register(Booking_Client)
admin.site.register(Ticket)
admin.site.register(Proovider)
admin.site.register(Dishes)
admin.site.register(Order)
admin.site.register(Product)

