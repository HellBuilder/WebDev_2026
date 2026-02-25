import { Component, Input } from '@angular/core';
import { Product } from '../../models/product.model';

@Component({
  selector: 'app-product-list',
  templateUrl: './product-list.component.html'
})
export class ProductListComponent {

  @Input() products: Product[] = [];

  removeProduct(productId: number) {
    this.products = this.products.filter(p => p.id !== productId);
  }
}
