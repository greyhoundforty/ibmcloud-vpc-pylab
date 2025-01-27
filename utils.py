import os
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_cloud_sdk_core import ApiException

ibmcloud_api_key = os.environ.get("IBMCLOUD_API_KEY")
if not ibmcloud_api_key:
    raise ValueError("IBMCLOUD_API_KEY environment variable not found")


def ibm_auth_client():
    try:
        authenticator = IAMAuthenticator(ibmcloud_api_key)
        return authenticator
    except ApiException as e:
        raise ValueError(f"Failed to authenticate with IBM Cloud: {e}")


def vpc_client(region):
    """IBM Cloud VPC client."""
    try:
        authenticator = ibm_auth_client()
        vpc_service = VpcV1(
            authenticator=authenticator
        )
        vpc_service.set_service_url(f"https://{region}.iaas.cloud.ibm.com/v1")
        return vpc_service
    except ApiException as e:
        raise ValueError(f"Failed to create VPC client: {e}")

def create_vpc(vpc_name, region, vpc_resource_group_id):
    """Create a VPC in the specified region."""

    resource_group_identity_model = {}
    resource_group_identity_model["id"] = vpc_resource_group_id

    address_prefix_management = "auto"
    classic_access = False
    resource_group = resource_group_identity_model
    vpc_service = vpc_client(region)
    create_vpc_response = vpc_service.create_vpc(
        address_prefix_management=address_prefix_management,
        classic_access=classic_access,
        name=vpc_name,
        resource_group=resource_group,
    )

    vpc = create_vpc_response.get_result()
    new_vpc_id = vpc["id"]
    print(new_vpc_id)
    return vpc