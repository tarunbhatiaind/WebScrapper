import  bs4
import urllib

from urllib.request import urlopen as uReq #grab the page
from bs4 import BeautifulSoup as soup  #parse HTML text

url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphic%20cards'
uClient = uReq(url) #open connection , getting the page
myHTML= uClient.read() #content into html
uClient.close() # close connection
page_soup = soup(myHTML,"html.parser") #mention the parser , html in our case
containers=page_soup.findAll("div",{"class":"item-container"})
contain = containers[0]
file="products.csv"
f=open(file,"w")
headers ="Brand , Product_Name, Shipping fee\n"
f.write(headers)

for contain in containers:
    divWithInfo = contain.find("div", "item-info")
    brand=divWithInfo.div.a.img["title"]
    title_container = divWithInfo.find("a", {"class": "item-title"})
    prod_name = title_container.text
    divWithAction=contain.find("div","item-action")
    #print(divWithAction.ul.find("li",{"class":"price-ship"}).text)
    #break
    fee_container=divWithAction.ul.find("li",{"class":"price-ship"})
    shippingFee=fee_container.text.strip()
    print("Brand is :"+brand,"\nproduct name:"+prod_name,"\nProduct_price:"+shippingFee)
    f.write(brand + "," + prod_name.replace(",","|") + "," + shippingFee +"\n")

f.close()
