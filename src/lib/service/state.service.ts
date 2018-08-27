import { Injectable } from "@angular/core";
import { FiveThingsState } from "../model/fivethings.model";
import { Subject } from "rxjs";

@Injectable()
export class StateService {
    stateSubject: Subject<FiveThingsState> = new Subject<FiveThingsState>();
    state: FiveThingsState = {
        thing1: null,
        thing2: null,
        thing3: null,
        thing4: null,
        thing5: null,
        saveStatus: "SAVE",
        date: new Date()
    }

    constructor() {}

    getState(): FiveThingsState {
        return this.state;
    }

    setState(state: FiveThingsState) {
        this.state = {
            ...this.state,
            ...state
        };
    }

    updateState(state: FiveThingsState) {
        this.setState(state);
        
        this.stateSubject.next(this.state);
    }

}