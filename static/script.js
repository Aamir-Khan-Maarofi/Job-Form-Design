$(document).ready(function () {
  var flag = true;
  var flag2 = true;

  $('#normal-trip').click(function () {

    if (flag) {
      if ($(this).is(':checked')) {
        normaltrip()
        flag = false;
        flag2 = true
      }
    }
  });

  $('#daily-trips').click(function () {
    console.log("DAILY JOB")
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

var pickup_option = {
  now: "00:00:00",
  title: 'Pickup Timing Title'
};

var return_option = {
  now: "00:00:00",
  title: 'Return Timing Title'
};

$('.pickup-timing').wickedpicker(pickup_option);

$('#return-time-div').empty();
$(document).on('change', '[name="toggle-return-timing"]', function () {
  var checkbox = $(this), // Selected or current checkbox
    value = checkbox.val(); // Value of checkbox

  if (checkbox.is(':checked')) {
    let appendHTML =
      `
        <label class="txt2" for="return-timing">Return Timing (If required)</label>
        <input type="text" name="return-timing" id="return-timing" class="return-timing" required />      
      `

    $('#return-time-div').append(appendHTML)
    $('.return-timing').wickedpicker(return_option);
  } else {
    $('#return-time-div').empty();
  }
});