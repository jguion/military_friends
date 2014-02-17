from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from friend_locations.models import *
import json

from collections import defaultdict

import urlparse
import facebook

def military_friends(request):

	bases = list(str(x.name) for x in MilitaryBase.objects.all())

	#current_location = CurrentLocation.objects.get()


	return render_to_response('login.html',
		  {'bases': bases},
		  context_instance=RequestContext(request))

def save_base(request):
	print request
	if request.POST:
		base_name = request.POST['base']
		fb_id = request.POST['fb_id']

		base = MilitaryBase.objects.get(name=base_name)
		values = {"fb_user_id":fb_id, "base":base}
		try:
			current_location = CurrentLocation.objects.get(fb_user_id=fb_id)
			setattr(current_location, "base", base)
			current_location.save()
		except CurrentLocation.DoesNotExist:
			current_location = CurrentLocation(fb_user_id=fb_id, base=base)
			current_location.save()

		return HttpResponse(status=200)
	else:
		return HttpResponse(status=404)

def get_friends(request):
	fb_id = request.GET['fb_id']
	access_token = request.GET['token']

	graph = facebook.GraphAPI(access_token)
	friends = graph.get_connections("me", "friends")

	locations = dict((x.fb_user_id, x) for x in CurrentLocation.objects.all())

	my_friends = []
	base_friends = defaultdict(list)
	base_info = {}
	for friend in friends['data']:
		fr_id = friend['id']
		current_location = locations.get(fr_id)
		if current_location:
			base = current_location.base
			info = {'fb_id':fr_id, 'base':base.name, 'latitude': base.longitude, 'longitude':base.latitude}
			my_friends.append(info)
			base_friends[base.name].append(fr_id)
			base_info[base.name] = info

	bases = {}
	for base, info in base_info.items():
		bases[base] = {'latitude': info['latitude'], 'longitude':info['longitude'], 'friends':base_friends[base]}

	current_base = locations.get(fb_id)
	if current_base:
		current_base = current_base.base.name

	json_string = json.dumps({'my_friends':my_friends, 'bases':bases, 'my_base':current_base})
	return HttpResponse(json_string)


