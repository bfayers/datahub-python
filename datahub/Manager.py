class Manager():
    def __init__(self, client_id=None, client_secret=None):
        if client_id is None:
            raise Exception("No Client ID Provided")
        if client_secret is None:
            raise Exception("No Client Secret Provided")
        self.client_id = client_id
        self.client_secret = client_secret