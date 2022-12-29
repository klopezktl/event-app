import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { WebApiService } from './web-api.service';

var apiUrl = "http://localhost:8080";
// var apiUrl = "http://127.0.0.1:8080"

var httpLink = {
  getAllEvent: apiUrl + "/event",
  deleteEventById: apiUrl + "/event",
  updateEventById: apiUrl + "/event",
  saveEvent: apiUrl + "/event"
}
@Injectable({
  providedIn: 'root'
})
export class HttpProviderService {
  constructor(private webApiService: WebApiService) { }

  public getAllEvent(): Observable<any> {
    console.log("--> getAllEvent")
    return this.webApiService.get(httpLink.getAllEvent);
  }
  public deleteEventById(model: any): Observable<any> {
    return this.webApiService.delete(httpLink.deleteEventById + '?event_id=' + model);
  }
  public updateEventById(model: any): Observable<any> {
    return this.webApiService.put(httpLink.updateEventById + '?event_id=' + model, '');
  }
  public saveEvent(model: any): Observable<any> {
    return this.webApiService.post(httpLink.saveEvent, model);
  }
}