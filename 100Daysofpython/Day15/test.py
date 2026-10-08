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


def find_resource(resource_id):
    for resource in resources:
        if resource["id"] == resource_id:
            return resource
    return None

print(find_resource("R001"))
print(find_resource("R999"))


def find_fellow(fellow_id):
    return fellows.get(fellow_id)


print(find_fellow("F001"))
print(find_fellow("F999"))

