import json
class JohnParser:

    def __init__(self,inputfile,outputfile= None):
        self.inputfile=inputfile
        self.outputfile=outputfile

    def parseJson(self):
        with open(self.inputfile, 'r') as inf:
           data_asJson = json.load(inf)
           return data_asJson

    def create_johnfile(self):
        data= self.parseJson()
        res_element=[]
        
        for record in data["records"]:
            
            if "result" in record:
                for r in record["result"]:
                    temp_string=record["name"] + ":"+ r["sha1"]
                    res_element.append(temp_string)
        with open(self.outputfile,"a") as of:
            for item in res_element:
                of.write(item)
                of.write("\n")


#if __name__ == "__main__":
    #jp=JohnParser("parsed_sample.txt","outputjohnfile.txt")
    #jp.create_johnfile()