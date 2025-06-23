from django.shortcuts import render, redirect
from functools import wraps
from django.contrib import messages
from Home.models import Events, student_data

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

def student(request):
    if request.method == "POST":
        student_name = request.POST.get("student_name")
        date = request.POST.get("date")
        classs = request.POST.get("class")
        image = request.FILES.get("image")

        students = student_data(
            student_name = student_name,
            date = date,
            classs = classs,
            image = image
        )
        students.save()
        return redirect("adminpage")
    
    return render(request, "student.html")



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
    query_name = request.GET.get("event_name")
    query_date = request.GET.get("event_date")

    items = Events.objects.all()

    if query_name:
        items = items.filter(event__icontains = query_name)
    if query_date:
        items = items.filter(date = query_date)
    return render(request, "loggedin.html", {'items': items})


@login_required
def createEvent(request):
    if request.method == "POST":
        event = request.POST.get("event")
        date = request.POST.get("date")
        time = request.POST.get("time")
        venue = request.POST.get("venue")
        for_class = request.POST.get("for_class")
        number = request.POST.get("number")
        description = request.POST.get("description")
        image = request.FILES.get("image")

        events = Events(
            event=event,
            date=date,
            number=number,
            description=description,
            image=image
        )
        events.save()
        return redirect("adminpage")

    return render(request, "createEvent.html")

def logout(request):
    request.session.flush()
    return redirect('/')

def views(request):
    return render(request, "views.html")