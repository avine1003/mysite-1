import datetime

from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
from django.views import View

from mysite import settings


def home(request):
    string = ['html', 'python', 'django']
    return render(request, 'home.html', {'string': string})


# class UploadFile(View):

def upload(request):
    # 上传文件
    if request.method == 'POST':
        file = request.FILES.get('file')
        # 对客户端发送到服务器的文件重命名,防止覆盖
        # 对路径细分
        """ 1.获取后缀名
            2.IMG_年月日
        """
        lastname = file.name.split('.')[-1]
        filename = "IMG_" + datetime.datetime.now().strftime("%Y%m%d%H%M%S") + '.' + lastname
        with open(settings.MEDIA_ROOT[0] + '/img/' + filename, 'wb') as f:
            for chunk in file.chunks():
                f.write(chunk)
        return HttpResponse('ok')
    return render(request, 'success.html')

# def register(request):
#     if request.method == 'POST':


