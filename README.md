# Awesome-Cloud-Resource

This resource is aimed at helping you design and implement cloud solutions increasing your domain expertise along with real-world industry level use cases. We'll be designing/developing cloud solutions on the basis of:
  - [Use Case]()
  - [Type of Industry]()
  - [Organization Type]()

## Use Cases
Implement the following cloud solutions to get hands-on with cloud technologies.
### 1. [Migrating on-prem application to AWS]()
#### Problem Statment:
A company wants to migrate its on-premises application to AWS. The application produces output files that vary in size from tens of gigabytes to hundreds of terabytes. The application data must be stored in a standard file system structure. The company wants a solution that scales automatically. is highly available, and requires minimum operational overhead
#### Solution:
For this scenario, an effective solution would involve leveraging AWS services to meet the scalability, high availability, and operational efficiency requirements. Here's an architecture that addresses the company's needs:

1. **AWS S3 for File Storage:**
   - Use Amazon S3 to store the application output files, as it offers highly scalable, durable, and available object storage with virtually unlimited capacity.
   - Configure lifecycle policies to automatically transition older files to cheaper storage tiers like S3 Infrequent Access or Glacier to minimize costs.

2. **AWS Snowball or AWS DataSync for Data Transfer:**
   - In the case of large on-premises data sets, use AWS Snowball or AWS DataSync for fast and secure data transfer to AWS.

3. **AWS EFS for File System Structure:**
   - Utilize Amazon Elastic File System (EFS) to provide a fully managed, scalable file storage service that supports standard file system interfaces. EFS offers seamless scalability and can automatically grow to petabyte scale.

4. **AWS Lambda for Automation:**
   - Employ AWS Lambda to automate the scaling and management of the application resources. Lambda can trigger operations based on defined criteria, ensuring the system can handle varying workloads with minimal manual intervention.

5. **Amazon CloudWatch for Monitoring:**
   - Implement Amazon CloudWatch to monitor the performance and health of the application and storage services. Configure alarms and automated responses to ensure high availability and timely remediation of issues.

By implementing this AWS architecture, the company can achieve a highly scalable, available, and low operational overhead solution for migrating their on-premises application to the cloud.
