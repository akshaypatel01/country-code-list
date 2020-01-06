import pandas as pd
data=pd.read_csv("country_codes.csv")
fl = open("country_list_json.json","a")
fl.write("[\n \t") 
for i in range(data.shape[0]):
    l1="{\n"
    l2="\t \"id\": "+str(i+1)+",\n"
    l3="\t \"country\" : \""+data["COUNTRY "][i]+"\",\n"
    l4="\t \"code\" : \" "+data["COUNTRY CODE "][i]+"\",\n"
    l5="\t \"iso code\" : \" "+data["ISO CODES "][i]+"\" \n },\n"
    obj=l1+l2+l3+l4+l5
    fl.write(obj)
fl.write("]")
fl.close() 