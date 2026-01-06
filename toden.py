import requests
import itertools
import json
import selenium
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

def getcookies():
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.binary_location = "/usr/bin/firefox"
    service = Service(executable_path ="/home/opc/bot_py/.venv/WebDriverManager/gecko/v0.35.0/geckodriver-v0.35.0-linux64/geckodriver")
    driver = webdriver.Firefox(options=options,service=service)
    driver.get("https://florr.io/")
    driver.implicitly_wait(2)
    driver.page_source
    cookies = []
    while True:
        a = len(cookies)
        cookies = driver.get_cookies()
        if len(cookies) >= 10:
            break
        print(len(cookies))
        #cookie_names = [cookie['name'] for cookie in cookies]
        driver.implicitly_wait(1)
    cookies = {cookie['name']:cookie['value'] for cookie in cookies}
    driver.close()
    return cookies

cookies = getcookies()
# cookies = {
#     '_abck': '6882C82CCC04D9F04331099A6AD797FD~0~YAAQCepCF9pnYb6VAQAAZZlPyQ04FQpnqiwmJeO/tVR3nI8/unqEp20PbpYu1KbwLVFgDhFYbMgw5uncbNO8quNXIKRGzXJrsfxrt6+THpsW8JXMiFRgp7lu0FR7UgFtgB0V+68dukmz3RFcS0WfN1mijxUPrKp2yz3/PUNry4TpRAwR68tjFPe+XAOFRDmqXanF/KKyvyBVueRU7/jPevO66xWuYurmtUKPW1GL7pW8V8MXMyXYBSXMoKkja42Kx7GkTc8VugicOrKeriN5lg47ohFRd6HFKe7HAu4O/BuIUtGGyujPM46iNNfKL78tquAbTYH7Z678FMb0Aa6ckOx1Ydyf9fgj6Lik/R4IaSmR0keYi8RSbGm+V9re/e5SCkr6zcKeA3Od/2chYk0fl5TtY8KDqjclngqBt7LDB8WQJNKdlxPxdPHg7dO/cQBbll048rPpRs70zyXhMUgomQR9mCHZGo4I0s7w0zsLZjfe3UDo6WugtIgwJSeXhDpNSf8VUacE/V6jFxfDqlcDtIr5o8CMnBnl2Mh5i8cdE+vB1Lgr+uKrg3Pbf1IkHqhi4gNU4VlPPhnQZmBD4ZmSCEkLdw6wb4H+dBSLyS2A0UrRBK2rH5qAWPVhQIX9vcGDiljiHkxyIsVlyFJUL2cGb15mzAZI8VZ4skzc5zszDei99Yrr~-1~-1~-1',
#     'bm_sv': 'EB1D4E961C86D731EA912455BFBC0CB5~YAAQCepCF85lYb6VAQAA8IdPyRvstlQTbSH7Uc1kZJafHoRRVe1s4wetDY8+xFPq2b5SJ1330vL4DuOQ3QcmhcWaUDmlw3WxA++LiszDc/oKIA0tILAmdSpIakOowdn0RM0VGMpls6+tZZQRk/5MZl1rWPFjK0PKB8woBub7sybfDOsxqGMZjFOCGq6iDkkOzyNFUorLjcxxXiJc8QTWr+XLaDr+FWKgrWWeKbvFg7/BTl5SQTopzoMIWDeDoGSWqIbcj6E2~1',
#     'bm_sz': '43C1ED35CCEBDA22C8F75ACECDD0614A~YAAQCepCF89lYb6VAQAA8IdPyRvA6F5E1SM+kdR9Tt7pRi9BrvxBgWhyPcgVqQtTYjNel0Cpla20NYDiGr/EVpo7cWiteoQSnEWq6XmR/n3at8jD8AkAD0Yfpi7vZESYSuhH7IQx7b1dhUGQtq0KCSnjnZBWqLlOhZ/JS2Xd473FioLNLabJ6Qh6LtEhSG65CAJ1rfWSyY8Zo6mzhYuGrvC628LoKKY+AsyC65LjdeWe/BR783f4Y/RLHx2F0ws6QuOVpjSi17qyPQ3JeKWo5gkZZHQ9ZJ6w4x5R6TvKaPvo3aMl3kOCoZBotgMYj5f4pQEWclg+5OImra7Lj29Y1qgW4IAxVfAQZrr3ZQ0PtruECkPvzHOq9/sB8Q9ReYU3kYV0VvDXdupT1DvYuX+foRezdXQgjuRYjR8MiFPqUXHAPJXKwJ/UiPTtL0DLMKcUtHDTQfQLzjOsruV+uZkURzAN8G7xUfq0/3m2X2wT2zrurjmYVRUzVue+qbrYcis25pF9jCU6aqFVfrdcmXUsnSEdDdxSJospH3B7vqzLuR6EOWIXbNZK+MRqUP4t9nWrDpK4yUyz1tcLcgYiMJwxQTIpwA==~4535873~3294790',
#     'ak_bmsc': '8A7F65358EEB7EA459F25A57FAD0A8A6~000000000000000000000000000000~YAAQjXfZF3Rt2MiVAQAAsSpLyRuVz+8rpW8UxcTzhjG+Fp4AC8sQ/i94h4hAXoPifVPmNuHvUrNv9FEeSNJSaIJ6M8pbYgjbhOZnohCdldyf2Uv56o7TvCh10+IQcWkptG3+1joSTYlwZX84LCxsYmwNpjYqXDA4ph/wt6iSLfC3BgM7Ln9HQ3GXO1VdGu2Jj+25BFwXrm1N+qoB4x0BAOdPV18IOtWgrzq+WfRlnRW+i4o8gLQ4mdr7BW9cKGjh+Wm2c+uPryzYm/3czIbznKj+rKZQIbhfz9yrBZtWyscCGB5cdIZOSyVj3QIQKed7b2snvLhulwW1u3EwZ0lJTVpZk3RjdQv8YDj1QkRZki+dKdyl62URKYMXvs92NAioitnjqVSF8Anh0CURuWc=',
#     'akacd_ost-prod-lb-2': '1742882101~rv=25~id=56b59aa6027436f585726c40fb933b0e',
#     'dtCookie': 'v_4_srv_12_sn_P4PNECEJR250F7OG4G3I3VVC88A6UB8I_perc_28543_ol_0_mul_3_app-3A200c4c21b0fea6c6_1',
#     'rxVisitor': '17428364204835GLLSCKRGKSK81DFLELI193RGPTOU60B',
#     'dtPC': '12$436426786_951h-vMVBLRFHBRNWCBMUFRGAKIDJWHTCWVRQA-0e0',
#     'rxvt': '1742838236376|1742836420623',
#     'forterToken': '43846b7e5ab64da5806facf12fb3b5d7_1742836428139__UDF43-mnf-a4_23ck_',
#     'BVBRANDID': '8d21ed43-4042-44d4-8f46-05ea13367bd8',
#     'atgRecSessionId': 'UJzJJU99KfNejOVIN5LTDCuHf5rqMDnC9egQ2Ii5XODnQ4tzApap!-1212610061!-700260313',
#     'atgRecVisitorId': '10ED0py6k_Rx9I3WwUfFBUBBCWGaH9HZbIT415NWWDurJ_Q9522',
#     'dtSa': '-',
#     'selectedStoreId': '2869',
#     'xdVisitorId': '10ED0py6k_Rx9I3WwUfFBUBBCWGaH9HZbIT415NWWDurJ_Q9522',
#     'lat': '33.848714',
#     'lng': '-117.888393',
#     'AKA_A2': 'A',
#     'ActiveID': 'QFAB-O8W1-SM1K-Y9J9-N6K3-ZJZS-LVHD-WQHZ',
#     'JSESSIONID': '6A5C879120EE143C0FC10D630D013B22-n1',
#     'OSESSIONID': '"fa9511bc172d7213"',
#     'cust_id': '"LlM5e16fxHdPYvVnz4h7wIZ0QA2P5wCtTQ3XIXDm8UQ="',
#     'ga_session': 'abd51e46-a4ed-4319-827b-13298435755f',
# }
print("got cookies")

