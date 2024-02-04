

# Terraform

Infrastructure as code tool that define cloud and on-prem resources in config files than you can version, reuse and share.

Why use it?
- Simplicity in keeping track of infrastructure
- Easier collaboration
- Reproducibility
- Ensure resources are removed

What terraform is not:
- Does not manage and update code on infrastructure
- Does not give you the ability to change immutable resources
- Not used to manage resources not define in your terraform files


Terraform lives on your machine and can interact/connect  with a cloud provider

Key terraform commands:
- init      get me the providers I need
- plan      what I'm about to do
- apply     do what is in the tf file
- destroy   remove everything defined in the tf file
- fmt       format the .tf file indentation

Don't forget to use terraform gitignore in your repo

To use variables in terraform you need a variables.tf file.

# Terraform Core Concepts

### Variables
Terraform has input and output variables, it is a key-value pair. Input variables are used as parameters to input values at run time to customize our deployments. Output variables are return values of a terraform module that can be used by other configurations.

### Module
Any set of Terraform configuration files in a folder is a module. Every Terraform configuration has at least one module, known as its root module.

### State
Terraform records information about what infrastructure is created in a Terraform state file. With the state file, Terraform is able to find the resources it created previously, supposed to manage and update them accordingly.

### Resources
Cloud Providers provides various services in their offerings, they are referenced as Resources in Terraform. Terraform resources can be anything from compute instances, virtual networks to higher-level components such as DNS records. Each resource has its own attributes to define that resource.

### Data Source
Data source performs a read-only operation. It allows data to be fetched or computed from resources/entities that are not defined or managed by Terraform or the current Terraform configuration.

# Import Existing Infrastructure
Terraform has a really nice feature for importing existing resources, which makes the migration of existing infrastructure into Terraform a lot easier.

# Outputs
Output values can be easily queried and displayed to the Terraform user.

Create a outputs.tf file:

    output "container_id" {
    description = "ID of the Docker container"
    value       = docker_container.nginx.id
    }

    output "image_id" {
    description = "ID of the Docker image"
    value       = docker_image.nginx.id
    }

- Run `terraform plan`
- Run `terraform apply`
- Run `terraform output`

# Best practices
## File structure

Community standard: main.tf variables.tf, data.tf, output.tf

## Apply classic code best practices

- source code management (github)
- functional programing
- DRY (don't repeat yourself)
- KISS (keep it simple, stupid)
- Human and clean
- Idempotency

## Structuring your TF code base

- Allow small state set-up
- Use TF as a platform
- Avoid huge-state --> invalid dependencies
- Avoid org changes (need to restructure the code)


#### When turning off the vms you lose your authentification to gcp

Run `export GOOGLE_APPLICATION_CREDENTIALS=~/.gc/ny-rides.json`
Run `gcloud auth activate-service-account --key-file $GOOGLE_APPLICATION_CREDENTIALS`

or add credentials in the provider in main.tf file