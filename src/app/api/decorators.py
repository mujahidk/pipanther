"""
Decorators

All API related decorators are available here.
"""
from functools import wraps

def crossdomain(domain):
    """
    Adding cross domain access control decorator to routes.

    Read more about 'Cross-Origin Resource Sharing'(CORS)
    URL: https://www.w3.org/TR/cors/
    """
    def decorator(function):
        """
        Decorator function.
        """
        @wraps(function)
        def wrapper(*args, **kwargs):
            """
            Decorated function wrapper. This method assumes the decorated method returns response
            object and adds HTTP header.
            """
            # Call the original method
            response = function(*args, **kwargs)
            # Add CORS header to response.
            response.headers['Access-Control-Allow-Origin'] = domain
            return response
        return wrapper
    return decorator
