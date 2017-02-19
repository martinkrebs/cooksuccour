from django.conf.urls import url

from . import views

#app_name = 'recipes'
# If you include the above app_name line, you also MUST append that namespace
# to your route names ie instead of name='edit' you must use name='recipes:edit'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^recipes/(?P<recipe_id>\d+)/$', views.detail, name='detail'),
    url(r'^recipes/create/$', views.create, name='create'),
    url(r'^recipes/(?P<recipe_id>\d+)/edit/$', views.edit, name='edit'),
]
