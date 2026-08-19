COMPUTE_PRICES = {
    "t2.micro": 0.0116,
    "t3.micro": 0.0104,
    "t3.small": 0.0208,
    "t3.medium": 0.0416,
}

DATABASE_PRICES = {
    "db.t3.micro": 0.017,
    "db.t3.small": 0.034,
    "db.t3.medium": 0.068,
}


def estimate_monthly_cost(config):

    hours_per_month = 730

    total = 0.0
    details = []

    for name, resource in config.resources.items():

        resource_type = resource.get("type")

        # -------------------------
        # COMPUTE
        # -------------------------

        if resource_type == "compute":

            instance_type = resource.get(
                "instance_type"
            )

            hourly_price = COMPUTE_PRICES.get(
                instance_type,
                0
            )

            monthly_cost = (
                hourly_price *
                hours_per_month
            )

            total += monthly_cost

            details.append(
                (name, monthly_cost)
            )

        # -------------------------
        # DATABASE
        # -------------------------

        elif resource_type == "database":

            instance_class = resource.get(
                "instance_class",
                "db.t3.micro"
            )

            hourly_price = DATABASE_PRICES.get(
                instance_class,
                0
            )

            monthly_cost = (
                hourly_price *
                hours_per_month
            )

            total += monthly_cost

            details.append(
                (name, monthly_cost)
            )

    return total, details