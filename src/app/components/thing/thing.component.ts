import { Component, Input, Output, EventEmitter, OnInit } from '@angular/core';
import { FormBuilder } from '@angular/forms';
import { ContentUtils } from '../../../lib/utils/content.util';
import { Store } from '@ngxs/store';
import { SaveState, ContentService } from '../../../lib/service/content.service';

@Component({
  selector: 'thing',
  templateUrl: './thing.html',
  styleUrls: ['./thing.css']
})
export class ThingComponent {
    @Input() title: string;
    @Output() thingClicked: EventEmitter<boolean> = new EventEmitter<boolean>();

    formData = this.formBuilder.group({
        thing: ""
    });

    utils = new ContentUtils();
    placeholder = null;

    constructor(private formBuilder: FormBuilder, private store: Store, private contentService: ContentService) {
    }

    ngOnInit() {
        this.placeholder = this.utils.getRandomPlaceholder(1)[0];
    }

    onSubmit() {

    }

    triggerEvent() {
        this.thingClicked.emit(true);
    }
}
