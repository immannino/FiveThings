export class Thing {
    date: string;
    content: string;
    order: number;

    constructor(date: string, content: string, order: number) {
        this.date = date;
        this.content = content;
        this.order = order;
    }
}

export enum Status {
    SUCCESS,
    FAILURE
}

export class Token {
    token: string;
}

export class FiveThingsState {
    thing1: Thing;
    thing2: Thing;
    thing3: Thing;
    thing4: Thing;
    thing5: Thing;
    saveStatus: string;
    date: Date;
}