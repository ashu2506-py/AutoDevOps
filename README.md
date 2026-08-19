# AutoDevOps

> **Infrastructure as Code Generator & Cloud Deployer**

AutoDevOps is a Python-based Infrastructure as Code (IaC) automation tool that converts a simple YAML infrastructure configuration into deployment-ready **Terraform**, **Ansible**, and **Kubernetes** configuration files.

The project provides configuration validation, automated code generation, safe dry-run execution, deployment logging, state management, infrastructure cost estimation, plugin support, and automated testing.

---

## 🚀 Features

- ✅ YAML-based infrastructure configuration
- ✅ YAML parsing using PyYAML
- ✅ Configuration validation using Pydantic
- ✅ Jinja2-based template generation
- ✅ Terraform configuration generation
- ✅ Ansible playbook generation
- ✅ Kubernetes manifest generation
- ✅ Safe Terraform plan simulation
- ✅ Safe deployment simulation
- ✅ Command execution using Python `subprocess`
- ✅ Deployment logging
- ✅ Deployment state management
- ✅ Infrastructure cost estimation
- ✅ Plugin architecture
- ✅ Typer-based CLI
- ✅ Automated testing with Pytest
- ✅ 90%+ test coverage
- ✅ Python package configuration
- ✅ Dry-run mode for safe experimentation

---

# 🏗️ Architecture

```text
                    ┌──────────────────────┐
                    │   YAML Configuration  │
                    │     example.yaml     │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │    YAML Parser       │
                    │      PyYAML          │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │    Configuration     │
                    │     Validation       │
                    │      Pydantic        │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │    Resource Models   │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Jinja2 Generator   │
                    └──────────┬───────────┘
                               │
             ┌─────────────────┼─────────────────┐
             │                 │                 │
             ▼                 ▼                 ▼
      ┌─────────────┐   ┌─────────────┐   ┌─────────────┐
      │  Terraform  │   │   Ansible   │   │ Kubernetes  │
      │    main.tf  │   │ playbook.yml│   │ manifests   │
      └─────────────┘   └─────────────┘   └─────────────┘
             │                 │                 │
             └─────────────────┼─────────────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │      Executor        │
                    │     subprocess       │
                    └──────────┬───────────┘
                               │
                    ┌──────────┴──────────┐
                    │                     │
                    ▼                     ▼
              ┌──────────┐          ┌──────────┐
              │ Dry Run  │          │ Execute  │
              └──────────┘          └──────────┘
                    │                     │
                    └──────────┬──────────┘
                               │
                    ┌──────────┴──────────┐
                    │                     │
                    ▼                     ▼
              Deployment Logs        State Manager
```

---

# 📁 Project Structure

```text
AutoDevOps/
│
├── app/
│   ├── __init__.py
│   ├── cli.py
│   ├── cost.py
│   ├── executor.py
│   ├── generator.py
│   ├── logger.py
│   ├── models.py
│   ├── parser.py
│   ├── state.py
│   └── validator.py
│
├── configs/
│   └── example.yaml
│
├── plugins/
│   ├── __init__.py
│   ├── base.py
│   ├── builtin.py
│   └── registry.py
│
├── templates/
│   ├── main.tf.j2
│   ├── playbook.yml.j2
│   └── kubernetes.yaml.j2
│
├── generated/
│   ├── terraform/
│   │   └── main.tf
│   ├── ansible/
│   │   └── playbook.yml
│   ├── kubernetes/
│   │   └── manifests.yaml
│   ├── deployment.log
│   └── state.json
│
├── tests/
│   ├── __init__.py
│   ├── test_cli.py
│   ├── test_cost.py
│   ├── test_executor.py
│   ├── test_generator.py
│   ├── test_parser.py
│   ├── test_plugins.py
│   ├── test_state.py
│   └── test_validator.py
│
├── .gitignore
├── README.md
├── requirements.txt
└── pyproject.toml
```

---

