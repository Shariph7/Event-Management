from django.shortcuts import render, redirect, get_object_or_404
from functools import wraps
from django.contrib import messages
from Home.models import Events, student
from django.contrib.auth.models import User

def login_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.session.get('logged_in'):
            return redirect('login')
        return view_func(request, *args, **kwargs)
    return wrapper

def login_required_student(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.session.get('logged_in'):
            return redirect('login_student')
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

def index(request):
    query_name = request.GET.get("event_name")
    query_date = request.GET.get("event_date")
    items = Events.objects.all()

    if query_name:
        items = items.filter(event__icontains=query_name)
    if query_date:
        items = items.filter(date=query_date)

    return render(request, "index.html", {'items': items})

@login_required
def adminpage(request):
    query_class = request.GET.get("for_class")
    query_academic = request.GET.get("academic")
    class_list = ["Nursery", "LKG", "UKG", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]

    if request.method == "POST" and "Delete_Event" in request.POST:
        event_id = request.POST.get("Delete_Event")
        event = get_object_or_404(Events, id=event_id)
        event.delete()
        return redirect("adminpage")

    items = Events.objects.all()
    if query_class:
        items = items.filter(for_class__icontains=query_class)
    if query_academic:
        items = items.filter(academic_year=query_academic)

    return render(request, "adminpage.html", {
        'items': items,
        'class_list': class_list,
        'query_academic': query_academic,
        'query_class': query_class,
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
        for_class = ", ".join(request.POST.getlist("for_class"))
        description = request.POST.get("description")

        events = Events(
            event=event,
            start_date=start_date,
            end_date=end_date,
            type=type,
            start_time=start_time,
            end_time=end_time,
            Money=Money,
            venue=venue,
            for_class=for_class,
            description=description
        )
        events.save()
        return redirect("adminpage")

    return render(request, "createEvent.html")

def logout(request):
    request.session.flush()
    return redirect('/')

def data(request):
    if request.method == "POST":
        fullname = request.POST.get("fullname")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        classess = request.POST.get("classess")

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('data')

        if student.objects.filter(fullname=fullname).exists():
            messages.error(request, "Username already exists.")
            return redirect('data')

        users = student(
            fullname=fullname,
            password=password,
            confirm_password=confirm_password,
            classess=classess
        )
        users.save()

        messages.success(request, "Registration successful.")
        return redirect('adminpage')

    return render(request, "data.html")

def login_student(request):
    error = None
    if request.method == 'POST':
        username = request.POST.get('name')
        password = request.POST.get('password')

        try:
            students = student.objects.get(fullname=username)
            if students.password == password:
                request.session['student_id'] = students.id

                return redirect('student_profie')
            else:
                error = "Incorrect password."
        except:
            error = "User not found."

    return render(request, 'login_student.html', {'error': error})

@login_required_student
def student_profie(request):
    student_id = request.session.get('student_id')

    student_obj = get_object_or_404(student, id=student_id)
    return render(request, "student.html", {'fullname': student_obj.fullname})