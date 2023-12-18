provider "azurerm" {
  features {}
  subscription_id = var.subscription_id
  client_id       = var.client_id
  client_secret   = var.client_secret
  tenant_id       = var.tenant_id
}

terraform {
  backend "azurerm" {
    resource_group_name   = "var.resource_group_name"
    storage_account_name  = "var.storage_account_name"
    container_name        = "var.container_name"
    key                   = "terraform.tfstate"
  }
}

# Azure Storage Account and Blob Container
resource "azurerm_storage_account" "example_storage" {
  name                     = "examplestorageaccount"
  resource_group_name      = azurerm_resource_group.example_rg.name
  location                 = "East US"
  account_tier             = "Standard"
  account_replication_type = "LRS"
}

resource "azurerm_storage_container" "gameplay_container" {
  name                  = "gameplaycontainer"
  storage_account_name  = azurerm_storage_account.example_storage.name
  container_access_type = "private"
}

# Azure Functions
resource "azurerm_function_app" "example_function" {
  name                      = "examplefunctionapp"
  location                  = azurerm_resource_group.example_rg.location
  resource_group_name       = azurerm_resource_group.example_rg.name
  app_service_plan_id       = azurerm_app_service_plan.example_plan.id
  storage_account_name      = azurerm_storage_account.example_storage.name
  storage_account_access_key= azurerm_storage_account.example_storage.primary_access_key
  version                   = "~3"
  https_only                = true

  app_settings = {
    "FUNCTIONS_WORKER_RUNTIME" = "node"
  }
}

# Azure Data Factory
resource "azurerm_data_factory" "example_data_factory" {
  name                = "exampledatafactory"
  location            = azurerm_resource_group.example_rg.location
  resource_group_name = azurerm_resource_group.example_rg.name

  identity {
    type = "SystemAssigned"
  }
}

# Azure SQL Database
resource "azurerm_sql_server" "example_sql_server" {
  name                         = "examplesqlserver"
  resource_group_name          = azurerm_resource_group.example_rg.name
  location                     = azurerm_resource_group.example_rg.location
  version                      = "12.0"
  administrator_login          = "var.adminuser"
  administrator_login_password = "var.adminpassword"

  tags = {
    environment = "production"
  }
}

resource "azurerm_sql_database" "example_sql_db" {
  name                = "examplesqldatabase"
  resource_group_name = azurerm_resource_group.example_rg.name
  location            = azurerm_resource_group.example_rg.location
  server_name         = azurerm_sql_server.example_sql_server.name
  edition             = "Standard"
  collation           = "SQL_Latin1_General_CP1_CI_AS"
  max_size_gb         = 20

  create_mode         = "Default"
}

resource "azurerm_key_vault" "example_key_vault" {
  name                        = "examplekeyvault"
  location                    = azurerm_resource_group.example_rg.location
  resource_group_name         = azurerm_resource_group.example_rg.name
  enabled_for_disk_encryption = true
  tenant_id                   = var.tenant_id
  soft_delete_retention_days  = 7
  purge_protection_enabled    = false

  sku_name = "standard"

  access_policy {
    tenant_id = var.tenant_id
    object_id = var.object_id

    key_permissions = [
      "create",
      "get"
    ]

    secret_permissions = [
      "set",
      "get"
    ]
  }
}

