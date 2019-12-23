"""Order_Kool URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.conf.urls import url
from django.contrib import admin
from order import views as my_order
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', my_order.index, name='home'),
    path('orders', my_order.index, name='home'),
    path('order/<int:order_id>/', my_order.show, name='show'),
    path('order/new/', my_order.new, name='new'),
    path('order/edit/<int:order_id>/', my_order.edit, name='edit'),
    path('order/delete/<int:order_id>/', my_order.destroy, name='delete'),
    path('products', my_order.index_product, name='home_product'),
    path('product/new/', my_order.new_product, name='new_product'),
    path('product/delete/<int:product_id>/', my_order.destroy_product, name='delete_product'),
    path('users/login/',auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path('users/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('users/change_password/', auth_views.PasswordChangeView.as_view(), {'post_change_redirect' : '/','template_name': 'change_password.html'}, name='change_password'),

]
