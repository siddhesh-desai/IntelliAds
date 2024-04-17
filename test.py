from gemini import Gemini
GeminiClient = Gemini(auto_cookies=True)

# Testing needed as cookies vary by region.
GeminiClient = Gemini(auto_cookies=True, target_cookies=["__Secure-1PSID", "__Secure-1PSIDTS"])
GeminiClient = Gemini(auto_cookies=True, target_cookies="all") # You can pass whole cookies

response = GeminiClient.generate_content("Hello, Gemini. What's the weather like in Seoul today?")
print(response.payload)