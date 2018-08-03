import { Component } from '@angular/core';
import { FormControl } from '@angular/forms';
import { ContentService } from '../../../lib/service/content.service';

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

    constructor(private contentService: ContentService) {
        this.contentService.dateStateSubject.subscribe((state) => {
            this.date.setValue(state);
        });
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
