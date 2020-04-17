import { Component, OnInit } from '@angular/core';
import {HhService} from '../hh.service';
import {ActivatedRoute} from '@angular/router';
import {Vacancy} from '../vacancy';

@Component({
  selector: 'app-company-vacancies',
  templateUrl: './company-vacancies.component.html',
  styleUrls: ['./company-vacancies.component.css']
})
export class CompanyVacanciesComponent implements OnInit {
  vacancies: Vacancy[] = [];
  constructor(private service: HhService, private route: ActivatedRoute) { }

  ngOnInit(): void {
    this.getVacancies();
  }
  getVacancies(): void {
    const id = +this.route.snapshot.paramMap.get('id');
    this.service.getCompanyVacancies(id).subscribe(companyVacancies => this.vacancies = companyVacancies);
  }

}
