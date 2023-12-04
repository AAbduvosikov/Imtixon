from django.shortcuts import render
from .models import Test


def main(request):
    testlar = Test.objects.all()
    return render(request=request, template_name='test.html',context={'testlar':testlar})


