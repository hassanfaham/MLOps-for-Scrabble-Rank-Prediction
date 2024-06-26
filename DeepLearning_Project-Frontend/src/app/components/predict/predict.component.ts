import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, FormArray, FormControl, ValidatorFn } from '@angular/forms';
import { Rating } from '../../models/rating.model';
import {FastapiService} from '../../services/fastapi.service';
@Component({
  selector: 'app-predict',
  templateUrl: './predict.component.html',
  styleUrls: ['./predict.component.css']
})
export class PredictComponent implements OnInit {


  rating = new Rating(0, 0, 0,false,false);
  prediction = 0;
  constructor(
    private _fastapiService: FastapiService,
  ) {
  }

  public onPredict(): void {
    this._fastapiService.predict(this.rating).subscribe(
      response => {
        var jsd = JSON.stringify(response);
        var js = JSON.parse(jsd);
        this.prediction = js.prediction;
      }
    );
  }
  ngOnInit(): void {
  }

}
