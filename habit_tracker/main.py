import requests 

pixela_endpoint = "https://pixe.la/v1/users"

user_prams = {
    "token":"d3h234n55j452n24h4254n",
    "username":"anurag",
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}
responce = requests.post(url=pixela_endpoint,json=user_prams)



print(responce.text)