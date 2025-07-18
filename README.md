# Liste İşlemleri Projesi

Bu projede Python programlama dili kullanılarak listeler üzerinde iki farklı işlem gerçekleştiren iki ayrı fonksiyon yazılmıştır. Fonksiyonlar aşağıda açıklanmıştır:

## 1. Flatten Fonksiyonu

**Amaç:**  
İç içe geçmiş (nested) listeleri tek boyutlu düz bir liste haline getirmektir.

**Örnek:**

input: [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]
output: [1, 'a', 'cat', 2, 3, 'dog', 4, 5]

Açıklama:

Liste, ne kadar derin iç içe olursa olsun tüm elemanlar ayrıştırılarak düzleştirilir.

String gibi iteratif ancak "non-scalar" (bölünmemesi gereken) veriler dikkate alınarak sadece listeler ayrıştırılır.

2. Tersine Çevirme Fonksiyonu (Deep Reverse)
Amaç:
Verilen bir listeyi ve içerisindeki tüm alt listeleri tersine çevirmektir.

Örnek:

input: [[1, 2], [3, 4], [5, 6, 7]]
output: [[[7, 6, 5], [4, 3], [2, 1]]]
Açıklama:

Tüm iç listeler elemanlarıyla birlikte ters çevrilir.

Dış liste de ters çevrilir ve sonuç olarak bu ters listeler tek bir dış liste içinde yer alır.

#Kullanım

from liste_islemleri import flatten, deep_reverse

# flatten örneği
data = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]
print(flatten(data))  # [1, 'a', 'cat', 2, 3, 'dog', 4, 5]

# deep reverse örneği
nested_list = [[1, 2], [3, 4], [5, 6, 7]]
print(deep_reverse(nested_list))  # [[[7, 6, 5], [4, 3], [2, 1]]]

