import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, map, of, timeout, catchError } from 'rxjs';

import { environment } from '../../environments/environment';
import { Product } from '../models/product.model';
import { Category } from '../models/category.model';

interface BackendCategory {
  id: number;
  name: string;
}

interface BackendProduct {
  id: number;
  name: string;
  description: string;
  price: number;
  image_url: string;
  product_url: string;
  count: number;
  is_active: boolean;
  category: number;
}

@Injectable({
  providedIn: 'root'
})
export class ProductService {
  private readonly apiUrls = Array.from(
    new Set([environment.apiUrl, 'http://127.0.0.1:8000/api', 'http://localhost:8000/api'])
  );

  constructor(private readonly http: HttpClient) {}

  getProducts(): Observable<Product[]> {
    return this.requestWithFallback<BackendProduct[]>('/products/').pipe(
      map((items) => items.map((item) => this.mapProduct(item))),
      map((items) => (items.length ? items : this.getDemoProducts())),
      catchError(() => of(this.readCache<Product[]>('products') ?? this.getDemoProducts()))
    );
  }

  getCategories(): Observable<Category[]> {
    return this.requestWithFallback<BackendCategory[]>('/categories/').pipe(
      map((items) => items.map((item) => this.mapCategory(item))),
      map((items) => (items.length ? items : this.getDemoCategories())),
      catchError(() => of(this.readCache<Category[]>('categories') ?? this.getDemoCategories()))
    );
  }

  getProductsByCategory(categoryId: number): Observable<Product[]> {
    return this.requestWithFallback<BackendProduct[]>(`/categories/${categoryId}/products/`).pipe(
      map((items) => items.map((item) => this.mapProduct(item))),
      map((items) =>
        items.length ? items : this.getDemoProducts().filter((item) => item.categoryId === categoryId)
      ),
      catchError(() =>
        of(
          this.readCache<Product[]>(`products-category-${categoryId}`) ??
            this.getDemoProducts().filter((item) => item.categoryId === categoryId)
        )
      )
    );
  }

  private mapCategory(item: BackendCategory): Category {
    const mapped = {
      id: item.id,
      name: item.name
    };
    this.writeCache('categories', mapped, true);
    return mapped;
  }

  private mapProduct(item: BackendProduct): Product {
    const mapped = {
      id: item.id,
      name: item.name,
      description: item.description,
      price: item.price,
      rating: this.estimateRating(item),
      image: item.image_url,
      images: [item.image_url],
      link: item.product_url,
      likes: 0,
      categoryId: item.category
    };
    this.writeCache('products', mapped, true);
    this.writeCache(`products-category-${mapped.categoryId}`, mapped, true);
    return mapped;
  }

  private estimateRating(item: BackendProduct): number {
    const base = item.is_active ? 4.4 : 3.8;
    const stockImpact = Math.min(item.count, 30) / 100;
    return Number((base + stockImpact).toFixed(1));
  }

  private requestWithFallback<T>(path: string, index = 0): Observable<T> {
    const currentUrl = this.apiUrls[index];
    return this.http.get<T>(`${currentUrl}${path}`).pipe(
      timeout(5000),
      catchError((error) => {
        if (index + 1 < this.apiUrls.length) {
          return this.requestWithFallback<T>(path, index + 1);
        }
        throw error;
      })
    );
  }

  private readCache<T>(key: string): T | null {
    try {
      const raw = localStorage.getItem(`store-${key}`);
      return raw ? (JSON.parse(raw) as T) : null;
    } catch {
      return null;
    }
  }

  private writeCache(key: string, value: unknown, isArrayItem = false): void {
    try {
      const storageKey = `store-${key}`;
      if (isArrayItem) {
        const existing = this.readCache<unknown[]>(key) ?? [];
        const item = value as { id: number };
        const next = [...existing.filter((v) => (v as { id: number }).id !== item.id), value];
        localStorage.setItem(storageKey, JSON.stringify(next));
        return;
      }
      localStorage.setItem(storageKey, JSON.stringify(value));
    } catch {
      // ignore cache errors
    }
  }

  private getDemoCategories(): Category[] {
    return [
      { id: 1, name: 'Smartphones' },
      { id: 2, name: 'Laptops' },
      { id: 3, name: 'Home Appliances' },
      { id: 4, name: 'TV & Entertainment' }
    ];
  }

