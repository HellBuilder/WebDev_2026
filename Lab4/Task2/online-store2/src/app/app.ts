import { Component, signal } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import {Header} from './components/header/header';
import {HomePage} from './components/home-page/home-page';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet, Header, HomePage],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App {
  protected readonly title = signal('online-store2');
}
