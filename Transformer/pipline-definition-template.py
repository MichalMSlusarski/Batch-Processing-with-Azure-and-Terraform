from azure.identity import DefaultAzureCredential
from azure.mgmt.datafactory import DataFactoryManagementClient
from azure.mgmt.resource import ResourceManagementClient

subscription_id = '<subscription-id>'
resource_group_name = '<resource-group-name>'
data_factory_name = '<data-factory-name>'
template_file_path = '<path-to-arm-template.json>'

credential = DefaultAzureCredential()

resource_client = ResourceManagementClient(credential, subscription_id)
datafactory_client = DataFactoryManagementClient(credential, subscription_id)

with open(template_file_path, 'r') as template_file:
    template = template_file.read()

deployments = resource_client.deployments.begin_create_or_update(
    resource_group_name,
    'DataFactoryDeployment',
    {
        'properties': {
            'mode': 'Incremental',
            'template': template,
        }
    }
)

deployment_result = deployments.result()

print("ARM Template deployment status:", deployment_result.properties.provisioning_state)
