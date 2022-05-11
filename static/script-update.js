// step one

function normalTripUpdate(type) {
    var selectors;
    if (type == 0) {
        selectors = `<select name="job-type" id="job_type">
            <option value="0" selected = "selected">Please Select</option>
            <option value="1">Arrival / Departure</option>
            <option value="2">Transfer - Within City Limits</option>
            <option value="3">Transfer - To/From Tuas; Jurong; Woodland; Selatar Airport</option>
            <option value="4">Disposal (Min 2 Hrs<span class="red">*</span> )</option>
        </select>`
    }
    else if (type == 1) {
        selectors = `<select name="job-type" id="job_type">
            <option value="0">Please Select</option>
            <option value="1" selected = "selected">Arrival / Departure</option>
            <option value="2">Transfer - Within City Limits</option>
            <option value="3">Transfer - To/From Tuas; Jurong; Woodland; Selatar Airport</option>
            <option value="4">Disposal (Min 2 Hrs<span class="red">*</span> )</option>
        </select>`
    }
    else if (type == 2) {
        selectors = `<select name="job-type" id="job_type">
            <option value="0">Please Select</option>
            <option value="1">Arrival / Departure</option>
            <option value="2" selected = "selected">Transfer - Within City Limits</option>
            <option value="3">Transfer - To/From Tuas; Jurong; Woodland; Selatar Airport</option>
            <option value="4">Disposal (Min 2 Hrs<span class="red">*</span> )</option>
        </select>`
    }
    else if (type == 3) {
        selectors = `<select name="job-type" id="job_type">
            <option value="0">Please Select</option>
            <option value="1">Arrival / Departure</option>
            <option value="2">Transfer - Within City Limits</option>
            <option value="3" selected = "selected">Transfer - To/From Tuas; Jurong; Woodland; Selatar Airport</option>
            <option value="4">Disposal (Min 2 Hrs<span class="red">*</span> )</option>
        </select>`
    }
    else if (type == 4) {
        selectors = `<select name="job-type" id="job_type">
            <option value="0">Please Select</option>
            <option value="1">Arrival / Departure</option>
            <option value="2">Transfer - Within City Limits</option>
            <option value="3">Transfer - To/From Tuas; Jurong; Woodland; Selatar Airport</option>
            <option value="4" selected = "selected">Disposal (Min 2 Hrs<span class="red">*</span> )</option>
        </select>`
    }

    var appendHtml = `
        <div class="step0">
            <div class="input-group1">
                <label class="txt2" for="job-type">Job Type <span class="red">*</span></label>
                ${selectors}
            </div>     
        </div>`;

    $("#body-from").append(appendHtml)
    $('.step1').remove()
    $('.step2').remove()
    $('.step3').remove()
}

function dailyTripsUpdate(start_date, end_date) {
    var appendHtml = `
        <div class="step1">
              <div class="input-group1">
                    <label class="txt2" for="start-date">Start Date <span class="red">*</span></label>
                    <input type="date" name="start-date" id="start-date" value="${start_date}" required/>
              </div>
              <div class="input-group1">
                  <label class="txt2" for="end-date">End Date <span class="red">*</span></label>
                  <input type="date" name="end-date" id="end-date" value="${end_date}" required/>
              </div>
              <div class="btns-group text-center">
                <button type="submit"  class="btn btn-next">Submit</button>
              </div>
        </div>`;
    $("#body-from").append(appendHtml)
    $('.step0').remove()
    $('.step2').remove()
    $('.step3').remove()
}

function arrivalUpdate(meetGreet, flDetails, spRequirements) {

    var meetAndGreetCode;
    
    if (meetGreet === "Yes"){
        meetAndGreetCode = `
        <div class="form-check pl-01">
            <input class="form-check-input" type="radio" name="Meet & Greet" value="Yes" id="meet-and-greet-yes" checked/>
            <p-label class="form-check-label" for="meet-and-greet-yes">Yes</p-label>
        </div>
  
  
        <div class="form-check pl-01">
            <input class="form-check-input" type="radio" name="Meet & Greet" value="No" id="meet-and-greet-no"/>
            <p-label class="form-check-label" for="meet-and-greet-no"> No</p-label>
        </div>`
    }
    else {
        meetAndGreetCode = `
        <div class="form-check pl-01">
            <input class="form-check-input" type="radio" name="Meet & Greet" value="Yes" id="meet-and-greet-yes"/>
            <p-label class="form-check-label" for="meet-and-greet-yes">Yes</p-label>
        </div>
  
  
        <div class="form-check pl-01">
            <input class="form-check-input" type="radio" name="Meet & Greet" value="No" id="meet-and-greet-no" checked/>
            <p-label class="form-check-label" for="meet-and-greet-no"> No</p-label>
        </div>`
    }
    
    

    var appendHtml = `
    <div class="step2">
          <div class="input-group1">
                <div class="row">
                  <div class="col-12">
                   <label class="txt2" for="Type-of-trip">Require Meet & Greet <span class="red">*</span></label>
                  </div>
                  <div class="row">
                    <div class="col-12">
                      ${meetAndGreetCode}
                    </div>
                  </div>
                        
                </div>
              </div>
              <div class="input-group1">
                <label class="txt2" for="Name">Flight Details (E.g; SQ 123, Arr/ Dep 1800 hrs) <span class="red">*</span></label>
                <input type="text" name="flight-details" id="flight-details" value="${flDetails}" required/>
              </div>
              <div class="input-group1">
                <label class="txt2" for="Name">For Special Requirements</label>
                <input type="text" name="special-requirements" id="special-requirements" value="${spRequirements}" />
              </div>
              
              <div class="btns-group text-center">
                <button type="submit"  class="btn btn-next">Submit</button>
              </div>
            </div>`;
    $("#body-from").append(appendHtml)
    $('.step3').remove()
}

function lastSubmitUpdate() {
    var appendHtml = `<div class="step3">
              <div class="btns-group text-center">
                <button type="submit"  class="btn btn-next">Submit</button>
              </div>
            </div>`;
    $("#body-from").append(appendHtml)
    $('.step2').remove()

}

// step one
$(document).ready(function () {
    var flag = true;
    var flag2 = true;
    var data = $('#my-data').data();
    console.log(data)
    if ($('#normal-trip').is(':checked')) {
        normalTripUpdate(data.job_type)
        flag = false;
        flag2 = true
    }

    if ($('#daily-trips').is(':checked')) {
        dailyTripsUpdate(data.start_date, data.end_date)
        flag2 = false;
        flag = true
    }
});

// step two
$(document).ready(function () {

    if ($('#normal-trip').is(':checked')) {
        var jobType = $('#job_type').val()
        var data = $('#my-data').data();

        if (jobType == 0) {
            $('.step2').remove()
            $('.step3').remove()
        }
        if (jobType == 1) {
            arrivalUpdate(data.meet_and_greet, data.flight_details, data.special_requirements)
        }
        else if (jobType > 1 || jobType >= 4) {
            $('.step2').remove()
            $('.step3').remove()
            lastSubmitUpdate()
        }
    }
});