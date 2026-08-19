from app.cost import estimate_monthly_cost
from app.models import InfrastructureConfig


def test_cost_estimation():

    config = InfrastructureConfig(
        project={
            "name": "demo"
        },
        resources={
            "web": {
                "type": "compute",
                "instance_type": "t2.micro"
            },
            "database": {
                "type": "database",
                "instance_class": "db.t3.micro"
            }
        }
    )

    total, details = (
        estimate_monthly_cost(config)
    )

    assert total > 0
    assert len(details) == 2


def test_unknown_resource_price():

    config = InfrastructureConfig(
        project={
            "name": "demo"
        },
        resources={
            "web": {
                "type": "compute",
                "instance_type": "unknown"
            }
        }
    )

    total, details = (
        estimate_monthly_cost(config)
    )

    assert total == 0