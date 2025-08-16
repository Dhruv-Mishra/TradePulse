def construct_url(option_type: str, from_date: str, to_date: str) -> str:
    url = f"https://www.nseindia.com/api/historicalOR/bulk-block-short-deals?optionType={option_type}&from={from_date}&to={to_date}&csv=true"
    return url

