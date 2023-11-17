from google.cloud import dataflow
from google.cloud import pubsub_v1



dataflow_client = dataflow.Client()
pipeline = dataflow.Pipeline(options=dataflow.PipelineOptions(beam_runner='DataflowRunner'))

# Reading from PubSub
topic_id = "customer_buyhistory"
project_id="your-project-id"
publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_id)

# Transforming Data Function
def transform_data(data):
    if data['age'] > 30:
        return data
    else:
        return None


# Add your data processing tasks to the pipeline
pipeline | 'ReadData' >> ReadFromPubSub(topic_path) | 'TransformData' >> Map(transform_data) | 'WriteToDestination' >> WriteToBigQuery(
                                                                                                query=f'INSERT INTO `swift-analogy-399205.test.bq-test` (si_id) VALUES ({data})',
                                                                                                )
# Run the pipeline
dataflow_client.run_pipeline(pipeline)
