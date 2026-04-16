prices = [50, 55, 50, 60, 65]

# Step 1: returns
returns = []
for i in range(1, len(prices)):
    r = (prices[i] - prices[i-1]) / prices[i-1]
    returns.append(r)

# Step 2: moving average + signals
k = 2
window_sum = sum(returns[:k])
prev_avg = window_sum / k

profit = 0

for i in range(k, len(returns)):
    window_sum += returns[i] - returns[i-k]
    curr_avg = window_sum / k

    # signal
    if curr_avg > prev_avg:
        print("BUY")
        profit += prices[i+1] - prices[i]   # next price move
    else:
        print("SELL")
        profit += prices[i] - prices[i+1]

    prev_avg = curr_avg

print("Total Profit:", profit)