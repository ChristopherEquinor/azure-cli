from azure.mgmt.resource.resources import (ResourceManagementClient,
                                           ResourceManagementClientConfiguration)
from azure.cli.commands._command_creation import get_mgmt_service_client

def _resource_client_factory(**_):
    return get_mgmt_service_client(ResourceManagementClient, ResourceManagementClientConfiguration)
