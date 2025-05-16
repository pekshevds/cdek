import pytest
from cdek import (
    fetch_fake_client_id,
    fetch_fake_client_secret,
    CDEKAuth,
    CDEKToken,
    CDEKLocation,
)


@pytest.fixture()
def fake_token() -> CDEKToken:
    return CDEKToken(
        CDEKAuth(
            client_id=fetch_fake_client_id(), client_secret=fetch_fake_client_secret()
        )
    )


@pytest.fixture()
def location(fake_token: CDEKToken) -> CDEKLocation:
    return CDEKLocation(token=fake_token)
