from selenium import webdriver
from pymongo import MongoClient
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
driver = webdriver.Chrome('D:/finalproject/chromedriver.exe')
client = MongoClient('localhost',27017)
db = client.CryptoData
delay=3
def NaverFinance_Silver():

    num=0
    rownum=0
    page=2

    pagenum_front = '/html/body/div/div/a['
    pagenum_end = ']'

    url = 'https://finance.naver.com/marketindex/worldGoldDetail.nhn?marketindexCd=CMDT_SI&fdtc=2'
    driver.get(url)

    element = driver.find_element_by_xpath("/html/body/div[3]/div[1]/div[2]/div[2]/iframe")
    driver.switch_to.frame(element)

    date=''
    endcost =''
    fluctuation = ''

    data = driver.find_element_by_xpath("/html/body/div/table/tbody")
    rows = data.find_elements_by_tag_name("td")
    while True:

        for p in rows:
            num += 1
            if num%4==1:
                date = p.text
                if date == '2018.07.31':
                    break;
            elif num%4==2:
                endcost = p.text
            elif num%4==0:
                fluctuation = p.text
                data = {'날짜': date, '종가': endcost, '등락율': fluctuation}
                print(data)
                rownum+=1
                db.NaverFinance_Silver.insert_one(data)
            if rownum==7:
                page_info = pagenum_front + str(page) + pagenum_end
                if page<5:
                    page += 1
                driver.find_element_by_xpath(page_info).click()
                print(page)
                num=0
                rownum=0
                data = driver.find_element_by_xpath("/html/body/div/table/tbody")
                rows = data.find_elements_by_tag_name("td")


def NaverFinance_Oil():

    num=0
    rownum=0
    page=2

    pagenum_front = '/html/body/div/div/a['
    pagenum_end = ']'

    url = 'https://finance.naver.com/marketindex/worldOilDetail.nhn?marketindexCd=OIL_DU&fdtc=2'
    driver.get(url)

    element = driver.find_element_by_xpath("/html/body/div[3]/div[1]/div[2]/div[2]/iframe")
    driver.switch_to.frame(element)

    date=''
    endcost =''
    fluctuation = ''

    data = driver.find_element_by_xpath("/html/body/div/table/tbody")
    rows = data.find_elements_by_tag_name("td")
    while True:

        for p in rows:
            num += 1
            if num%4==1:
                date = p.text
                if date == '2018.07.31':
                    break;
            elif num%4==2:
                endcost = p.text
            elif num%4==0:
                fluctuation = p.text
                data = {'날짜': date, '종가': endcost, '등락율': fluctuation}
                print(data)
                rownum+=1
                db.NaverFinance_Oil.insert_one(data)
            if rownum==7:
                page_info = pagenum_front + str(page) + pagenum_end
                if page<5:
                    page += 1
                driver.find_element_by_xpath(page_info).click()
                print(page)
                num=0
                rownum=0
                data = driver.find_element_by_xpath("/html/body/div/table/tbody")
                rows = data.find_elements_by_tag_name("td")


def NaverFinance_Gold():

    num=0
    rownum=0
    page=2

    pagenum_front = '/html/body/div/div/a['
    pagenum_end = ']'

    url = 'https://finance.naver.com/marketindex/worldGoldDetail.nhn?marketindexCd=CMDT_GC&fdtc=2'
    driver.get(url)

    element = driver.find_element_by_xpath("/html/body/div[3]/div[1]/div[2]/div[2]/iframe")
    driver.switch_to.frame(element)

    date=''
    endcost =''
    fluctuation = ''

    data = driver.find_element_by_xpath("/html/body/div/table/tbody")
    rows = data.find_elements_by_tag_name("td")
    while True:

        for p in rows:
            num += 1
            if num%4==1:
                date = p.text
                if date == '2018.07.31':
                    break;
            elif num%4==2:
                endcost = p.text
            elif num%4==0:
                fluctuation = p.text
                data = {'날짜': date, '종가': endcost, '등락율': fluctuation}
                print(data)
                rownum+=1
                db.NaverFinance_Gold.insert_one(data)
            if rownum==7:
                page_info = pagenum_front + str(page) + pagenum_end
                if page<5:
                    page += 1
                driver.find_element_by_xpath(page_info).click()
                print(page)
                num=0
                rownum=0
                data = driver.find_element_by_xpath("/html/body/div/table/tbody")
                rows = data.find_elements_by_tag_name("td")












    #for tab in table.find_elements_by_tag_name("tr"):
     #   data = tab.find_elements_by_tag_name("td")
      #  s = "{} , {}\n".format(td[1].text, td[2].text)
       # print(s)


