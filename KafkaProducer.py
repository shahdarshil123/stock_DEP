import pandas as pd
from kafka import KafkaProducer
from time import sleep
from json import dumps
import json

def send_data():
    try:
        producer = KafkaProducer(bootstrap_servers=['localhost:9092'], #change ip here
                                value_serializer=lambda x: 
                                dumps(x).encode('utf-8'), max_block_ms=5000)
        # producer.send('demo_test', value={'surnasdasdame':'parasdasdmar'})
        df = pd.read_csv("./indexProcessed.csv")
        while True:
            dict_stock = df.sample(1).to_dict(orient="records")[0]
            producer.send('demo_test', value=dict_stock)
            print('Data row sent')
            sleep(1)

    except Exception as e:
        print(f"Error occured while connecting to Kafka server {e}")

if __name__ == '__main__':
    send_data()



