from looney import Product
from looney_report import generate_products, ADJECTIVES, NOUNS


def test_default_product_price():
    """Test product default price is 10"""

    price_product = Product()
    assert price_product.price == 10


def test_stealability_explode():
    """Test sealability and explode return the correct output"""

    assert Product().stealability() == "kinda stealable."
    assert Product().explode() == "...boom!"


def test_generate_products():
    """Test number of products generated"""

    adjective, noun = Product().name.split()
    assert len(generate_products()) == 30
    assert noun in NOUNS
    assert adjective in ADJECTIVES
