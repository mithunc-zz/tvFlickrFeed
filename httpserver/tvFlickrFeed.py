import urllib2
import json
import web
# import html

class tvFlickrFeed:
	def GET(self):

		response = urllib2.urlopen('http://api.flickr.com/services/feeds/photos_public.gne?format=json')
		data = response.read();

		data = data.replace('\\\'', '')
		data = data.replace('jsonFlickrFeed(', '')
		data = data.replace('})', "}")

		feedJson = json.JSONDecoder().decode(data)

		render = web.template.render('tvFF')

		return render.tvFlickrFeedTemplate(feedJson)