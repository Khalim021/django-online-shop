
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

urlpatterns += i18n_patterns(
    path('accounts/', include('registration.backends.default.urls')),
    path('admin/', admin.site.urls),
    path('', include('home.urls', namespace='home')),
    path('shop/', include('shop.urls', namespace='shop')),
    path('watch/', include('watches.urls', namespace='watch')),
    path('mobile/', include('mobile.urls', namespace='mobile')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('wishlist/', include('wishlist.urls', namespace='wishlist')),
    path('contact/', include('contact.urls', namespace='contact')),
    path('checkout/', include('checkouts.urls', namespace='checkout')),
    path('user/', include('users.urls', namespace='profile')),
)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)







