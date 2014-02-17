from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',

	url(r'military_friends/?', 'friend_locations.views.military_friends'),
	url(r'save_base/?', 'friend_locations.views.save_base'),
	url(r'get_friends/?', 'friend_locations.views.get_friends'),
	(r'^facebook/', include('django_facebook.urls')),
	(r'^accounts/', include('django_facebook.auth_urls')), #Don't add this line if you use django registration or userena for registration and auth
	#url(r'boston/?$', 'boston_disorder.views.crm'),
    #url(r'boston/physical/(?P<map_type>[a-zA-Z0-9: _]*)/?$', 'boston_disorder.views.crm'),
    #url(r'boston/social/(?P<map_type>[a-zA-Z0-9: _]*)/?$', 'boston_disorder.views.calls'),
    #url(r'boston/display_map/physical/(?P<map_type>[a-zA-Z0-9: _]*)/?$', 'boston_disorder.views.limited_crm'),
    #url(r'boston/display_map/social/(?P<map_type>[a-zA-Z0-9: _]*)/?$', 'boston_disorder.views.limited_calls'),
    #url(r'boston/more_info/?$', 'boston_disorder.views.more_info')

)
