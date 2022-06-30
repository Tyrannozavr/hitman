import json
from rest_framework.renderers import JSONRenderer


class UserJsonRenderers(JSONRenderer):
    charset = 'utf-8'
    def render(self, data, accepted_media_type=None, renderer_context=None):
        token = data.get('token')

        if isinstance(token, bytes):
            data['token'] = token.decode('utf-8')

        return json.dumps({
            'user': data
        })