# 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core application |
| Typer | Command-line interface |
| PyYAML | YAML parsing |
| Pydantic | Configuration validation |
| Jinja2 | Infrastructure template generation |
| Terraform | Infrastructure as Code |
| Ansible | Configuration automation |
| Kubernetes | Container orchestration manifests |
| Pytest | Automated testing |
| pytest-cov | Code coverage |
| Git | Version control |
| GitHub | Source code hosting |

---

# 📋 Requirements

Before running AutoDevOps, make sure you have:

- Python **3.10 or newer**
- pip
- Git

Terraform and Ansible are optional when using the application in **dry-run mode**.

---

# ⚙️ Installation

## 1. Clone the repository

```bash
git clone https://github.com/ashu2506-py/AutoDevOps.git
```

Enter the project:

```bash
cd AutoDevOps
```


---

## 2. Create a virtual environment

### Windows

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

---

## 3. Install the project

```bash
pip install -e .
```

For development and testing:

```bash
pip install pytest pytest-cov
```

Or install the requirements:

```bash
pip install -r requirements.txt
```

---

# 📝 Configuration

AutoDevOps uses a YAML file to describe the desired infrastructure.

Example:

```yaml
project:
  name: auto-web-app
  provider: aws
  region: us-east-1

resources:
  web_server:
    type: compute
    instance_type: t2.micro

  database:
    type: database
    engine: postgres
    version: "15"

  main_network:
    type: network
    cidr: 10.0.0.0/16
```

The configuration contains two main sections:

### Project

```yaml
project:
  name: auto-web-app
  provider: aws
  region: us-east-1
```

This defines the project name, cloud provider, and region.

### Resources

```yaml
resources:
  web_server:
    type: compute
    instance_type: t2.micro
```

Resources describe the infrastructure that should be generated.

Supported resource categories currently include:

- `compute`
- `database`
- `network`

---

# 🖥️ CLI Usage

After installation, AutoDevOps can be run using:

```bash
autodevops
```

You can also run it using:

```bash
python -m app.cli
```

---

## Show help

```bash
autodevops --help
```

---

## Check that AutoDevOps is running

```bash
autodevops hello
```

Output:

```text
AutoDevOps is running!
```

---

# ✅ Validate Configuration

Validate a YAML configuration:

```bash
autodevops validate configs/example.yaml
```

Example output:

```text
Configuration is valid.
Project: auto-web-app
Provider: aws
Region: us-east-1
Resources found: 3
```

Validation checks:

- File existence
- YAML syntax
- Required project information
- Resource availability
- Supported resource types
- Configuration structure

---

# 🏗️ Generate Infrastructure

Generate Terraform, Ansible, and Kubernetes files:

```bash
autodevops generate configs/example.yaml
```

Expected output:

```text
Terraform generated successfully: generated\terraform\main.tf
Ansible generated successfully: generated\ansible\playbook.yml
Kubernetes generated successfully: generated\kubernetes\manifests.yaml
```

Generated files:

```text
generated/
├── terraform/
│   └── main.tf
├── ansible/
│   └── playbook.yml
└── kubernetes/
    └── manifests.yaml
```

---

# 🔍 Terraform Plan

Run a safe Terraform plan simulation:

```bash
autodevops plan configs/example.yaml
```

AutoDevOps uses dry-run mode by default.

Example:

```text
Command: terraform init
DRY-RUN: command was not executed.

Command: terraform plan
DRY-RUN: command was not executed.

Plan completed in DRY-RUN mode.
State saved successfully.
```

No real cloud resources are created during dry-run operation.

---

# 🚀 Deployment

Run a safe deployment simulation:

```bash
autodevops deploy configs/example.yaml
```

Example:

```text
Command: terraform init
DRY-RUN: command was not executed.

Command: terraform apply -auto-approve
DRY-RUN: command was not executed.

Deployment simulation completed safely.
State saved successfully.
```

This allows the complete deployment workflow to be demonstrated without accidentally creating cloud infrastructure.

---

# 💰 Cost Estimation

