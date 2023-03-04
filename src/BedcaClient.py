import pycurl
from io import BytesIO
import json
import xmltodict
from src.BedcaXMLRequests import BedcaRequest

class BedcaClient():
    apiBase = 'https://www.bedca.net/bdpub/procquery.php'
    
    def getFood(self,foodId: int, rawXML: bool = False) -> str:
        foodGroupXML = BedcaRequest.getFoodXML(foodId)

        if (rawXML):
            return self.curlXMLRequest(self.apiBase, foodGroupXML)
        else:
            return self.XMLToStdClass(self.curlXMLRequest(self.apiBase, foodGroupXML))

    def getFoodGroups(self,rawXML: str = False) -> str:
        foodGroupXML = BedcaRequest.getFoodGroupsXML()

        if (rawXML):
            return self.curlXMLRequest(self.apiBase, foodGroupXML)
        else:
            return self.XMLToStdClass(self.curlXMLRequest(self.apiBase, foodGroupXML))

    def getFoodsInGroup(self,foodGroupId: int, rawXML: str = False) -> str:
        foodGroupXML = BedcaRequest.getFoodGroupXML(foodGroupId)

        if (rawXML):
            return self.curlXMLRequest(self.apiBase, foodGroupXML)
        else:
            return self.XMLToStdClass(self.curlXMLRequest(self.apiBase, foodGroupXML))

    def XMLToStdClass(self,xml: str) -> str:
        dictXML = xmltodict.parse(xml)
        return json.dumps(dictXML,indent=4)

    def curlXMLRequest(self,url: str, xml: str) -> str:
        headers = [
            "Content-Type: text/xml",
            "Connection: close"]

        buffer = BytesIO()
        crl = pycurl.Curl() 

        crl.setopt(crl.URL, url);
        crl.setopt(crl.ENCODING, 'UTF-8')
        crl.setopt(crl.POST, True)
        crl.setopt(crl.POSTFIELDS, xml)
        crl.setopt(crl.HTTPHEADER, headers)
        crl.setopt(crl.SSL_VERIFYPEER, False)
        crl.setopt(crl.SSL_VERIFYHOST, False)
        crl.setopt(crl.WRITEDATA, buffer)
        crl.perform()
        crl.close()

        body = buffer.getvalue()

        return body.decode('UTF-8')