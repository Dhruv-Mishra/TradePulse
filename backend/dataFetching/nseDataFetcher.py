from nsepython import nse_largedeals_historical

from_date = "14-08-2025"
to_date = "15-08-2025"
result = nse_largedeals_historical(from_date, to_date,"bulk_deals")
print(result)