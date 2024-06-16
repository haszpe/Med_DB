"""medDB URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from django.contrib import admin
from django.urls import path, include       #include jest dodane, ma się przydać w przyszłości
from users import views
#from views import home, list_employee, user_login, user_logout

urlpatterns = [
    path("", views.home, name='home'),
    path("admin/", admin.site.urls),
    path("login/", views.user_login, name='login'),
    path("logout/", views.user_logout, name='logout'),
    path("list_employee/", views.list_employee, name='list_employee'),
    path("add_laboratory/", views.add_laboratory, name='add_laboratory'),
    path("add_employee/", views.add_employee, name='add_employee'),
    path("add_experiment/", views.add_experiment, name='add_experiment'),
    path("add_project/", views.add_project, name='add_project'),
    path("add_result/", views.add_result, name='add_result'),
    path("add_key_word/", views.add_key_word, name='add_key_word'),
    path("add_protocol/", views.add_protocol, name='add_protocol'),
    path("add_patient/", views.add_patient, name='add_patient'),
    path("add_all/", views.add_all, name='add_all'),
]
