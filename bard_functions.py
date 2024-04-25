# from bardapi import BardCookies
# from gemini import Gemini
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)


# ------------------------------------------------------------------
# Provide input to Bard and get output
# Input - Prompt String
# Output - Answer of Prompt String

def answer_prompt_bard(query):
    # To store the session of Bard
    # cookies = {"_ga": "GA1.1.320811548.1709229555", "AEC": "AQTF6Hw1rRoVGiH3sevDEbqX6eLTfUFZwIBSwSnPx2uW5InmSE7VsFuHTg",
    #            "1P_JAR": "2024-04-11-04",
    #            "SID": "g.a000iggtRa_5UA2BgE2mkJ_ZHFTuJUSHp1xMpqqdrRY2I8D04KTgpEqlnqLWRZHBf1ZngIdLnAACgYKAboSAQASFQHGX2MioVk9p7E8h476QKElW_DDWhoVAUF8yKoN26m1iPr58B1yoCN9Ilez0076",
    #            "__Secure-1PSID": "g.a000iggtRa_5UA2BgE2mkJ_ZHFTuJUSHp1xMpqqdrRY2I8D04KTgZnZfa7gr9DVhdCfd5CQhOAACgYKAaUSAQASFQHGX2MikwXIYaYkRQx8eX-llxN7khoVAUF8yKoEVjM0gbxlj2zF6hCaLNUe0076",
    #            "__Secure-3PSID": "g.a000iggtRa_5UA2BgE2mkJ_ZHFTuJUSHp1xMpqqdrRY2I8D04KTgfYs11VWIi87A_rAB_HjjFwACgYKAa8SAQASFQHGX2Mi6lr_e1QS7WKyDlrIGskJfRoVAUF8yKoJZucn9Qj-W8ruzLuiUOHI0076",
    #            "HSID": "A_rdN0cWXpQmoVzpq", "SSID": "A0K9VxzvqK_z2bxEO", "APISID": "ar8WmoiW9DayMKyU/AriatMESjYnTzvpP6",
    #            "SAPISID": "5Pra-XlXt_Ml7lRx/AO6EkY9CkpKPhAUbA",
    #            "__Secure-1PAPISID": "5Pra-XlXt_Ml7lRx/AO6EkY9CkpKPhAUbA",
    #            "__Secure-3PAPISID": "5Pra-XlXt_Ml7lRx/AO6EkY9CkpKPhAUbA", "OGPC": "19026792-1:", "OGP": "-19026792:",
    #            "NID": "513", "_ga_WC57KJ50ZZ": "GS1.1.1713361978.3.1.1713362034.0.0.0",
    #            "__Secure-1PSIDTS": "sidts-CjEB7F1E_FhZ0Aq2mmn71zk0RbrwTAMQ76BYtxZMMS7o0tocT9Nb8Tv-GpIe6lZpi19rEAA",
    #            "__Secure-3PSIDTS": "sidts-CjEB7F1E_FhZ0Aq2mmn71zk0RbrwTAMQ76BYtxZMMS7o0tocT9Nb8Tv-GpIe6lZpi19rEAA",
    #            "SIDCC": "AKEyXzVDbsHvlMpH9ABWF_7TxIAFZeUDSR5BhW88IEygLcKsne-aMhommuXJEbxtpfuYvMPRh_7N",
    #            "__Secure-1PSIDCC": "AKEyXzVY3inONO5mk38_7KL_19avBxSR2EUX6Vc7nhCl_fjHWKhiDOFuKECgsMlr9zJFRdcoplU",
    #            "__Secure-3PSIDCC": "AKEyXzWspk27oU0MshdYmvqt02D_8VDpa1eF21L97_4IAMObjK3Gex4-xTU3BBAArd8fZek0rDQi"}

    # bard = BardCookies(cookie_dict=cookie_dict)
    # GeminiClient = Gemini(cookies=cookies)
    # response = GeminiClient.send_request(query)
    # print(response.text)

    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(query)

    return response.text

    # ans = bard.get_answer(query)
    # return ans['content']


# ------------------------------------------------------------------
# Create an optimal prompt for creating an advertisement
# Input - Features of product and customer
# Output - Prompt String

def create_prompt_from_description(product_name, product_desc, customer_name, customer_interests,
                                   delivery_platform="WhatsApp"):
    prompt = "Generate a creative personalized according to customer's interests' short text-based advertisement to " \
             "be delivered on '" + delivery_platform + "' including emojis for the product - '" + product_name + "' with " \
                                                                                                                 " the description - '" + product_desc + "'. The advertisement is to be delivered to the customer named '" + customer_name + \
             "' whose interests are as follows - '" + customer_interests + "'. No need of Hashtags. No need of product " \
                                                                           "link. Start with response directly. "
    return prompt


# ------------------------------------------------------------------
# print(answer_prompt_bard("Hello"))
