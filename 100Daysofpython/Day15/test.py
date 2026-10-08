resources = [
    {
        "id": "R001",
        "name": "Laptop",
        "category": "Electronics",
        "total": 10,
        "available": 10
    },
    {
        "id": "R002",
        "name": "Keyboard",
        "category": "Accessories",
        "total": 5,
        "available": 5
    },
    {
        "id": "R003",
        "name": "Headset",
        "category": "Accessories",
        "total": 3,
        "available": 3
    }
]

fellows = {
    "F001": "Samuel",
    "F002": "Emmanuel",
    "F003": "Edor"
}

borrow_records = []


def list_resources():
    for resource in resources:
        print(
            f"{resource['id']} | "
            f"{resource['name']} | "
            f"{resource['category']} | "
            f"Total: {resource['total']} | "
            f"Available: {resource['available']} "

        )

list_resources()