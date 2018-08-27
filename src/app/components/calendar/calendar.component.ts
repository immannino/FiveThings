import { Component, OnInit } from '@angular/core';
import { FormControl } from '@angular/forms';
import { ContentService } from '../../../lib/service/content.service';
import { StateService } from '../../../lib/service/state.service';
import { FiveThingsState } from '../../../lib/model/fivethings.model';

@Component({
  selector: 'calendar',
  templateUrl: './calendar.html',
  styleUrls: ['./calendar.css']
})
export class CalendarComponent {
    date = new FormControl(new Date());

    daysOfWeek = [
        "Sunday",
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday"
    ];

    constructor(private stateService: StateService) {
        this.stateService.stateSubject.subscribe((state) => {
            this.date.setValue(state.date);
        });
    }

    updateDate() {
        let state = this.stateService.getState();

        state.date = this.date.value;
        this.stateService.updateState(state);
    }

    getDateText() {
        let date = new Date(this.date.value);
        let dayText = date.toLocaleDateString('en-US', { weekday: 'long' }); 
        let monthText = date.toLocaleDateString('en-US', { month: 'long' }); 
        return `${dayText} ${monthText} ${this.ordinal_suffix_of(date.getDate())}, ${date.getFullYear()}`
    }

    ordinal_suffix_of(i) {
        var j = i % 10,
            k = i % 100;
        if (j == 1 && k != 11) {
            return i + "st";
        }
        if (j == 2 && k != 12) {
            return i + "nd";
        }
        if (j == 3 && k != 13) {
            return i + "rd";
        }
        return i + "th";
    }
}