  private getDemoProducts(): Product[] {
    return [
      {
        id: 1001,
        name: 'iPhone 15 128GB',
        description: 'Modern flagship with strong cameras and smooth performance for daily use.',
        price: 439990,
        rating: 4.8,
        image: 'https://images.unsplash.com/photo-1696446701905-8b34f2f33e0b',
        images: ['https://images.unsplash.com/photo-1696446701905-8b34f2f33e0b'],
        link: 'https://kaspi.kz/shop/p/apple-iphone-15-128gb-113252342/',
        likes: 0,
        categoryId: 1
      },
      {
        id: 1002,
        name: 'Samsung Galaxy A55 5G',
        description: 'Balanced phone with excellent screen and battery life at mid-range price.',
        price: 224990,
        rating: 4.6,
        image: 'https://images.unsplash.com/photo-1610945265064-0e34e5519bbf',
        images: ['https://images.unsplash.com/photo-1610945265064-0e34e5519bbf'],
        link: 'https://kaspi.kz/shop/p/samsung-galaxy-a55-5g-256gb-117420102/',
        likes: 0,
        categoryId: 1
      },
      {
        id: 2001,
        name: 'MacBook Air M2',
        description: 'Lightweight laptop with long battery life and strong performance.',
        price: 799990,
        rating: 4.9,
        image: 'https://images.unsplash.com/photo-1517336714739-489689fd1ca8',
        images: ['https://images.unsplash.com/photo-1517336714739-489689fd1ca8'],
        link: 'https://kaspi.kz/shop/p/apple-macbook-air-13-m2-16gb-512gb-112484992/',
        likes: 0,
        categoryId: 2
      },
      {
        id: 2002,
        name: 'ASUS Vivobook 15',
        description: 'Practical laptop for office tasks, study, and everyday web usage.',
        price: 319990,
        rating: 4.5,
        image: 'https://images.unsplash.com/photo-1496181133206-80ce9b88a853',
        images: ['https://images.unsplash.com/photo-1496181133206-80ce9b88a853'],
        link: 'https://kaspi.kz/shop/p/asus-vivobook-15-i5-16gb-512gb-ssd-119842675/',
        likes: 0,
        categoryId: 2
      },
      {
        id: 3001,
        name: 'Xiaomi Mi Smart Air Fryer',
        description: 'Compact air fryer for quick home cooking with less oil.',
        price: 48990,
        rating: 4.4,
        image: 'https://images.unsplash.com/photo-1586201375761-83865001e31c',
        images: ['https://images.unsplash.com/photo-1586201375761-83865001e31c'],
        link: 'https://kaspi.kz/shop/p/xiaomi-mi-smart-air-fryer-3-5l-104998562/',
        likes: 0,
        categoryId: 3
      },
      {
        id: 3002,
        name: 'Tefal Electric Kettle 1.7L',
        description: 'Fast boiling kettle suitable for home and small office setups.',
        price: 26990,
        rating: 4.3,
        image: 'https://images.unsplash.com/photo-1570222094114-d054a817e56b',
        images: ['https://images.unsplash.com/photo-1570222094114-d054a817e56b'],
        link: 'https://kaspi.kz/shop/p/tefal-ko8518-1-7l-103390414/',
        likes: 0,
        categoryId: 3
      },
      {
        id: 4001,
        name: 'Samsung 55-inch 4K TV',
        description: 'Crisp 4K smart TV for movies, sports, and streaming services.',
        price: 289990,
        rating: 4.7,
        image: 'https://images.unsplash.com/photo-1593784991095-a205069470b6',
        images: ['https://images.unsplash.com/photo-1593784991095-a205069470b6'],
        link: 'https://kaspi.kz/shop/p/samsung-ue55cu7100uxce-55-111273456/',
        likes: 0,
        categoryId: 4
      },
      {
        id: 4002,
        name: 'PlayStation 5 Slim',
        description: 'Current-gen console with fast loading and immersive gameplay.',
        price: 339990,
        rating: 4.8,
        image: 'https://images.unsplash.com/photo-1606813907291-d86efa9b94db',
        images: ['https://images.unsplash.com/photo-1606813907291-d86efa9b94db'],
        link: 'https://kaspi.kz/shop/p/sony-playstation-5-slim-1tb-117334812/',
        likes: 0,
        categoryId: 4
      }
    ];
  }
}

