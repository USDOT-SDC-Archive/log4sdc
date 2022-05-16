# Deployment Plan

### Deployment Build Environment
- Windows or Linux
- AWS CLI [version 2.1.39](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html)
- Terraform [v0.12.26](https://releases.hashicorp.com/terraform/0.12.26/)
- AWS Provider [2.70.0](https://registry.terraform.io/providers/hashicorp/aws/2.70.0)

### Deployment of [v2.1](https://github.com/USDOT-SDC/sdc-dot-gitlab/tree/2.1)

* Copy tfstate file from old s3 bucket location to the new location
  * aws s3 cp s3://prod-lambda-bucket-004118380849/sdc-dot-gitlab/terraform/terraform.tfstate s3://prod.sdc.dot.gov.platform.terraform/sdc-dot-gitlab/terraform/terraform.tfstate
* Clone the sdc-dot-gitlab repository into a Linux environment (e.g., SDC build machine)
* Change to the sdc-dot-gitlab folder
* Change to the terraform folder
  * cd terraform
* Copy gitlab configuration file gitlab.rb into the binary bucket
  * aws s3 cp gitlab.rb s3://prod-sdc-dot-binaries-004118380849/gitlab/
* Execute the following commands to deploy the updates:
  * terraform init -var-file=config/backend-ecs-prod.tfvars
  * terraform apply -var-file=config/ecs-prod.tfvars

