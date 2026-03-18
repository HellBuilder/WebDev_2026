import { Component } from '@angular/core';
import {ProductList} from '../../product-list/product-list';
import {Input, Output, EventEmitter} from '@angular/core';
@Component({
  selector: 'app-modal',
  imports: [ProductList],
  templateUrl: './modal.html',
  styleUrl: './modal.css',
})
export class Modal {
  isOpen = @Input<boolean>(true);
  closeModal = @Output<void>();
  @Output() close = new EventEmitter<void>();
  protected OnClose() {
    this.isOpen = false;
    this.closeModal();
  }

  protected onBackdropClick() {
    this.isOpen = false;
    this.closeModal();
  }
}
