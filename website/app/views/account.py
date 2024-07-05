from django.shortcuts import render, HttpResponse, redirect
from django import forms

from app.utils.encrypt import md5
import app.models as models
from app.utils.checkcode import check_code
from django.urls import reverse

class loginForm(forms.Form):
    user = forms.CharField(label="管理员账号", max_length=20, required=True,
                           widget=forms.widgets.TextInput(
                               attrs={'placeholder': '输入账号', 'class': 'form-control form-control-lg'}),
                           error_messages={"required": "账户输入不能为空"})
    password = forms.CharField(label="管理员账号", max_length=20, required=True,
                               widget=forms.widgets.PasswordInput(
                                   attrs={'placeholder': '输入密码', 'class': 'form-control form-control-lg'
                                          }), error_messages={"required": "密码输入不能为空"})
    image_code =forms.CharField( max_length=4, required=True,
                               widget=forms.widgets.TextInput(
                                   attrs={'placeholder': '输入验证码', 'class': 'form-control form-control-lg'
                                          }), error_messages={"required": "请输入验证码"})

    def clean_password(self):
        password = self.cleaned_data.get('password')
        return md5(password)




def login(request):
    message=""
    if request.method == "GET":
        form = loginForm()
        return render(request, "login.html", { "form": form, "message":  message})
    elif request.method == "POST":
        form = loginForm(data=request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            user_input_code=form.cleaned_data.pop('image_code')
            image_code=request.session.get('image_code',"")
            if image_code =="":
                message="验证码超时失效，请刷新页面后重试！"
                return render(request, "login.html", { "form": form, "message": message})
            if image_code.upper()!=user_input_code.upper():
                message="验证码错误！"
                return render(request, "login.html", { "form": form, "message": message})

            admin = models.admin.objects.filter(**form.cleaned_data).first()
            if not admin:

                message="账户密码验证失败！"
                return render(request, "login.html", { "form": form, "message": message})
                # 跳转到管理界面
            else:
                request.session["info"] = {'id': admin.id, 'user': admin.user}
                request.session.set_expiry(60*24*60*30)
                next_url = request.GET.get('next', reverse('meters'))
                return redirect(next_url)


from io import BytesIO


# 生成默认含4个字符验证码的图片
def image_code(request):
    img, code = check_code()
    request.session['image_code']=code
    request.session.set_expiry(60)
    stream=BytesIO()
    img.save(stream,'png')
    return HttpResponse(stream.getvalue())
