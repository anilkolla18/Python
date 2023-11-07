import requests

# Define the base URL for your REST API
base_url = "https://api.example.com/"

# Function to add a new resource
def add_resource():
    # Construct the URL for the 'add' operation
    url = base_url + "add"
    # Make a POST request to add a resource
    response = requests.post(url)
    if response.status_code == 201:
        print("Resource added successfully.")
    else:
        print("Failed to add the resource.")

# Function to update an existing resource
def update_resource():
    # Construct the URL for the 'update' operation
    url = base_url + "update"
    # Make a PUT request to update a resource
    response = requests.put(url)
    if response.status_code == 200:
        print("Resource updated successfully.")
    else:
        print("Failed to update the resource.")

# Function to delete a resource
def delete_resource():
    # Construct the URL for the 'delete' operation
    url = base_url + "delete"
    # Make a DELETE request to delete a resource
    response = requests.delete(url)
    if response.status_code == 204:
        print("Resource deleted successfully.")
    else:
        print("Failed to delete the resource.")

# Main function
def main():
    operation = input("Enter an operation (add, update, delete): ")
    
    if operation == "add":
        add_resource()
    elif operation == "update":
        update_resource()
    elif operation == "delete":
        delete_resource()
    else:
        print("Invalid operation. Please enter 'add', 'update', or 'delete'.")

if __name__ == "__main__":
    main()
