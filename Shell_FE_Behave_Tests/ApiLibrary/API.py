import requests

class API:

    BASE_PATH = "http://ec2-54-254-162-245.ap-southeast-1.compute.amazonaws.com:9000/items/"
    TEAM_NAME = "Shell India - 1"
    @staticmethod
    def post(headline: str, news_link: str, pub_date_time: str):
        data = {
        "name": f"{headline}",
        "description": f"News Link: {news_link}",
        "price": int(pub_date_time.split(" ")[0].replace("-", "")),
        "item_type": API.TEAM_NAME,
        }
        headers = {     
            'Content-Type': 'application/json'  
        }
            
        headers = {     
            'Content-Type': 'application/json'  
        } 
            
        response = requests.post(API.BASE_PATH, json= data, headers=headers)
        if response.status_code == 200:
            return response.json().get("id")
        return None

    def get(id: str):
        response = requests.get(API.BASE_PATH + id)
    pass


def main():
    API.post()
    API.get("1")
    pass