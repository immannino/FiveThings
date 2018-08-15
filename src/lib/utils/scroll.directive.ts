import { Directive, EventEmitter, Output, HostListener } from "@angular/core";

@Directive({
    selector: "[scrollable]"
 })
 export class ScrollDirective {
    @Output() onScroll: EventEmitter<number[]> = new EventEmitter<number[]>();
    
    @HostListener("click", ["$event"])
    public onThingHappened(event: any): void {
        console.log("CLICK EVENT")
    }
    @HostListener("scroll", ["$event"])
    public onListenerTriggered(event: any): void {
        this.onScroll.emit([event.clientX, event.clientY]);
        console.log("SCROLL EVENT")
    }
 }