def NaverFinance_Copper():

    num=0
    rownum=0
    page=2

    pagenum_front = '/html/body/div/div/a['
    pagenum_end = ']'

    url = 'https://finance.naver.com/marketindex/worldOilDetail.nhn?marketindexCd=OIL_DU&fdtc=2'
    driver.get(url)

    element = driver.find_element_by_xpath("/html/body/div[3]/div[1]/div[2]/div[2]/iframe")
    driver.switch_to.frame(element)

    date=''
    endcost =''
    fluctuation = ''

    data = driver.find_element_by_xpath("/html/body/div/table/tbody")
    rows = data.find_elements_by_tag_name("td")
    while True:

        for p in rows:
            num += 1
            if num%4==1:
                date = p.text
                if date == '2018.07.31':
                    break;
            elif num%4==2:
                endcost = p.text
            elif num%4==0:
                fluctuation = p.text
                data = {'날짜': date, '종가': endcost, '등락율': fluctuation}
                print(data)
                rownum+=1
                db.NaverFinance_Oil.insert_one(data)
            if rownum==7:
                page_info = pagenum_front + str(page) + pagenum_end
                if page<5:
                    page += 1
                driver.find_element_by_xpath(page_info).click()
                print(page)
                num=0
                rownum=0
                data = driver.find_element_by_xpath("/html/body/div/table/tbody")
                rows = data.find_elements_by_tag_name("td")


def Moneynet_normal():

    url_front = 'https://www.moneynet.co.kr/index.php?mid=free_board&page='
    url_mid = 12

    money_front = '/html/body/div[4]/div[1]/div[1]/div[3]/div[2]/div/div/div[2]/table/tbody/tr['
    money_mid = 5
    money_end = ']/td[2]/a[1]'

    moneyday_front = '/html/body/div[4]/div[1]/div[1]/div[3]/div[2]/div/div/div[2]/table/tbody/tr['

    moneyday_end = ']/td[6]/span'

    loading_check = '/html/body/div[4]/div[1]/div[1]/div[3]/div[2]/div/div/div[2]/table/tbody/tr[5]/td[2]/a[1]'

    url = url_front + str(url_mid)
    driver.get(url)
    info_list = []
    past_data = '2021.05.02'
    while True:
        try:
            money_info = money_front + str(money_mid) + money_end
            moneyday_info = moneyday_front + str(money_mid) + moneyday_end
            money = driver.find_element_by_xpath(money_info).text
            moneyday = driver.find_element_by_xpath(moneyday_info).text


            if moneyday != past_data:
                data = {'날짜': past_data, '제목': info_list}
                db.MoneyNet_Normal.insert_one(data)
                info_list = []
            else:
                if money not in info_list:
                    info_list.append(money)
                    print(money+'날짜 '+ past_data)


                money_mid += 1


            if money_mid>23:
                money_mid =5
                url_mid += 1
                url = url_front + str(url_mid)
                driver.get(url)
                WebDriverWait(driver, delay).until(
                    expected_conditions.visibility_of_element_located(
                        (By.XPATH, loading_check)
                    )
                )
            past_data = moneyday
            if int(url_mid)>4207:
                break;
        except:
            money_mid = 5
            url_mid += 1
            url = url_front + str(url_mid)
            driver.get(url)
            WebDriverWait(driver, delay).until(
                expected_conditions.visibility_of_element_located(
                    (By.XPATH, loading_check)
                )
            )


