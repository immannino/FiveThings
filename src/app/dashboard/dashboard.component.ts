import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { ContentService } from '../../lib/service/content.service';

@Component({
  selector: 'dashboard',
  templateUrl: './dashboard.html',
  styleUrls: ['./dashboard.css']
})
export class DashboardComponent {
  isLoggedIn: boolean = false;

  constructor(private router: Router, private contentService: ContentService){
    this.contentService.loginStateSubject.subscribe((state) => {
      this.isLoggedIn = state;
    });
  }

  handleLogout(status: boolean) {
    this.contentService.toggleLoginState(status);
  }
}
