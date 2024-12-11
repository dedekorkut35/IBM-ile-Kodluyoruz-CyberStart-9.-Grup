import math

# Öklid mesafesi fonksiyonu
def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

# Kullanıcıdan noktaları alma
x1 = float(input("1. noktanın X koordinatını girin: "))
y1 = float(input("1. noktanın Y koordinatını girin: "))
x2 = float(input("2. noktanın X koordinatını girin: "))
y2 = float(input("2. noktanın Y koordinatını girin: "))

# Noktaları liste olarak tanımlama
points = [(x1, y1), (x2, y2)]

# İki nokta arasındaki mesafeyi hesaplama
distance = euclideanDistance(points[0], points[1])

# Sonucu yazdırma
print("1. nokta:", points[0])
print("2. nokta:", points[1])
print("İki nokta arasındaki mesafe:", distance)
