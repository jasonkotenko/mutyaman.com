from django.conf.urls.defaults import patterns, include
from product.urls import urlpatterns as productpatterns
from satchmo_store import shop
from satchmo_store.shop.views.sitemaps import sitemaps
from signals_ahoy.signals import collect_urls
from django.views.generic.simple import redirect_to
from django.contrib import admin
from satchmo_store.urls import urlpatterns as satchmopatterns
admin.autodiscover()

urlpatterns = []

urlpatterns += patterns('',
    (r'^blog/$', 'posts.views.latest'),
    (r'^blog/(?P<req_name>.*)/$', 'posts.views.post'),
    (r'^away/$', 'django.views.generic.simple.direct_to_template', {'template':'away.html'}),
    (r'^cart/$', 'django.views.generic.simple.direct_to_template', {'template':'away.html'}),
    (r'^$',redirect_to, {'url': '/category/coco-nectar'}, 'satchmo_shop_home'),
    (r'^googlehostedservice.html$', 'django.views.generic.simple.direct_to_template', {'template':'googlehostedservice.html'}),
    (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
    (r'^robots.txt$', 'django.views.generic.simple.direct_to_template', {'template':'robots.txt'}),

    #(r'^$','satchmo_store.shop.views.home.home', {}, 'satchmo_shop_home'),
    #(r'^admin/(.*)', include(admin.site.urls)), 
)

urlpatterns += patterns('satchmo_store.shop.views',    
    (r'^add/$', 'smart.smart_add', {}, 'satchmo_smart_add'),
    #(r'^cart/$', 'cart.display', {}, 'satchmo_cart'),
    (r'^cart/accept/$', 'cart.agree_terms', {}, 'satchmo_cart_accept_terms'),
    (r'^cart/add/$', 'cart.add', {}, 'satchmo_cart_add'),
    (r'^cart/add/ajax/$', 'cart.add_ajax', {}, 'satchmo_cart_add_ajax'),
    (r'^cart/qty/$', 'cart.set_quantity', {}, 'satchmo_cart_set_qty'),
    (r'^cart/qty/ajax/$', 'cart.set_quantity_ajax', {}, 'satchmo_cart_set_qty_ajax'),
    (r'^cart/remove/$', 'cart.remove', {}, 'satchmo_cart_remove'),
    (r'^cart/remove/ajax/$', 'cart.remove_ajax', {}, 'satchmo_cart_remove_ajax'),
    (r'^checkout/', include('payment.urls')),
    (r'^contact/$', 'contact.form', {}, 'satchmo_contact'),
    (r'^history/$', 'orders.order_history', {}, 'satchmo_order_history'),
    (r'^quickorder/$', 'cart.add_multiple', {}, 'satchmo_quick_order'),
    (r'^tracking/(?P<order_id>\d+)/$', 'orders.order_tracking', {}, 'satchmo_order_tracking'),
    (r'^search/$', 'search.search_view', {}, 'satchmo_search'),
)

# here we add product patterns directly into the root url
urlpatterns += productpatterns

urlpatterns += patterns('',
    (r'^contact/thankyou/$','django.views.generic.simple.direct_to_template',
        {'template':'shop/contact_thanks.html'},'satchmo_contact_thanks'),
    (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap',
        {'sitemaps': sitemaps},
        'satchmo_sitemap_xml'),
)

urlpatterns += satchmopatterns

from django.conf.urls.defaults import *

# here we are sending a signal to add patterns to the base of the shop.
collect_urls.send(sender=shop, patterns=urlpatterns)
