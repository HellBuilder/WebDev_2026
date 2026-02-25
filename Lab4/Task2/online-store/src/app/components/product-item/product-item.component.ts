import { Component, Input, Output, EventEmitter } from '@angular/core';
import { Product } from '../../models/product.model';

@Component({
  selector: 'app-product-item',
  templateUrl: './product-item.component.html'
})
export class ProductItemComponent {

  @Input() product!: Product;
  @Output() delete = new EventEmitter<number>();

  like() {
    this.product.likes++;
  }

  remove() {
    this.delete.emit(this.product.id);
  }

  shareWhatsApp() {
    const url =
      'https://wa.me/?text=' +
      encodeURIComponent(this.product.link);
    window.open(url, '_blank');
  }
}
