import requests
from bs4 import BeautifulSoup
import csv



def websc():
    global dist_name
    global cases
    global alpha

    r=requests.get('https://covid19.mohp.gov.np/')
    html=r.content

    soup=BeautifulSoup(html,'html.parser')
    #csv_file=open('covid_cases.csv','w')
    #csv_writer=csv.writer(csv_file)
    #csv_writer.writerow(['District','No_of_Cases'])

    #dist_name = []
    #cases=[]
    
    alpha = soup.find_all('div',{'class':'ant-row ant-row-center'})
    print(alpha)
    
   

websc()








