

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


#### When turning off the vms you lose your authentification to gcp

Run `export GOOGLE_APPLICATION_CREDENTIALS=~/.gc/ny-rides.json`
Run `gcloud auth activate-service-account --key-file $GOOGLE_APPLICATION_CREDENTIALS`

or add credentials in the provider in main.tf file