# cookies = {
#     'AKA_A2': 'A',
#     '_abck': '6882C82CCC04D9F04331099A6AD797FD~-1~YAAQFOpCF0QjVqyVAQAAG86sxg1j2ffMmy+KraCAsZmFoMPhJ8Rnj8MG2eV/EFv0sZMo9F3+iGkytIJGf8TEby3U56amcP6pCsKROUB8YS1tVrt8kmkdozy6qaFlZymtZU6mI74JJ+Tc5eYcrREenTt8BnyLrOvf4a94o4rs4oX9ZaT3yWURmT/xneR87PwjF75ROqzxifVCFB9Lxr2JP6g2ca0pCXKAcVPx5vo81CuU7QnHuUqmKcAbntitSeaQI2/boOt/krHUHiNiYqQguhN+kOX0/POal9wTQpSEVSSu2b5oy26VLcILwSY850dnI3QCckl6QzqnJ3TCZW/kKj/n8BCspt2gsONAxDjK2r2t3uOqhAvxEkhXQP0v9loXhF8u7Yb4OD1gxxoWflDfR4nqA/HR+vavReShIahpA8T+S3o=~-1~-1~-1',
#     'ak_bmsc': '15AE027FEE25DEB5689096A6107F793B~000000000000000000000000000000~YAAQFOpCF0UjVqyVAQAAG86sxhvMCKnqfkpqYS+dCUEvK04obEWVNa8wcBPvojOG3BnJacIN4WZ9YTF+PeLoupKdBZf5y1HJNTyY+xUCDMje3ROZDmMfj30Piha1BfUGizefvhJ19p7RJjtQU/wWXcwZg7wWZ2YSc6SFoZBujXE78Lac+GUDsWRKe9AfjF9X435V/+F+o9+fpVJTwA1IxPghTq2v0qqF3PWCa05pvbnOFbBgjF+QWWPUnRfIEd5piq0Go+5KBQ2f/QVxzQzH7vBUEY1PKlkmw96fCYPM1QT70vNK3epca4P1wNs8QbjNvvx3BfHFqKs7TsrHwLe109p8Ph8nzcBZ3RfnLPBuh1H8MhC7Qf+S02VeZJeUxL+Qcv83k4J1Zc/oiVYfZHs=',
#     'bm_sz': '2B2192AA374F037298984271A1252CC7~YAAQFOpCF0YjVqyVAQAAG86sxhv9nfbDmZzLq22BeLAiqsooFad+zwplDsvKspHEzhBBUL8crBWGsa6KDMEUmsX9NxUo5VtNHiMD4RxtTEpXoFZ874npKfDeALh2nsMACY2gq5Vk+VwG+QgG2ngicthnKWo2dSlUJja3is9RmJuoOIFzAx6q2o95+jL+V6wKw5Ok1JDVBTVTr8ScKs1GGK8H2ZoambjKNkQKeKs+QjrHMb6ENxBH3qgR8fAkTErscOc2N/7Obiu7BgDIWw10CABBb4EPkvRad16cglcNRHC06a3xqauNBGcmOMt/T4k9LlwzTgEvhe9ws7CVH7USfAmTQC4JXWSuHCZa/DEr54e5Ve8SM+7+u3hzRWVIY/kVzWKJBdRGdW6LQ7f6uBCME0zScw==~3553072~3684663',
#     'ActiveID': 'K20T-FHGG-28KN-UJ8F-QNAB-C3HP-DE2C-R799',
#     'JSESSIONID': '81D36600367C37452F14FBCED4550732-n1',
#     'OSESSIONID': '"58d340c9e777b0b1"',
#     'akacd_ost-prod-lb-2': '1742881248~rv=63~id=3977aa9ac92508bf59875f629bc75c37',
#     'cust_id': '"7yp2U+Tr7Y/7QynV3IeHD3scLhv3IgHyPTejLlqSLYk="',
#     'ga_session': '08967331-31cb-46b9-ba04-1ea5f4ccea76',
# }

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Sec-Fetch-Site': 'none',
    # 'Cookie': 'AKA_A2=A; _abck=6882C82CCC04D9F04331099A6AD797FD~-1~YAAQFOpCF0QjVqyVAQAAG86sxg1j2ffMmy+KraCAsZmFoMPhJ8Rnj8MG2eV/EFv0sZMo9F3+iGkytIJGf8TEby3U56amcP6pCsKROUB8YS1tVrt8kmkdozy6qaFlZymtZU6mI74JJ+Tc5eYcrREenTt8BnyLrOvf4a94o4rs4oX9ZaT3yWURmT/xneR87PwjF75ROqzxifVCFB9Lxr2JP6g2ca0pCXKAcVPx5vo81CuU7QnHuUqmKcAbntitSeaQI2/boOt/krHUHiNiYqQguhN+kOX0/POal9wTQpSEVSSu2b5oy26VLcILwSY850dnI3QCckl6QzqnJ3TCZW/kKj/n8BCspt2gsONAxDjK2r2t3uOqhAvxEkhXQP0v9loXhF8u7Yb4OD1gxxoWflDfR4nqA/HR+vavReShIahpA8T+S3o=~-1~-1~-1; ak_bmsc=15AE027FEE25DEB5689096A6107F793B~000000000000000000000000000000~YAAQFOpCF0UjVqyVAQAAG86sxhvMCKnqfkpqYS+dCUEvK04obEWVNa8wcBPvojOG3BnJacIN4WZ9YTF+PeLoupKdBZf5y1HJNTyY+xUCDMje3ROZDmMfj30Piha1BfUGizefvhJ19p7RJjtQU/wWXcwZg7wWZ2YSc6SFoZBujXE78Lac+GUDsWRKe9AfjF9X435V/+F+o9+fpVJTwA1IxPghTq2v0qqF3PWCa05pvbnOFbBgjF+QWWPUnRfIEd5piq0Go+5KBQ2f/QVxzQzH7vBUEY1PKlkmw96fCYPM1QT70vNK3epca4P1wNs8QbjNvvx3BfHFqKs7TsrHwLe109p8Ph8nzcBZ3RfnLPBuh1H8MhC7Qf+S02VeZJeUxL+Qcv83k4J1Zc/oiVYfZHs=; bm_sz=2B2192AA374F037298984271A1252CC7~YAAQFOpCF0YjVqyVAQAAG86sxhv9nfbDmZzLq22BeLAiqsooFad+zwplDsvKspHEzhBBUL8crBWGsa6KDMEUmsX9NxUo5VtNHiMD4RxtTEpXoFZ874npKfDeALh2nsMACY2gq5Vk+VwG+QgG2ngicthnKWo2dSlUJja3is9RmJuoOIFzAx6q2o95+jL+V6wKw5Ok1JDVBTVTr8ScKs1GGK8H2ZoambjKNkQKeKs+QjrHMb6ENxBH3qgR8fAkTErscOc2N/7Obiu7BgDIWw10CABBb4EPkvRad16cglcNRHC06a3xqauNBGcmOMt/T4k9LlwzTgEvhe9ws7CVH7USfAmTQC4JXWSuHCZa/DEr54e5Ve8SM+7+u3hzRWVIY/kVzWKJBdRGdW6LQ7f6uBCME0zScw==~3553072~3684663; ActiveID=QFAB-O8W1-SM1K-Y9J9-N6K3-ZJZS-LVHD-WQHZ; JSESSIONID=6A5C879120EE143C0FC10D630D013B22-n1; OSESSIONID="fa9511bc172d7213"; akacd_ost-prod-lb-2=1742838168~rv=91~id=b42831255cea18c3a151c4daa848770b; cust_id="LlM5e16fxHdPYvVnz4h7wIZ0QA2P5wCtTQ3XIXDm8UQ="; ga_session=abd51e46-a4ed-4319-827b-13298435755f',
    'Sec-Fetch-Mode': 'navigate',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.3 Safari/605.1.15',
    'Accept-Language': 'en-US,en;q=0.9',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Sec-Fetch-Dest': 'document',
    'Priority': 'u=0, i',
}
letters = "abcdefghijklmnopqrstuvwxyz"
digits = "0123456789"
# target_plate = "7cnf470"
# target_plate = "7cnx997"
# target_letter = target_plate[3] 
# target_digits = target_plate[4:] 
# resume_flag = False

