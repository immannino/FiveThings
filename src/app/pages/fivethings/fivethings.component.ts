import { Component, OnInit } from '@angular/core';
import { FiveThingsState } from '../../../lib/model/fivethings.model';
import { StateService } from '../../../lib/service/state.service';

@Component({
  selector: 'app-fivethings',
  templateUrl: './fivethings.component.html',
  styleUrls: ['./fivethings.component.css']
})
export class FivethingsComponent implements OnInit {
  state: FiveThingsState = null;
  constructor(private stateService: StateService) { 
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
}
