from azure.identity import DefaultAzureCredential
from azure.mgmt.datafactory import DataFactoryManagementClient
from azure.mgmt.resource import ResourceManagementClient

# Azure subscription ID, resource group name, Data Factory name, and ARM template path
subscription_id = '<your-subscription-id>'
resource_group_name = '<your-resource-group-name>'
data_factory_name = '<your-data-factory-name>'
template_file_path = '<path-to-your-arm-template.json>'

# Authenticate using Azure credentials
credential = DefaultAzureCredential()

# Initialize Resource Management and Data Factory Management clients
resource_client = ResourceManagementClient(credential, subscription_id)
datafactory_client = DataFactoryManagementClient(credential, subscription_id)

# Read the ARM template file
with open(template_file_path, 'r') as template_file:
    template = template_file.read()

# Deploy the ARM template to create or update resources (like pipeline)
deployments = resource_client.deployments.begin_create_or_update(
    resource_group_name,
    'DataFactoryDeployment',
    {
        'properties': {
            'mode': 'Incremental',
            'template': template,
            # Additional parameters, if required
        }
    }
)

deployment_result = deployments.result()

print("ARM Template deployment status:", deployment_result.properties.provisioning_state)
