"""Test cases for error handlers"""


from service import app
from service.models import DataValidationError
from service.common import status
from service.common.error_handlers import (
    request_validation_error,
    bad_request,
    not_found,
    method_not_supported,
    mediatype_not_supported,
    internal_server_error,
)


def test_request_validation_error():
    """It should test the request_validation_error handler"""
    with app.app_context():
        resp, code = request_validation_error(DataValidationError("bad data"))
        assert code == status.HTTP_400_BAD_REQUEST
        data = resp.get_json()
        assert data["error"] == "Bad Request"
        assert data["message"] == "bad data"


def test_bad_request():
    """It should test the bad_request handler"""
    with app.app_context():
        resp, code = bad_request("bad request")
        assert code == status.HTTP_400_BAD_REQUEST
        data = resp.get_json()
        assert data["error"] == "Bad Request"


def test_not_found():
    """It should test the not_found handler"""
    with app.app_context():
        resp, code = not_found("missing")
        assert code == status.HTTP_404_NOT_FOUND
        data = resp.get_json()
        assert data["error"] == "Not Found"


def test_method_not_supported():
    """It should test the method_not_supported handler"""
    with app.app_context():
        resp, code = method_not_supported("method not allowed")
        assert code == status.HTTP_405_METHOD_NOT_ALLOWED
        data = resp.get_json()
        assert data["error"] == "Method not Allowed"


def test_mediatype_not_supported():
    """It should test the mediatype_not_supported handler"""
    with app.app_context():
        resp, code = mediatype_not_supported("wrong content type")
        assert code == status.HTTP_415_UNSUPPORTED_MEDIA_TYPE
        data = resp.get_json()
        assert data["error"] == "Unsupported media type"


def test_internal_server_error():
    """It should test the internal_server_error handler"""
    with app.app_context():
        resp, code = internal_server_error("server exploded")
        assert code == status.HTTP_500_INTERNAL_SERVER_ERROR
        data = resp.get_json()
        assert data["error"] == "Internal Server Error"
