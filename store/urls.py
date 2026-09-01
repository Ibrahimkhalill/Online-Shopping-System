from django.urls import path
from.import views
from django.views.generic import RedirectView
from django.conf.urls import url

urlpatterns =[
    url(r'^favicon\.ico$',RedirectView.as_view(url='/static/images/favicon.ico')),
	path('',views.store,name="store"),
	path('cart/',views.cart,name="cart"),
	path('checkout/',views.checkout,name="checkout"),

	path('update_item/',views.updateItem,name="update_item"),
    path('process_order/',views.processOrder,name="process_order"),
    path('item_search/',views.itemSearch,name="item_search"),

	
]