def Moneynet_Hot():

    url_front = 'https://www.moneynet.co.kr/index.php?mid=best_board&page='
    url_mid = 1

    money_front = '/html/body/div[4]/div[1]/div[1]/div[3]/div[2]/div[2]/div[2]/table/tbody/tr['
    money_mid = 4
    money_end = ']/td[2]/a[1]'

    moneyday_front = '/html/body/div[4]/div[1]/div[1]/div[3]/div[2]/div[2]/div[2]/table/tbody/tr['

    moneyday_end = ']/td[4]'

    loading_check = '/html/body/div[4]/div[1]/div[1]/div[3]/div[2]/div[2]/div[2]/table/tbody/tr[4]/td[2]/a[1]'

    url = url_front + str(url_mid)
    driver.get(url)
    info_list = []
    past_data = '2021.05.13'
    while True:
        try:
            money_info = money_front + str(money_mid) + money_end
            moneyday_info = moneyday_front + str(money_mid) + moneyday_end
            money = driver.find_element_by_xpath(money_info).text
            moneyday = driver.find_element_by_xpath(moneyday_info).text


            if moneyday != past_data:
                data = {'날짜': past_data, '제목': info_list}
                db.MoneyNet_Best.insert_one(data)
                info_list = []
            else:
                if money not in info_list:
                    info_list.append(money)
                    print(money)


                money_mid += 1


            if money_mid>23:
                money_mid = 4
                url_mid += 1
                url = url_front + str(url_mid)
                driver.get(url)
                WebDriverWait(driver, delay).until(
                    expected_conditions.visibility_of_element_located(
                        (By.XPATH, loading_check)
                    )
                )
            past_data = moneyday
            if int(url_mid)>49:
                break;
        except:
            money_mid = 4
            url_mid += 1
            url = url_front + str(url_mid)
            driver.get(url)
            WebDriverWait(driver, delay).until(
                expected_conditions.visibility_of_element_located(
                    (By.XPATH, loading_check)
                )
            )


def BitcoinGallery_Hot():

    url_front = 'https://gall.dcinside.com/board/lists/?id=bitcoins&page='
    url_mid = 3
    url_end = '&exception_mode=recommend'

    gallery_front = '/html/body/div[2]/div[2]/main/section[1]/article[2]/div[2]/table/tbody/tr['
    gallery_mid = 6
    gallery_end = ']/td[2]/a[1]'

    galleryday_front = '/html/body/div[2]/div[2]/main/section[1]/article[2]/div[2]/table/tbody/tr['
    galleryday_end = ']/td[4]'

    loading_check = '/html/body/div[2]/div[2]/main/section[1]/article[2]/div[2]/table/tbody/tr[1]/td[2]/a[1]'

    url = url_front + str(url_mid) + url_end
    driver.get(url)

    while True:

        try:
            gallery_info = gallery_front + str(gallery_mid) + gallery_end
            galleryday_info = galleryday_front + str(gallery_mid) + galleryday_end

            gallery = driver.find_element_by_xpath(gallery_info).text
            galleryday = driver.find_element_by_xpath(galleryday_info).text

            if len(galleryday) < 7 :
                galleryday = '21.'+galleryday

            data = {'날짜': galleryday, '제목': gallery}
            print(data)
            db.BitCoinGallery.insert_one(data)
            gallery_mid += 1

        except:
            gallery_mid = 6
            url_mid += 1
            url = url_front + str(url_mid) + url_end
            driver.get(url)
            WebDriverWait(driver, delay).until(
                expected_conditions.visibility_of_element_located(
                    (By.XPATH, loading_check)
                )
            )
        if int(galleryday[0:2])==17 and int(galleryday[3:5])<8:
            break;


def Change_url(url):
    url_front = 'https://search.naver.com/search.naver?where=news&query=%EA%B0%80%EC%83%81%ED%99%94%ED%8F%90&sm=tab_opt&sort=1&photo=2&field=0&pd=3&ds=2018.08.01&de='
    url_mid = url

    url = url_front + url_mid

    driver.get(url)
    WebDriverWait(driver, delay).until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, '/html/body/div[3]/div[2]/div/div[1]/section[1]/div/div[3]/ul/li[1]/div/div/a')
        )
    )


