from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index,name="home"),
    path('dashboard/', views.dashboard,name="dashboard"),
    path('acustomer/', views.acustomer,name="acustomer"),    
    path('login/', views.login, name='login'),
    path('registration/', views.registration, name='registration'),

    #customer
    path('CustomerList/',views.CustomerList,name="CustomerList"),
    path('CustomerAdd/',views.CustomerAdd,name="CustomerAdd"),
    path('customer/',views.customer,name="customer"),  #add_function
    path('Customer_uedit/<int:id>/',views.Customer_uedit,name="Customer_uedit"),
    path('Update_Customer/<int:id>/',views.Update_Customer,name="Update_Customer"),
    path('delete1/<int:id>/',views.CDelete,name="delete1"),


    #product
    path('ProductList/',views.ProductList,name="ProductList"),
    path('ProductAdd/',views.ProductAdd,name="ProductAdd"),
    path('Product1/',views.Product1,name="Product1"),
    path('Productedit/<int:id>/',views.Productedit,name="Productedit"),
    path('ProductUpdate/<int:id>/',views.ProductUpdate,name="ProductUpdate"),
    path('deleteproduct/<int:id>/',views.deleteproduct,name="deleteproduct"),

    #order
    path('OrderList/',views.OrderList,name="OrderList"),
    path('OrderAdd/',views.OrderAdd,name="OrderAdd"),
    path('Order1/',views.Order1,name="Order1"),
    path('Orderedit/<int:id>/',views.Orderedit,name="Orderedit"),
    path('OrderUpdate/<int:id>/',views.OrderUpdate,name="OrderUpdate"),
    path('oldelete/<int:id>/',views.oldelete,name="oldelete"),

    #payment
    path('PaymentList/',views.PaymentList,name="PaymentList"),
    path('PaymentAdd/',views.Paymentadd,name="Paymentadd"),
    path('Payment1/',views.Payment1,name="order1"),
    path('Paymentedit/<int:id>/',views.Paymentedit,name="Paymentedit"),
    path('Paymentupdate/<int:id>/',views.Paymentupdate,name="Paymentupdate"),
    path('deletepayment/<int:id>/',views.deletepayment,name="deletepayment"),

    #employee
    path('EmployeeList/',views.EmployeeList,name="EmployeeList"),
    path('EmployeeAdd/',views.EmployeeAdd,name="EmployeeAdd"),
    path('Employee1/',views.Employee1,name="Employee1"),  #add_function
    path('Employeeedit/<int:id>/',views.Employeeedit,name="Employeeedit"),
    path('Update_Employee/<int:id>/',views.Update_Employee,name="Update_Employee"),
    path('delete/<int:id>/',views.EDelete,name="delete"),

    #customer details
    path('CustomerdetailsList/',views.CustomerdetailsList,name="CustomerdetailsList"),
    path('CustomerdetailsAdd/',views.CustomerdetailsAdd,name="CustomerdetailsAdd"),
    path('customerdetails1/',views.customerdetails1,name="customerdetails1"),  #add_function
    path('Customerdetails_uedit/<int:id>/',views.Customerdetails_uedit,name="Customerdetails_uedit"),
    path('Update_Customerdetails/<int:id>/',views.Update_Customerdetails,name="Update_Customerdetails"),
    path('cddelete/<int:id>/',views.CDDelete,name="cddelete"),

    #category
    path('CategoryList/',views.CategoryList,name="CategoryList"),
    path('CategoryAdd/',views.CategoryAdd,name="CategoryAdd"),
    path('Category1/',views.Category1,name="Category1"),  #add_function
    path('Category_uedit/<int:id>/',views.Category_uedit,name="Category_uedit"),
    path('CategoryUpdate/<int:id>/',views.CategoryUpdate,name="CategoryUpdate"),
    path('catdelete/<int:id>/',views.CatDelete,name="catdelete"),

    #color
    path('ColorList/',views.ColorList,name="ColorList"),
    path('ColorAdd/',views.ColorAdd,name="ColorAdd"),
    path('Color11/',views.Color11,name="Color11"),  #add_function
    path('Coloredit/<int:id>/',views.Coloredit,name="Coloredit"),
    path('ColorUpdate/<int:id>/',views.ColorUpdate,name="ColorUpdate"),
    path('clrdelete/<int:id>/',views.ClrDelete,name="clrdelete"),

    #order details
    path('OrderdetailsList/',views.OrderdetailsList,name="OrderdetailsList"),
    path('OrderdetailsAdd/',views.OrderdetailsAdd,name="OrderdetailsAdd"),
    path('Orderdetails1/',views.Orderdetails1,name="Orderdetails1"),  #add_function
    path('Orderdetailsedit/<int:id>/',views.Orderdetailsedit,name="Orderdetailsedit"),
    path('OrderdetailsUpdate/<int:id>/',views.OrderdetailsUpdate,name="OrderdetailsUpdate"),
    path('oddelete/<int:id>/',views.oddelete,name="oddelete"),

    #group
    path('GroupList/',views.GroupList,name="GroupList"),
    path('GroupAdd/',views.GroupAdd,name="GroupAdd"),
    path('Group1/',views.Group1,name="Group1"),  #add_function
    path('Groupedit/<int:id>/',views.Groupedit,name="Groupedit"),
    path('GroupUpdate/<int:id>/',views.GroupUpdate,name="GroupUpdate"),
    path('gdelete/<int:id>/',views.GDelete,name="gdelete"),
]