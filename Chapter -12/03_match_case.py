#As lik switch case in other languages

def http_status(status): 
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case 500 | 503:
            return "Internal server error"
        case _:
            return "Something's wrong with the internet"
        
print(http_status(400))
# Output: Bad request
print(http_status(404))
# Output: Not found
print(http_status(418))
# Output: I'm a teapot
print(http_status(500))
# Output: Internal server error
print(http_status(300))

