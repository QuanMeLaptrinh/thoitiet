import requests

city = "Hanoi"
api_key = "6bcc7ce459d789fd82bfdaf1290ff273"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=vi"

response = requests.get(url)
data = response.json()

if response.status_code == 200:
    print(f"🌤️ Thời tiết tại {data['name']}: {data['weather'][0]['description']}")
    print(f"🌡️ Nhiệt độ: {data['main']['temp']}°C (cảm giác: {data['main']['feels_like']}°C)")
    print(f"💧 Độ ẩm: {data['main']['humidity']}%")
    print(f"💨 Gió: {data['wind']['speed']} m/s")
else:
    print("Lỗi khi lấy dữ liệu thời tiết:", data.get("message", "Không rõ lỗi"))
