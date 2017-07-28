import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler, Stream, API
from confluent_kafka import Producer, KafkaError
import tweepy
import ast

consumer_key = 'Ldo3AYvmEUafLCYa9XG4xqZpA'
consumer_secret = 'kgwMI52weme9PWSt0EhBDuBJzNvrim5gCcnoR2gAa8rTIPmdry'
access_token = '763088089837293568-5BiCrY2uyeSlV5YlWBdzlUwPC6TIwEx'
access_token_secret = 'kko4RLMGw6ndDcPWweZ4HaOWq4X0HhOjgwPjvI34LCtkB'

# producer
class KafkaTweetListener(StreamListener):

    def __init__(self,p):
        self.p = p

    def on_data(self, data):
        # load tweet json object from data
        # use producer to publish tweet message to topic
        p.produce('test', data+'\n')
        data = json.loads(data)
        print(data['text'] +'\n')
        return True

    def on_error(self, status):
        print('Error:',status)


if __name__ == '__main__':
    print("starting tweet stream")

    # instantiate listener
    # instantiate a stream (passing auth credentials)
    # start the filtered stream tracking one or more popular hashtags

    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = API(auth)
    
    conf_p = {'bootstrap.servers': 'localhost,9092',
            'group.id': 'predictor-p',
            'default.topic.config': {'acks': 'all'}
    }

    p = Producer(conf_p)

    tweetListener = KafkaTweetListener(p)
    tweetStream = Stream(auth=api.auth, listener=tweetListener)
    tweetStream.filter(track=['ethereum'])

    p.flush()
    