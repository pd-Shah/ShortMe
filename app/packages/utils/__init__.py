from os.path import join
from urllib.parse import (
    urljoin,
    urlparse,
)
from flask import (
    request,
)


def is_url_safe(endpoint, ):
    safe = False
    if endpoint:
        ref_url = urlparse(request.host_url)
        test_url = urlparse(urljoin(
            request.host_url, endpoint
        ))
        safe = ref_url.netloc == test_url.netloc and test_url.scheme in ("http", "https",)
    return safe
