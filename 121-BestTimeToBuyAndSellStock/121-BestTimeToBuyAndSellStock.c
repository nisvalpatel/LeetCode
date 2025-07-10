// Last updated: 7/10/2025, 11:58:21 AM
int maxProfit(int* prices, int pricesSize) {
    int buyDay = 0;
    int profit = 0;
    int temp_profit;
    for (int i = 1; i < pricesSize; i++){
        temp_profit = prices[i] - prices[buyDay];
        if (prices[i] < prices[buyDay]){
            buyDay = i;
        } else if (temp_profit > profit){
            profit = temp_profit;
        }
    }
    return profit;
}