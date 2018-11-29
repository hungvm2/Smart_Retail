from django.shortcuts import render
from static.face_recognition import detector
# Create your views here.


def index(request):
    if request.method == "GET":
        content = {
            'img': '',
            'orderlist': [],
            'name': '',
            'phone': '',
            'address': '',
        }
        return render(request, 'orderinfo.html', content)
    elif request.method == "POST":
        user = detector.run_camera_and_predict_person()
        content = {
            'img': 'static/face_recognition/dataset/User.1.1.jpg',
            'orderlist': ['Samsung', 'LG', 'Apple', 'Sony'],
            'name': user,
            'phone': '0924791235',
            'address': '17 Duy Tan, Cau Giay, Ha Noi',
        }
        return render(request, 'orderinfo.html', content)
