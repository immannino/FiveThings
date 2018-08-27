import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { FiveThingsService } from '../lib/service/fivethings.service';
import { AuthenticationService } from '../lib/service/authentication.service';
import { AppMaterialsModule } from './app-materials.module';
import { LoginComponent } from './login/login.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { ContentService } from '../lib/service/content.service';
import { AppRoutingModule } from './app-routes.module';
import { CalendarComponent } from './components/calendar/calendar.component';
import { ThingComponent } from './components/thing/thing.component';
import { StateService } from '../lib/service/state.service';

@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    DashboardComponent,
    CalendarComponent,
    ThingComponent
  ],
  imports: [
    BrowserModule,
    AppMaterialsModule,
    FormsModule,
    ReactiveFormsModule,
    AppRoutingModule
  ],
  providers: [ FiveThingsService, AuthenticationService, ContentService, StateService ],
  bootstrap: [AppComponent]
})
export class AppModule { }
