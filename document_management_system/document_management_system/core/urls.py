from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('accounts.urls', namespace='account')),
    path('', include('documents.urls', namespace='document')),
   

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

'''
template_name='account/password_reset.html'
template_name='account/password_reset_done.html'
template_name='account/password_reset_confirm.html'
template_name='account/password_reset_complete.html'
path('password_change/', auth_views.PasswordChangeView.as_view(),
        name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(),
        name='password_change_done'),

    path('password_reset/', auth_views.PasswordResetView.as_view(),
        name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(),
        name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),
        name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(),
        name='password_reset_complete'),
'''