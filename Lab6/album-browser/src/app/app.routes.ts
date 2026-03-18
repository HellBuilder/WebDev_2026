import { Routes } from '@angular/router';
import {createComponent} from '@angular/core';

export const routes: Routes = [
  { path: '/home', component: HomeComponent },
  { path: '/about', component: AboutComponent },
  { path: '/albums', component: AlbumsComponent },
  { path: '/albums/:id', component: AlbumDetailComponent },
  { path: '/albums/:id/photos', component: AlbumPhotosComponent}
];
