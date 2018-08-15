import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { ContentService } from '../../lib/service/content.service';

@Component({
  selector: 'login',
  templateUrl: './login.html',
  styleUrls: ['./login.css']
})
export class LoginComponent {
  constructor(private router: Router, private contentService: ContentService){}

  handleLogin() {
    this.contentService.toggleLoginState(true);
  }
}