def Get_NewsdataVer3():
    url_front = 'https://search.naver.com/search.naver?where=news&query=%EA%B0%80%EC%83%81%ED%99%94%ED%8F%90&sm=tab_opt&sort=1&photo=2&field=0&pd=3&ds=2018.08.01&de='
    url_mid = '2021.04.30'
    url_end = '&docid=&related=0&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so%3Add%2Cp%3Afrom20010101to20210430'
    url = url_front + url_mid + url_end
    driver.get(url)
    count = 0


    datelink_front = '/html/body/div[3]/div[2]/div/div[1]/div[2]/div/div/a['
    datelink_mid = 1
    datelink_end = ']'

    date_front = '/html/body/div[3]/div[2]/div/div[1]/section[1]/div/div[3]/ul/li['
    date_mid = 1
    date_end = ']/div/div/div[1]/div/span'

    newsline_front = '/html/body/div[3]/div[2]/div/div[1]/section[1]/div/div[3]/ul/li['
    newsline_mid = 1
    newsline_end = ']/div/div/a'

    next = '/html/body/div[3]/div[2]/div/div[1]/div[2]/div/a[2]'

    company_front = '/html/body/div[3]/div[2]/div/div[1]/section[1]/div/div[3]/ul/li['
    company_mid = 1
    company_end = ']/div/div/div[1]/div[2]/a'
    date_past='2021.04.30'

    newslines = []

    banned_list = []
    loading_check = '/html/body/div[3]/div[2]/div/div[1]/section[1]/div/div[3]/ul/li[1]/div/div/a'

    while True:
        try:

            datelink_info = datelink_front + str(datelink_mid) + datelink_end
            company_info = company_front+ str(company_mid) + company_end

            date_info = date_front + str(date_mid) + date_end
            date_info2 = '/html/body/div[3]/div[2]/div/div[1]/section[1]/div/div[3]/ul/li[1]/div/div/div[1]/div/span[2]'
            newsline_info = newsline_front + str(newsline_mid) + newsline_end

            date = driver.find_element_by_xpath(date_info).text

            try:
                int(date[0:4])
            except:
                date = driver.find_element_by_xpath(date_info2).text


            newsline = driver.find_element_by_xpath(newsline_info).text
            company = driver.find_element_by_xpath(company_info).text

            if company in banned_list:
                if company_mid<10:
                    date_mid += 1
                    newsline_mid += 1
                    company_mid += 1
                else:
                    count += 1
                    driver.find_element_by_xpath(next).click()
                    if count > 300:
                        Change_url(date_past)

                        count = 0
                    WebDriverWait(driver, delay).until(
                        expected_conditions.visibility_of_element_located(
                            (By.XPATH, loading_check)
                        )
                    )
                    date_mid = 1
                    newsline_mid = 1
                    company_mid = 1

                #print(company + "감지하였다. 스킵한다.")
                continue

            #print(date + ' ' + newsline + ' ' + company)


            if date != date_past :

                data = {'날짜': date_past, '기사': newslines}
                #데이터 삽입

                db.NewsData_Video.insert_one(data)
                newslines = []
                #print('날짜'+date + '이전날짜' + date_past)
            else:
                print(date + ' ' + newsline + ' ' + company)
                newslines.append(newsline)

            date_past = date
            #print("블럭번호" + str(company_mid) + "페이지번호" + str(count) + "기사번호 "+ str(newsline_mid))
            date_mid += 1
            newsline_mid += 1
            company_mid += 1


        except:
            count+=1
            driver.find_element_by_xpath(next).click()
            if count>300:
                Change_url(date_past)

                count=0
            WebDriverWait(driver, delay).until(
                expected_conditions.visibility_of_element_located(
                    (By.XPATH, loading_check)
                )
            )
            date_mid = 1
            newsline_mid = 1
            company_mid = 1