Estimate the monthly cost of configured infrastructure:

```bash
autodevops estimate configs/example.yaml
```

Example:

```text
Estimated Monthly Cost
-----------------------
web_server: $8.47/month
database: $12.41/month
-----------------------
Estimated Total: $20.88/month

Note: This is a demonstration estimate, not live cloud pricing.
```

> The estimator uses predefined demonstration pricing and is not a live cloud-provider pricing API.

---

# 📜 Deployment Logs

View deployment logs:

```bash
autodevops logs
```

Example:

```text
[2026-08-19T12:32:52+00:00] COMMAND: terraform init
[2026-08-19T12:32:52+00:00] DRY-RUN: command was not executed.
[2026-08-19T12:32:52+00:00] COMMAND: terraform plan
[2026-08-19T12:32:52+00:00] DRY-RUN: command was not executed.
```

Logs are stored in:

```text
generated/deployment.log
```

---

# 📊 Deployment State

View the latest deployment state:

```bash
autodevops status
```

Example:

```text
AutoDevOps Status
-----------------
project: auto-web-app
operation: plan
status: dry-run
generated_file: generated\terraform\main.tf
return_code: 0
updated_at: 2026-08-19T...
```

State is stored in:

```text
generated/state.json
```

---

# 🔌 Plugin Architecture

AutoDevOps includes a plugin registry for extending infrastructure generation capabilities.

List available plugins:

```bash
autodevops plugins
```

Example:

```text
Available Plugins
-----------------
terraform: Terraform infrastructure generator
ansible: Ansible playbook generator
kubernetes: Kubernetes manifest generator
```

Current built-in plugins:

```text
TerraformPlugin
AnsiblePlugin
KubernetesPlugin
```

The plugin system is designed to allow additional infrastructure generators to be registered without redesigning the entire application.

---

# 🧪 Testing

Run all tests:

```bash
pytest -v
```

The test suite covers:

- YAML parsing
- Invalid YAML handling
- Configuration validation
- Resource validation
- Terraform generation
- Ansible generation
- Kubernetes generation
- Executor behavior
- Dry-run execution
- Command failures
- Command timeout handling
- Deployment logging
- State management
- Cost estimation
- CLI commands
- Plugin registry

---

# 📈 Test Coverage

Run:

```bash
pytest --cov=app --cov-report=term-missing
```

The project currently achieves approximately:

```text
96% code coverage
```

with the complete automated test suite passing.

---

# 📦 Build the Python Package

AutoDevOps uses `pyproject.toml` for Python packaging.

Install the build package:

```bash
pip install build
```

Build the distribution:

```bash
python -m build
```

The package files will be created in:

```text
dist/
```

Example:

```text
dist/
├── autodevops-1.0.0-py3-none-any.whl
└── autodevops-1.0.0.tar.gz
```

---

# 🔐 Safe Execution

AutoDevOps is designed with safety in mind.

By default, infrastructure commands are executed in **dry-run mode**.

For example:

```text
Command: terraform apply -auto-approve
DRY-RUN: command was not executed.
```

This prevents accidental infrastructure creation while developing and testing the project.

Actual command execution requires explicitly disabling dry-run behavior in the application code.

---

# 📂 Generated Files

After running:

```bash
autodevops generate configs/example.yaml
```

the generated directory contains:

```text
generated/
│
├── terraform/
│   └── main.tf
│
├── ansible/
│   └── playbook.yml
│
├── kubernetes/
│   └── manifests.yaml
│
├── deployment.log
│
└── state.json
```

### Terraform

```text
generated/terraform/main.tf
```

Contains AWS Terraform resources generated from the YAML configuration.

### Ansible

```text
generated/ansible/playbook.yml
```

Contains the generated Ansible playbook.

### Kubernetes

```text
generated/kubernetes/manifests.yaml
```

Contains Kubernetes Deployment and Service manifests.

### Deployment Log

```text
generated/deployment.log
```

Stores execution information.

### State

```text
generated/state.json
```

