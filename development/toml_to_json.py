import requests

url = "https://a4a30cd42304455b892151382cbb5bdb.us-east-1.aws.found.io:9243/api/detection_engine/rules"
api_key= "YTlDT0xKZ0JzYzJ6OGxTUHdxMmc6TWRXNnZMLTVkZHIzdk51WXgzelRRZw=="
headers = {
    'Content-Type': 'application/json;charset=UTF-8',
    'kbn-xsrf': 'true',
    'Authorization': 'ApiKey ' + api_key
}

elastic_data = requests.post(url, headers=headers, data=data).json()
print(elastic_data)