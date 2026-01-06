import asyncio
import httpx
from json import JSONDecodeError
from typing import Generator

pattern = "B??????"
modelMatches = ["750li"]
stateCode = "WA"

rateLimitPerSecond = 15
numWorkers = 8

digits = "0123456789"
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
maxTries = 5
rateLimitTimeout = 900

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Sec-Fetch-Site': 'none',
    # 'Cookie': 'forterToken=6c21e8274de041a5966a3fa9fc7c4947_1742933435252__UDF43-mnf-a4_23ck_; __wid=417872132; atgRecSessionId=RAPO7aRwDEdB8f2iCSOG5WjF2tiTS6oWfu8MyGnnap78pXsVCt7U!183772526!787272387; atgRecVisitorId=10D7f9mAHGZTg3m6Ih1c7gl9vNmLzZkvlKnYij2ue3t4oMY6C85; bm_sv=0F9E2D687712D055385C7CB7AFAAA8EB~YAAQlHfZF+3QNsWVAQAAeaPtzhsQtsVuPQGpl2DI0gWNkio3L+cZSLJ8d3aEVBW6IFhi25dp7ASUABx5qDndDo+guDjlUs1TiKIoxMEVILFLQfhX9a6uOJd3LTK1I3dcp2jabH798Wg/2Fe6LEmAPGaUMY5JtcwWRe2ioZv17zQCkMTFE7oFMj3FVI5vqcIcKJB8AiNMyDbjd/5CnrZ+xD1FYGR/xDZoI9pJ8dlghZNnBal1MHwjgxV7DRBq3wKRU2Ggqwo=~1; xdVisitorId=10D7f9mAHGZTg3m6Ih1c7gl9vNmLzZkvlKnYij2ue3t4oMY6C85; bm_sz=CB1FE3071DEF3313AF627820D573E36D~YAAQlHfZFxjQNsWVAQAA7KDtzhut5WpR1w8oNtHHJRPOWFmRI00U1Ou85PkecCkZGJb9E56HpiPhbZ+4nqORgDiN8NshzlB/TKnBsJpIQ4EYpqU8df0DffJgxdufvILfkTASoYVsa2AgLr4/eoyhCmVlIRLqpXylq5oIbGTtJsnT4J7TbCKz7+AMiS6SpMR5qelwCDSlBOHpezA24AwYwV22Sfc/twWKd3Zy1Smx3mkig0wU8wuMPNr6gfeRFXR1d12Apnsq6Gzoc50z3OsiDK4MLrCPyYMIHYeOHq1nOi3ey3R42Nz/NFDfugCZ9Y8C/f6x5FxqjzUNj29LXoZ85DG9CvR67SdNngJEIP8bJcV229RGJ0nxrWEWP0epsb02q5QcdPk1juybQUBhfmrohZwJd6QgBZX1FBB+slcOuA/Rwb5oPTxz8FQgACJ6xOLhQ6VwwI/FIdcWWiUiHlScnUdwMPW0RjZu23jpehHM1XHVfiR57AiGbYMCqH1QU1fEpcsdBi1V8QuFxQFysy7b5BYDkumHfDqwyjVEbGyocBKfkwbeyL1tzJVk6Q==~3553584~3553350; ak_bmsc=9049F9DA2528F980443B1F4A4A7A4959~000000000000000000000000000000~YAAQFOpCF6GC8K2VAQAAG2bUzhuQ77c/39AKvMT6m0PmNsAJCN6/krx+qC7eGvk4YfWxQWh1d5CSsvZvIHo8UePe0K30iLaVcTydcmunR4t9SwSDEuLhYt9t9JfdcLqZHCevvw89EHlkJvV7FUDqIJCLkAd5Ji1Ah3BZQlZxa9QuKVqVA3RW4gn5ts27AxFZsBmC/iOhQDGZHiJDKLHCre0HRQXU2XlF1OVdjDy8nglVeJPA13ebv1/QeG8a2z4b/N8HkFPUNw8syprPS6RzcvyoE6mDfHWYpxpwAlUta6eWJDEnuiV6432CcHYicoKEytbTruN91PSrvOqVESZkUw+QN6kGlqZ1+JMh7ADDo08+FeNJCiP3ZUitMJt7GlUXhbz8ny7xwqtlaw9WNuEQ0TMSG/k0a33OrNn6/mD71FaobjArrdrkIGl7Cu7PUYV4QqSLYVwDMxnv/nv0D5ny; AKA_A2=A; _abck=9BE080A076A30367AED8BE59D75B18AB~0~YAAQFOpCF9iRyq2VAQAANJNDzg20NNoCDx5jDDB1UgkIGvXFLXfL7sNb389s+rB2iZ7bpvCw3hfuwhNaHhvugmzqRrXR6YAWDzzFZ6KefAxeL8saBrw0sT7u3Z5xfA+JTddaB48+OK0UGqz6Cm7qL2p1+BIJMwCfMMy9JVt69QhxjEFPr3jVVXaMtD0l9q2BtJvMmb5HPw4orpkoOtqyhXow0GGf0MQyObiobEbMN0LLj8dyeP9RnvRS+3AeA0JQr/J/pI4+RtcTErj56q5jWy869hoEnu42qYAF/izFOdy6UyrSMxY6ypoR5ddfbveGiv8Jqe6GUeUHHU4YauOnY4zfdmAl/TaSsSOEh5zMY/h+wSeAWTukEpdGsXduMiaqKvGR5ltL3OswYSTXrfluSezMa+w3D8deBTIBWsTlUzRVpiPpuuH+weMagQTrIHaE2jRngwHrk7hVFHEwfarRrZmc1ZZIgYDMXQ3QVfTO3HuLcAKeyTPrtijV32fEHTcLAtQ5kB9TMqmQR+r/tfJClNxj7vtEst/ztsSF0PMyzo9e4QWftmK8pmjyVQhKoA9W5/q4SigHQiSp~-1~-1~-1; dtCookie=v_4_srv_10_sn_IQJJTNIBNUI296FVD2BDML3R3F400A6O_perc_31217_ol_1_app-3A200c4c21b0fea6c6_0; selectedStoreId=3067; lat=33.837638; lng=-117.887428; ActiveID=VH3E-5N57-WNFC-POZ5-JXPB-NI3E-G4AI-W7F2; JSESSIONID=2491B1B36E99AD0B5CD496E6FB203AEE-n1; OSESSIONID="fb7aed78876a8db8"; akacd_ost-prod-lb-2=1742962432~rv=45~id=726ff508471c012c1fc3b4ecf77516de; cust_id="4KHxC02h7Lg2eO4ztGlkPM8fi5dC2UkpV539gbm/Qgk="; ga_session=8841ccf7-6046-4d0f-b85d-2e12ba16652f',
    'Sec-Fetch-Mode': 'navigate',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.3 Safari/605.1.15',
    'Accept-Language': 'en-US,en;q=0.9',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Sec-Fetch-Dest': 'document',
    'Priority': 'u=0, i',
}

