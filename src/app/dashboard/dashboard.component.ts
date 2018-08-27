import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { StateService } from '../../lib/service/state.service';
import { FiveThingsState } from '../../lib/model/fivethings.model';

@Component({
  selector: 'dashboard',
  templateUrl: './dashboard.html',
  styleUrls: ['./dashboard.css']
})
export class DashboardComponent {
  state: FiveThingsState = null;

  constructor(private router: Router, private stateService: StateService){
    this.stateService.stateSubject.subscribe((state) => {
      this.state = {
        ...this.state,
        ...state
      };
    });
  }

  ngOnInit() {
    this.state = this.stateService.getState();
  }

  logout() {
    //saveState();
    this.router.navigate(['login']);
  }
}