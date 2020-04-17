import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Observable} from 'rxjs';
import {Company} from './company';
import {LoginResponse} from './login';
import {Vacancy} from './vacancy';
@Injectable({
  providedIn: 'root'
})
export class HhService {
  BASE_URL = 'http://127.0.0.1:8000';

  constructor(private httpClient: HttpClient) { }

  getCompanies(): Observable<Company[]> {
    return this.httpClient.get<Company[]>(`${this.BASE_URL}/api/companies/`);
  }

    getCompanyVacancies(id: number): Observable<Vacancy[]> {
      return this.httpClient.get<Vacancy[]>(`${this.BASE_URL}/api/companies/${id}/vacancies`);
    }

    login(username, password): Observable<LoginResponse> {
      return this.httpClient.post<LoginResponse>(`${this.BASE_URL}/api/login/`, {
        username,
        password
      });
  }
}