def GenerateCALicensePlate(plateFormat: str) -> Generator[str, None, None]:
    """
    Generator function that creates California license plates with the given plate format.
    :param plateFormat: The format of the plate to iterate for. This is a seven character code where ? represents an unknown value.
    :return: Yields a California license plate in order.
    """
    # California license plate format:
    # DLLLDDD
    # L = letter
    # D = digit
    plateFormatList = list(plateFormat)

    possibleFirstValues = digits if plateFormatList[0] == "?" else plateFormatList[0]
    possibleSecondValues = letters if plateFormatList[1] == "?" else plateFormatList[1]
    possibleThirdValues = letters if plateFormatList[2] == "?" else plateFormatList[2]
    possibleFourthValues = letters if plateFormatList[3] == "?" else plateFormatList[3]
    possibleFifthValues = digits if plateFormatList[4] == "?" else plateFormatList[4]
    possibleSixthValues = digits if plateFormatList[5] == "?" else plateFormatList[5]
    possibleSeventhValues = digits if plateFormatList[6] == "?" else plateFormatList[6]

    for first in possibleFirstValues:
        for second in possibleSecondValues:
            for third in possibleThirdValues:
                for fourth in possibleFourthValues:
                    for fifth in possibleFifthValues:
                        for sixth in possibleSixthValues:
                            for seventh in possibleSeventhValues:
                                yield f"{first}{second}{third}{fourth}{fifth}{sixth}{seventh}"

def GenerateWALicensePlate(plateFormat: str) -> Generator[str, None, None]:
    """
    Generator function that creates Washington license plates with the given plate format.
    :param plateFormat: The format of the plate to iterate for. This is a seven character code where ? represents an unknown value.
    :return: Yields a Washington license plate in order.
    """
    # Washington license plate format:
    # LLLDDDD
    # L = letter
    # D = digit
    plateFormatList = list(plateFormat)

    possibleFirstValues = letters if plateFormatList[0] == "?" else plateFormatList[0]
    possibleSecondValues = letters if plateFormatList[1] == "?" else plateFormatList[1]
    possibleThirdValues = letters if plateFormatList[2] == "?" else plateFormatList[2]
    possibleFourthValues = digits if plateFormatList[3] == "?" else plateFormatList[3]
    possibleFifthValues = digits if plateFormatList[4] == "?" else plateFormatList[4]
    possibleSixthValues = digits if plateFormatList[5] == "?" else plateFormatList[5]
    possibleSeventhValues = digits if plateFormatList[6] == "?" else plateFormatList[6]

    for first in possibleFirstValues:
        for second in possibleSecondValues:
            for third in possibleThirdValues:
                for fourth in possibleFourthValues:
                    for fifth in possibleFifthValues:
                        for sixth in possibleSixthValues:
                            for seventh in possibleSeventhValues:
                                yield f"{first}{second}{third}{fourth}{fifth}{sixth}{seventh}"

