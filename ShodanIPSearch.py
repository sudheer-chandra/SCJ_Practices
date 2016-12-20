import shodan

# SHODAN API KEY FROM SHODAN ACCOUNT
API_KEY = "ByaWJ1VL3o9oEOuLgTqUWnZz9bBoqdBK"

# CREATING AN OBJECT OF THE CLASS shodan
api = shodan.Shodan(API_KEY)

# QUERY SEARCH
query = 'swiggy'
result = api.search(query)

# LOOP THROUGH THE MATCHES OF THE JSON AND PRINT IP & HOSTNAMES
for service in result['matches']:
    print('IP ADDRESS : %s' % service['ip_str'])
    print('Hostname : %s' % service['hostnames'])
