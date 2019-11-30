from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^add_post$', add_post, name='add-post'),
    url(r'^view_post/(?P<post_id>\d+)$', view_post, name='view-post'),
    url(r'^delete_post/(?P<post_id>\d+)$',delete_post, name='delete-post'),
    url(r'^update_post/(?P<post_id>\d+)$',update_post, name='update-post'),
    url(r'^delete_comment/(?P<comment_id>\d+)$',delete_comment, name='delete-comment'),
]
