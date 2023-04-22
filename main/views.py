from django.shortcuts import render

def index(requset):
    return render(request=requset, template_name='main/index.html')



def about(requset):
    return render(request=requset, template_name='main/about.html')


def shop(requset):
    return render(request=requset, template_name='main/shop.html')

def furniture(requset):
    return render(request=requset, template_name='main/furniture.html')

def contacts(requset):
    if requset.method == "POST":
        print(requset.POST)
    return render(request=requset, template_name='main/contacts.html')