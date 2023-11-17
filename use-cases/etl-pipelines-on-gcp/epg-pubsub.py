from google.cloud import pubsub

# Create topic for each source, I'm taking: 
# 1. customer_buyhistory
# 2. customer_support
# 3. customer_buytype

def create_topic(project_id: str, topic_id: str) -> None:
   
    """Create a new Pub/Sub topic."""
    from google.cloud import pubsub_v1

    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(project_id, topic_id)

    topic = publisher.create_topic(request={"name": topic_path})

    print(f"Created topic: {topic.name}")
    
# Create push and pull subscription for each topic as: 
# 1. customer_buyhistoryd
    # customer_buyhistory_push
    # customer_buyhistory_pull
# 2. customer_support
    # customer_support_push
    # customer_support_pull
# 3. customer_buytype
    # customer_buytype_push
    # customer_buytype_pull


def create_push_subscription(project_id: str, topic_id: str, subscription_id: str, endpoint: str) -> None:
    
    """Create a new push subscription on the given topic."""
    # [START pubsub_create_push_subscription]
    from google.cloud import pubsub_v1

    # TODO(developer)
    # project_id = "your-project-id"
    # topic_id = "your-topic-id"
    # subscription_id = "your-subscription-id"
    # endpoint = "https://my-test-project.appspot.com/push"

    publisher = pubsub_v1.PublisherClient()
    subscriber = pubsub_v1.SubscriberClient()
    topic_path = publisher.topic_path(project_id, topic_id)
    subscription_path = subscriber.subscription_path(project_id, subscription_id)

    push_config = pubsub_v1.types.PushConfig(push_endpoint=endpoint)

    # Wrap the subscriber in a 'with' block to automatically call close() to
    # close the underlying gRPC channel when done.
    with subscriber:
        subscription = subscriber.create_subscription(
            request={
                "name": subscription_path,
                "topic": topic_path,
                "push_config": push_config,
            }
        )

    print(f"Push subscription created: {subscription}.")
    print(f"Endpoint for subscription is: {endpoint}")
    # [END pubsub_create_push_subscription]

def create_pull_subscription(project_id: str, topic_id: str, subscription_id: str) -> None:
    """Create a new pull subscription on the given topic."""
    # [START pubsub_create_pull_subscription]
    from google.cloud import pubsub_v1

    # TODO(developer)
    # project_id = "your-project-id"
    # topic_id = "your-topic-id"
    # subscription_id = "your-subscription-id"

    publisher = pubsub_v1.PublisherClient()
    subscriber = pubsub_v1.SubscriberClient()
    topic_path = publisher.topic_path(project_id, topic_id)
    subscription_path = subscriber.subscription_path(project_id, subscription_id)

    # Wrap the subscriber in a 'with' block to automatically call close() to
    # close the underlying gRPC channel when done.
    with subscriber:
        subscription = subscriber.create_subscription(
            request={"name": subscription_path, "topic": topic_path}
        )

    print(f"Subscription created: {subscription}")
    # [END pubsub_create_pull_subscription]


if __name__ == "__main__":

    topic_id = "customer_buyhistory"
    create_topic(project_id="your-project-id", topic_id=topic_id)

    topic_id = "customer_buyhistory"
    subscription_id = "customer_buyhistory_push"
    endpoint = "https://my-test-project.appspot.com/push"
    create_push_subscription(project_id="your-project-id", topic_id=topic_id, subscription_id=subscription_id, endpoint=endpoint)

    topic_id = "customer_buyhistory"
    subscription_id = "customer_buyhistory_pull"
    create_pull_subscription(project_id="your-project-id", topic_id=topic_id, subscription_id=subscription_id)

