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
    var data = $('#my-data').data();

    if ($('#normal-trip').is(':checked')) {
        var jobType = $('#job_type').val()

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


// Step one and two for edit
// step one
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


//time pickers
$(document).ready(function () {
    var data = $('#my-data').data();
    var pickup_option = {
        now: data.pickup_time,
        title: 'Pickup Timing Title'
    };

    var return_option = {
        now: data.return_time,
        title: 'Return Timing Title'
    };

    // Time Picker Code
    $('.pickup-timing').wickedpicker(pickup_option);
    console.log(data.return_time == "None")
    if (data.return_time != "None") {
        let appendHTML = `
          <label class="txt2" for="return-timing">Return Timing (If required)</label>
          <input type="text" name="return-timing" id="return-timing"  class="return-timing input100" required />      
        `
        $('#return-time-div').append(appendHTML)
        $('.return-timing').wickedpicker(return_option);
        console.log("ADDED EXISTING RETURN TIME");
    }
    else {
        console.log("DO NOT ADDED EXISTING RETURN TIME");
    }

    $(document).on('change', '[name="toggle-return-timing"]', function () {
        var checkbox = $(this), // Selected or current checkbox
            value = checkbox.val(); // Value of checkbox

        if (checkbox.is(':checked')) {
            let appendHTML = `
          <label class="txt2" for="return-timing">Return Timing (If required)</label>
          <input type="text" name="return-timing" id="return-timing"  class="return-timing input100" required />      
        `

            $('#return-time-div').append(appendHTML)
            var return_option = {
                now: "00:00:00",
                title: 'Return Timing Title'
            };
            $('.return-timing').wickedpicker(return_option);
        } else {
            $('#return-time-div').empty();
        }
    });
});