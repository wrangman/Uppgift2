import csv
import subprocess
import locale
from collections import Counter



def load_sales(filename):
   products = {}
   all_products = []
   
   with open(filename, 'r') as file:
      reader = csv.DictReader(file)
      for row in reader:
         product = row['Product']
         sales = float(row['Sales'])
         
         all_products.append(product)
         
         if product in products:
               products[product] += sales
         else:
               products[product] = sales

               
   return products, all_products

def analyze_sales_data(products, all_products):

   # Hitta den mest sålda produkten
   product_count = Counter(all_products)
   most_common_product = product_count.most_common(1)[0]

   #TODO: Hitta den mest lukerativa produkten och använd max(products, key=products.get) (PS: products.get är en liten funktion som hämtar alla produkter i dictionary)
   
   most_lucrative_product = 0
   product_value = 0 # FIXME: använd  products[most_lucrative_product]
   
   print(f"Mest lukrativa produkt: \"{most_lucrative_product}\" med försäljning på {locale.currency(0,grouping=True)}")  #FIXME: Lägg in product_value här
   
   #TODO: skapa gärna en funktion för format_currency här.
   print(f"Mest sålda produkt: {most_common_product[0]}, Antal: {most_common_product[1]}")


# Sätt språkinställning till svenska (Sverige)
locale.setlocale(locale.LC_ALL, 'sv_SE.UTF-8')

subprocess.run('cls', shell=True)


products, all_products = load_sales('sales_data.csv')
analyze_sales_data(products, all_products)
