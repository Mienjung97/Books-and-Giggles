from django.http import HttpResponse


class StripeWH_Handler:
    """
    Hande Stripe webhooks
    """

    def __init__(self, request):
        self.request = request
    
    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webook event
        """

        return HttpResponse(
            content=f'Unhandled webhook recived: {event["type"]}',
            status=200)