Stores the latest deployment operation and status.

---

# 🧩 Error Handling

AutoDevOps handles common configuration and execution errors including:

- Missing configuration files
- Invalid YAML syntax
- Empty YAML files
- Unsupported file extensions
- Invalid configuration structures
- Missing required project information
- Unsupported resource types
- Missing external commands
- Command failures
- Command timeouts
- Invalid state files

Errors are reported through the CLI with appropriate exit codes.

---

# 🔄 Typical Workflow

A typical AutoDevOps workflow is:

```text
1. Create YAML configuration
          ↓
2. Validate configuration
          ↓
3. Generate infrastructure
          ↓
4. Review generated Terraform/Ansible/Kubernetes
          ↓
5. Run safe plan
          ↓
6. Review deployment logs
          ↓
7. Check deployment state
          ↓
8. Estimate infrastructure cost
          ↓
9. Deploy when ready
```

Example:

```bash
autodevops validate configs/example.yaml

autodevops generate configs/example.yaml

autodevops estimate configs/example.yaml

autodevops plan configs/example.yaml

autodevops status

autodevops logs
```

---

# 🎯 Project Objectives

The main objectives of AutoDevOps are:

1. Convert high-level infrastructure descriptions into Infrastructure as Code.
2. Reduce manual infrastructure configuration.
3. Provide reusable Jinja2-based templates.
4. Generate Terraform, Ansible, and Kubernetes configuration.
5. Provide safe deployment simulations.
6. Track deployment logs and state.
7. Provide infrastructure cost estimation.
8. Provide an extensible plugin architecture.
9. Maintain strong automated test coverage.
10. Provide a reusable Python CLI application.

---

# 🧱 Design Principles

AutoDevOps follows several design principles:

### Configuration Driven

Infrastructure is described through YAML rather than hard-coded Python logic.

### Template Driven

Infrastructure output is generated through Jinja2 templates.

### Modular

Parsing, validation, generation, execution, logging, state management, and cost estimation are separated into different modules.

### Safe by Default

Dry-run mode prevents accidental infrastructure deployment.

### Extensible

The plugin registry allows additional generators to be added.

### Testable

Core functionality is covered through automated Pytest tests.

---

# 🔮 Future Improvements

Possible future enhancements include:

- Live AWS pricing integration
- AWS/GCP/Azure provider support
- More Terraform resource types
- More Kubernetes resource types
- Remote Terraform state
- Terraform state inspection
- Real cloud deployment workflows
- CI/CD integration
- Docker support
- GitHub Actions integration
- Plugin discovery through Python entry points
- Interactive CLI configuration
- Web dashboard
- Deployment rollback
- Infrastructure drift detection

---

# 👨‍💻 Development

Clone the repository:

```bash
git clone https://github.com/ashu2506-py/AutoDevOps.git
cd AutoDevOps
```

Create the environment:

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

Install in editable mode:

```bash
pip install -e .
```

Run tests:

```bash
pytest -v
```

Run coverage:

```bash
pytest --cov=app --cov-report=term-missing
```

---

# 📌 Example Quick Start

After installation, the complete workflow can be demonstrated using:

```bash
autodevops validate configs/example.yaml
```

```bash
autodevops generate configs/example.yaml
```

```bash
autodevops estimate configs/example.yaml
```

```bash
autodevops plan configs/example.yaml
```

```bash
autodevops deploy configs/example.yaml
```

```bash
autodevops status
```

```bash
autodevops logs
```

```bash
autodevops plugins
```

---

# 📄 License

This project was developed as part of an internship project and is intended for educational and demonstration purposes.

---

# 🙌 Acknowledgements

This project uses the following open-source technologies:

- Python
- PyYAML
- Pydantic
- Jinja2
- Typer
- Terraform
- Ansible
- Kubernetes
- Pytest

---

# ⭐ AutoDevOps

**Infrastructure configuration → Validation → IaC Generation → Safe Deployment**

Built with Python and designed for modular, automated Infrastructure as Code workflows.