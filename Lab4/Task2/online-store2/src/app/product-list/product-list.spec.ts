import { Component } from '@angular/core';

@Component({
  selector: 'app-product-list',
  templateUrl: './product.component.html',
  styleUrls: ['./product.component.css']
})
export class ProductComponent {

  categories = [
    { id: 1, name: 'Smartphones' },
    { id: 2, name: 'Laptops' },
    { id: 3, name: 'Headphones' },
    { id: 4, name: 'Tablets' }
  ];

  selectedCategoryId: number | null = null;

  products = [
    {
      id: 1,
      categoryId: 1,
      name: 'Smartphone example',
      description: 'Short smartphone description.',
      price: 0,
      rating: 0
    },
    {
      id: 2,
      categoryId: 2,
      name: 'Laptop example',
      description: 'Short laptop description.',
      price: 0,
      rating: 0
    },
    {
      id: 3,
      categoryId: 3,
      name: 'Headphones example',
      description: 'Short headphones description.',
      price: 0,
      rating: 0
    },
    {
      id: 4,
      categoryId: 4,
      name: 'Tablet example',
      description: 'Short tablet description.',
      price: 0,
      rating: 0
    }
  ];

  selectCategory(categoryId: number) {
    this.selectedCategoryId = categoryId;
  }

  get filteredProducts() {
    return this.products.filter(
      product => product.categoryId === this.selectedCategoryId
    );
  }
}
