"""smart_home URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include

from measurement.views import SensorsView, SensorView, MeasurementsView, UpdateSensor

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('measurement.urls')),  # подключаем маршруты из приложения measurement
    path('sensors/', SensorsView.as_view()),  # краткая инф по ВСЕМ датчикам + можно добавить новый датчик, указав
                                                # ИМЯ и ОПИСАНИЕ
    path('sensor/<pk>/', SensorView.as_view()),  # полная инф по 1 датчику (вместе с измерениями)
    path('measurements/', MeasurementsView.as_view()),  # добавление нового измерения с указанием ID ДАТЧИКА и ТЕМПЕРАТ.
    path('sensors/<pk>/', UpdateSensor.as_view())  # изменение ОПИСАНИЯ датчика
]