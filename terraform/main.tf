# -----------------------------------------------------------------------------
# TERRAFORM MAIN CONFIGURATION FILE
# -----------------------------------------------------------------------------
# This file defines the actual infrastructure resources that Terraform will
# create, update, or destroy in the target cloud provider.

# 1. PROVIDER BLOCK
# The provider block tells Terraform which cloud provider you are using.
# Here we use AWS. Terraform will download the necessary plugins for AWS.
provider "aws" {
  region = var.aws_region
}

# 2. RESOURCE BLOCK: S3 BUCKET
# A "resource" is a piece of infrastructure. The first string ("aws_s3_bucket")
# is the resource type defined by the provider. The second ("example_bucket")
# is the internal Terraform name used to reference this resource elsewhere in code.
resource "aws_s3_bucket" "example_bucket" {
  # The actual name of the bucket in AWS. This must be globally unique!
  bucket = "meta-projects-devops-lab-bucket"

  # Tags are key-value pairs used for billing and organization in AWS.
  tags = {
    Environment = "Dev"
    Project     = "DevOps-Lab"
  }
}

# 3. RESOURCE BLOCK: SECURITY GROUP
# A Security Group acts as a virtual firewall for EC2 instances.
resource "aws_security_group" "web_sg" {
  name        = "allow_web"
  description = "Allow inbound web traffic"

  # INGRESS RULES (Inbound Traffic)
  # This block defines what traffic is allowed INTO the resource.
  ingress {
    description = "HTTP from anywhere"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"] # 0.0.0.0/0 means "all IP addresses" (public)
  }

  # EGRESS RULES (Outbound Traffic)
  # This block defines what traffic is allowed OUT of the resource.
  egress {
    from_port   = 0   # 0 to 0 with protocol "-1" means "allow all traffic"
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
