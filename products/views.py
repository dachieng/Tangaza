from django.shortcuts import render
from .models import Upload, Category
from django.http import HttpResponse, HttpResponseRedirect, request
from django.core.files.storage import FileSystemStorage

# Create your views here.

def index(request):
    uploads = Upload.objects.filter(user_id= request.user.id)
    return render(request, "myproducts.html", {"products":uploads})

def upload(request):
    current_user = request.user
    categories = Category.objects.all()
    return render(request, "upload.html", {"current_user": current_user, "categories": categories})

def save(request):
    if request.method == 'POST' and request.FILES['myfile']:
        upload = Upload()
        upload.productname = request.POST['name']
        upload.price = request.POST['price']
        upload.quantity = request.POST['quantity']
        upload.description = request.POST['details']
        upload.category = request.POST['category']
        upload.user_id = request.POST["user_id"]
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        upload.image = request.FILES['myfile']
        upload.save()  

        return HttpResponseRedirect("/subscriptions")

def uploadSuccess(request):
    return render(request, 'uploadsuccess.html')

def category(request):
    return render(request, "category.html")

def saveCategory(request):
    category = Category()
    category.name = request.POST["name"]
    category.save()
    return HttpResponseRedirect('categorysuccess')  

def editdetails(request, id):
    product = Upload.objects.get(pk=id)
    return render(request, "editproduct.html", {"product":product})

def edit(request):
    product = Upload.objects.get(pk=request.POST["id"])
    product.productname = request.POST["name"]
    product.price = request.POST["price"]
    product.quantity = request.POST["quantity"]
    product.description = request.POST["details"]
    product.save()
    return HttpResponseRedirect("/products")
    
    

    