async def FetchVehicleData(printLock: asyncio.Lock, client: httpx.AsyncClient, licensePlate: str) -> tuple[str, list[dict]]:
    """
    Fetches the vehicle data from the API endpoint.
    :param printLock: The asyncio lock to use to protect print statements from getting garbled.
    :param client: The httpx client session to fetch with. httpx is used instead of asyncio because the API uses HTTP/2.
    :param licensePlate: The license plate to fetch vehicle data for.
    :return: Yields a list of dictionaries with the vehicle data. The list is empty if there were no matches returned by the API.
    """
    endpoint = f"https://www.oreillyauto.com/vehicle/plate/{licensePlate}/{stateCode}/false"

    tries = 0
    while tries < maxTries:
        try:
            tries = tries + 1
            response = await client.get(endpoint)
            plateMatches = response.json()['plates']
        except httpx.RemoteProtocolError:
            async with printLock:
                print(f"INFO: Session invalidated. Emptying cookies and retrying...\r", end="")
            client.cookies.clear()
        except JSONDecodeError:
            if "Access Denied" in response.text:
                async with printLock:
                    print(f"ERROR: We are currently ratelimited. Retrying after {rateLimitTimeout} seconds\r", end="")
                await asyncio.sleep(rateLimitTimeout)
            else:
                async with printLock:
                    print(f"ERROR: Could not decode data into a valid dictionary. Retrying...\r", end="")
        except KeyError:
            async with printLock:
                print(f"ERROR: Data received in an invalid format. Retrying...\r", end="")
        except:
            async with printLock:
                print(f"ERROR: Could not fetch or parse data for license plate: {licensePlate}")
            plateMatches = []
            break
        else:
            async with printLock:
                print(f"INFO: Successfully fetched data for license plate: {licensePlate} ({len(plateMatches)} results)\r", end="")
            break
    else:
        print(f"ERROR: Ran out of trials for license plate: {licensePlate}. Skipping...")
        plateMatches = []

    return licensePlate, plateMatches

async def worker(printLock: asyncio.Lock, queue: asyncio.Queue, client: httpx.AsyncClient) -> None:
    """
    Worker task in the queue that continuously pulls license plates and fetches their API data.
    :param printLock: The asyncio lock to use to protect print statements from getting garbled.
    :param queue: The asyncio queue to pull from.
    :param client: The httpx client session to fetch with. httpx is used instead of asyncio because the API uses HTTP/2.
    :return: This function does not return anything.
    """
    while True:
        thisLicensePlate = await queue.get()
        if thisLicensePlate is None:
            break

        thisLicensePlate, plateMatches = await FetchVehicleData(printLock, client, thisLicensePlate)
        for plateMatch in plateMatches:
            if plateMatch['make'] == "BMW" and plateMatch['model'].lower() in modelMatches:
                carInformation = f"{plateMatch['year']} {plateMatch['make']} {plateMatch['model']} ({plateMatch['subModel'][0]['value']}) [Engine: {plateMatch['engine'][0]['value']}]"
                async with printLock:
                    print(f"MATCH: Found match with license plate: {thisLicensePlate}: {carInformation}")

        queue.task_done()
        await asyncio.sleep(1/(rateLimitPerSecond * numWorkers))

async def main():
    printLock = asyncio.Lock()
    queue = asyncio.Queue()
    licensePlateGenerator = GenerateWALicensePlate(pattern)
    print(f"INFO: Initialized generator! Using pattern: {pattern} in state: {stateCode}")

    async with httpx.AsyncClient(http2=True, headers=headers, timeout=None) as client:
        tasks = []
        for i in range(numWorkers):
            tasks.append(asyncio.create_task(worker(printLock, queue, client)))

        try:
            while True:
                await queue.put(next(licensePlateGenerator))
        except StopIteration:
            print("INFO: All license plates fed into queue\n")

        await queue.join()

        for i in range(numWorkers):
            await queue.put(None)
        await asyncio.gather(*tasks)
        print("\033[2K\n")
        print("INFO: Done! Exiting...")

asyncio.run(main())