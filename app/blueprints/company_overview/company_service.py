from vnstock import Vnstock, Company


class CompanyService: 
    @staticmethod
    def get_company_news(stock_code: str, source = 'TCBS'):
        company = Company(symbol=stock_code, source=source)
        return company.news()