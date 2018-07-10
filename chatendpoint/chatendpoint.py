# -*- coding: utf-8 -*-

"""Main module."""

import tornado.escape
import tornado.ioloop
import tornado.web


class Endpoint(tornado.web.RequestHandler):
    """Get and recieve variables with this endpoint template."""
    def post(self):
        """Get request."""
        j = tornado.escape.json_decode(self.request.body)
        # Do something with json

        response = self.process_data(j)
        if response is None:
            response = {}

        if not isinstance(response, dict):
            raise ValueError(
                f"data_processor returning non-dictionary non-null result."
                f"  This must be a dictionary: {str(response)}"
            )

        self.write(response)


def self_factory(func):
    def with_self(self, *args, **kwargs):
        return func(*args, **kwargs)
    return with_self


class ChatEndpoints(object):
    """Load all endpoints and start web app."""

    def __init__(self):
        """Init chat endpoints."""
        self._urls = []
        self._endpoint_classes = []

    def add_post_endpoint(self, path, data_processor):
        """Load post endpoints."""
        if not isinstance(path, str):
            raise ValueError(f"url must be a string. Current value: {path}")
        if not callable(data_processor):
            raise ValueError(f"data_processor must be a function")

        class A(object):
            """Dummy object."""
            def __init__(self):
                """Init."""
                self.process_data = data_processor

        E = type('E', (Endpoint, A), dict())

        self._endpoint_classes.append(E)
        self._urls.append(path)

    def start(self, port=8888):
        """Start the web application."""
        if len(self._urls) == 0:
            raise ValueError("add endpoint first before starting.")
        if len(self._urls) != len(self._endpoint_classes):
            raise ValueError(
                "Do not manually update _urls or _endpoint_classes"
            )

        endpoints = []
        for idx, url in enumerate(self._urls):
            endpoints.append((url, self._endpoint_classes[idx]))
        print("Server: https://localhost:8888")
        print("endpoints: ", endpoints)
        application = tornado.web.Application(endpoints)

        application.listen(port)
        tornado.ioloop.IOLoop.instance().start()
