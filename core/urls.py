from django.conf.urls import  include, url

from core.views import index,  hello_world, article_detail, profile

urlpatterns = [
   url(r'^$', index , name='core_index'),
   url(r'^profile$', profile , name='core_profile'),
   url(r'^detail/(?P<pk>\d+)$', article_detail , name='core_article_detail'),
   url(r'^helloworld/$', hello_world, name = 'core_hello_world')
]