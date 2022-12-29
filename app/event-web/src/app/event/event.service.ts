import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

import {  Observable, throwError } from 'rxjs';
import { catchError } from 'rxjs/operators';

import { Event } from './event';

@Injectable({
  providedIn: 'root'
})
export class EventService {

  private apiURL = "http://172.17.0.2:8080";

  httpOptions = {
    headers: new HttpHeaders({
      'Content-Type': 'application/json'
    })
  }

  constructor(private httpClient: HttpClient) { }

  getAll(): Observable<any> {

    return this.httpClient.get(this.apiURL + '/event/')

    .pipe(
      catchError(this.errorHandler)
    )
  }

  create(event:Event): Observable<any> {

    return this.httpClient.post(this.apiURL + '/post/', JSON.stringify(event), this.httpOptions)

    .pipe(
      catchError(this.errorHandler)
    )
  }

  update(id:number, event:Event): Observable<any> {

    return this.httpClient.put(this.apiURL + '/event/' + id, JSON.stringify(event), this.httpOptions)

    .pipe(
      catchError(this.errorHandler)
    )
  }

  delete(id:number): Observable<any> {

    return this.httpClient.delete(this.apiURL + '/event/' + id, this.httpOptions)

    .pipe(
      catchError(this.errorHandler)
    )
  }

  errorHandler(error:any) {
    let errorMessage = '';
    if(error.error instanceof ErrorEvent) {
      errorMessage = error.error.message;
    } else {
      errorMessage = `Error Code: ${error.status}\nMessage: ${error.message}`;
    }
    return throwError(errorMessage);
 }

}
