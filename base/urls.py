from django.urls import path,include
from . import views

urlpatterns = [
   path('',views.allProducts,name="home"),
   path('login/',views.logIn,name="log-in"),
   path('register/',views.register,name="register"),
    path('logout/', views.logOut,name="logout"),
    path('products/<str:pk>/',views.listProducts,name="product"),
    path('productsCreate/',views.createProducts,name="create-products"),
    path('products/update/<str:pk>/',views.updateProduct,name="update-product"),
    path('products/delete/<str:pk>/',views.deleteProduct,name="delete-product"),
    
    
    
    
    path('userProfile/<str:pk>/',views.allOrders,name="user-profile"),
    
     path('orders/delete/<str:pk>',views.deleteOrder,name="delete-orders"),
]