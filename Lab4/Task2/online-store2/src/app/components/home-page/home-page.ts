import { Component } from '@angular/core';
import {ProductList} from '../../product-list/product-list';
import {Modal} from '../modal/modal';
import {NgIf} from '@angular/common';

@Component({
  selector: 'app-home-page',
  imports: [ProductList, Modal, NgIf],
  templateUrl: './home-page.html',
  styleUrl: './home-page.css',
})
export class HomePage {

}
