import os
from django.conf.urls import url, include
from django.core.urlresolvers import set_urlconf, resolve, reverse


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eventex.settings')


def index(request):
    pass


def auth(request):
    pass


def list_(request):
    pass


def edit(request):
    pass


def new(request):
    pass


def delete(request):
    pass


class LENDConf:

    def __init__(self, model):
        self.model = model
        self.urlpatterns = [
            url(r'^$', list_, name='list'),
            url(r'^(\d+)/$', edit, name='edit'),
            url(r'^new/$', new, name='new'),
            url(r'^delete/$', delete, name='delete'),
        ]


class MySiteURLConf:
    urlpatterns = [
        url(r'^$', index, name='index'),
        url(r'^login/$', auth, kwargs={'action': 'login'}, name='login'),
        url(r'^logout/$', auth, kwargs={'action': 'logout'}, name='logout'),
        url(r'^groups/', include(LENDConf('groups'), namespace='groups')),
        url(r'^users/', include(LENDConf('users'), namespace='users')),
    ]


set_urlconf(MySiteURLConf)

print('Resolve: ', resolve('/'))
print('Reverse: ', reverse('index'))

print('Resolve: ', resolve('/login/'))
print('Reverse: ', reverse('login'))

print('Resolve: ', resolve('/logout/'))
print('Reverse: ', reverse('logout'))

print('Resolve: ', resolve('/groups/'))
print('Reverse: ', reverse('groups:list'))

print('Resolve: ', resolve('/groups/1/'))
print('Reverse: ', reverse('groups:edit', args=[1]))

print('Resolve: ', resolve('/groups/new/'))
print('Reverse: ', reverse('groups:new'))

print('Resolve: ', resolve('/groups/delete/'))
print('Reverse: ', reverse('groups:delete'))

print('Resolve: ', resolve('/users/'))
print('Reverse: ', reverse('users:list'))

print('Resolve: ', resolve('/users/1/'))
print('Reverse: ', reverse('users:edit', args=[1]))

print('Resolve: ', resolve('/users/new/'))
print('Reverse: ', reverse('users:new'))

print('Resolve: ', resolve('/users/delete/'))
print('Reverse: ', reverse('users:delete'))
