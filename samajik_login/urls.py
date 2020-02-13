from django.urls import path

from samajik_login.views import HomepageView

app_name='samajik_login'


urlpatterns=[

    path('home/',HomepageView.as_view(),name='home-page')
]