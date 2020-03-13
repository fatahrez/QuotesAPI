from django.urls import path

from QuotesApp import settings
from quotes import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.QuotesView.as_view(), name="quotes"),
]