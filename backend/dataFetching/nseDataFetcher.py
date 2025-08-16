from backend.dataFetching.utils import construct_url

from_date = "14-08-2025"
to_date = "15-08-2025"
result = construct_url("block_deals", from_date, to_date)
print(result)