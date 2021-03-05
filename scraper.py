from selenium import webdriver
import time
import pickle

driver = webdriver.Chrome()
lista=[]
driver.get("http://www.amazon.it")

def openProduct(elem):
    product={}
    product["id"]=elem.get_attribute("data-asin")
    elem.click()
    time.sleep(0.5)
    product["price"]=driver.find_element_by_class_name("a-color-price").text
##    product["price"]=driver.find_element_by_id("price").text
    product["name"]=driver.find_element_by_id("title").text
    driver.back()
    driver.refresh()
    lista.append(product)
    return product


def searchProduct(productName):
    driver.get("http://www.amazon.it")
    serach = driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]')
    serach.send_keys(productName+"\n")

    n = len(driver.find_elements_by_class_name("s-result-item"))

    for i in range(1,n-2):
        e=driver.find_elements_by_class_name("s-result-item")[i]
        try:
            print(openProduct(e))
        except:
            pass



f=open("products.txt","rb")
l=f.readlines()

for x in l:
    try:
        searchProduct(x.decode("utf-8"))
    except:
        pass
pickle.dumps(lista,open("dump.stc","wb"))