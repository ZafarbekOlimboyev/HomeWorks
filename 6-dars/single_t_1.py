import requests
import time
def dowbload_html(url):
    html_cod = requests.get(url)
    return html_cod.text

def write_html(html_cod, html_name):
    with open(f"./single_t_1/{html_name}.html", "w") as h:
        h.write(html_cod)

if __name__ == "__main__":
    start_time = time.time_ns() // 1_000_000
    url = "https://multimediya.uz/multimediya/index.php?mavzu="
    for i in range(1,13):
        html_cod = dowbload_html(f"{url}{i}")
        write_html(html_cod,f"{i} - Maruza")
    end_time = time.time_ns() // 1_000_000
    print(end_time - start_time, "Millisekundda yuklab olindi.")
 # 20364 Millisekundda yuklab olindi.