#from __future__ import print_function
import urllib2
from bs4 import BeautifulSoup
from pandas import DataFrame as pd_df
#import re


#update the column name and urls here

android_urls={'Flipkart':'https://play.google.com/store/apps/details?id=com.flipkart.android&hl=en', 
              'Snapdeal':'https://play.google.com/store/apps/details?id=com.snapdeal.main',
               'Amazon':'https://play.google.com/store/apps/details?id=com.amazon.mShop.android.shopping',
              'eBay':'https://play.google.com/store/apps/details?id=com.ebay.mobile'
              } 

itunes_urls={'Zara':'https://itunes.apple.com/gb/app/zara/id547951480?mt=8',
                'Amazon':'https://itunes.apple.com/gb/app/amazon/id335187483?mt=8', 
               'Argos':'https://itunes.apple.com/gb/app/argos/id370371087?mt=8',
              'Zalando':'https://itunes.apple.com/gb/app/zalando-fashion-high-street/id585629514?mt=8'
              } 


def android_extract(urls):
    result = {}
    for name in urls:
    
        url_content = urllib2.urlopen(urls[name]).read()

        soup = BeautifulSoup(url_content, "html.parser")

        ratings =  (soup.find('div',attrs={"class" : "score"}).text)

        vol =  (soup.find('span',attrs={"class" : "reviews-num"}).text)

        result[name] = [ratings,vol]

    return(result)

def itunes_extract(urls):
    result = {}
    for name in urls:
    
        url_content = urllib2.urlopen(urls[name]).read()

        soup = BeautifulSoup(url_content, "html.parser")
        #print(name)

        ratings_t =  soup.find('div',attrs={"id" : "left-stack"}).find('div',attrs={'class':'rating','itemprop':None})

        if ratings_t is not None:
            ratings  =  ratings_t['aria-label'].split(',')[0].replace(' and a half','.5').replace('stars','')
            vol = ratings_t['aria-label'].split(',')[1].replace('Ratings','').replace(' ','')
            result[name] = [ratings,vol]
            
        else:
            result[name] = ['None','None']
            
        

    return(result)
''' 
def options(x):
    return {
        '1': android_extract(android_urls),
        '2': itunes_extract(itunes_urls),
    }.get(x, 'Please try again with the right option 1 or 2')

'''
    
and_res =  android_extract(android_urls)
print(pd_df(and_res))
pd_df(and_res).to_csv('and.csv')
ip_res =  itunes_extract(itunes_urls)
print(pd_df(ip_res))
pd_df(ip_res).to_csv('ip.csv')
'''

for res in and_res:
    print(res)
    print(and_res[res])
    
ip_res =  itunes_extract(itunes_urls)
for res in ip_res:
    print(res)
    print(ip_res[res])


if __name__ == "__main__":
    print(options(str(raw_input('Enter your desired option: \n "1" for Android \n "2" for iOS\n'))))
'''
