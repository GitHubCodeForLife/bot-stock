from vnstock import Vnstock, Company
from flask_caching import Cache
from app.shareData import ShareData
class CompanyService: 
    @staticmethod
    def get_company_news(stock_code: str, source = 'TCBS'):
        cache_key = "company_news_" + stock_code + "_" + source;
        company_news = ShareData.cache.get(cache_key)
        # check if not stored in cached and fetch data from vnstock
        if company_news is None:
            company_news = Company(symbol=stock_code, source=source).news()
            print(company_news, cache_key) 
            ShareData.cache.set(cache_key, company_news, timeout=60)

        return company_news