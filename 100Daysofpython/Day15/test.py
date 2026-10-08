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
    },
    {
    "id": "R004",
    "name": "Projector",
    "category": "Electronics",
    "total": 4,
    "available": 4
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

def add_resource():
    resource_id = input("Enter resource ID: ").strip()

    if find_resource(resource_id):
        print("Error: Resource ID already exists.")
        return

    name = input("Enter resource name: ").strip()
    category = input("Enter category: ").strip()
    total = int(input("Enter total units: "))

    resource = {
        "id": resource_id,
        "name": name,
        "category": category,
        "total": total,
        "available": total
    }

    resources.append( resource)

print("Resource added successfully.")