for a, c, d in itertools.product(letters, digits, digits):
    plate = "7" + a + "sa" + "7" + c + d
    if str(a) not in list(letters[letters.index("a"):])) or ((int(str("7")+str(c)+str(d)) <= 0) and str(a) == letters[letters.index("a"):][0]) :
        # print(plate)
        continue
    else:
        url = f'https://www.oreillyauto.com/vehicle/plate/{plate}/CA/false'
        response = requests.get(url, cookies=cookies, headers=headers)
        with open("plates.txt", "a") as h:
            try:
                if json.loads(response.content)['plates'][0]['make'] == "BMW":
                    h.write(plate + "," + str(response.content) + "\n")
                    print(plate + "," + str(response.content) + "\n")
                else:
                    print(plate)
            except Exception as e:
                print(e)
                print(plate + " not found")

for e,f,g,h in itertools.product(letters, digits, digits, digits):
    plate = "7ci" + e + f + g + h

    url = f'https://www.oreillyauto.com/vehicle/plate/{plate}/CA/false'
    response = requests.get(url, cookies=cookies, headers=headers)
    with open("plates.txt", "a") as h:
        try:
            if json.loads(response.content)['plates'][0]['make'] == "BMW":
                h.write(plate + "," + str(response.content) + "\n")
                print(plate + "," + str(response.content) + "\n")
            else:
                print(plate)
        except Exception as e:
                print(e)
                print(plate + " not found")