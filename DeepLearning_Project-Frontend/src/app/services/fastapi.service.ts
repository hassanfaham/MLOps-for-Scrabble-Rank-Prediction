import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Rating } from '../models/rating.model';
@Injectable({
  providedIn: 'root'
})
export class FastapiService {

  private _http: HttpClient;
  private _baseUrl: string;

  constructor(http: HttpClient) {
    this._http = http;
    this._baseUrl = "http://127.0.0.1:8000"
  }
  public predict(data: Rating): Observable<string> {
    return this._http.post<string>(this._baseUrl + '/predict', data);
  }
}
