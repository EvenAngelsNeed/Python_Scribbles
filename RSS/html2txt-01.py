import html2text

html_content = """ <p>some text in html </p> """
text_content = html2text.html2text(html_content)

print("HTML Content:")
print(html_content)

print("\nText Content:")
print(text_content) #[0:20])

input()