import { Component, Input, Output, EventEmitter, OnInit } from '@angular/core';
import { FormBuilder } from '@angular/forms';
import { ContentUtils } from '../../../lib/utils/content.util';
import { ContentService } from '../../../lib/service/content.service';
import { StateService } from '../../../lib/service/state.service';
import { FiveThingsState } from '../../../lib/model/fivethings.model';

@Component({
  selector: 'thing',
  templateUrl: './thing.html',
  styleUrls: ['./thing.css']
})
export class ThingComponent {
    @Input() title: string;
    @Input() formName: string;

    formData = this.formBuilder.group({
        thing1: "",
        thing2: "",
        thing3: "",
        thing4: "",
        thing5: ""
    });

    utils = new ContentUtils();
    placeholder = null;

    state: FiveThingsState = null;

    constructor(private formBuilder: FormBuilder, private stateService: StateService, private contentService: ContentService) {
        this.stateService.stateSubject.subscribe((state) => {
            this.state = {
                ...this.state,
                ...state
            };
        });
    }

    ngOnInit() {
        this.state = this.stateService.getState();
        this.placeholder = this.utils.getRandomPlaceholder(5);
    }

    onSubmit() {
        this.state = {
            ...this.state,
            ...this.formData.value,
            saveStatus: "SAVED"
        }

        this.stateService.updateState(this.state);
        console.log(this.state);
    }
}
