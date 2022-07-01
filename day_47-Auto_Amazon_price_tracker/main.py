import requests
from bs4 import BeautifulSoup
import smtplib
URL="https://www.amazon.com/Instant-Pot-Pressure-Steamer-Sterilizer/dp/B08PPZWNCV/ref=dp_fod_2?pd_rd_i=B08PPZWNCV&th=1"
EMAIL="vlahos89@gmail.com"
PASSWORD="Efthimios123!"
BUY_PRICE = 200


#request data/website from amazon website with additional headers
response=requests.get(URL,headers={"Accept-Language": "en-US,en;q=0.9", "User-Agent": "Mozilla/5.0 "
    "(Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"})
#covert website into text
amazon_web=response.text
#use beautiful soup to analyze HTML website
soup= BeautifulSoup(amazon_web,"html.parser")
#finding price
price_text = soup.find(name="span", class_="a-offscreen").getText()
price_wo_currency=price_text.split("$")[1]
float_price=float(price_wo_currency)
print(float_price)

title = soup.find(name="span", class_="a-offscreen").getText().strip()
print(title)


if float_price < BUY_PRICE:
    message = f"{title} is now {float_price}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login(EMAIL,PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}"
        )


