from NcosSdk.csclient import CSClient
class Auth:

    @classmethod
    def Login(self):

        client = CSClient._get_auth(self,'192.168.50.1', 'admin', 'Password123')

        return  client