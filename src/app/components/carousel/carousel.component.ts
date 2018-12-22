import { Component, Input } from '@angular/core';
import { CarouselItem } from '../../../lib/model/carousel.model';

@Component({
  selector: 'carousel',
  templateUrl: './carousel.html',
  styleUrls: ['./carousel.css']
})
export class CarouselComponent {
    @Input() items: CarouselItem[];
    constructor(){}

    // ngOnInit() {
    //   setInterval(() => {
    //     this.rotate();
    //   }, 5000);
    // }

    // rotate() {

    // }
}