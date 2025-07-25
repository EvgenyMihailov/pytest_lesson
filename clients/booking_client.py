import requests


class BookingClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def create_booking(self,data, headers):
        return requests.post(url=f"{self.base_url}/booking", json=data, headers=headers)

    def delete_booking(self, booking_id, headers):
        return requests.delete(url=f"{self.base_url}/booking/{booking_id}", headers=headers)

    def update_booking(self,data, headers, booking_id):

        return requests.put(url=f"{self.base_url}/booking/{booking_id}", json=data, headers=headers)


    def get_token(self,data, headers):
        return requests.post(url=f"{self.base_url}/auth", json=data, headers=headers)