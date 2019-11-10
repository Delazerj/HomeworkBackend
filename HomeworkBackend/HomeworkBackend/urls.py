from django.urls import path

from HomeworkBackend.HomeworkBackend import views

urlpatterns = [
    path('snowboarder/', views.snowboarder_list),
    path ('snowboarder/<int:id>', views.snowboarder_detail),

    path('country/', views.country_list),
    path ('country/<int:id>', views.country_detail),
]