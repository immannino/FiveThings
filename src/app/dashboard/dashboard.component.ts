import { Component, HostListener, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'dashboard',
  templateUrl: './dashboard.html',
  styleUrls: ['./dashboard.css']
})
export class DashboardComponent {
  constructor(private router: Router){
  }

  things = []
  activeThing = null;
  pageHeight: number = null;
  pageWidth: number = null;

  ngOnInit() {
    document.addEventListener('window:scroll', this.onWindowScroll);
    this.setDimensions();
    this.buildThings();
    this.activeThing = this.things[0];
  }

  handleNextThing(index: number) {
    this.updateActiveThing(index);
    console.log("thing clicked");
  }

  updateActiveThing(index: number) {
    this.activeThing = this.things[index];
  }

  setDimensions() {
    this.pageHeight = document.body.clientHeight;
    this.pageWidth = document.body.clientWidth;
  }

  buildThings() {
    this.things.push(new ThingProps(0, "Thing 1", "t-light-red", "t-light-red red-props", `${Math.round(this.pageHeight * 0.78)}px`, "250px", 0, Math.round(this.pageHeight * 0.78)));
    this.things.push(new ThingProps(1, "Thing 2", "t-light-blue", "t-light-blue blue-props", `${Math.round(this.pageHeight * 0.81)}px`, "200px", 0, Math.round(this.pageHeight * 0.81)));
    this.things.push(new ThingProps(2, "Thing 3", "t-light-yellow", "t-light-yellow yellow-props", `${Math.round(this.pageHeight * 0.84)}px`, "150px", 0, Math.round(this.pageHeight * 0.81)));
    this.things.push(new ThingProps(3, "Thing 4", "t-light-green", "t-light-green green-props", `${Math.round(this.pageHeight * 0.87)}px`, "100px", 0, Math.round(this.pageHeight * 0.81)));
    this.things.push(new ThingProps(4, "Thing 5", "t-light-pink", "t-light-pink pink-props", `${Math.round(this.pageHeight * 0.90)}px`, "50px", 0, Math.round(this.pageHeight * 0.81)));
  }

  onWindowScroll(event) {
      console.log(event);
      console.log("scrolling...");
  }

  // @HostListener('wheel', ['$event'])
  onThing($event) {
    // console.log($event)
    let currentHeght = +this.activeThing.top.substring(0, this.activeThing.top.length - 2);
    console.log(`Current height: ${currentHeght}`);
    if (currentHeght > 0) {
      let newHeight = Math.round(currentHeght + $event.deltaY);
      this.activeThing.top = `${newHeight}px`;
    } else if (this.activeThing.index < 4) {
      this.updateActiveThing(this.activeThing.index + 1);
    } else if (this.activeThing.index === 4) {
      this.updateActiveThing(3);
    }
  }

  
}

export class ThingProps {
  index: number;
  name: string;
  color: string;
  cssClass: string; // Deprecated
  top: string;
  left: string;
  maxHeight: number;
  startingHeight: number;

  constructor(index, name, color, cssClass, top, left, maxHeight, startingHeight) {
    this.index = index;
    this.name = name;
    this.color = color;
    this.cssClass = cssClass;
    this.top = top;
    this.left = left;
    this.maxHeight = maxHeight;
    this.startingHeight = startingHeight;
  }
}
