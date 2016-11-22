import requests

userKey = "8d07dd35f35cff89551615df83668874";
def main():

	headers = {"user-key" : userKey}

	# Make a get request with the parameters.
	requests.get('https://developers.zomato.com/api/v2.1/search?entity_id=280&entity_type=city', headers=headers)
	
	# Print the content of the response (the data the server returned)
	print response.status_code;
	print response.content;

if __name__ == "__main__":
	main();