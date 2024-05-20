import randomss
from looney import Product

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    """Creating a list of 30 different products"""

    products = set()
    for i in range(num_products):
        adjective = random.sample(ADJECTIVES, 1)
        noun = random.sample(NOUNS, 1)
        name = adjective[0] + ' ' + noun[0]
        price = random.randint(5, 100)
        weight = random.randint(5, 100)
        flammability = random.uniform(0, 2.5)
        prod = Product(name, price, weight, flammability)
        products.add(prod)
    return products
    

def inventory_report(products):
    """Divides up the products list into septerate lists"""

    name_list = set()
    weight_list = []
    price_list = []
    flammability_list = []
    for product in products:
        name_list.add(product.name)
        weight_list.append(product.weight)
        price_list.append(product.price)
        flammability_list.append(product.flammability)
    uniques = len(name_list)
    mean_weight = sum(weight_list) / len(products)
    mean_price = sum(price_list) / len(products)
    mean_flammability = sum(flammability_list) / len(products)
    return (uniques, mean_price, mean_weight, mean_flammability)


if __name__ == '__main__':
    inventory_report(generate_products())
