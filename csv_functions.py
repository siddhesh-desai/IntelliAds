import pandas as pd
import sqlite3
from bard_functions import *

df = pd.read_csv('dataset1.csv')
df.columns = df.columns.str.strip()

connection = sqlite3.connect('demo.db')
df.to_sql('da', connection, if_exists='replace')


def create_ad_for_all(product_name,product_desc):
    connection = sqlite3.connect('demo.db')  # Replace 'your_database.db' with your actual database name
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM da')
    data = cursor.fetchall()
    new_data = []
    for i in data:
        cust_name = i[1]+" "+i[2]
        # product_name = "US POLO T SHirts"
        # product_desc = "Durable, Pack of 2 Black and White, Seasonal, Premium"
        cust_desc = i[7]
        pp = create_prompt_from_description(product_name=product_name, product_desc=product_desc,
                                                          customer_name=cust_name, customer_interests=cust_desc)
        print(pp)
        new_data.append(answer_prompt_bard(pp))

        # print(type(i))


    cursor.execute('ALTER TABLE da ADD COLUMN ad_gen TEXT')
    #
    print(new_data)
    #

    for index, value in enumerate(new_data):
        cursor.execute('UPDATE da SET ad_gen = ? WHERE rowid = ?', (value, index + 1))

    # for value in new_data:
    #     cursor.execute('INSERT INTO da (ad_gen) VALUES (?)', (value,))

    # Commit the changes and close the database connection
    connection.commit()
    connection.close()
#     for i in data:


