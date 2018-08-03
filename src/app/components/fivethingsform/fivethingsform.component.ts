import { Component } from '@angular/core';
import { FormBuilder } from '@angular/forms';
import { ContentUtils } from '../../../lib/utils/content.util';
import { Store } from '@ngxs/store';
import { SaveState, ContentService } from '../../../lib/service/content.service';

@Component({
  selector: 'fivethingsform',
  templateUrl: './fivethingsform.html',
  styleUrls: ['./fivethingsform.css']
})
export class FivethingsFormComponent {
    fiveThingsForm = this.formBuilder.group({
        thing1: "",
        thing2: "",
        thing3: "",
        thing4: "",
        thing5: "",
        date: ""
    });
    saveState: SaveState = SaveState.SAVE;

    utils = new ContentUtils();
    placeholders = [];

    constructor(private formBuilder: FormBuilder, private store: Store, private contentService: ContentService) {
        this.placeholders = this.utils.getRandomPlaceholder();

        this.contentService.saveStateSubject.subscribe((state: SaveState) => {
            this.saveState = state;
        });
    }

    onSubmit() {
        if (this.saveState === SaveState.SAVE) {
            this.contentService.toggleSaveState(SaveState.SAVED);
        } else {
            this.contentService.toggleSaveState(SaveState.SAVE);
        }
    }
}
