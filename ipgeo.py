import requests

def get_ip_geolocation(ip):
    url = f"http://ip-api.com/json/{ip}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if data["status"] == "fail":
            print("Invalid IP address or request failed.")
        else:
            print(f"IP Address: {data['query']}")
            print(f"Country: {data['country']}")
            print(f"Region: {data['regionName']}")
            print(f"City: {data['city']}")
            print(f"ZIP Code: {data['zip']}")
            print(f"Latitude: {data['lat']}, Longitude: {data['lon']}")
            print(f"ISP: {data['isp']}")
            print(f"Organization: {data['org']}")
    else:
        print("Failed to retrieve data.")

if __name__ == "__main__":
    ip = input("Enter an IP address: ")
    get_ip_geolocation(ip)
