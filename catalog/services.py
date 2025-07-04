from catalog.models import Category, Product


def get_products_in_category(category_id):

    return Product.objects.filter(category_id=category_id)

# class ProductService:
#
#     @staticmethod
#     def is_popular(product_id):
#         popular = Product.objects.filter(product_id=product_id)
#
#         return popular
