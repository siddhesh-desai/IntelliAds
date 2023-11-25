from bardapi import BardCookies


# ------------------------------------------------------------------
# Provide input to Bard and get output
# Input - Prompt String
# Output - Answer of Prompt String

def answer_prompt_bard(query):
    # To store the session of Bard
    cookie_dict = {
        "__Secure-1PSID": "dQj61PLYUQiINFxNU7igjgH903TfAJozliAByaQ_Sc5tlyjN0eMZWqe01m4cgSKh1xrvow.",
        "__Secure-1PSIDTS": "sidts-CjEBNiGH7vlVh7dmfArOPW7c4S3i5H-j5_Bd-WPb3CrBsohPIfHHzf_B-i5_LpP77HJOEAA"
    }

    bard = BardCookies(cookie_dict=cookie_dict)

    ans = bard.get_answer(query)
    return ans['content']


# ------------------------------------------------------------------
# Create an optimal prompt for creating an advertisement
# Input - Features of product and customer
# Output - Prompt String

def create_prompt_from_description(product_name, product_desc, customer_name, customer_interests, delivery_platform="WhatsApp"):
    prompt = "Generate a creative personalized according to customer's interests' short text-based advertisement to " \
             "be delivered on '" + delivery_platform + "' including emojis for the product - '" + product_name + "' with " \
            " the description - '" + product_desc + "'. The advertisement is to be delivered to the customer named '" + customer_name + \
             "' whose interests are as follows - '" + customer_interests + "'. No need of Hashtags. No need of product " \
            "link. Start with response directly. "

    return prompt

# ------------------------------------------------------------------
# print(answer_prompt_bard("Hello"))
