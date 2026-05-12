# -----------------------------------------------------------------------------
# TERRAFORM VARIABLES FILE
# -----------------------------------------------------------------------------
# Variables allow you to customize Terraform modules without altering the
# actual source code in main.tf. This makes your code reusable across
# different environments (e.g., dev, staging, prod).

variable "aws_region" {
  description = "The AWS region where resources will be deployed (e.g., us-east-1, eu-west-1)"
  type        = string
  default     = "eu-west-1" # If the user doesn't provide a value, fallback to Ireland.
}
