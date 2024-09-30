from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Products,Orders
from .forms import ProductCreationForm,OrderCreationForm,UserForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def logIn(request):
    
    page = 'LogIn'
    
    
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'user does not exist')
            
        user = authenticate(request, username=username , password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'username or password does not exist')
    
    context = {'page':page}
    return render(request,'Login.html',context)

def register(request):
    page = 'register'
    form = UserForm()
    
    if request.method == 'POST':
        form = UserForm(request.POST)
        
        if form.is_valid():
                user = form.save(commit=False)
                user.username = user.username.lower()
                user.save()
                login(request, user)
        else:
             messages.error(request, 'an error occured')
               
                
        return redirect('home')
    
   
         
         
         
    context ={'page': page , 'form':form}
    return render(request, 'Register.html',context)

def logOut(request):
    logout(request)
    
    return redirect('log-in')
    


@login_required(login_url='log-in')
def allProducts(request):
    products = Products.objects.all()
   
    context = {'products':products}
    return render(request,'home.html',context)

@login_required(login_url='log-in')
def listProducts(request,pk):
    product = Products.objects.get(id=pk)
    form = OrderCreationForm(request.POST,request.FILES)
    order = Products.objects.get(id=pk)
    
    #create order
    
    if request.method == 'POST':
        
        createdOrder=Orders.objects.create(
        User=request.user,
        
        quantity=request.POST.get("quantity"),
        
        orders = order
        )
        return redirect('home')
        
    
    
    
    context = {'product':product,'form':form}
    return render(request,'product.html',context)

@login_required(login_url='log-in')  
def createProducts(request):
    form = ProductCreationForm(request.POST,request.FILES)
    
    
    # if request.method == 'POST':
    #     Products.objects.create(
    #     productName = request.POST.get('productName'),
    #     description = request.POST.get('description'),
    #     image = request.POST.get('image'),)
    if form.is_valid():
            form.save()
            return redirect('home')
    

    
    context = {'form':form}
    return render(request,'createProduct.html',context)


@login_required(login_url='log-in') 
def updateProduct(request,pk):
    product = Products.objects.get(id=pk)
    form = ProductCreationForm(request.POST,request.FILES,instance=product)
    
    
    if request.method == 'POST':
        form = ProductCreationForm(request.POST,request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product', pk=product.id)

    context = {'product':product,'form':form}
    return render(request,'updateProduct.html',context)


@login_required(login_url='log-in')
def deleteProduct(request,pk):
    product = Products.objects.get(id=pk)
    
    
    
    
    if request.method == 'POST':
        product.delete()
        return redirect('home')
    
    return render(request, 'delete.html', {'obj':product})



@login_required(login_url='log-in')    
def allOrders(request,pk):
    user = User.objects.get(id=pk)
    
    order =user.orders_set.all()
    
    
    
    context = {'order':order,}
    return render(request,'userProfile.html',context)

# @login_required(login_url='log-in')  
# def createOrders(request,pk):
#     form = OrderCreationForm(request.POST,request.FILES)
#     product = Products.objects.get(id=pk)
    
    
#     if request.method == 'POST':
#         order =  Orders.objects.create(
#         user=request.user,
#         orders=product,
#         quantity=request.POST.get["quantity"] )
    
   
#     context = {'order':order,'form':form}
#     return render(request,'product.html',context)

@login_required(login_url='log-in')
def deleteOrder(request,pk):
    order = Orders.objects.get(id=pk)
    
    if request.user != order.User:
        return HttpResponse('not the user')
    
    if request.method == 'POST':
        order.delete()
        return redirect('user-profile', order.User.id)
    
    
    
    return render(request, 'orderDelete.html', {'obj':order})

