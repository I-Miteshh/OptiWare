# OptiWare - Data Warehouse Optimization

**OptiWare** is a project focused on optimizing data warehouse performance using Azure services and modern data engineering techniques. The project includes:

- **Data Warehouse Optimization**: Implementing Columnstore and B-Tree indexing strategies in Azure Data Lake and Azure Databricks, improving query performance by 20% and reducing data retrieval times.
- **Real-Time Data Ingestion**: Integrating efficient data pipelines with Apache Kafka to handle real-time data ingestion.
- **Data Visualization**: Using Power BI for visualizing insights, improving data processing efficiency by 30% and enhancing real-time analytics capabilities.

## Directory Structure

- **data/**: Contains raw and processed data files.
- **scripts/**: Includes setup and data ingestion scripts.
- **notebooks/**: Contains Databricks notebooks for data processing.
- **adf_pipeline/**: Contains Azure Data Factory pipeline templates.
- **kafka_scripts/**: Includes Kafka producer and consumer scripts.
- **visualization/**: Contains Power BI and other visualization files.

## Setup Instructions

1. Clone the repository:
   
- git clone https://github.com/your-username/OptiWare.git
-  cd OptiWare

2. Run the setup script:
- cd scripts
- chmod +x install.sh
- ./install.sh

3. Upload dataset and configure Azure services as needed.

4. Set up Kafka producers and consumers using the provided scripts.

5. Configure and deploy the ADF pipeline using the provided template.

### Summary

 OptiWare leverages advanced data engineering techniques to optimize data warehouse performance and streamline real-time analytics.
