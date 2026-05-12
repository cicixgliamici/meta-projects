# Terraform Lab

This is a simple laboratory to understand the basic concepts of Infrastructure as Code (IaC) with Terraform.

## Prerequisites
- Terraform CLI installed.
- AWS credentials configured (`aws configure`), or you can simply run the validation commands to study the syntax without deploying anything.

## Basic Commands

1. **Initialization**: Downloads the necessary providers (e.g., AWS).
   ```bash
   terraform init
   ```

2. **Formatting and Validation**: Ensure the code is correct before proceeding.
   ```bash
   terraform fmt
   terraform validate
   ```

3. **Planning (Dry Run)**: Shows what Terraform intends to create, modify, or destroy. This is essential for reviewing changes!
   ```bash
   terraform plan
   ```

4. **Application**: Actually creates the infrastructure.
   ```bash
   terraform apply
   ```

5. **Destruction**: Deletes all created resources (essential so you don't pay unnecessary AWS costs after the lab).
   ```bash
   terraform destroy
   ```
