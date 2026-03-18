import {Component, OnInit} from '@angular/core';
import {ApiService} from '../../services/api';

@Component({
  imports: [ApiService, Component],
  selector: 'app-albums-component',
  styleUrl: './albums-component.css',
  templateUrl: './albums-component.html',
})
class AlbumsComponent implements OnInit {
  albums: any[] = [];

  constructor(private api: ApiService) {}

  ngOnInit() {
    this.api.getAlbums().subscribe((data: any) => {
      this.albums = data;
    });
  }
}

export default AlbumsComponent
