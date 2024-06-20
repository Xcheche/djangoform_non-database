from django.contrib import messages
from django.shortcuts import render, redirect

from .models import Student

from .forms import StudentInfo


# Create your views here.
def home(request):
    if request.method == "POST":
        fm = StudentInfo(request.POST)

        # pulling forms.py details
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone_no"]
        message = request.POST["message"]
        # saving
        s = Student(name=name, email=email, phone=phone, message=message)
        if fm.is_valid():
            s.save()

        # sent message alert
        messages.success(request, "Form submitted successfully!")
        return redirect("success_page")
        print(f"post data {fm}")
    else:
        fm = StudentInfo()
        print(f"get data {fm}")
    return render(request, "home.html", {"form": fm})


# formfields directly in views.py
# def home(request):
#     if request.method == "POST":
#         fm = StudentInfo(request.POST)
#         print(f"post data {fm}")
#     else:
#         fm = StudentInfo(  # from here
#             label_suffix="-",
#             initial={
#                 "name": "Full Name",
#                 "email": "Email",
#                 "phone": "Phone",
#             },
#         )
#         print(f"get data {fm}")
#     return render(request, "home.html", {"form": fm})


# view for succes_page or sent message
def success_page(request):
    return render(request, "success.html")
