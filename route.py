from http.client import HTTPException

import http.client
import json



from flask import Flask
app = Flask(__name__)

hslHost = 'api.reittiopas.fi'
hslRouteUrl = '/hsl/prod/?request=lines&user=olliko&pass=olliko&format=json&epsg_out=4326'
routes = {}

def get_route(name):
    conn = http.client.HTTPConnection(hslHost)

    if name in routes:
        print("cached %s" % name)
        return routes[name]

    try:
        print("not cached %s" % name)

        url = str.join('', (hslRouteUrl, "&query=%s" % name))
        
        print(url)
        conn.request('GET', url)
        resp = conn.getresponse()
        routes[name] = resp.read().decode()

        return routes[name]

    except HTTPException as ex:
        print("HTTPException: {0}".format(err))

    return

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/route/<name>")
def route(name):
    return get_route(name)

if __name__ == "__main__":
    app.run(port=6006, debug=True)
