import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { NgxsModule } from '@ngxs/store';

import { AppComponent } from './app.component';
import { FiveThingsService } from '../lib/service/fivethings.service';
import { AuthenticationService } from '../lib/service/authentication.service';
import { AppMaterialsModule } from './app-materials.module';
import { LoginComponent } from './login/login.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { FivethingsFormComponent } from './components/fivethingsform/fivethingsform.component';
import { AuthState } from '../shared/state/auth.state';
import { FivethingsState } from '../shared/state/fivethings.state';

@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    DashboardComponent,
    FivethingsFormComponent
  ],
  imports: [
    BrowserModule,
    AppMaterialsModule,
    NgxsModule.forRoot([AuthState, FivethingsState]),
  ],
  providers: [ FiveThingsService, AuthenticationService ],
  bootstrap: [AppComponent]
})
export class AppModule { }
