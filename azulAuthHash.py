import hashlib
import hmac
from collections import OrderedDict

class azulAuthHash():

    _AuthKey = 'asdhakjshdkjasdasmndajksdkjaskldga8odya9d8yoasyd98asdyaisdhoaisyd0a8sydoashd8oasydoiahdpiashd09ayusidhaos8dy0a8dya08syd0a8ssdsax'

    def _generate_hash(self, args):

        args_string = ''.join(str(v) for v in args.values())
        # args_string = ''.join(map(str, args.values()))  # this way works too

        hash_sha512_string = hmac.new(bytes(self._AuthKey, 'utf8'), bytes(args_string, 'utf8'), hashlib.sha512).hexdigest()

        ''''
        Azul documentation as December 2020, says that we need do this:
        * 1 - concatenating a few fields (those in dict format at method: _getAzulFormFields())
        * 2 - calculate a hash sha512
        * 3 - convert the hash to hexadecimal string
        '''

        return hash_sha512_string

    def _getAzulFormFields(self):

        return OrderedDict([
                            ('MerchantId', str('39038540035')),
                            ('MerchantName', 'Azul Test'),
                            ('MerchantType', 'E-Commerce'),
                            ('CurrencyCode', '$'),
                            ('OrderNumber', '001'),
                            ('Amount', str('2000')),
                            ('ITBIS', str('1000')),
                            ('ApprovedUrl', 'https://azul.com.do'),
                            ('DeclinedUrl', 'https://azul.com.do'),
                            ('CancelUrl', 'https://azul.com.do'),
                            ('UseCustomField1', str('0')),
                            ('CustomField1Label', ''),
                            ('CustomField1Value', ''),
                            ('UseCustomField2', str('0')),
                            ('CustomField2Label', ''),
                            ('CustomField2Value', ''),
                            ('AuthKey', self._AuthKey) # ***** WARNING! *****, DON'T SEND THIS FIELD IN THE POST FORM IN CLIENT SIDE. Tips: unset($args['AuthKey'])
                            ])


azulAuthHash = azulAuthHash()
data = azulAuthHash._getAzulFormFields()
authHash = azulAuthHash._generate_hash(data)
print (authHash)