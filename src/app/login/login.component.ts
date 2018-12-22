import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { CarouselItem } from 'src/lib/model/carousel.model';

@Component({
  selector: 'login',
  templateUrl: './login.html',
  styleUrls: ['./login.css']
})
export class LoginComponent {
  carouselItems: CarouselItem[] = [
    {
      path: './assets/svgs/ic_intro_write.svg',
      description: 'Write things'
    },
    {
      path: './assets/svgs/ic_intro_help.svg',
      description: 'Things about stuff'
    },
    {
      path: './assets/svgs/ic_intro_search.svg',
      description: 'Search for stuff'
    }
  ];
  
  constructor(private router: Router){}
}
