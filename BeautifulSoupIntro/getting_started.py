from bs4 import BeautifulSoup


html = """
        <!DOCTYPE html><html><head><title>Example HTML</title></head><body><h1>Hello, World!</h1><p>A simple HTML page for testing web scraping with BeautifulSoup.</p>
                <a class='link' href='www.miuul.com' target='blank' aria-label='Miuul (Opens Miuul Page)'>Click</a>
                <li>Outsider</li>
                <ul>
                    <li>Item 1</li>
                    <li>Item 2</li>
                </ul>
            </body>
            </html>

"""

soup = BeautifulSoup(html, "html.parser")

print(soup.title.text)
# print(soup.prettify())
# print(soup.ul.li) <li>Item 1</li>
# print(type(soup.ul)) <class 'bs4.element.Tag'>