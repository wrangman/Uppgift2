from collections import Counter
import csv
import locale
import subprocess


def load_sales(filename):
   products = {}  #ordbok dictionary
   list_products = []
   
   with open(filename, 'r') as file:
      reader = csv.DictReader(file)
      
      for row in reader:
         product = row['Product']
         sales = float(row['Sales'])
         
         list_products.append(product)
         
         if product in products:
               products[product] += sales
         else:
               products[product] = sales
               
   return products
                
def analyze_sales_data(products):
      
   #TODO: Hitta den mest sålda produkten (TIPS! Använd Counter från collections)
   most_common_product = Counter(products)
   most_common = most_common_product.most_common(1)[0]

   #TODO: Hitta den mest lukrativa produkten med max: max(products, key=products.get)
   most_lucrative_product = 0
   
   print(f"Mest sålda produkt: {most_common[0]}, Antal: {most_common[1]}")
   print(f"Mest lukrativa produkt: \"{most_lucrative_product}\" med försäljning på {locale.currency(0,grouping=True)}") #TODO: BONUS: kan du skapa en funktion som skriver ut rätt formaterad valuta istället för detta?


subprocess.run('cls', shell=True)

# Sätt språkinställning till svenska (Sverige) används för att skriva ut formaterad valuta
locale.setlocale(locale.LC_ALL, 'sv_SE.UTF-8')  

products = load_sales('sales_data.csv')

print(products)
analyze_sales_data(products)

