from django.urls import path, include

import app1.views
import djangoProject4.views

# http://localhost:8000/app1
urlpatterns = [
    path('', app1.views.start5 ),
    path('/js01',app1.views.js01,name='js01'),
    path('/js02',app1.views.js02,name='js02'),
    path('/js03',app1.views.js03,name='js03'),
    path('/js04',app1.views.js04,name='js04'),
    path('/js05',app1.views.js05,name='js05'),
    path('/js06',app1.views.js06,name='js06'),
    # path('insert')

]
