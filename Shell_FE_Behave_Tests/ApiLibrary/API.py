import requests

class API:

    BASE_PATH = "http://ec2-54-254-162-245.ap-southeast-1.compute.amazonaws.com:9000/items/"
    TEAM_NAME = "Shell India - 1"

    @staticmethod
    def post(name: str, description: str, price: str):
        data = {
        "name": f"{name}",
        "description": f"{description}",
        "price": int(price) if price.find("-") == -1 else int(price.split(" ")[0].replace("-", "")),
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

    @staticmethod
    def get(id: int):
        response = requests.get(API.BASE_PATH + str(id))
        return response


    @staticmethod
    def validate(name: str, description: str, price: str, id: int):
        price = int(price) if price.find("-") == -1 else int(price.split(" ")[0].replace("-", ""))
        response = API.get(id)
        # print(headline)
        # print(news_link)
        # print(pub_date_time)
        # print(response)
        if response.status_code == 200:
            response = response.json()
            print(response)
            if response.get("name") == name and response.get("description") == f"{description}" and int(response.get("price")) == price and response.get("item_type") == API.TEAM_NAME:
                return True
        return False

def main():
    id = API.post("Test Headline", "https://www.google.com", "2021-09-30 00:00:00")
    print(id)
    print(API.validate("Test Headline", "https://www.google.com", "2021-09-30 00:00:00", id))


if __name__ == "__main__":
    main()