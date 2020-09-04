from datetime import datetime
from unittest.mock import MagicMock

import pytest

from roughcast.email_verification import ActivationError, _get_activation_key, activate


@pytest.mark.django_db
class TestActivate:
    def test_bad_signature(self):
        key = ""
        with pytest.raises(ActivationError) as e:
            activate(key)

        assert e.value.message == "Code is invalid."

    def test_expired_signature(self, user, freezer):
        key = _get_activation_key(user)
        current_year = datetime.now().year
        two_years_hence = current_year + 2
        freezer.move_to(f"{two_years_hence}-01-01")
        with pytest.raises(ActivationError) as e:
            activate(key)

        assert e.value.message == "Code has expired."

    def test_no_such_user(self):
        user = MagicMock()
        user.get_username.return_value = "spiders_georg"
        key = _get_activation_key(user)
        with pytest.raises(ActivationError) as e:
            activate(key)

        assert e.value.message == "No matching user found."

    def test_user_already_verified(self, user_factory):
        user = user_factory(is_email_verified=True)
        key = _get_activation_key(user)
        with pytest.raises(ActivationError) as e:
            activate(key)

        assert e.value.message == "This email is already verified."

    def test_good(self, user_factory):
        user = user_factory(is_email_verified=False)
        key = _get_activation_key(user)
        activate(key)

        user.refresh_from_db()
        assert user.is_email_verified
