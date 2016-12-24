from django.conf.urls import patterns, include, url
from django.contrib import admin
import settings

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'my_blog.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       # url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATICFILES_DIRS, 'show_indexes': True}),
                       (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
                        {'document_root': settings.STATIC_PATH}),
                       url(r'^home$', 'article.views.home', name='home'),
                       # url(r'^(\d+)/$', 'article.views.detail', name='detail'),
                       url(r'^(?P<id>\d+)/$', 'article.views.detail', name='detail'),
                       url(r'^login/$', 'login.views.login', name='login'),
                       url(r'^regist/$', 'login.views.regist', name='regist'),
                       url(r'^$', 'login.views.login', name='login'),
                       url(r'^add$', 'DeviceManagement.views.add_device', name='add_device'),
                       )
