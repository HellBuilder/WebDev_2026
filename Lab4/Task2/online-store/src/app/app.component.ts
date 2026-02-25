import { Component } from '@angular/core';
import { Category } from './models/category.model';
import { Product } from './models/product.model';
import { ProductService } from './services/product.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html'
})
export class AppComponent {

  categories: Category[] = [];
  selectedCategoryId: number | null = null;
  selectedProducts: Product[] = [];

  constructor(private productService: ProductService) {
    this.categories = this.productService.getCategories();
  }

  selectCategory(categoryId: number) {
    this.selectedCategoryId = categoryId;
    this.selectedProducts =
      this.productService.getProductsByCategory(categoryId);
  }
}
