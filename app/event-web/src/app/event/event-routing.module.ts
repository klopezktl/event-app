import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ListComponent } from './list/list.component';
import { CreateComponent } from './create/create.component';
import { UpdateComponent } from './update/update.component';
import { DeleteComponent } from './delete/delete.component';

const routes: Routes = [
  { path: 'event', redirectTo: 'post/index', pathMatch: 'full'},
  { path: 'event/index', component: ListComponent },
  { path: 'event/:event_id/delete', component: DeleteComponent },
  { path: 'event/create', component: CreateComponent },
  { path: 'event/:event_id/edit', component: UpdateComponent }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class EventRoutingModule { }
