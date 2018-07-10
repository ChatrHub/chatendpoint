"""Demo for accessing backend inventory management for a car dealership."""
from __init__ import ChatEndpoints


"""
    Step 1: Create data_processor functions to interact with custom backend systems.
    All responses in this demo are hard coded.  For production systems, interact with
    persistant data stores then format the response variables.  Variables
    (return / recieve) must be setup in the dialog before taking a custom action.

    Step 2. Call add_post_endpoint for each endpoint you want to create.

    Step 3. Start the server in the background.
"""


def car_inventory(dialog_variables):
    """Get car inventory."""
    if 'car_brand' not in dialog_variables:
        return {
            'inventory_count': 0,
            'inventory_response': (
                'Variable car_brand must be defined before processing this action, '
                'please update dialog in ChatrHub.'
            )
        }

    cb = dialog_variables['car_brand']
    if cb == 'Ford':
        return {
            'inventory_count': 4,
            'inventory_response': 'We have 2 F-150s and 2 Exporers you can test drive from on our lot.'
        }
    else:
        return {
            'inventory_count': 0,
            'inventory_response': 'We do not have {cb} in stock.'
        }


def car_pricing(dialog_variables):
    """Get car inventory."""
    if 'car_model' not in dialog_variables:
        return {'error_message': (
            'Variable car_model must be defined before processing this action, '
            'please update dialog in ChatrHub.')
        }

    cm = dialog_variables['car_model']
    if cm == 'F-150':
        return {
            'price': 51000,
            'pricing_response': 'We have 2 F-150s one for $51,000 and another for $80,000.  Would you like to schedule a test drive?'
        }
    elif cm == 'Explorer':
        return {
            'price': 22000,
            'pricing_response': 'We have 2 F-150s one for $22,000 and another for $43,000.  Would you like to schedule a test drive?'
        }
    else:
        return {
            'price': 0,
            'pricing_response': 'We dont have pricing information on anything other than F-150s and Explorers.'
        }


if __name__ == '__main__':
    ce = ChatEndpoints()
    ce.add_post_endpoint(path='/get_car_inventory', data_processor=car_inventory)
    ce.add_post_endpoint(path='/get_car_pricing', data_processor=car_pricing)
    ce.start()
