# Docker Compose Setup for Odoo 15

This Docker Compose setup is designed to create a development environment for Odoo 15 with a PostgreSQL database.

## First Step: Create Docker Network

Before running the Docker Compose file, create the external network `my-network`:

```bash
docker network create my-network
```

## Usage

Starting the docker services in detached mode run:

```bash
docker compose up -d
```

Access the Odoo @ <http://localhost:8069> 🚀.

To stop the docker services, run:

```bash
docker compose down
```

## Odoo Module Scaffolding Script

A Python script to scaffold a basic folder structure for an Odoo module.

### Create a new Odoo module

Run the script with the desired module name as an argument:

```bash
python3 odoo_scaffold.py your_module_name
```

Replace your_module_name with your Odoo module's name.

Module Structure
The script creates directories for controllers, models, security, views, data, and demo, along with necessary Python files.

Customizing the Module
After the module structure is created, add your custom code, views, models, and data as needed.
