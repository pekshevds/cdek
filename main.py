from cdek import CDEKAuth, CDEKToken, CDEKLocation


def fetch_fake_client_id() -> str:
    return "wqGwiQx0gg8mLtiEKsUinjVSICCjtTEP"


def fetch_fake_client_secret() -> str:
    return "RmAmgvSgSl1yirlz9QupbzOJVqhCxcP5"


def fetch_fake_url() -> str:
    return "/v2/oauth/token"


def main() -> None:
    cdek_auth = CDEKAuth(
        client_id=fetch_fake_client_id(),
        client_secret=fetch_fake_client_secret(),
    )
    cdek_token = CDEKToken(cdek_auth)
    print(cdek_token)
    location = CDEKLocation(cdek_token)
    print(location.fetch_postalcodes(code=30233))


if __name__ == "__main__":
    main()
