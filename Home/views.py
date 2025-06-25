from django.shortcuts import render, redirect
from functools import wraps
from django.contrib import messages
from Home.models import Events

# Create your views here.
def login_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.session.get('logged_in'):
            return redirect('login')
        return view_func(request, *args, **kwargs)
    return wrapper

def login(request):
    if request.method == "POST":
        name = request.POST.get("name")
        password = request.POST.get("password")

        if name == "admin" and password == "admin":
            request.session['logged_in'] = True
            return redirect("adminpage")
        else:
            messages.error(request, "Invalid username or password.")
            return render(request, "login.html")

    return render(request, "login.html")

# Index
def index(request):
    query_name = request.GET.get("event_name")
    query_date = request.GET.get("event_date")

    items = Events.objects.all()

    if query_name:
        items = items.filter(event__icontains = query_name)
    if query_date:
        items = items.filter(date = query_date)
    return render(request, "index.html", {'items':items})

@login_required
def adminpage(request):
    query_class = request.GET.get("for_class")
    class_list = ["Nursery", "LKG", "UKG", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

    items = []
    if query_class:
        items = Events.objects.filter(for_class__iexact=query_class)

    return render(request, "adminpage.html", {
        'items': items,
        'class_list': class_list
    })



@login_required
def createEvent(request):
    if request.method == "POST":
        event = request.POST.get("event")
        start_date = request.POST.get("start_date")
        end_date = request.POST.get("end_date")
        type = request.POST.get("type")
        start_time = request.POST.get("start_time")
        end_time = request.POST.get("end_time")  
        venue = request.POST.get("venue")
        Money = request.POST.get("Money")
        for_class = request.POST.get("for_class")
        description = request.POST.get("description")

        events = Events(
            event = event,
            start_date = start_date,
            end_date = end_date,
            type = type,
            start_time = start_time,
            end_time = end_time,
            Money = Money,
            venue = venue,
            for_class = for_class,
            description = description
        )
        events.save()
        return redirect("adminpage")

    return render(request, "createEvent.html")

def logout(request):
    request.session.flush()
    return redirect('/')