import { Component, OnInit, ViewChild } from '@angular/core';
import { NgForm } from '@angular/forms';
import { Router } from '@angular/router';
import { ToastrService } from 'ngx-toastr';
import { HttpProviderService } from '../Service/http-provider.service';

@Component({
  selector: 'app-add-event',
  templateUrl: './add-event.component.html',
  styleUrls: ['./add-event.component.scss']
})
export class AddEventComponent implements OnInit {
  addEventForm: eventForm = new eventForm();

  @ViewChild("eventForm")
  eventForm!: NgForm;
  isSubmitted: boolean = false;
  constructor(private router: Router, private httpProvider: HttpProviderService, private toastr: ToastrService) { }

  ngOnInit(): void {  }

  AddEvent(isValid: any) {
    this.isSubmitted = true;
    if (isValid) {
      this.httpProvider.saveEvent(this.addEventForm).subscribe(async data => {
        if (data != null && data.body != null) {
          console.log("## data: ", data)
          if (data != null  != null) {
            var resultData = data.body;
            console.log("## resultData: ", resultData)
            if (resultData != null) {
              this.toastr.success(data.statusText);
              setTimeout(() => {
                this.router.navigate(['/Home']);
              }, 500);
            }
          }
        }
      },
        async error => {
          this.toastr.error(error.message);
          setTimeout(() => {
            this.router.navigate(['/Home']);
          }, 500);
        });
    }
  }
}

export class eventForm {
  event_name: string = "";
  start_date: string = "";
  end_date: string = "";
}