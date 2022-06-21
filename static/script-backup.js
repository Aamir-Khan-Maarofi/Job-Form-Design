// step one

function normaltrip() {
    var appendHtml = `<div class="step0">
            <div class="input-group1">
                    <label class="txt2" for="job-type" >Job Type <span class="red">*</span></label>
                    <select name="job-type" id="job_type" class="input100">
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
  
  function dailytips() {
    var appendHtml = `<div class="step1">
              <div class="input-group1">
                    <label class="txt2" for="start-date">Start Date <span class="red">*</span></label>
                    <input type="date" name="start-date"  class="input100" id="start-date" required/>
              </div>
              <div class="input-group1">
                  <label class="txt2" for="end-date">End Date <span class="red">*</span></label>
                  <input type="date" name="end-date" class="input100" id="end-date"  class="input100" required/>
              </div>
              <div class="btns-group text-center contact100-form-btn">
                <button type="submit"  class="btn-next"><svg xmlns="http://www.w3.org/2000/svg" version="1.1" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:svgjs="http://svgjs.com/svgjs" width="20" height="20" x="0" y="0" viewBox="0 0 520 520" style="enable-background:new 0 0 512 512" xml:space="preserve" class=""><g><g xmlns="http://www.w3.org/2000/svg" id="_15-Checked" data-name="15-Checked"><path d="m232.019 422.469a10 10 0 0 1 -8.624-4.938c-33.227-56.607-121.81-177.14-122.7-178.351a10 10 0 0 1 1.027-13.039l27.239-26.918a10 10 0 0 1 12.755-1.085l88.222 61.6c59.034-75.7 113.87-128 149.946-158.861 40.616-34.738 66.471-50.377 67.553-51.021a10 10 0 0 1 5.145-1.425h44.068a10 10 0 0 1 6.65 17.469c-125.143 111.464-261.232 349.13-262.592 351.518a10 10 0 0 1 -8.624 5.05z" fill="#ffffff" data-original="#000000" class=""></path><path d="m230.1 464.132c-99.252 0-180-80.747-180-180s80.748-180 180-180a179.651 179.651 0 0 1 58.491 9.72 10 10 0 1 1 -6.5 18.916 159.712 159.712 0 0 0 -52-8.636c-88.225 0-160 71.776-160 160s71.775 160 160 160 160-71.776 160-160a161.236 161.236 0 0 0 -3.246-32.231 10 10 0 1 1 19.6-4.005 181.324 181.324 0 0 1 3.651 36.236c.004 99.253-80.744 180-179.996 180z" fill="#ffffff" data-original="#000000" class=""></path></g></g></svg> Submit</button>
              </div>
            </div>`;
    $("#body-from").append(appendHtml)
    $('.step0').remove()
    $('.step2').remove()
    $('.step3').remove()
  }
  
  function arrival() {
    var appendHtml = `<div class="step2">
          <div class="input-group1">
                <div class="row">
                  <div class="col-12">
                   <label class="txt2" for="Type-of-trip">Require Meet & Greet <span class="red">*</span></label>
                  </div>
                  <div class="row">
                    <div class="col-12">
                      <div class="form-check pl-01">
                        <input class="form-check-input" type="radio" name="Meet & Greet" value="Yes" id="meet-and-greet-yes"/>
                        <p-label class="form-check-label" for="meet-and-greet-yes">Yes</p-label>
                      </div>
                      
                      
                      <div class="form-check pl-01">
                        <input class="form-check-input" type="radio" name="Meet & Greet" value="No" id="meet-and-greet-no"/>
                        <p-label class="form-check-label" for="meet-and-greet-no"> No</p-label>
                      </div>
                    </div>
                  </div>
                        
                </div>
              </div>
              <div class="input-group1">
                <label class="txt2" for="Name">Flight Details (E.g; SQ 123, Arr/ Dep 1800 hrs) <span class="red">*</span></label>
                <input type="text" name="flight-details"  class="input100" id="flight-details" required/>
              </div>
              <div class="input-group1">
                <label class="txt2" for="Name">For Special Requirements</label>
                <input type="text" name="special-requirements"  class="input100" id="special-requirements" />
              </div>
              
              <div class="btns-group text-center contact100-form-btn">
              <button type="submit"  class="btn-next"><svg xmlns="http://www.w3.org/2000/svg" version="1.1" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:svgjs="http://svgjs.com/svgjs" width="20" height="20" x="0" y="0" viewBox="0 0 520 520" style="enable-background:new 0 0 512 512" xml:space="preserve" class=""><g><g xmlns="http://www.w3.org/2000/svg" id="_15-Checked" data-name="15-Checked"><path d="m232.019 422.469a10 10 0 0 1 -8.624-4.938c-33.227-56.607-121.81-177.14-122.7-178.351a10 10 0 0 1 1.027-13.039l27.239-26.918a10 10 0 0 1 12.755-1.085l88.222 61.6c59.034-75.7 113.87-128 149.946-158.861 40.616-34.738 66.471-50.377 67.553-51.021a10 10 0 0 1 5.145-1.425h44.068a10 10 0 0 1 6.65 17.469c-125.143 111.464-261.232 349.13-262.592 351.518a10 10 0 0 1 -8.624 5.05z" fill="#ffffff" data-original="#000000" class=""></path><path d="m230.1 464.132c-99.252 0-180-80.747-180-180s80.748-180 180-180a179.651 179.651 0 0 1 58.491 9.72 10 10 0 1 1 -6.5 18.916 159.712 159.712 0 0 0 -52-8.636c-88.225 0-160 71.776-160 160s71.775 160 160 160 160-71.776 160-160a161.236 161.236 0 0 0 -3.246-32.231 10 10 0 1 1 19.6-4.005 181.324 181.324 0 0 1 3.651 36.236c.004 99.253-80.744 180-179.996 180z" fill="#ffffff" data-original="#000000" class=""></path></g></g></svg> Submit</button>
            </div>
            </div>`;
    $("#body-from").append(appendHtml)
    $('.step3').remove()
  }
  
  function lastSubmit() {
    var appendHtml = `<div class="step3">
    <div class="btns-group text-center contact100-form-btn">
    <button type="submit"  class="btn-next"><svg xmlns="http://www.w3.org/2000/svg" version="1.1" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:svgjs="http://svgjs.com/svgjs" width="20" height="20" x="0" y="0" viewBox="0 0 520 520" style="enable-background:new 0 0 512 512" xml:space="preserve" class=""><g><g xmlns="http://www.w3.org/2000/svg" id="_15-Checked" data-name="15-Checked"><path d="m232.019 422.469a10 10 0 0 1 -8.624-4.938c-33.227-56.607-121.81-177.14-122.7-178.351a10 10 0 0 1 1.027-13.039l27.239-26.918a10 10 0 0 1 12.755-1.085l88.222 61.6c59.034-75.7 113.87-128 149.946-158.861 40.616-34.738 66.471-50.377 67.553-51.021a10 10 0 0 1 5.145-1.425h44.068a10 10 0 0 1 6.65 17.469c-125.143 111.464-261.232 349.13-262.592 351.518a10 10 0 0 1 -8.624 5.05z" fill="#ffffff" data-original="#000000" class=""></path><path d="m230.1 464.132c-99.252 0-180-80.747-180-180s80.748-180 180-180a179.651 179.651 0 0 1 58.491 9.72 10 10 0 1 1 -6.5 18.916 159.712 159.712 0 0 0 -52-8.636c-88.225 0-160 71.776-160 160s71.775 160 160 160 160-71.776 160-160a161.236 161.236 0 0 0 -3.246-32.231 10 10 0 1 1 19.6-4.005 181.324 181.324 0 0 1 3.651 36.236c.004 99.253-80.744 180-179.996 180z" fill="#ffffff" data-original="#000000" class=""></path></g></g></svg> Submit</button>
  </div>
            </div>`;
    $("#body-from").append(appendHtml)
    $('.step2').remove()
  
  }
  
  
  
  $(document).ready(function () {
    var flag = true;
    var flag2 = true;
  
    $('#normal-trip').click(function () {
  
      debugger
      if (flag) {
        if ($(this).is(':checked')) {
          normaltrip()
          flag = false;
          flag2 = true
        }
      }
  
    });
  
    $('#daily-trips').click(function () {
      if (flag2) {
        if ($(this).is(':checked')) {
          dailytips()
          flag2 = false;
          flag = true
        }
      }
  
  
    });
  });
  // step one
  
  // step two
  $(document).ready(function () {
    $('body').on('change', '#job_type', function () {
  
      if (this.value == 0) {
        $('.step2').remove()
        $('.step3').remove()
      }
      if (this.value == 1) {
        arrival()
  
      }
      else if (this.value >= 1 || this.value >= 4) {
        $('.step2').remove()
        $('.step3').remove()
        lastSubmit()
      }
  
  
    });
  });
  
  