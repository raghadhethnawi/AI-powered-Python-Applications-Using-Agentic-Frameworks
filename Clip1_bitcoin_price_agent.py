import requests # Step 1: Import the requests library to handle API calls

# Step 2: Define a class to represent the API Agent
class BitcoinPriceAgent:
    def __init__(self, api_url):
        """
        Step 3: Initialize the agent with the API URL.
        :param api_url: URL of the API to fetch Bitcoin price data
        """
        
        self.api_url = api_url
        
    def fetch_bitcoin_price(self):
        """
        Step 4: Fetch the current Bitcoin price in USD from the API and display it.
        """
        try:
            # Step 4.1: Make a GET request to the API 
            response = requests.get(self.api_url)
            
            # Step 4.2: Check if the response was successful
            if response.status_code == 200:
               # Step 4.3: Pasrse the JSON data returned by the API 
               data = response.json()
               
               # Step 4.4: Extract the Bitcoin price in USD
               bitcoin_price = data['bitcoin']['usd']
               
               # Step 4.5: Print the current Bitcoin price
               print(f"Current Bitcoin Price (USD): ${bitcoin_price}")
            else:
                # Step 4.6: Handle cases where the API call fails
                print("Failed to fetch Bitcoin price. Please check the API")
        except Exception as e:
            # Step 4.7: Handle exceptions such as network errors or invalid responses
            print(f"An error occured: {e}")
        
# Step 5: Define the API URL for the CoinDesk Bitcoin Price Index
api_url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"

# Step 6: Create an instance of the BitcoinPriceAgent with the API URL
agent = BitcoinPriceAgent(api_url)

# Step 7: Execute the Agent's task to fetch and display the Bitoin price
agent.fetch_bitcoin_price()