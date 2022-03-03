#Importing relevant packages
import json 

#Defining simple moving average function with prices as parameter
def simpleMovingAverageStrategy(prices):

#Initializing variables    
    i = 0
    buy = 0
    total_profit = 0
    first_buy = 0
    
#Creating a for loop to go through the prices for moving averafe
    for p in prices:
        if i >= 5: 
            moving_average = (prices[i-1] + prices[i-2] + prices[i-3] + prices[i-4] + prices[i-5]) / 5 #Taking moving average of 5 days
        
            if p > moving_average and buy == 0: #buy
                print("buying at: ", p)
                buy = p
                
                if first_buy == 0:
                    first_buy = p
                
            elif p < moving_average and buy != 0: #sell
                print("selling at: ", p)
                print("trade profit: ", p - buy)
                total_profit += p - buy
                buy = 0
            
        i += 1        #Iterating through each price
    
    final_percentage = (total_profit / first_buy) * 100
    print("first buy: ", first_buy)
    print("total profit: ", total_profit)
    print("final percentage: ", final_percentage, "%")
    
 #    return profit 

    return total_profit, final_percentage
    
#Defining mean reversion strategy function

def meanReversionStrategy(prices):
    
#Initializing variables
    i = 0
    buy = 0
    is_first_buy = True
    total_profit = 0
    first_buy = 0
    
#Creating a for loop
    for current_price in prices:
        
        if i >= 5:
            
            average_price = (prices[i-1] + prices[i-2] + prices[i-3] + prices[i-4] + prices[i-5]) / 5 #defining mean reversion
            if (current_price < 0.95 * average_price) and buy == 0: # buy
            
                buy = current_price
                
                print("buy at:", buy)
                
                if is_first_buy:
                    
                    first_buy = current_price
                    
                    is_first_buy = False
            
    
            elif (current_price > 1.05 * average_price) and buy != 0: # sell
                
                profit = current_price - buy
                profit = round(profit, 2)
                
                print("sell at:", current_price)
                print("trade profit:", profit)
                
                total_profit += profit
                
                buy = 0
        
        i += 1
        
#Printing all the relevant variables    

    print("---------------------------------------")
    
    print ("Total profit:", round(total_profit,2))
    
    print("First buy:", first_buy)

#Defining final profit percentage, returning profit and returns

    final_profit_percentage = (total_profit / first_buy) * 100
    final_profit_percentage = round(final_profit_percentage, 2)
    print("Percentage return:", final_profit_percentage, "%")
    
    return total_profit, final_profit_percentage

#Creating a function to save the results

def save_Results(results):
    json.dump(results,open("/home/ubuntu/environment/Homework5/results.json","w"), indent=4) 
    
#Listing all the stocks inside the ticker

tickers = ["tsla", "adbe", "amazon", "apple", "ba", "btc", "dodgx", "goog","msft", "v", "fb"]

#Storing results in the dictionary

results = {}

#Create a for loop for the tickers, so it goes through each and every one of these

for stock in tickers:
    fil = open("/home/ubuntu/environment/week10/" + stock + ".txt")
    lines = fil.readlines()
    
#Storing prices in a list, printing them 
    prices = []
    print(f'{stock} output')
    
#Creating a for loop in to append the prices 
    for line in lines:
        prices.append(float(line))
        
    profit, returns = meanReversionStrategy(prices)
    simple_profit, simple_returns = simpleMovingAverageStrategy(prices)
    
#Calling the results    

#For Simple Moving Average
    results[stock + " simple moving average profit"] = simple_profit
    results[stock + " simple moving average returns"] = simple_returns
    
#For Mean Reversion     
    results[stock + " mean reversion profit"] = profit
    results[stock + " mean reversion returns"] = returns

# Calling the function to save results    
    save_Results(results)
    