import os
from tamga import Tamga
from utils import *

logger = Tamga(logToJSON=True,logToConsole=True)


## need additional click options for `public` and `private` to determine if we create public gateways
## then need logic to attach subnets if public gateway is created
@click.command()
@click.option(
    "--region", 
    prompt="Enter the IBM Cloud region to deploy the VPC", help="IBM Cloud region"
    )
@click.option(
    "--ssh-key",
    prompt="The name of an existing SSH key to use for the lab.",
    help="VPC SSH key name",
)
@click.option("--tailnet-id", prompt="Your Tailscale Tailnet ID", help="Tailnet ID")
@click.option(
    "--dns-zone",
    prompt="Name of the Private DNS zone to create",
    help="DNS Zone name",
)
def main(region, ssh_key, tailnet_id, dns_zone):
    """
    """
    # create vpc, gateway, subnets
    # create dns service instance, zone, vpc attachment
    # create tailscale key
    # deploy vpc tailscale instance with cloud-init
    # create custom resolvers (this may be a bit further up the stack)
    pass

if __name__ == "__main__":
    main()