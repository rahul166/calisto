from django.conf.urls import url
from . import views

app_name='groups'

url=[
    url(r'^$',views.ListGroup.as_view(),name='all'),
    url(r'^new/$',views.CreateGroup.as_view(),name='create'),
    url(r'^posts/in/(?p<slug>[-\w]+)/$',views.SingleGroup.as_view(),name='single')
]



