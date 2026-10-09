import requests 
USERNAME = "betibachao"
TOKEN = "d3h234n55j452n24h4254n"
pixela_endpoint = "https://pixe.la/v1/users"

user_prams = {
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}
# responce = requests.post(url=pixela_endpoint,json=user_prams)
# print(responce.text)

# Graph 
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id":"graph1",
    "name":"Coding",
    "unit":"commit",
    "type":"float",
    "color":"ajisai"
}


'''Header API headers act as control signals that guide how the server interprets 
 the request and how the client should handle the response'''


headers = {
    "X-USER-TOKEN":TOKEN
}
responce = requests.post(url=graph_endpoint,json=graph_config,headers=headers)
print(responce.text)