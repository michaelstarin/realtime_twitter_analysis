import oandapy
import json
from confluent_kafka import Producer, KafkaError

# Practice account ID's
account = "6980117"
access_token = "7a11383cac0d8b9c415a10ed98ae7dd4-45f4f642696ef97d375d3a61ae14f04c"
oanda = oandapy.API(environment="practice", access_token=access_token)

#producer
class MyStreamer(oandapy.Streamer):
    def __init__(self, count=99999999999999, *args, **kwargs):
        super(MyStreamer, self).__init__(*args, **kwargs)
        self.count = count
        self.reccnt = 0

    def on_success(self, data):
        p.produce('test', str(data))
        print(data, "\n")
        self.reccnt += 1
        if self.reccnt == self.count:
            self.disconnect()

    def on_error(self, data):
        self.disconnect()
        
p = Producer({'bootstrap.servers':'localhost,9092'})       
stream = MyStreamer(environment="practice", access_token=access_token)
stream.rates(account, instruments="EUR_USD",ignore_heartbeat=True)
p.flush()