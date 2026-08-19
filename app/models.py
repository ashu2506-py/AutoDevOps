from typing import Dict, Optional

from pydantic import BaseModel, Field


class Project(BaseModel):
    name: str
    provider: str = "aws"
    region: str = "us-east-1"


class WebServer(BaseModel):
    type: str = "compute"
    instance_type: str = "t2.micro"
    ami: Optional[str] = None


class Database(BaseModel):
    type: str = "database"
    engine: str = "postgres"
    version: str = "15"
    instance_class: str = "db.t3.micro"


class Network(BaseModel):
    type: str = "network"
    cidr: str = "10.0.0.0/16"


class InfrastructureConfig(BaseModel):
    project: Project
    resources: Dict[str, Dict] = Field(default_factory=dict)

    def typed_resources(self):
        result = {
            "compute": [],
            "database": [],
            "network": []
        }

        for name, resource in self.resources.items():

            resource_type = resource.get("type")

            if resource_type == "compute":
                result["compute"].append(
                    (name, WebServer(**resource))
                )

            elif resource_type == "database":
                result["database"].append(
                    (name, Database(**resource))
                )

            elif resource_type == "network":
                result["network"].append(
                    (name, Network(**resource))
                )

        return result