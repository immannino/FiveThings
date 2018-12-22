import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { FivethingsComponent } from './fivethings.component';

describe('FivethingsComponent', () => {
  let component: FivethingsComponent;
  let fixture: ComponentFixture<FivethingsComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ FivethingsComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(FivethingsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
