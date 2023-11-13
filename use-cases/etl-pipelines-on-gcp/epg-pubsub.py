# Import the necessary libraries
from google.cloud import pubsub

# Create a Pub/Sub client
pubsub_client = pubsub.Client()

# Create a topic
topic = pubsub_client.topic('retail-data')

# Create a publisher
publisher = topic.publisher()

# Publish data to the topic
publisher.publish(data.encode('utf-8'))
