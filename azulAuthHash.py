import hashlib
from collections import OrderedDict

class azulAuthHash():

    def _generate_hash(self, args):

        args_string = ''.join(str(v) for v in args.values())
        # args_string = ''.join(map(str, args.values()))  # this way works too
        utf_string = args_string.encode('UTF-16LE')
        hash_sha512_string = hashlib.sha512(utf_string).hexdigest()

        ''''
        Azul documentation as December 2020, says that we need do this:
        * 1 - concatenating a few fields (those in dict format at method: _getAzulFormFields())
        * 2 - calculate a hash sha512
        * 3 - convert the hash to hexadecimal string
        '''

        return hash_sha512_string

    def _getAzulFormFields(self):

        return OrderedDict([
                            ('MerchantId', str('455593373663')),
                            ('MerchantName', 'Fast Food Services'),
                            ('MerchantType', 'Fast Food Industry'),
                            ('CurrencyCode', '$'),
                            ('OrderNumber', '001234'),
                            ('Amount', str('100000')),
                            ('ITBIS', str('18000')),
                            ('ApprovedUrl', 'softnet.do/success'),
                            ('DeclinedUrl', 'softnet.do/declined'),
                            ('CancelUrl', 'softnet.do/canceled'),
                            ('UseCustomField1', str('1')),
                            ('CustomField1Label', 'Foo'),
                            ('CustomField1Value', 'Bar'),
                            ('UseCustomField2', str('0')),
                            ('CustomField2Label', ''),
                            ('CustomField2Value', ''),
                            ('AuthKey', 'asdhakjshdkjasdasmndajksdkjaskldga8odya9d8yoasyd98asdyaisdhoaisyd0a8sydoashd8oasydoiahdpiashd09ayusidhaos8dy0a8dya08syd0a8ssdsax') # ***** WARNING! *****, DON'T SEND THIS FIELD IN THE POST FORM IN CLIENT SIDE. Tips: unset($args['AuthKey'])
                            ])        


azulAuthHash = azulAuthHash()
data = azulAuthHash._getAzulFormFields()
authHash = azulAuthHash._generate_hash(data)
print (authHash)