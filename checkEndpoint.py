import requests

class CheckEndpoint():

    _requestUrl = False
    _pro = 'enabled'

    def checkEndPoint(self,url):
        try:
            get = requests.get(url)
            if get.status_code == 200 or get.status_code == 302:
                print(f"{url}: is reachable")
                return True
            else:
                print(f"{url}: is Not reachable, status_code: {get.status_code}")
                return False

        #Exception
        except requests.exceptions.RequestException as e:
            # print URL with Errs
            # raise SystemExit(f"{url}: is Not reachable \nErr: {e}")
            print(f"{url}: is Not reachable, status_code INSIDE OF EXCEPTION: {e}")
            return False

    def setRequestUrlAzul(self):
        if self._pro == 'enabled': # prod

            self._requestUrl = 'https://pagosx.azul.com.do/paymentpage/default.aspx'

            # validate if main endpoint is up, else use alternative endpoint
            if(self.checkEndPoint(self._requestUrl) == False): 
                self._requestUrl = 'https://contpagos.azul.com.do/paymentpage/default.aspx'

        else: 
            self._requestUrl = 'https://pruebas.azul.com.do/PaymentPage/'

        # print (self._requestUrl)


checkEndpoint = CheckEndpoint()
checkEndpoint.setRequestUrlAzul()

print (checkEndpoint._requestUrl)