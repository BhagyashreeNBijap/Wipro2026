from bs4 import BeautifulSoup

html = """
<table>
<tr>
<td>Ravi</td>
<td>30</td>
<td>Fever</td>
<td>Dr. Sharma</td>
</tr>
</table>
"""

soup = BeautifulSoup(html, "lxml")
rows = soup.find_all("tr")

for row in rows:
    cols = row.find_all("td")
    print(
        "Name:", cols[0].text,
        "Age:", cols[1].text,
        "Disease:", cols[2].text,
        "Doctor:", cols[3].text
    )
