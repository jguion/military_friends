from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',

	url(r'military_friends/?', 'friend_locations.views.military_friends'),
	url(r'save_base/?', 'friend_locations.views.save_base'),
	url(r'get_friends/?', 'friend_locations.views.get_friends'),
	
)
