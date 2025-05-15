from cdek import (
    CDEKAuth,
    CDEKToken,
    CDEKLocation,
    fetch_fake_client_id,
    fetch_fake_client_secret,
)


def main() -> None:
    cdek_auth = CDEKAuth(
        client_id=fetch_fake_client_id(),
        client_secret=fetch_fake_client_secret(),
    )
    cdek_token = CDEKToken(cdek_auth)
    print(cdek_token)
    calculator = CDEKLocation(cdek_token)
    print(calculator.fetch_regions())


if __name__ == "__main__":
    main()
