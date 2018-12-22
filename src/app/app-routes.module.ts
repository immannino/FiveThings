import { NgModule }              from '@angular/core';
import { RouterModule, Routes }  from '@angular/router';

import { DashboardComponent }   from './dashboard/dashboard.component';
import { LoginComponent }     from './login/login.component';
import { SettingsComponent } from './pages/settings/settings.component';
import { SearchComponent } from './pages/search/search.component';
import { AnalyticsComponent } from './pages/analytics/analytics.component';
import { FivethingsComponent } from './pages/fivethings/fivethings.component';

const appRoutes: Routes = [
    { path: 'login', component: LoginComponent },
    { path: 'dashboard', 
      component: DashboardComponent,
      children: [
        { path: 'settings', component: SettingsComponent },
        { path: 'search', component: SearchComponent },
        { path: 'analytics', component: AnalyticsComponent },
        { path: 'fivethings', component: FivethingsComponent }
      ]
    },
    { path: '',   redirectTo: '/login', pathMatch: 'full' },
    { path: '**', component: DashboardComponent }
  ];

@NgModule({
  imports: [
    RouterModule.forRoot(
      appRoutes
      // { enableTracing: true } // <-- debugging purposes only
    )
  ],
  exports: [
    RouterModule
  ]
})
export class AppRoutingModule {}