import falcon


class HelloWorld:
    def on_get(self, req, resp):
        resp.body = "Hello, world!"


hello_world = HelloWorld()

api = application = falcon.API()
api.add_route("/", hello_world)
