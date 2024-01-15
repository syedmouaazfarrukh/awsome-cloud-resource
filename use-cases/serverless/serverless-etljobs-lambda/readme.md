### Leverage Batch Processing for ETL Jobs on AWS

#### Problem Statement:

An e-commerce company receives a large volume of daily transaction data that needs to be processed and loaded into a data warehouse for analytics. The current process relies on traditional ETL (Extract, Transform, Load) jobs running on a fixed schedule, which results in occasional performance bottlenecks and delays during peak times.

#### Existing State:

The current ETL process is handled by a monolithic application running on a single server. The system struggles to cope with the increasing volume of daily transactions, leading to slower processing times and occasional job failures. Scaling the existing infrastructure to handle peak loads is both time-consuming and resource-intensive.

#### Proposed Solutions:


### Solution 2: Serverless Batch Processing with AWS Lambda and Step Functions

**Description:**
Refactor ETL jobs into serverless functions using AWS Lambda and orchestrate them using AWS Step Functions. Each function performs a specific task in the ETL process.

**Advantages:**
- **Zero Server Management:** AWS Lambda automatically scales based on the number of incoming events.
- **Cost-Efficiency:** Pay only for the compute time consumed by each Lambda function.
- **Ease of Orchestration:** Step Functions simplifies the coordination of multiple Lambda functions, providing a visual representation of the workflow.

**Estimated Costs/Quotas:**
- Costs are based on the number of Lambda invocations and execution time.
- AWS provides a free tier for Lambda and Step Functions, covering a certain number of requests and compute time.
- Additional costs may include data transfer and storage for processed data.

**Step by Step Implementation:**

1. Download the dataset from [Kaggle](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce?resource=download) to be used as sample.
2. *In progress*


### Conclusion:

Both solutions offer efficient ways to leverage batch processing for ETL jobs on AWS. The choice between containerization with ECS and serverless with Lambda depends on factors such as the complexity of ETL workflows, resource requirements, and preferred management style. It's essential to analyze the specific needs of the ETL process and consider the associated costs for data storage, transfer, and compute resources.