def Newsdata_Photo():
    url_front = 'https://search.naver.com/search.naver?where=news&query=%EA%B0%80%EC%83%81%ED%99%94%ED%8F%90&sm=tab_opt&sort=1&photo=1&field=0&pd=3&ds=2018.08.01&de='
    url_mid = '2021.04.30'
    url_end = '&docid=&related=0&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so%3Add%2Cp%3Afrom20010101to20210430'
    url = url_front + url_mid + url_end
    driver.get(url)
    count = 0


    datelink_front = '/html/body/div[3]/div[2]/div/div[1]/div[2]/div/div/a['
    datelink_mid = 1
    datelink_end = ']'

    date_front = '/html/body/div[3]/div[2]/div/div[1]/section[1]/div/div[3]/ul/li['
    date_mid = 1
    date_end = ']/div/div/div[1]/div/span'

    newsline_front = '/html/body/div[3]/div[2]/div/div[1]/section[1]/div/div[3]/ul/li['
    newsline_mid = 1
    newsline_end = ']/div/div/a'

    next = '/html/body/div[3]/div[2]/div/div[1]/div[2]/div/a[2]'

    company_front = '/html/body/div[3]/div[2]/div/div[1]/section[1]/div/div[3]/ul/li['
    company_mid = 1
    company_end = ']/div/div/div[1]/div[2]/a'
    date_past='2021.04.30'

    newslines = []

    banned_list = ['뉴스인사이드', '로이슈','마켓뉴스', 'CCTV뉴스', '내외경제tv', '비욘드포스트']
    loading_check = '/html/body/div[3]/div[2]/div/div[1]/section[1]/div/div[3]/ul/li[1]/div/div/a'

    while True:
        try:

            datelink_info = datelink_front + str(datelink_mid) + datelink_end
            company_info = company_front+ str(company_mid) + company_end

            date_info = date_front + str(date_mid) + date_end
            date_info2 = '/html/body/div[3]/div[2]/div/div[1]/section[1]/div/div[3]/ul/li[1]/div/div/div[1]/div/span[2]'
            newsline_info = newsline_front + str(newsline_mid) + newsline_end

            date = driver.find_element_by_xpath(date_info).text

            try:
                int(date[0:4])
            except:
                date = driver.find_element_by_xpath(date_info2).text


            newsline = driver.find_element_by_xpath(newsline_info).text
            company = driver.find_element_by_xpath(company_info).text

            if company in banned_list:
                if company_mid<10:
                    date_mid += 1
                    newsline_mid += 1
                    company_mid += 1
                else:
                    count += 1
                    driver.find_element_by_xpath(next).click()
                    if count > 300:
                        Change_url(date_past)

                        count = 0
                    WebDriverWait(driver, delay).until(
                        expected_conditions.visibility_of_element_located(
                            (By.XPATH, loading_check)
                        )
                    )
                    date_mid = 1
                    newsline_mid = 1
                    company_mid = 1

                #print(company + "감지하였다. 스킵한다.")
                continue

            #print(date + ' ' + newsline + ' ' + company)


            if date != date_past :

                data = {'날짜': date_past, '기사': newslines}
                #데이터 삽입

                db.NewsData_Photo.insert_one(data)
                newslines = []
                #print('날짜'+date + '이전날짜' + date_past)
            else:
                print(date + ' ' + newsline + ' ' + company)
                newslines.append(newsline)

            date_past = date
            #print("블럭번호" + str(company_mid) + "페이지번호" + str(count) + "기사번호 "+ str(newsline_mid))
            date_mid += 1
            newsline_mid += 1
            company_mid += 1


        except:
            count+=1
            driver.find_element_by_xpath(next).click()
            if count>300:
                Change_url(date_past)

                count=0
            WebDriverWait(driver, delay).until(
                expected_conditions.visibility_of_element_located(
                    (By.XPATH, loading_check)
                )
            )
            date_mid = 1
            newsline_mid = 1
            company_mid = 1


def To_CSV_Finance():
    list1 = list(db.NaverFinance_Oil.find({},{'_id':0}))
    list123 = []
    for k in list1:
        list123.append(k)
    column = ['날짜','종가','등락율']

    df = pd.DataFrame(list123,columns=column)

    df.to_csv('오잉.csv', index=False, encoding='cp949')


def To_CSV_UserComment():
    list1 = list(db.BitCoinGallery.find({},{'_id':0}))
    list123 = []

    for k in list1:
        date = k['날짜']
        t = k['제목']
        list123.append([date,t])

    column = ['날짜','제목']
    df = pd.DataFrame(list123,columns=column)

    df.to_csv('비트코인갤러리_인기글.csv', index=False, encoding='utf-8-sig' )


def To_CSV_Article():
    list1 = list(db.NewsData.find({},{'_id':0}))
    list123 = []

    for k in list1:
        date = k['날짜']
        if len(k['기사']) == 0:
            continue
        for t in k['기사']:
            list123.append([date,t])
    column = ['날짜','기사']
    df = pd.DataFrame(list123,columns=column)

    df.to_csv('뉴스_지면기사.csv', index=False, encoding='utf-8-sig')


def To_CSV_Stock():
    list1 = list(db.StockData_Samsung.find({},{'_id':0}))
    list123 = []

    for k in list1:
        date = k['날짜']
        cost = k['종가']
        fluctuation = k['등락률']
        volume= k['거래량']
        list123.append(date,cost,fluctuation,volume)
    column = ['날짜','종가','등락률','거래량']
    df = pd.DataFrame(list123,columns=column)

    df.to_csv('삼성.csv', index=False, encoding='utf-8-sig')
