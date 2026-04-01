import { Component, OnInit } from '@angular/core';
import { Product } from './models/product.model';
import { Category } from './models/category.model';
import { ProductService } from './services/product.service';
import { ProductListComponent } from './components/product-list/product-list.component';

@Component({
  selector: 'app-root',
  imports: [ProductListComponent],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App implements OnInit {
  categories: Category[] = [];
  selectedCategoryId: number | null = null;
  products: Product[] = [];
  categoriesError = '';

  constructor(private readonly productService: ProductService) {}

  ngOnInit(): void {
    this.loadCategories();
  }

  loadCategories(): void {
    this.categoriesError = '';
    this.productService.getCategories().subscribe({
      next: (categories) => {
        this.categories = categories;
        if (categories.length > 0) {
          this.selectCategory(categories[0].id);
        } else {
          this.categoriesError = 'No categories found in API response.';
        }
      },
      error: () => {
        this.categories = [];
        this.categoriesError = 'Could not load categories. Make sure Django server is running on 127.0.0.1:8000.';
      }
    });
  }

  selectCategory(categoryId: number): void {
    this.selectedCategoryId = categoryId;
    this.productService.getProductsByCategory(categoryId).subscribe((products) => {
      this.products = products;
    });
  }

  onLikeProduct(productId: number): void {
    this.products = this.products.map((product) =>
      product.id === productId ? { ...product, likes: product.likes + 1 } : product
    );
  }

  onDeleteProduct(productId: number): void {
    this.products = this.products.filter((product) => product.id !== productId);
  }

  onShareProduct(payload: { id: number; platform: 'whatsapp' | 'telegram' }): void {
    const targetProduct = this.products.find((product) => product.id === payload.id);
    if (!targetProduct) {
      return;
    }

    const shareUrl = this.buildShareUrl(targetProduct, payload.platform);
    if (!shareUrl) {
      return;
    }

    window.open(shareUrl, '_blank', 'noopener');
  }

  private buildShareUrl(product: Product, platform: 'whatsapp' | 'telegram'): string {
    if (platform === 'whatsapp') {
      const text = encodeURIComponent(`Check out this product: ${product.link}`);
      return `https://wa.me/?text=${text}`;
    }

    const encodedLink = encodeURIComponent(product.link);
    const encodedName = encodeURIComponent(product.name);
    return `https://t.me/share/url?url=${encodedLink}&text=${encodedName}`;
  }
}
