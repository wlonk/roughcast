import pytest


@pytest.mark.django_db
class TestLoginView:
    def test_serializer_errors(self, client):
        response = client.post("/api/login/")
        assert response.status_code == 400
        assert response.json() == {
            "username": ["This field is required."],
            "password": ["This field is required."],
        }
