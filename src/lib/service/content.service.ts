import { Injectable } from "@angular/core";
import { Subject } from "rxjs";

@Injectable()
export class ContentService {
    saveStateSubject: Subject<string> = new Subject<string>();
    dateStateSubject: Subject<Date> = new Subject<Date>();
    loginStateSubject: Subject<boolean> = new Subject<boolean>();

    toggleSaveState(state: SaveState) {
        this.saveStateSubject.next(state);
    }

    toggleDateState(state: Date) {
        this.dateStateSubject.next(state);
    }

    toggleLoginState(state: boolean) {
        this.loginStateSubject.next(state);
    }
}

export enum SaveState {
    SAVE = "SAVE",
    SAVED = "SAVED"
}