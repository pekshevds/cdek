from cdek import CDEKAuth, CDEKToken, CDEKDeliveryPoint


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
    delivery_point = CDEKDeliveryPoint(cdek_token)
    print(delivery_point.fetch_deliverypoints(city_code=270))


if __name__ == "__main__":
    main()
