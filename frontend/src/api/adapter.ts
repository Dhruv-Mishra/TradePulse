// Example adapter for block deals data
export function parseBlockDeals(apiResponse) {
  return apiResponse.map(item => ({
    date: item.DATE,
    symbol: item.SYMBOL,
    security: item['SECURITY NAME'],
    client: item['CLIENT NAME'],
    action: item['BUY / SELL'],
    quantity: Number(item['QUANTITY TRADED'].replace(/,/g, "")),
    price: Number(item['TRADE PRICE / WGHT. AVG. PRICE']),
    remarks: item.REMARKS
  }));
}
