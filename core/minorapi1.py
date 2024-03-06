import requests

def get_lulc_stats(api_key, year, distcode=None):
    url = "https://bhuvan-app1.nrsc.gov.in/api/lulc/curljson.php"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    params = {
        "year": year,
        "distcode": distcode,
        "token": api_key
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Raise an exception for bad status codes
        print("Response status code:", response.status_code)
        print("Response headers:", response.headers)
        print("Response text:", response.text)  # Debugging print to see the response text
        
        # Check if the response is JSON before attempting to parse it
        content_type = response.headers.get('Content-Type', '')
        if 'application/json' in content_type:
            data = response.json()
            return data
        else:
            print(f"Response content type is {content_type}, not JSON.")
            # Optionally, print the response text if it's not empty
            if response.text:
                print("Response content:", response.text)
            return None
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
        return None
    except requests.exceptions.RequestException as err:
        print(f"Request error occurred: {err}")
        return None



def main():
    api_key = "d35010b652519c0edb8d09278bcfbe69902e0ebd"  # Replace this with your actual API key
    year = "1112"  # Change this to "1112" for statistics of 2011-2012 year
    distcode = "2701"  # Example district code
    # statcode = "GA"  # Example state code, uncomment and specify if needed
    
    data = get_lulc_stats(api_key, year, distcode)
    
    if data:
        print("LULC Stats:")
        print(data)
    else:
        print("Failed to fetch LULC stats.")

if __name__ == "__main__":
    main()
