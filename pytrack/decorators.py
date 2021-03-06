from django.utils.decorators import decorator_from_middleware
from minimar.pytrack.middleware import TrackVisitorMiddleware

track_visitor = decorator_from_middleware(TrackVisitorMiddleware)
