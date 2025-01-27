import os
import click
from tamga import Tamga
from utils import *
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

logger = Tamga(logToJSON=True, logToConsole=True)

ibmcloud_api_key = os.getenv("IBMCLOUD_API_KEY")
if not ibmcloud_api_key:
    logger.error("IBMCLOUD_API_KEY is not set")
    exit(1)

tailscale_api_key = os.getenv("TAILSCALE_API_KEY")
if not tailscale_api_key:
    logger.error("TAILSCALE_API_KEY is not set")
    exit(1)

tailnet_id = os.getenv("TAILNET_ID")
if not tailnet_id:
    logger.error("TAILNET_ID is not set")
    exit(1)

## need additional click options for `public` and `private` to determine if we create public gateways
## then need logic to attach subnets if public gateway is created
@click.command()
@click.option(
    "--region",
    prompt="Enter the IBM Cloud region to deploy the VPC",
    help="IBM Cloud region",
)
@click.option(
    "--ssh-key",
    prompt="Name of an existing SSH key in the region. If not provided, a new one will be created.",
    help="VPC SSH key name",
)
@click.option(
    "--dns-zone",
    prompt="Name of the Private DNS zone to create",
    help="DNS Zone name",
)
def main(region, ssh_key, dns_zone):
    """ """
    logger.info(f"Creating VPC in the {region} region")
    logger.info(f"Using SSH key: {ssh_key} for compute instance.")
    # create vpc, gateway, subnets
    # create dns service instance, zone, vpc attachment
    # create tailscale key
    # deploy vpc tailscale instance with cloud-init
    # create custom resolvers (this may be a bit further up the stack)
    create_key = create_tailscale_key(token=tailscale_api_key, tailnet_id=tailnet_id)
    logger.info(f"Created Tailscale key: {create_key}")


if __name__ == "__main__":
    main()
