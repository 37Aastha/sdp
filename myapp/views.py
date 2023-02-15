from django.shortcuts import render,redirect
from .models import *

def index(request):
    return render(request, 'index.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def login(request):
  return render(request, 'login.html')

def registration(request):
 return render(request, 'registration.html')
    
def acustomer(request):
    return render(request, 'acustomer.html')

#customer
def CustomerList(request):
    fatch_data_from_cutomer=Customer.objects.all()
    return render(request,'Customer/CustomerList.html',{'fatch_data1':fatch_data_from_cutomer})

def CustomerAdd(request):
    return render(request,'Customer/CustomerAdd.html')

def customer(request):
    First_Name=request.POST.get('First_Name')
    Last_Name=request.POST.get('Last_Name')
    Number=request.POST.get('Number')
    Email=request.POST.get('Email')
    Password=request.POST.get('Password')
    customer_detail_add=Customer(first_name=First_Name,last_name=Last_Name,number=Number,email=Email,
                                 password=Password)
    customer_detail_add.save()
    return redirect('/CustomerList/')
  
def Customer_uedit(request,id):
    custedit=Customer.objects.get(c_id=id)
    return render(request,'Customer/CustomerUpdate.html',{'customersedit':custedit})

def Update_Customer(request,id):
    First_Name=request.POST.get('First_Name')
    Last_Name=request.POST.get('Last_Name')
    Number=request.POST.get('Number')
    Email=request.POST.get('Email')
    Password=request.POST.get('Password')
    customer_detail_add=Customer(c_id=id,first_name=First_Name,last_name=Last_Name,number=Number,email=Email,
                                 password=Password)
    customer_detail_add.save()
    return redirect('/CustomerList/')

def CDelete(request,id):
    customerdelete1=Customer.objects.get(c_id=id)
    customerdelete1.delete()
    return redirect('/CustomerList/')

#product
def ProductList(request):
    productl=Product.objects.all()
    return render(request,'product/ProductList.html',{'product_fatch':productl})

def ProductAdd(request):
    return render(request,'product/ProductAdd.html')

def Product1(request):
    name1=request.POST.get('name')
    desc1=request.POST.get('desc')
    price1=request.POST.get('price')
    product1=Product(p_name=name1,p_desc=desc1,p_price=price1)
    product1.save()
    return redirect('/ProductList/')

def Productedit(request,id):
    proedit11=Product.objects.get(p_id=id)
    return render(request,'product/ProductUpdate1.html',{'proedit1':proedit11})

def ProductUpdate(request,id):
    p_name=request.POST.get('p_name')
    p_desc=request.POST.get('p_desc')
    p_price=request.POST.get('p_price')
    Product1=Product(p_id=id,p_name=p_name,p_desc=p_desc,p_price=p_price)
    Product1.save()
    return redirect('/ProductList/')

def deleteproduct(request,id):
    productdelete=Product.objects.get(p_id=id)
    productdelete.delete()
    return redirect('/ProductList/')

# def deleteproduct(request,id):
#     pdelete=Product.objects.get(p_id=id)
#     pdelete.delete()
#     return redirect('/ProductList/')

#order
def OrderList(request):
    OL=Order.objects.all()
    return render(request,'order/OrderList.html',{'Orderl_fatch':OL})

def OrderAdd(request):
    ocust=Customer.objects.all()
    return render(request,'order/OrderAdd.html',{'ocust1':ocust })

def Order1(request):
    ocid1=request.POST.get('cid')
    ocid11=Customer.objects.get(c_id=ocid1)

    total_sum1=request.POST.get('total_sum')
    date1=request.POST.get('date')
    pay_method1=request.POST.get('paymethod')
    order11=Order(c=ocid11,total_sum=total_sum1,date=date1,pay_method=pay_method1)
    order11.save()
    return redirect('/OrderList/')

def Orderedit(request,id):
    ocust1=Customer.objects.all()
    oedit=Order.objects.get(o_id=id)
    return render(request,'order/OrderUpdate.html',{'oedit1':oedit,'ocust11':ocust1 })

def OrderUpdate(request,id):
    ocid=request.POST.get('cid')
    ocid1=Customer.objects.get(c_id=ocid)

    total_sum=request.POST.get('total_sum')
    date=request.POST.get('date')
    pay_method=request.POST.get('pay_method')
    order1=Order(o_id=id,c=ocid1,total_sum=total_sum,date=date,pay_method=pay_method)
    order1.save()
    return redirect('/OrderList/')

def oldelete(request,id):
    odelete=Order.objects.get(o_id=id)
    odelete.delete()
    return redirect('/OrderList/')

#payment
def PaymentList(request):
    PL=Payment.objects.all()
    
    return render(request,'Payment/PaymentList.html',{'Payment_fatch':PL})

def Paymentadd(request):
    cpay=Customer.objects.all()
    opay=Order.objects.all()
    return render(request,'Payment/PaymentAdd.html'
                  ,{'cpay1':cpay ,'opay1':opay})

def Payment1(request):
    cp1=request.POST.get('cid')
    cid1=Customer.objects.get(c_id=cp1)

    op=request.POST.get('oid')
    op1=Order.objects.get(o_id=op)

    date=request.POST.get('date')
    amount=request.POST.get('amount')
    PaymentA=Payment(c=cid1,o=op1,date=date,amount=amount)
    PaymentA.save()
    return redirect('/PaymentList/')

def Paymentedit(request,id):
    cpay1=Customer.objects.all()
    opay1=Order.objects.all()
    oedit1=Payment.objects.get(pay_id=id)
    return render(request,'Payment/PaymentUpdate.html'
                  ,{'oedit11':oedit1 ,'cpay11':cpay1 ,'opay11':opay1})

def Paymentupdate(request,id):
    cp1=request.POST.get('cid')
    cid11=Customer.objects.get(c_id=cp1)

    op111=request.POST.get('oid')
    op11=Order.objects.get(o_id=op111)
    
    date1=request.POST.get('date')
    amount1=request.POST.get('amount')
    PaymentA=Payment(pay_id=id,c=cid11,o=op11,date=date1,amount=amount1)
    PaymentA.save()
    return redirect('/PaymentList/')


def deletepayment(request,id):
    pdelete=Payment.objects.get(pay_id=id)
    pdelete.delete()
    return redirect('/PaymentList/')

#employee
def EmployeeList(request):
    fatch_data_from_employee=Employee.objects.all()
    return render(request,'employee/EmployeeList.html',{'fatch_data1':fatch_data_from_employee})

def EmployeeAdd(request):
    return render(request,'employee/EmployeeAdd.html')

def Employee1(request):
    First_Name=request.POST.get('First_Name')
    Last_Name=request.POST.get('Last_Name')
    Number=request.POST.get('Number')
    Email=request.POST.get('Email')
    Password=request.POST.get('Password')
    employee_detail_add=Employee(first_name=First_Name,last_name=Last_Name,number=Number,email=Email,
                                 password=Password)
    employee_detail_add.save()
    return redirect('/EmployeeList/')
  
def Employeeedit(request,id):
    empedit=Employee.objects.get(e_id=id)
    return render(request,'Employee/EmployeeUpdate.html',{'empsedit':empedit})

def Update_Employee(request,id):
    First_Name=request.POST.get('First_Name')
    Last_Name=request.POST.get('Last_Name')
    Number=request.POST.get('Number')
    Email=request.POST.get('Email')
    Password=request.POST.get('Password')
    employee_detail_add=Employee(e_id=id,first_name=First_Name,last_name=Last_Name,number=Number,email=Email,
                                 password=Password)
    employee_detail_add.save()
    return redirect('/EmployeeList/')

def EDelete(request,id):
    employeedelete1=Employee.objects.get(e_id=id)
    employeedelete1.delete()
    return redirect('/EmployeeList/')

#customer details
def CustomerdetailsList(request):
    fatch_data_from_custdetails=Custdetails.objects.all()
    return render(request,'custdetails/CustomerdetailsList.html',{'fatch_data1':fatch_data_from_custdetails})

def CustomerdetailsAdd(request):
    return render(request,'custdetails/CustomerdetailsAdd.html')

def customerdetails1(request):
    age=request.POST.get('age')
    gender=request.POST.get('gender')
    dob=request.POST.get('dob')
    address=request.POST.get('address')
    zip=request.POST.get('zip')
    customerdetails_detail_add=Custdetails(age=age,gender=gender,dob=dob,address=address,
                                 zip=zip)
    customerdetails_detail_add.save()
    return redirect('/CustomerdetailsList/')
  
def Customerdetails_uedit(request,id):
    cstdtledit=Custdetails.objects.get(cd_id=id)
    return render(request,'custdetails/CustomerdetailsUpdate.html',{'customerdetailssedit':cstdtledit})

def Update_Customerdetails(request,id):
    age=request.POST.get('age')
    gender=request.POST.get('gender')
    dob=request.POST.get('dob')
    address=request.POST.get('address')
    zip=request.POST.get('zip')
    customerdetails_detail_add=Custdetails(cd_id=id,age=age,gender=gender,dob=dob,address=address,
                                 zip=zip)
    customerdetails_detail_add.save()
    return redirect('/CustomerdetailsList/')

def CDDelete(request,id):
    customerdetailsdelete=Custdetails.objects.get(cd_id=id)
    customerdetailsdelete.delete()
    return redirect('/CustomerdetailsList/')

#category
def CategoryList(request):
    fatch_data_from_category=Category.objects.all()
    return render(request,'category/CategoryList.html',{'fatch_data1':fatch_data_from_category})

def CategoryAdd(request):
    return render(request,'category/CategoryAdd.html')

def Category1(request):
    cat_name=request.POST.get('cat_name')
    category_detail_add=Category(cat_name=cat_name)
    category_detail_add.save()
    return redirect('/CategoryList/')
  
def Category_uedit(request,id):
    categoryedit=Category.objects.get(cat_id=id)
    return render(request,'category/CategoryUpdate.html',{'categoryedit':categoryedit})

def CategoryUpdate(request,id):
    cat_name=request.POST.get('cat_name')
    category_detail_add=Category(cat_id=id,cat_name=cat_name)
    category_detail_add.save()
    return redirect('/CategoryList/')

def CatDelete(request,id):
    categorydelete=Category.objects.get(cat_id=id)
    categorydelete.delete()
    return redirect('/CategoryList/')

#color
def ColorList(request):
    CL=Color.objects.all()
    return render(request,'color/ColorList.html',{'colorfatch_data1':CL})

def ColorAdd(request):
    cpro=Product.objects.all()
    return render(request,'color/ColorAdd.html',{'cpro11':cpro })

def Color11(request):
    copid=request.POST.get('pid')
    copid1=Product.objects.get(p_id=copid)

    name=request.POST.get('name')
    code=request.POST.get('code')
    Color1=Color(p=copid1,name=name,code=code)
    Color1.save()
    return redirect('/ColorList/')

def Coloredit(request,id):
    cpro11=Product.objects.all()
    cedit=Color.objects.get(color_id=id)
    return render(request,'color/ColorUpdate.html',{'colorsedit':cedit,'cpro11':cpro11})

def ColorUpdate(request,id):
    copid=request.POST.get('pid')
    copid1=Product.objects.get(p_id=copid)

    name=request.POST.get('name')
    code=request.POST.get('code')
    color1=Color(color_id=id,p=copid1,name=name,code=code)
    color1.save()
    return redirect('/ColorList/')

def ClrDelete(request,id):
    cdelete=Color.objects.get(color_id=id)
    cdelete.delete()
    return redirect('/ColorList/')

#order details
def OrderdetailsList(request):
    OL=Orderdetails.objects.all()
    
    return render(request,'orderdetails/OrderdetailsList.html',{'Orderdetails_fatch':OL})

def OrderdetailsAdd(request):
    opay=Order.objects.all()
    ppay=Product.objects.all()
    return render(request,'orderdetails/OrderdetailsAdd.html'
                  ,{'opay1':opay,'ppay1':ppay })

def Orderdetails1(request):
   
    op=request.POST.get('oid')
    op1=Order.objects.get(o_id=op)

    pp1=request.POST.get('pid')
    pid1=Product.objects.get(p_id=pp1)

    price=request.POST.get('price')
    quantity=request.POST.get('quantity')
    discount=request.POST.get('discount')
    OrderdetailsA=Orderdetails(o=op1,p=pid1,price=price,quantity=quantity,discount=discount)
    OrderdetailsA.save()
    return redirect('/OrderdetailsList/')

def Orderdetailsedit(request,id):
    opay1=Order.objects.all()
    ppay1=Product.objects.all()
    oedit1=Orderdetails.objects.get(od_id=id)
    return render(request,'Orderdetails/OrderdetailsUpdate.html'
                  ,{'oedit11':oedit1 ,'ppay11':ppay1 ,'opay11':opay1})

def OrderdetailsUpdate(request,id):
    op1=request.POST.get('oid')
    op11=Order.objects.get(o_id=op1)

    pp1=request.POST.get('pid')
    pid11=Product.objects.get(p_id=pp1)
    
    price=request.POST.get('price')
    quantity=request.POST.get('quantity')
    discount=request.POST.get('discount')
    OrderdetailsA=Orderdetails(od_id=id,o=op11,p=pid11,price=price,quantity=quantity,discount=discount)
    OrderdetailsA.save()
    return redirect('/OrderdetailsList/')


def oddelete(request,id):
    odelete=Orderdetails.objects.get(od_id=id)
    odelete.delete()
    return redirect('/OrderdetailsList/')

#group
def GroupList(request):
    GL=Group.objects.all()
    return render(request,'group/GroupList.html',{'fatch_data11':GL})

def GroupAdd(request):
    cus=Customer.objects.all()
    return render(request,'group/GroupAdd.html',{'cpro1':cus })

def Group1(request):
    cpid=request.POST.get('cid')
    cpid1=Customer.objects.get(c_id=cpid)

    created_date=request.POST.get('created_date')
    created_by=request.POST.get('created_by')
    Group1=Group(c=cpid1,created_date=created_date,created_by=created_by)
    Group1.save()
    return redirect('/GroupList/')

def Groupedit(request,id):
    cpro1=Customer.objects.all()
    gedit=Group.objects.get(g_id=id)
    return render(request,'group/GroupUpdate.html',{'Groupsedit':gedit,'cpro11':cpro1})

def GroupUpdate(request,id):
    cpid=request.POST.get('cid')
    cpid1=Customer.objects.get(c_id=cpid)

    created_date=request.POST.get('created_date')
    created_by=request.POST.get('created_by')
    Group1=Group(g_id=id,c=cpid1,created_date=created_date,created_by=created_by)
    Group1.save()
    return redirect('/GroupList/')

def GDelete(request,id):
    gdelete=Group.objects.get(g_id=id)
    gdelete.delete()
    return redirect('/GroupList/')
