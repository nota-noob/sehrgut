import requests
import itertools
import json

cookies = {
    'AKA_A2': 'A',
    '_abck': '6882C82CCC04D9F04331099A6AD797FD~-1~YAAQFOpCF0QjVqyVAQAAG86sxg1j2ffMmy+KraCAsZmFoMPhJ8Rnj8MG2eV/EFv0sZMo9F3+iGkytIJGf8TEby3U56amcP6pCsKROUB8YS1tVrt8kmkdozy6qaFlZymtZU6mI74JJ+Tc5eYcrREenTt8BnyLrOvf4a94o4rs4oX9ZaT3yWURmT/xneR87PwjF75ROqzxifVCFB9Lxr2JP6g2ca0pCXKAcVPx5vo81CuU7QnHuUqmKcAbntitSeaQI2/boOt/krHUHiNiYqQguhN+kOX0/POal9wTQpSEVSSu2b5oy26VLcILwSY850dnI3QCckl6QzqnJ3TCZW/kKj/n8BCspt2gsONAxDjK2r2t3uOqhAvxEkhXQP0v9loXhF8u7Yb4OD1gxxoWflDfR4nqA/HR+vavReShIahpA8T+S3o=~-1~-1~-1',
    'ak_bmsc': '15AE027FEE25DEB5689096A6107F793B~000000000000000000000000000000~YAAQFOpCF0UjVqyVAQAAG86sxhvMCKnqfkpqYS+dCUEvK04obEWVNa8wcBPvojOG3BnJacIN4WZ9YTF+PeLoupKdBZf5y1HJNTyY+xUCDMje3ROZDmMfj30Piha1BfUGizefvhJ19p7RJjtQU/wWXcwZg7wWZ2YSc6SFoZBujXE78Lac+GUDsWRKe9AfjF9X435V/+F+o9+fpVJTwA1IxPghTq2v0qqF3PWCa05pvbnOFbBgjF+QWWPUnRfIEd5piq0Go+5KBQ2f/QVxzQzH7vBUEY1PKlkmw96fCYPM1QT70vNK3epca4P1wNs8QbjNvvx3BfHFqKs7TsrHwLe109p8Ph8nzcBZ3RfnLPBuh1H8MhC7Qf+S02VeZJeUxL+Qcv83k4J1Zc/oiVYfZHs=',
    'bm_sz': '2B2192AA374F037298984271A1252CC7~YAAQFOpCF0YjVqyVAQAAG86sxhv9nfbDmZzLq22BeLAiqsooFad+zwplDsvKspHEzhBBUL8crBWGsa6KDMEUmsX9NxUo5VtNHiMD4RxtTEpXoFZ874npKfDeALh2nsMACY2gq5Vk+VwG+QgG2ngicthnKWo2dSlUJja3is9RmJuoOIFzAx6q2o95+jL+V6wKw5Ok1JDVBTVTr8ScKs1GGK8H2ZoambjKNkQKeKs+QjrHMb6ENxBH3qgR8fAkTErscOc2N/7Obiu7BgDIWw10CABBb4EPkvRad16cglcNRHC06a3xqauNBGcmOMt/T4k9LlwzTgEvhe9ws7CVH7USfAmTQC4JXWSuHCZa/DEr54e5Ve8SM+7+u3hzRWVIY/kVzWKJBdRGdW6LQ7f6uBCME0zScw==~3553072~3684663',
    'ActiveID': 'QFAB-O8W1-SM1K-Y9J9-N6K3-ZJZS-LVHD-WQHZ',
    'JSESSIONID': '6A5C879120EE143C0FC10D630D013B22-n1',
    'OSESSIONID': '"fa9511bc172d7213"',
    'akacd_ost-prod-lb-2': '1742838168~rv=91~id=b42831255cea18c3a151c4daa848770b',
    'cust_id': '"LlM5e16fxHdPYvVnz4h7wIZ0QA2P5wCtTQ3XIXDm8UQ="',
    'ga_session': 'abd51e46-a4ed-4319-827b-13298435755f',
}

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
digits = "123456789"

for a, b, c, d in itertools.product(letters, digits, digits, digits):
    plate = "7ci" + a + b + c + d
    url = f'https://www.oreillyauto.com/vehicle/plate/{plate}/CA/false'
    response = requests.get(url, cookies=cookies, headers=headers)
    with open("plates2.txt", "a") as h:
        try:
            if json.loads(response.content)['plates'][0]['make'] == "BMW":
                h.write(plate + "," + str(response.content) + "\n")
                print(plate + "," + str(response.content) + "\n")
            else:
                print(plate)
        except:
            pass