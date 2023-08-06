import requests
import websocket

def check_web_service(url):
    """ Function to check if a web service is up

    Args:
        url (str): url to check if web service is up
    """
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)
        
def check_api_service(url):
    """ Function to check if a API service is up
    
    Args:
        url (str): url to check if API service is up
    """
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)


def check_websocket_service(url):
    """ Function to check if a websocket service is up

    Args:
        url (str): Url to check if WS service in up
    """
    try:
        ws = websocket.WebSocket()
        if ws.connect:
            return True
        else:
            return False
    except websocket.WebSocketException as e:
        print("An error occurred:", e)