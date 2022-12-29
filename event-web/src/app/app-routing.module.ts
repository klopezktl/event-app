import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AddEventComponent } from './add-event/add-event.component';
import { EditEventComponent } from './edit-event/edit-event.component';
import { HomeComponent } from './home/home.component';
import { DeleteEventComponent } from './delete-event/delete-event.component';
const routes: Routes = [
  { path: '', redirectTo: 'Home', pathMatch: 'full'},
  { path: 'Home', component: HomeComponent },
  { path: 'DeleteEvent/:eventId', component: DeleteEventComponent },
  { path: 'AddEvent', component: AddEventComponent },
  { path: 'EditEvent/:eventId', component: EditEventComponent }
];
 @NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }