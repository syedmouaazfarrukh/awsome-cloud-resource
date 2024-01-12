### Leverage Batch Processing for ETL Jobs on AWS

#### Problem Statement:

An e-commerce company receives a large volume of daily transaction data that needs to be processed and loaded into a data warehouse for analytics. The current process relies on traditional ETL (Extract, Transform, Load) jobs running on a fixed schedule, which results in occasional performance bottlenecks and delays during peak times.

#### Existing State:

The current ETL process is handled by a monolithic application running on a single server. The system struggles to cope with the increasing volume of daily transactions, leading to slower processing times and occasional job failures. Scaling the existing infrastructure to handle peak loads is both time-consuming and resource-intensive.

#### Proposed Solutions:

### Solution 1: Containerized Batch Processing with Amazon ECS (Elastic Container Service)

**Description:**
Containerize ETL jobs and deploy them on Amazon ECS. This allows for efficient packaging, rapid scaling, and dynamic resource allocation based on demand.

**Advantages:**
- **Scalability:** Easily scale the number of containers to handle varying workloads.
- **Isolation:** Each ETL job runs in its own container, ensuring resource isolation and fault tolerance.
- **Resource Efficiency:** Containers share the underlying infrastructure, maximizing resource utilization.

**Estimated Costs/Quotas:**
- Costs are based on the number of containers and their resource usage (CPU, memory).
- AWS provides a free tier for ECS, covering a certain amount of container and task resources.
- Additional costs may include data transfer and storage for processed data in Amazon S3 or a data warehouse.


**Step by Step Implementation:**

1. Download the dataset from [Kaggle](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce?resource=download) to be used as sample.
2. Setup your problem by running `use-cases\containers\containerize-etljobs-ecs\setup-your-problem\main.py`
    - It must be observed that here we are considering one/two transformation and therefore there won't be much load but in practical scenarios, etl jobs when group together are compute extensive. Play around this and learn as much as you can!
3. Now separate two ETL jobs and create separate folders for each one and test their functionalities.
4. Create Dockerfile for each job in their respective folders
5. Then follow the `docker-commands.md` to build and push your docker images on ECR (Elastic Container Registry)
6. Create ECS (Elastic Container Service) *Tasks Definitions* using a JSON format. Read [JSON Validation](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/create-task-definition.html#json-validate-for-create). You would also need to create a `executionRoleArn` for which you should read [IAM Roles](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html)
7. Create ECS cluster and connect it with your task definitions.
8. The cluster will only execute your tasks/ETL jobs once.
9. In order to run at regular intervals, Go to CloudWatch/Events/Rules, create a EventBrideRule and connect it with the cluster and tasks.



### Conclusion:

The proposed solution leverages containerized batch processing with Amazon ECS to address performance bottlenecks in an e-commerce company's ETL process. By containerizing ETL jobs, the solution offers scalability, isolation, and resource efficiency. Estimated costs include container resources, with AWS providing a free tier for ECS, and additional costs for data transfer and storage. Implementation involves dataset setup, separation of ETL jobs, Dockerfile creation, ECR image management, ECS task definition creation, and CloudWatch Events for scheduling, providing a comprehensive solution for efficient ETL processing on AWS.