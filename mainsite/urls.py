from django.urls import path
from .views import *

urlpatterns = [
                path('',                                   index),
                path('shows',                              shows),
                path('shows/new',                          shows_new),
                path('shows/create',                       shows_create),
                path('shows/<int:show_id>',                show),
                path('shows/<int:show_id>/edit',           show_edit),
                path('shows/<int:show_id>/update',         show_update),
                path('shows/<int:show_id>/delete',         show_delete),
                path('shows/<int:show_id>/destroy',        show_destroy),
              ]
