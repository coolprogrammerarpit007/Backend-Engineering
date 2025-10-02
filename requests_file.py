# Python Requests Library

# import requests

# response = requests.get("https://api.github.com")
# # print(response)
# print(response.status_code)


# Inspect the response

# A Response is the object that contains the results of your request. 

# Work with the status code
# The first piece of information that you can gather from Response is the status code. A status code informs you of the status of the request.
# For example, a 200 OK status means that your request was successful, while a 404 NOT FOUND status means that the resource you were looking for wasn’t found.


# import requests
# from requests.exceptions import HTTPError


# URLS = ["https://api.github.com", "https://api.github.com/invalid"]

# for url in URLS:
#     try:
#         response = requests.get(url)
#         response.raise_for_status()

#     except HTTPError as http_err:
#         print(f"HTTP Error Occurs: {http_err}")

#     except Exception as err:
#         print(f"Other error occurs: {err}")

#     else:
#         print("Success")



# Access The Response Content
# The response of a GET request often has some valuable information, known as a payload, in the message body. Using the attributes and methods of Response, you can view the payload in a variety of formats.

# import requests
# response = requests.get("https://api.github.com")
# response_conetnt = response.content
# print(response_conetnt)

# While .content gives you access to the raw bytes of the response payload, you’ll often want to convert them into a string using a character encoding such as UTF-8. response will do that for you when you access .text:

# response.encoding = "utf-8"
# text_content = response.text
# print(text_content)



# get the json content
# json_content = response.json()
# print(json_content)


# Add query String Parameters

# import requests
# import sys


# response = requests.get("https://api.github.com/search/repositories",params={"q": "language:python", "sort": "stars", "order": "desc"})


# json_response = response.json()
# popular_repositories = json_response["items"]
# for repo in popular_repositories[:3]:
#     print(f"Name: {repo['name']}")
#     print(f"Description: {repo['description']}")
#     print(f"Stars: {repo['stargazers_count']}\n")



# Other Useful HTTP Methods

# Aside from GET, other popular HTTP methods include POST, PUT, DELETE, HEAD, PATCH, and OPTIONS. For each of these HTTP methods, Requests provides a function with a similar signature to get().


# import requests

# requests.get("https://httpbin.org/get")
# requests.post("https://httpbin.org/post", data={"key": "value"})
# requests.put("https://httpbin.org/put", data={"key": "value"})
# requests.delete("https://httpbin.org/delete")
# requests.head("https://httpbin.org/get")
# requests.patch("https://httpbin.org/patch", data={"key": "value"})
# requests.options("https://httpbin.org/get")


# Send Request Data

# According to the HTTP specification, POST, PUT, and the less common PATCH requests pass their data through the message body rather than through parameters in the query string. With Requests, you pass this payload to the corresponding function’s data parameter.


# The requests.Session object in Python is used to persist certain parameters across multiple HTTP requests, which brings both convenience and performance benefits when interacting with web APIs or servers repeatedly.

# Why Use requests.Session?
# Persistence: Cookies (like authentication tokens or tracking IDs) are preserved across all requests made using the session. This is especially useful for operations like logging in once and then making further authenticated requests.

# Connection Pooling: The session object reuses underlying TCP connections for requests to the same host, which can significantly improve speed by avoiding the overhead of repeatedly establishing new connections.

# Shared State: You can easily set headers, authentication, and other configuration defaults once at the session level. These will apply to all subsequent requests made through the session unless overridden at the request level.