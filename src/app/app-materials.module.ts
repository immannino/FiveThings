import { NgModule }                           from '@angular/core';
import { NoopAnimationsModule }                 from '@angular/platform-browser/animations';
import { MatCommonModule, MatButtonModule, MatCardModule, MatTooltipModule, MatFormFieldModule, MatInputModule, MatDatepickerModule, MatNativeDateModule, MatExpansionModule } from '@angular/material';

@NgModule({
  imports: [ NoopAnimationsModule, MatCommonModule, MatButtonModule, MatCardModule, MatTooltipModule, MatFormFieldModule, MatInputModule, MatDatepickerModule, MatNativeDateModule, MatExpansionModule ],
  exports: [ NoopAnimationsModule, MatCommonModule, MatButtonModule, MatCardModule, MatTooltipModule, MatFormFieldModule, MatInputModule, MatDatepickerModule, MatNativeDateModule, MatExpansionModule ],
})
export class AppMaterialsModule { }