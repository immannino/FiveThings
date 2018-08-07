import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'dashboard',
  templateUrl: './dashboard.html',
  styleUrls: ['./dashboard.css']
})
export class DashboardComponent {
  constructor(private router: Router){
    this.buildThings();
    this.activeThing = this.things[0];
  }

  things = []
  activeThing = null;

  handleNextThing(index: number) {
    this.updateActiveThing(index);
    console.log("thing clicked");
  }

  updateActiveThing(index: number) {
    this.activeThing = this.things[index];
  }

  buildThings() {
    this.things.push(new ThingProps("Thing 1", "t-light-red", "t-light-red red-props"));
    this.things.push(new ThingProps("Thing 2", "t-light-blue", "t-light-blue blue-props"));
    this.things.push(new ThingProps("Thing 3", "t-light-yellow", "t-light-yellow yellow-props"));
    this.things.push(new ThingProps("Thing 4", "t-light-green", "t-light-green green-props"));
    this.things.push(new ThingProps("Thing 5", "t-light-pink", "t-light-pink pink-props"));
  }
}

export class ThingProps {
  name: string;
  color: string;
  cssClass: string;

  constructor(name, color, cssClass) {
    this.name = name;
    this.color = color;
    this.cssClass = cssClass;
  }
}
