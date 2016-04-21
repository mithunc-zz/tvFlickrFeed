import web

from tvFlickrFeed import tvFlickrFeed

urls = (
	'/tvFlickrFeed.tvml', 'tvFlickrFeed'
)

if __name__ == "__main__":
	app = web.application(urls, globals())
	app.run()