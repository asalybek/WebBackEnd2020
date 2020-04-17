import { Component, OnInit } from '@angular/core';
import {HhService} from '../hh.service';
import {Company} from '../company';

@Component({
  selector: 'app-companies-list',
  templateUrl: './companies-list.component.html',
  styleUrls: ['./companies-list.component.css']
})
export class CompaniesListComponent implements OnInit {
  companies: Company[] = [];
  constructor(private service: HhService) { }

  ngOnInit(): void {
    this.getCompanies();
  }
  getCompanies(): void {
    this.service.getCompanies().subscribe(companies => this.companies = companies);
  }
}
