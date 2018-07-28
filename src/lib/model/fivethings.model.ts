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

/**
 * Most likely state module classes.
 *  Props (
 *      Token: string,
 *      Login Credentials: {
 *          email: string,
 *          password: string
 *      },
 * 
 * 
 * ) 
 *
 */
export class Token {
    token: string;
}