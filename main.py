from cdek import (
    CDEKAuth,
    CDEKToken,
    CDEKLocation,
    RegionsRequestDto,
    fetch_fake_client_id,
    fetch_fake_client_secret,
)


def main() -> None:
    cdek_auth = CDEKAuth(
        client_id=fetch_fake_client_id(),
        client_secret=fetch_fake_client_secret(),
    )
    location = CDEKLocation(CDEKToken(cdek_auth))
    regions = location.fetch_regions(RegionsRequestDto(country_codes=["RU"]))
    if regions:
        regions.sort(key=lambda region: region.country_code)
        for index, region in enumerate(regions):
            print(f"{index} - {region}")


if __name__ == "__main__":
    main()
