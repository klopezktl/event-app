import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { WebApiService } from './web-api.service';

var apiUrl = "http://localhost:8080";
// var apiUrl = "http://127.0.0.1:8080"

var httpLink = {
  getAllEvent: apiUrl + "/event",
  deleteEventById: apiUrl + "/event",
  updateEventById: apiUrl + "/event",
  saveEvent: apiUrl + "/event",
  getEventDetailById: apiUrl + "/event",
}
@Injectable({
  providedIn: 'root'
})
export class HttpProviderService {
  constructor(private webApiService: WebApiService) { }

  public getAllEvent(): Observable<any> {
    return this.webApiService.get(httpLink.getAllEvent);
  }
  public deleteEventById(model: any): Observable<any> {
    return this.webApiService.delete(httpLink.deleteEventById + '/' + model);
  }
  public updateEventById(model: any, event_data: any): Observable<any> {
    return this.webApiService.put(httpLink.updateEventById + '/' + model, event_data);
  }
  public saveEvent(model: any): Observable<any> {
    return this.webApiService.post(httpLink.saveEvent, model);
  }

  public getEventDetailById(model: any): Observable<any> {
    return this.webApiService.get(httpLink.getEventDetailById + '/' + model);
  }
}