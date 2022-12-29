import { Component, OnInit, ViewChild } from '@angular/core';
import { NgForm } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { ToastrService } from 'ngx-toastr';
import { HttpProviderService } from '../Service/http-provider.service';

@Component({
  selector: 'app-edit-event',
  templateUrl: './edit-event.component.html',
  styleUrls: ['./edit-event.component.scss']
})
export class EditEventComponent implements OnInit {
  editEventForm: eventForm = new eventForm();

  @ViewChild("eventForm")
  eventForm!: NgForm;

  isSubmitted: boolean = false;
  eventId: any;

  constructor(private toastr: ToastrService, private route: ActivatedRoute, private router: Router,
    private httpProvider: HttpProviderService) { }

  ngOnInit(): void {
    this.eventId = this.route.snapshot.params['eventId'];
    this.getEventDetailById();
  }

  getEventDetailById() {
    this.httpProvider.getEventDetailById(this.eventId).subscribe((data: any) => {
      if (data != null) {
        var resultData = data;
        if (resultData) {
            this.editEventForm.id = resultData.id;
            this.editEventForm.event_name = resultData.event_name;
            this.editEventForm.start_date = resultData.start_date;
            this.editEventForm.end_date = resultData.end_date;
        }
      }
    },
      (error: any) => { });
  }

  EditEvent(isValid: any) {
    this.isSubmitted = true;
    if (isValid) {
      var updatedEventForm = {
        'event_name': this.editEventForm.event_name,
        'start_date': this.editEventForm.start_date,
        'end_date': this.editEventForm.end_date
      }
      this.httpProvider.updateEventById(this.eventId, updatedEventForm).subscribe(async data => {
        console.log("## ata: ", data)
        if (data != null) {
          var resultData = data.body;
          if (resultData != null && data.ok) {
            if (resultData != null && data.ok) {
              this.toastr.success(data.statusText);
              setTimeout(() => {
                this.router.navigate(['/Home']);
              }, 500);
            }
          }
        }
      },
        async error => {
          this.toastr.error(error.error.message);
          setTimeout(() => {
            this.router.navigate(['/Home']);
          }, 500);
        });
    }
  }
}

export class eventForm {
  id: number = 0;
  event_name: string = "";
  start_date: string = "";
  end_date: string = "";
}