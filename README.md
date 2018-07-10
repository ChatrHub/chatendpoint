# chatendpoint | ChatrHub

Create custom actions for ChatrHub's automated chat agents https://chatrhub.com.  (Create a free account if you dont have one already here: https://chatrhub.com/signup/index.html).  Use this module when you want your chat dialog to interface with internal systems such as inventory or user management data stores.

You can pass variables collected in the dialog to the endpoint for processing and you can also pass variables back to the dialog to display to the user.

## Prerequisites

- Linux Server
- Python3.6

## Getting Started

### 1. Install

pip install chatendpoint

### 2. Create Endpoints

```python
from chatendpoint.chatendpoint import ChatEndpoints
def create_user(dialog_variables):
    # All dialog variables will be available in the dialog_variables dictionary
    # dialog_variables example:
    #   {
    #       'literal': 'F-150',
    #       'value': 'F-150',
    #   }
    # Using the dialog variables, access your data store, manipulate data, and
    # return a dictionary which will add/update variables back to dialog.
    return {'user_created': 'success'}

if __name__ == "__main__":
    ce = ChatEndpoints()
    # Create as many endpoints as you need.
    ce.add_post_endpoint(path='/create_user', data_processor=create_user)
    ce.start(port=8888)
```

- See demos/car_dealership_demo.py for a more in-depth example

- These endpoints will allow you to receive dialog variables, process the data as needed, then return any variables that should be be added or updated to the dialog.

- Default port is 8888

### 3. Dialog Setup

In the ChatrHub portal make sure you collect any variables via questionnaires before sending to your action endpoint.  Setup a free account at https://chatrhub.com/signup/index.html

### 4. Open Firewall

Open port 8888 (Or whatever port you selected) to the ChatrHub IP address obtained by sending an email to admin@chatrhub.com.

### 5. Run server

Run the server in the background by running the script created in step 2.

## License

This project is licensed under the MIT License.
