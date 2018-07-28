import { Injectable } from "@angular/core";
import { Observer, Observable } from "rxjs";
import { Thing } from "../model/fivethings.model";

@Injectable()
export class FiveThingsService {
    constructor() {}

    getSingleFiveThingsPost(): Observable<Thing> {
        return null;
    }

    updateSingleFiveThingsPost(): Observable<boolean> {
        return null;
    }

    saveSingleFiveThingsPost(): Observable<boolean> {
        return null;
    }

    getAllFiveThingPosts(): Observable<Thing[]> {
        return null;
    }
}