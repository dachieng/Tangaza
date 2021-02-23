from django.urls import path

from . import views

urlpatterns = [
    #path('',views.home, name='home'),
    path('save',views.createsubscription, name='save'),
    path('success',views.success, name='success'),
    path('',views.displaysubscription, name='fetch'),
    path('pay/<int:subscription_id>' ,views.payment, name='pay' ),
    path('confirmation',views.confirmation, name='confirmation')
]

