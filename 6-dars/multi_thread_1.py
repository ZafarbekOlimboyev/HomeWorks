import requests
import time
import concurrent.futures

def download_html(url):
    html_code = requests.get(url)
    return html_code.text

def write_html(html_code, html_name):
    with open(f"./multi_t_2/{html_name}.html", "w") as h:
        h.write(html_code)

if __name__ == "__main__":
    start_time = time.time_ns() // 1_000_000
    url_base = "https://multimediya.uz/multimediya/index.php?mavzu="
    urls = [f"{url_base}{i}" for i in range(1, 13)]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = list(executor.map(download_html, urls))

    for i, result in enumerate(results):
        write_html(result, f"{i+1} - Maruza")

    end_time = time.time_ns() // 1_000_000
    print(end_time - start_time, "millisekundda yuklab olindi.")

# 1566 millisekundda yuklab olindi.