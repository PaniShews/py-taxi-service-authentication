from django.test import TestCase

urlpatterns = [
    path("test-session/", test_session_view, name="test-session"),
]

