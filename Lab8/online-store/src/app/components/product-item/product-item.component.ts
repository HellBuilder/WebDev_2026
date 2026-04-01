import { Component, EventEmitter, Input, Output } from '@angular/core';
import { DecimalPipe } from '@angular/common';
import { Product } from '../../models/product.model';

@Component({
  selector: 'app-product-item',
  standalone: true,
  imports: [DecimalPipe],
  templateUrl: './product-item.component.html',
  styleUrl: './product-item.component.css'
})
export class ProductItemComponent {
  @Input({ required: true }) product!: Product;

  @Output() like = new EventEmitter<number>();
  @Output() delete = new EventEmitter<number>();
  @Output() share = new EventEmitter<{ id: number; platform: 'whatsapp' | 'telegram' }>();

  onLike(): void {
    this.like.emit(this.product.id);
  }

  onDelete(): void {
    this.delete.emit(this.product.id);
  }

  onShare(platform: 'whatsapp' | 'telegram'): void {
    this.share.emit({ id: this.product.id, platform });
  }

  get ratingStars(): string {
    const fullStars = Math.round(this.product.rating);
    return `${'★'.repeat(fullStars)}${'☆'.repeat(5 - fullStars)}`;
  }
}

