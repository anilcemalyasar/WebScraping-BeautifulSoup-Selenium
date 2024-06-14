from bs4 import BeautifulSoup

html = """
        <!DOCTYPE html><html><head><title>Example HTML</title></head><body><h1>Hello, World!</h1><p>A simple HTML page for testing web scraping with BeautifulSoup.</p>
                <a class='link' href='www.miuul.com' target='blank' aria-label='Miuul (Opens Miuul Page)'>Click</a>
                <li>Outsider</li>
                <ul>
                    <li class='list-item'>Item 1</li>
                    <li class='list-item'>Item 2</li>
                </ul>
            </body>
            </html>

"""

soup = BeautifulSoup(html, "html.parser")

# To find a element with class name 'link'
print(soup.find('a', attrs={"class": "link", "target": "blank"}))

for li_element in soup.find_all("li"):
    print(li_element, type(li_element))

li_elements = soup.find_all("li", attrs={"class": "list-item"})
print(li_elements)



