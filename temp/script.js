// step one

function normaltrip(){
  var appendHtml=`<div class="step0">
        <div class="input-group1">
                <label class="txt2" for="job-type">Job Type <span class="red">*</span></label>
                <select name="job-type" id="job_type">
                  <option value="0">Please Select</option>
                  <option value="1">Arrival / Departure</option>
                  <option value="2">Transfer - Within City Limits</option>
                  <option value="3">Transfer - To/From Tuas; Jurong; Woodland; Selatar Airport</option>
                  <option value="4">Disposal (Min 2 Hrs<span class="red">*</span> )</option>
                </select>
              </div>
         
        </div>`;
    $("#body-from").append(appendHtml)
    $('.step1').remove()
    $('.step2').remove()
     $('.step3').remove()
  }
  
  function dailytips(){
    var appendHtml=`<div class="step1">
          <div class="input-group1">
                <label class="txt2" for="start-date">Start Date <span class="red">*</span></label>
                <input type="date" name="start-date" id="start-date" required/>
          </div>
          <div class="input-group1">
              <label class="txt2" for="end-date">End Date <span class="red">*</span></label>
              <input type="date" name="end-date" id="end-date" required/>
          </div>
          <div class="btns-group text-center">
            <a type="submit" value="submit" class="btn btn-next">Submit</a>
          </div>
        </div>`;
    $("#body-from").append(appendHtml)
    $('.step0').remove()
    $('.step2').remove()
     $('.step3').remove()
  }
  
  function arrival(){
    var appendHtml=`<div class="step2">
      <div class="input-group1">
            <div class="row">
              <div class="col-12">
               <label class="txt2" for="Type-of-trip">Require Meet & Greet <span class="red">*</span></label>
              </div>
              <div class="row">
                <div class="col-12">
                  <div class="form-check pl-01">
                    <input class="form-check-input" type="radio" name="Meet & Greet" id="meet-and-greet-yes"/>
                    <p-label class="form-check-label" for="meet-and-greet-yes">Yes</p-label>
                  </div>
                  
                  
                  <div class="form-check pl-01">
                    <input class="form-check-input" type="radio" name="Meet & Greet" id="meet-and-greet-no"/>
                    <p-label class="form-check-label" for="meet-and-greet-no"> No</p-label>
                  </div>
                </div>
              </div>
                    
            </div>
          </div>
          <div class="input-group1">
            <label class="txt2" for="Name">Flight Details (E.g; SQ 123, Arr/ Dep 1800 hrs) <span class="red">*</span></label>
            <input type="text" name="flight-details" id="flight-details" required/>
          </div>
          <div class="input-group1">
            <label class="txt2" for="Name">For Special Requirements</label>
            <input type="text" name="special-requirements" id="special-requirements" />
          </div>
          
          <div class="btns-group text-center">
            <a type="submit" value="submit" class="btn btn-next">Submit</a>
          </div>
        </div>`;
    $("#body-from").append(appendHtml)
    $('.step3').remove()
  }
  
  function lastSubmit(){
    var appendHtml=`<div class="step3">
          <div class="btns-group text-center">
            <a type="submit" value="submit" class="btn btn-next">Submit</a>
          </div>
        </div>`;
    $("#body-from").append(appendHtml)
    $('.step2').remove()
  
  }
  
  
  
  $(document).ready(function () {
      var flag =true;
      var flag2 =true;
      $('#normal-trip').click(function () {
    
        debugger
       if (flag) {
            if ($(this).is(':checked')) {
              normaltrip()
              flag =false;
              flag2=true
            }
        }
       
      });
  
      $('#daily-tips').click(function () {
        if (flag2) {
          if ($(this).is(':checked')) {
          dailytips()
          flag2 =false;
          flag=true
        }
        }
  
       
      });
    });
    // step one
  
    // step two
    $(document).ready(function () {   
      $('body').on('change','#job_type', function() {
     
        if (this.value==0){
          $('.step2').remove()
          $('.step3').remove()
        }
        if(this.value==1){
          arrival()
  
        }
        else if (this.value >= 1 || this.value >=4 ){
          $('.step2').remove()
          $('.step3').remove()
          lastSubmit()
        }
       
  
      });
  }); 
  