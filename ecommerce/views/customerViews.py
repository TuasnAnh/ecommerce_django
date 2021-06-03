from ecommerce.views.views import login
from django.http.response import HttpResponseNotAllowed, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from ..models import Person, User
from ..currentAuthen import authen


def homepage(request):
    if request.method == "GET":
        print(authen.username)
        if not authen.checkAuthen():
            return redirect("login")

        return render(request, "customer/homepage.html")


def register(request):
    if request.method == "GET":
        return render(request, "customer/register.html")
    else:
        username = request.POST.get("username")
        password = request.POST.get("password")
        repassword = request.POST.get("repassword")
        name = request.POST.get("name")
        gender = request.POST.get("gender")
        phone = request.POST.get("Phone")
        email = request.POST.get("Email")
        birth = request.POST.get("birth")
        address = request.POST.get("address")

        if (
            len(username) <= 0
            or len(password) <= 0
            or len(repassword) <= 0
            or len(name) <= 0
            or len(gender) <= 0
            or len(phone) <= 0
            or len(email) <= 0
            or len(birth) <= 0
            or len(address) <= 0
        ):
            messages.info(request, "Bạn chưa nhập đủ thông tin")
            return redirect("register")

        print(username, password, repassword, name, gender, phone, email, birth, address)

        existEmail = User.objects.filter(username=username).exists()
        if existEmail:
            messages.info(request, "Đã tồn tại tài khoản này")
            return redirect("register")

        if password != repassword:
            messages.info(request, "Không trùng mật khẩu")
            return redirect("register")

        user = User(username=username, pass_field=password, role="Customer")
        user.save()

        # get lastest id
        userId = User.objects.latest("id")
        person = Person(
            user_id=userId, gender=gender, birthday=birth, address=address, phone=phone, name=name, email=email
        )
        person.save()
        return redirect("login")
