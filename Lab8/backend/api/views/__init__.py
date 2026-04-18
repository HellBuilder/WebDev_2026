# Switch implementation by changing the import below.
# from .fbv import products_list, product_detail
# from .cbv import ProductListAPIView, ProductDetailAPIView
# from .mixins import ProductListCreateView as ProductListAPIView, ProductDetailView as ProductDetailAPIView
from .generics import (
    ProductListAPIView,
    ProductDetailAPIView,
    CategoryListAPIView,
    CategoryDetailAPIView,
    CategoryProductsAPIView,
)
