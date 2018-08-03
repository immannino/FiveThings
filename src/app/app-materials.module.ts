import { NgModule }                           from '@angular/core';
import { NoopAnimationsModule }                 from '@angular/platform-browser/animations';
import { MatCommonModule, MatButtonModule, MatCardModule, MatTooltipModule, MatFormFieldModule, MatInputModule, MatDatepickerModule, MatNativeDateModule } from '@angular/material';

@NgModule({
  imports: [ NoopAnimationsModule, MatCommonModule, MatButtonModule, MatCardModule, MatTooltipModule, MatFormFieldModule, MatInputModule, MatDatepickerModule, MatNativeDateModule ],
  exports: [ NoopAnimationsModule, MatCommonModule, MatButtonModule, MatCardModule, MatTooltipModule, MatFormFieldModule, MatInputModule, MatDatepickerModule, MatNativeDateModule ],
})
export class AppMaterialsModule { }