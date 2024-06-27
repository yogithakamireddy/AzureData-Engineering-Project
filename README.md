# Azure-Data-Engineering-Project
## Introduction
The use case for this project is building an end to end solution by ingesting the tables from on-premise SQL Server database using Azure Data Factory and then store the data in Azure Data Lake. Then Azure databricks is used to transform the RAW data to the most cleanest form of data and then we are using Azure Synapse Analytics to load the clean data and finally using Microsoft Power BI to integrate with Azure synapse analytics to build an interactive dashboard. Also, we are using Microsoft Entra ID and Azure Key Vault for the monitoring and governance purpose. 
## Architecture
(https://github.com/yogithakamireddy/AzureData-Engineering-Project/assets/147282987/a073d8d3-e609-44eb-8f05-b97ac652a6d8)
## Technologies Used
1. Microsoft SQL Server
2. Azure Data Factory
3. Azure Data Lake Storage Gen2
4. Azure Databricks
5. Azure Synapse Analytics
6. Azure Key vault
7. Microsoft Entra ID and
8. Microsoft Power BI
9. Python 
## Setup and Installation
To install Microsoft SQL server download .exe file from :https://www.microsoft.com/en-in/sql-server/sql-server-downloads
After installation, you need to install SQL Server Management Studio or SSMS download it from the following 
link:https://learn.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms?view=sql-server-ver15
### Database samples
Link:https://learn.microsoft.com/en-us/sql/samples/adventureworks-install-configure?view=sql-server-ver16&tabs=ssms#download-backup-files
## Data Pipeline Details
### Data Ingestion
<b>Data Source:</b> The data is sourced from an on-premises SQL Server database.
Method of ingestion: The data is ingested into Azure using Azure Data Factory (ADF). The following steps outline the process:
1. Install Integration Runtime: Install a self-hosted integration runtime (SHIR) to securely connect the on-premises SQL Server database to Azure Data Factory.
2. Create Linked Services: Linked services define the connection to the data source (on-premises SQL Server) and the data destination (Azure Data Lake).
3. Create Datasets for SQL server tables and Azure bronze container
4. Create pipeline : The pipeline consists of a linked service to the SQL Server, a linked service to Azure Data Lake, datasets for both the source and destination, and a copy activity that defines the data movement.
### Data Transformation
. In Azure Data Lake Storage, create two additional containers: silver and gold.</br>
. <b>Mount Azure Data Lake Storage to Databricks</b> to access the data stored in the bronze, silver, and gold containers.</br>
. Bronze to Silver Transformation:</br>
  &nbsp;&nbsp;Objective: Apply initial transformations to the raw data loaded into the bronze container.</br>
  &nbsp;&nbsp;Process: The data from the bronze container is read, transformed, and then written to the silver container.</br>
  &nbsp;&nbsp;Notebook: The transformation logic is implemented in a Databricks notebook, which is available in the Bronze to Silver Notebook.</br>
. Silver to Gold Transformation:</br>
  &nbsp;&nbsp;Objective: Apply further transformations to the data in the silver container to create a refined dataset.</br>
  &nbsp;&nbsp;Process: The data from the silver container is read, additional transformations are applied, and the final dataset is written to the gold container.</br>
  &nbsp;&nbsp;Notebook: The transformation logic is implemented in a Databricks notebook, which is available in the Silver to Gold Notebook.</br> 
. Integrating Notebooks with Azure Data Factory:</br>
  &nbsp;&nbsp;The Databricks notebooks are integrated into the Azure Data Factory pipeline created in the Data Ingestion part.</br>
### Data Loading
. Create a serverless SQL database in Azure Synapse Analytics\
. Configure a connection between Azure Data Lake and Synapse Analytics to ensure that data updates in the Data Lake are reflected in the serverless SQL database.\
. Create a synapse pipeline to load data from gold container into the serverless SQL DB, creating views in the serverless SQL DB.\
. The stored procedure script is available in the StoredProcedure script.
### Reporting
. Connect Power BI to the serverless SQL database in Azure Synapse Analytics to enable data visualization and reporting.\
. Use the imported data in Power BI to create dashboards and reports.
### End-to-End Pipeline Testing
A Trigger was implemented in Databricks to automate the execution of the data pipeline. Upon triggering, the pipeline successfully detected and processed new data inserted into the on-premise SQL database.</br>This updated data was seamlessly loaded into the serverless SQL database in Azure Synapse Analytics. The updated data in the serverless database automatically refreshed Power BI analytics, ensuring real-time insights and accurate analysis.
## Challenges
During the project, I faced challenges with access management, specifically with Azure Role-Based Access Control (RBAC). Properly configuring RBAC to ensure the right permissions and access levels was critical but sometimes complex.

For more information on Azure RBAC, refer https://learn.microsoft.com/en-us/azure/role-based-access-control/overview.
