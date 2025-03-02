from rest_framework.throttling import SimpleRateThrottle

class IPThrottle(SimpleRateThrottle):
    scope = 'ip'

    def get_cache_key(self, request, view):
        # Apply IP throttling only if the user is not authenticated
        if request.user.is_authenticated:
            return None  # No IP throttling for authenticated users
        return self.get_ident(request)