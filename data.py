import os


# URL for the Urban Routes application
URBAN_ROUTES_URL = os.getenv(
    'URBAN_ROUTES_URL',
    'https://cnt-8606da0a-fab0-4edf-a6c5-1eb2ada40539.containerhub.tripleten-services.com/'
)

# Test data constants
ADDRESS_FROM = 'East 2nd Street, 601'
ADDRESS_TO = '1300 1st St'
PHONE_NUMBER = '+1 123 123 12 12'
CARD_NUMBER = '1234 5678 9100'
CARD_CODE = '1111'
MESSAGE_FOR_DRIVER = 'Stop at the juice bar, please'
