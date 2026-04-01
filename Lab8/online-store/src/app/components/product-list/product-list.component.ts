import { Component, EventEmitter, Input, Output } from '@angular/core';
import { Product } from '../../models/product.model';
import { ProductItemComponent } from '../product-item/product-item.component';

@Component({
  selector: 'app-product-list',
  standalone: true,
  imports: [ProductItemComponent],
  templateUrl: './product-list.component.html',
  styleUrl: './product-list.component.css'
})
export class ProductListComponent {
  @Input() products: Product[] = [];

  @Output() like = new EventEmitter<number>();
  @Output() delete = new EventEmitter<number>();
  @Output() share = new EventEmitter<{ id: number; platform: 'whatsapp' | 'telegram' }>();

  onLike(id: number): void {
    this.like.emit(id);
  }

  onDelete(id: number): void {
    this.delete.emit(id);
  }

  onShare(payload: { id: number; platform: 'whatsapp' | 'telegram' }): void {
    this.share.emit(payload);
  }
}

