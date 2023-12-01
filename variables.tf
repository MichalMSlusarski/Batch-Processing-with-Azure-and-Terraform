variable "subscription_id" {
  description = "The subscription ID for the Azure provider"
  type        = string
}

variable "client_id" {
  description = "The client ID for the Azure provider"
  type        = string
}

variable "client_secret" {
  description = "The client secret for the Azure provider"
  type        = string
}

variable "tenant_id" {
  description = "The tenant ID for the Azure provider"
  type        = string
}

variable "resource_group_name" {
  description = "The name of the resource group for the backend"
  type        = string
}

variable "storage_account_name" {
  description = "The name of the storage account for the backend"
  type        = string
}

variable "container_name" {
  description = "The name of the container for the backend"
  type        = string
}

variable "object_id" {
  description = "The object ID for the key vault access policy"
  type        = string
}