def Coinpan_Specific():

    url_front = 'https://www.moneynet.co.kr/index.php?mid=free_board&page='
    url_mid = 3450

    money_front = '/html/body/div[4]/div[1]/div[1]/div[3]/div[2]/div/div/div[2]/table/tbody/tr['
    money_mid = 5
    money_end = ']/td[2]/a[1]'

    moneyday_front = '/html/body/div[4]/div[1]/div[1]/div[3]/div[2]/div/div/div[2]/table/tbody/tr['

    moneyday_end = ']/td[6]/span'

    loading_check = '/html/body/div[4]/div[1]/div[1]/div[3]/div[2]/div/div/div[1]/div[1]/div[1]/div/h1/a'

    specificInfo_front = '/html/body/div[4]/div[1]/div[1]/div[3]/div[2]/div/div/div[1]/div[3]/div/div[1]'
    specificInfo_front1 = '/html/body/div[4]/div[1]/div[1]/div[3]/div[2]/div/div/div[1]/div[4]/div/div[1]'
    specificInfo_front_1 = '/p['
    specificInfo_front_2 = '/div/p['
    specificInfo_mid = 1
    specificInfo_mid1=1
    specificInfo_mid2 = 1
    specificInfo_mid3 = 5
    specificInfo_end = ']'
    url = url_front + str(url_mid)
    driver.get(url)

    wait_info = '/html/body/div[4]/div[1]/div[1]/div[3]/div[2]/div/div/div[2]/table/tbody/tr[1]/td[2]/a[1]/span'
    while True:
        try:
            money_info = money_front + str(money_mid) + money_end
            moneyday_info = moneyday_front + str(money_mid) + moneyday_end

            money = driver.find_element_by_xpath(money_info).text
            moneyday = driver.find_element_by_xpath(moneyday_info).text
            lines = []
            if money_mid == 10:
                txt3 = driver.find_element_by_xpath('sdf').text

            driver.find_element_by_xpath(money_info).click()
            WebDriverWait(driver, delay).until(
                expected_conditions.visibility_of_element_located(
                    (By.XPATH, loading_check)
                )
            )
            while True:
                try:
                    anw = specificInfo_front + specificInfo_front_1 + str(specificInfo_mid) + specificInfo_end
                    txt = driver.find_element_by_xpath(anw).text
                    lines.append(txt)
                    specificInfo_mid += 1
                except:
                    try:
                        anw2 = specificInfo_front + specificInfo_front_2 + str(specificInfo_mid1) + specificInfo_end
                        txt2 = driver.find_element_by_xpath(anw2).text
                        lines.append(txt2)
                        specificInfo_mid1 += 1
                    except:
                        try:
                            anw3 =  specificInfo_front1 + specificInfo_front_1 + str(specificInfo_mid2) + specificInfo_end
                            txt3 = driver.find_element_by_xpath(anw3).text
                            if specificInfo_mid2 == 5:
                                txt3 = driver.find_element_by_xpath('sdf').text
                            lines.append(txt3)
                            specificInfo_mid2 += 1

                        except:
                            try:
                                anw4 = specificInfo_front1 + specificInfo_front_1 + str(specificInfo_mid3) + specificInfo_end
                                txt4 = driver.find_element_by_xpath(anw4).text
                                lines.append(txt4)
                                specificInfo_mid3 += 1
                            except:


                                data = {'날짜': moneyday, '제목': money, '내용': lines}
                                db.MoneyNet_Specific2.insert_one(data)
                                print(lines)
                                print(money +' 날짜' + moneyday)



                                specificInfo_mid = 1
                                specificInfo_mid1 = 1
                                specificInfo_mid2 = 1
                                specificInfo_mid3 = 5
                                money_mid += 1
                                driver.back()
                                WebDriverWait(driver, delay).until(
                                    expected_conditions.visibility_of_element_located(
                                        (By.XPATH, wait_info)
                                    )
                                )
                                break;


            if int(url_mid) > 4214:
                print('끝')
                break;
        except:
            money_mid = 5
            url_mid += 1
            url = url_front + str(url_mid)
            driver.get(url)
            WebDriverWait(driver, delay).until(
                expected_conditions.visibility_of_element_located(
                    (By.XPATH, wait_info)
                )
            )

def To_CSV_Coinpan():
    list1 = list(db.MoneyNet_Specific2.find({},{'_id':0}))
    list123 = []
    check = []
    for k in list1:
        date = k['날짜']
        title = k['제목']
        specific = ''
        for t in k['내용']:
            if t != '':
                specific += t
        if k['제목'] not in check:
            list123.append([date, title, specific])
        check.append(k['제목'])
    column = ['날짜','제목','내용']

    df = pd.DataFrame(list123,columns=column)

    df.to_csv('User_data2.csv', index=False, encoding='utf-8-sig')




To_CSV_Coinpan()
