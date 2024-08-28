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

    @staticmethod
    def get(id: int):
        response = requests.get(API.BASE_PATH + str(id))
        return response


    @staticmethod
    def validate(headline: str, news_link: str, pub_date_time: str, id: int):
        response = API.get(id)
        print(headline)
        print(news_link)
        print(pub_date_time)
        print(response)
        if response.status_code == 200:
            response = response.json()
            print(response)
            if response.get("name") == headline and response.get("description") == f"News Link: {news_link}" and int(response.get("price")) == int(pub_date_time.split(" ")[0].replace("-", "")) and response.get("item_type") == API.TEAM_NAME:
                return True
        return False

def main():
    id = API.post("Test Headline", "https://www.google.com", "2021-09-30 00:00:00")
    print(id)
    print(API.validate("Test Headline", "https://www.google.com", "2021-09-30 00:00:00", id))


if __name__ == "__main__":
    main()