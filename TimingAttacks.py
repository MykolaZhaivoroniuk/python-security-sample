# Issue
def checkToken(userSupplied):
    account = account.retrieveToken(userSupplied)

    if account:
        if account.service.token == user.service.token:
            return True
    
    return False


# Remediation
import hmac

def checkToken(userSupplied):
    account = account.retrieveToken(userSupplied)

    if account:
        return hmac.compare_digest(account.service.token, user.service.token)
    
    return False