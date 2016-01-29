from broadcast.Pubnub import Pubnub
from django.conf import settings
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse

import json


def json_response(data, status=200):
    return HttpResponse(json.dumps(data, cls=DjangoJSONEncoder), status=status, content_type="application/json")


def broadcast(channel, message):
    # Publish it to pubnub.
    pubnub_client = Pubnub(
        publish_key=settings.PUBNUB_PUBLISH_KEY,
        subscribe_key=settings.PUBNUB_SUBSCRIBE_KEY
    )
    message = json.dumps(message)

    assert len(message) < 7200, "Response content was too long for pubnub, channel: %s" % channel
    try:
        resp = pubnub_client.publish({
            'channel': channel,
            'message': message
        })
        assert isinstance(resp, list), "invalid response from pubnub %s\n\n%s" % (resp, message)
        assert resp[0] == 1, "failed response from pubnub %s\n\n%s" % (resp, message)
        return resp
    except Exception as e:
        print "Exception: ", e