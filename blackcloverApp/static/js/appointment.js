document.addEventListener('DOMContentLoaded', function() { 

    document.querySelector('#submit-form').onclick = () => {
    const fname = $('#fname').value;
    const lname = $('#lname').value;
    const phone = $('#phone').value;
    const email = $('#email').value;    
    const doctor = $('#doctor').value;
    const date = $('#date').value;
    const time = $('#time').value;
    const comment = $('#comment').value;

    let request = new XMLHttpRequest();
    request.open('POST', '/appointment')
    var csrf_token = $("[name=csrfmiddlewaretoken]").val();
    request.setRequestHeader("X-CSRFToken", csrf_token);


    
      let appointment_data = new FormData();
      appointment_data.append('fname', fname);
      appointment_data.append('lname', lname);
      appointment_data.append('phone', phone);
      appointment_data.append('email', email);     
      appointment_data.append('doctor', doctor);
      appointment_data.append('date', date);
      appointment_data.append('time', time);
      appointment_data.append('comment', comment);

      
        request.send(appointment_data);
        request.onload = () => {
          const response = request.responseText;
          const success = JSON.parse(response)['success'];
          const error_message = JSON.parse(response)['message'];
       
       if (success === true) {
         window.location.href = '/';
    }
}
}
})
