from langchain_community.document_loaders import AsyncChromiumLoader
from langchain_community.document_transformers import BeautifulSoupTransformer
class ScrapData:
    def __init__(self,website_list) -> None:
        self.website_list=website_list
        self.loader=AsyncChromiumLoader(self.website_list)
        self.bs_transformer=BeautifulSoupTransformer()
        
    def get_data(self):
        html=self.loader.load()
        docs_transformed=self.bs_transformer.transform_documents(html)
        data_list=[]
        for doc in docs_transformed:
            data_dict={}
            data_dict["website"]=doc.metadata.get('source')
            data_dict["site_content"]=doc.page_content
            data_list.append(data_dict)
        return data_list


# Test script for the above class
if __name__=="__main__":
    news_site=["https://time.com/","https://www.gadgets360.com/","https://indianexpress.com/","https://news.google.com/"]
    scrapper=ScrapData(news_site)
    data=scrapper.get_data()
    print(data)
