from django.urls import path
from django.conf.urls import url


from . import views

urlpatterns = [
   path('', views.index, name = "index" ),
   path('upload', views.upload, name = "upload"),
   path('uploadsuccess', views.uploadSuccess, name = "uploadsuccess"),
   path('save', views.save, name = "save"),
   path('category', views.category, name="category"),
   path('savecategory', views.saveCategory, name="savecategory"),
   path('editdetails/<int:id>', views.editdetails, name="editdetails"),
   path('edit',views.edit, name="edit"),
]