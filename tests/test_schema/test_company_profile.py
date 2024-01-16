import pytest
from fmp import CompanyProfile 

import pydantic

def test_fmp_company_profile_is_a_pydantic_base_model () :
    assert issubclass(CompanyProfile, pydantic.BaseModel)
    
def test_fmp_company_profile_has_expected_properties () :
    company_profile = CompanyProfile(**{
		"symbol": "AAPL",
		"price": 178.72,
		"beta": 1.286802,
		"volAvg": 58405568,
		"mktCap": 2794144143933,
		"lastDiv": 0.96,
		"range": "124.17-198.23",
		"changes": -0.13,
		"companyName": "Apple Inc.",
		"currency": "USD",
		"cik": "0000320193",
		"isin": "US0378331005",
		"cusip": "037833100",
		"exchange": "NASDAQ Global Select",
		"exchangeShortName": "NASDAQ",
		"industry": "Consumer Electronics",
		"website": "https://www.apple.com",
		"description": "Apple Inc. designs, manufactures, and markets smartphones, personal computers, tablets, wearables, and accessories worldwide. It also sells various related services. In addition, the company offers iPhone, a line of smartphones; Mac, a line of personal computers; iPad, a line of multi-purpose tablets; AirPods Max, an over-ear wireless headphone; and wearables, home, and accessories comprising AirPods, Apple TV, Apple Watch, Beats products, HomePod, and iPod touch. Further, it provides AppleCare support services; cloud services store services; and operates various platforms, including the App Store that allow customers to discover and download applications and digital content, such as books, music, video, games, and podcasts. Additionally, the company offers various services, such as Apple Arcade, a game subscription service; Apple Music, which offers users a curated listening experience with on-demand radio stations; Apple News+, a subscription news and magazine service; Apple TV+, which offers exclusive original content; Apple Card, a co-branded credit card; and Apple Pay, a cashless payment service, as well as licenses its intellectual property. The company serves consumers, and small and mid-sized businesses; and the education, enterprise, and government markets. It distributes third-party applications for its products through the App Store. The company also sells its products through its retail and online stores, and direct sales force; and third-party cellular network carriers, wholesalers, retailers, and resellers. Apple Inc. was incorporated in 1977 and is headquartered in Cupertino, California.",
		"ceo": "Mr. Timothy D. Cook",
		"sector": "Technology",
		"country": "US",
		"fullTimeEmployees": "164000",
		"phone": "408 996 1010",
		"address": "One Apple Park Way",
		"city": "Cupertino",
		"state": "CA",
		"zip": "95014",
		"dcfDiff": 4.15176,
		"dcf": 150.082,
		"image": "https://financialmodelingprep.com/image-stock/AAPL.png",
		"ipoDate": "1980-12-12",
		"defaultImage": False,
		"isEtf": False,
		"isActivelyTrading": True,
		"isAdr": False,
		"isFund": False
	})
    
    assert company_profile.symbol == "AAPL"
    assert company_profile.price == 178.72
    assert company_profile.beta == 1.286802
    assert company_profile.volAvg == 58405568
    assert company_profile.mktCap == 2794144143933
    assert company_profile.lastDiv == 0.96
    assert company_profile.range == (124.17, 198.23)
    assert company_profile.changes == -0.13
    assert company_profile.companyName == "Apple Inc."
    assert company_profile.currency == "USD"
    assert company_profile.cik == "0000320193"
    assert company_profile.isin == "US0378331005"
    assert company_profile.cusip == "037833100"
    assert company_profile.exchange == "NASDAQ Global Select"
    assert company_profile.exchangeShortName == "NASDAQ"
    assert company_profile.industry == "Consumer Electronics"
    assert company_profile.website == "https://www.apple.com"
    assert company_profile.description == "Apple Inc. designs, manufactures, and markets smartphones, personal computers, tablets, wearables, and accessories worldwide. It also sells various related services. In addition, the company offers iPhone, a line of smartphones; Mac, a line of personal computers; iPad, a line of multi-purpose tablets; AirPods Max, an over-ear wireless headphone; and wearables, home, and accessories comprising AirPods, Apple TV, Apple Watch, Beats products, HomePod, and iPod touch. Further, it provides AppleCare support services; cloud services store services; and operates various platforms, including the App Store that allow customers to discover and download applications and digital content, such as books, music, video, games, and podcasts. Additionally, the company offers various services, such as Apple Arcade, a game subscription service; Apple Music, which offers users a curated listening experience with on-demand radio stations; Apple News+, a subscription news and magazine service; Apple TV+, which offers exclusive original content; Apple Card, a co-branded credit card; and Apple Pay, a cashless payment service, as well as licenses its intellectual property. The company serves consumers, and small and mid-sized businesses; and the education, enterprise, and government markets. It distributes third-party applications for its products through the App Store. The company also sells its products through its retail and online stores, and direct sales force; and third-party cellular network carriers, wholesalers, retailers, and resellers. Apple Inc. was incorporated in 1977 and is headquartered in Cupertino, California."
    assert company_profile.ceo == "Mr. Timothy D. Cook"
    assert company_profile.sector == "Technology"
    assert company_profile.country == "US"
    assert company_profile.fullTimeEmployees == 164000
    assert company_profile.phone == "408 996 1010"
    assert company_profile.address == "One Apple Park Way"
    assert company_profile.city == "Cupertino"
    assert company_profile.state == "CA"
    assert company_profile.zip == "95014"
    assert company_profile.dcfDiff == 4.15176
    assert company_profile.dcf == 150.082
    assert company_profile.image == "https://financialmodelingprep.com/image-stock/AAPL.png"
    assert company_profile.ipoDate == "1980-12-12"
    assert company_profile.defaultImage == False
    assert company_profile.isEtf == False
    assert company_profile.isActivelyTrading == True
    assert company_profile.isAdr == False
    assert company_profile.isFund == False
    
    
    