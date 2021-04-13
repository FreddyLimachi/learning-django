"""coffeeshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from django.conf import settings

from core import views as core_view
from services import views as services_view
from blog import views as blog_view
from pages import views as pages_view
from contact import views as contact_view

urlpatterns = [
    # paths admin
    path('admin/', admin.site.urls),

    # paths core
    path('', core_view.home, name = "home"),
    path('about', core_view.about, name = "about"),

    path('services', services_view.services, name = "services"),

    path('store', core_view.store, name = "store"),
    path('contact', contact_view.contact, name = "contact"),
    path('blog', blog_view.blog, name = "blog"),
    path('page/<int:page_id>', pages_view.page, name = "sample"),
    path('blog/category/<int:category_id>', blog_view.category, name = "category"),

]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
