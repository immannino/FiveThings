import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { NgxsModule } from '@ngxs/store';
import { NgxsFormPluginModule } from '@ngxs/form-plugin';

import { AppComponent } from './app.component';
import { FiveThingsService } from '../lib/service/fivethings.service';
import { AuthenticationService } from '../lib/service/authentication.service';
import { AppMaterialsModule } from './app-materials.module';
import { LoginComponent } from './login/login.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { FivethingsFormComponent } from './components/fivethingsform/fivethingsform.component';
import { AuthState } from '../shared/state/auth.state';
import { FivethingsState } from '../shared/state/fivethings.state';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { FormState } from '../shared/state/form.state';
import { ContentService } from '../lib/service/content.service';
import { AppRoutingModule } from './app-routes.module';
import { CalendarComponent } from './components/calendar/calendar.component';

@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    DashboardComponent,
    FivethingsFormComponent,
    CalendarComponent
  ],
  imports: [
    BrowserModule,
    AppMaterialsModule,
    FormsModule,
    ReactiveFormsModule,
    NgxsModule.forRoot([AuthState, FivethingsState, FormState]),
    NgxsFormPluginModule.forRoot(),
    AppRoutingModule
  ],
  providers: [ FiveThingsService, AuthenticationService, ContentService ],
  bootstrap: [AppComponent]
})
export class AppModule { }
