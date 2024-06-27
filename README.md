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
Source of the data: The data is sourced from an on-premises SQL Server database.
Method of ingestion: The data is ingested into Azure using Azure Data Factory (ADF). The following steps outline the process:
1. Install Integration Runtime: Install a self-hosted integration runtime (SHIR) to securely connect the on-premises SQL Server database to Azure Data Factory.
2. Create Linked Services: Linked services define the connection to the data source (on-premises SQL Server) and the data destination (Azure Data Lake).
3. Create Datasets for SQL server tables and Azure bronze container
4. Create pipeline : The pipeline consists of a linked service to the SQL Server, a linked service to Azure Data Lake, datasets for both the source and destination, and a copy activity that defines the data movement.
### Data Transformation
. In Azure Data Lake Storage, create two additional containers: silver and gold.
. Mount Azure Data Lake Storage to Databricks to access the data stored in the bronze, silver, and gold containers.
. Bronze to Silver Transformation:
  Objective: Apply initial transformations to the raw data loaded into the bronze container.
  Process: The data from the bronze container is read, transformed, and then written to the silver container.
  Notebook: The transformation logic is implemented in a Databricks notebook, which is available in the Bronze to Silver Notebook.
. Silver to Gold Transformation:
  Objective: Apply further transformations to the data in the silver container to create a refined dataset.
  Process: The data from the silver container is read, additional transformations are applied, and the final dataset is written to the gold container.
  Notebook: The transformation logic is implemented in a Databricks notebook, which is available in the Silver to Gold Notebook. 
. Integrating Notebooks with Azure Data Factory:
  The Databricks notebooks are integrated into the Azure Data Factory pipeline created in the Data Ingestion part.
### Data Loading
### Reporting
### End-to-End Pipeline Testing
## Challenges
During the project, I faced challenges with access management, specifically with Azure Role-Based Access Control (RBAC). Properly configuring RBAC to ensure the right permissions and access levels was critical but sometimes complex.

For more information on Azure RBAC, refer https://learn.microsoft.com/en-us/azure/role-based-access-control/overview.
