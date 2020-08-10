document.addEventListener('DOMContentLoaded', function() {
  // **REGISTER**

    document.querySelector('#submit-register').onclick = () => {
     
    const username = document.querySelector('#register-username').value;
    const password = document.querySelector('#register-password').value;
    const first_name = document.querySelector('#register-first-name').value;
    const last_name = document.querySelector('#register-last-name').value;
    const email = document.querySelector('#register-email').value;
    const key=document.querySelector('#key').value
    if (username !== '' && password !== '' && first_name !== '' && last_name !== '' && email !== '' && key=='577ash2fkwd') {

    let request = new XMLHttpRequest();
    request.open('POST', '/register');
    const csrf_token = document.querySelector('#csrf').childNodes[0]['value'];
    request.setRequestHeader("X-CSRFToken", csrf_token);

     let register_data = new FormData();
     register_data.append('username', username);
     register_data.append('password', password);
     register_data.append('first_name', first_name);
     register_data.append('last_name', last_name);
     register_data.append('email', email);

    
     request.send(register_data);
     request.onload = () => {
       const response = request.responseText;
       const success = JSON.parse(response)['success'];
       const error_message = JSON.parse(response)['message'];
       
       // If views.py returns a JSON response where success = true, 
       // the page is reloaded in order to redirect the user to index.html.
       if (success === true) {
         window.location.href = '/';
       } else {
         document.querySelector('.error-register').innerHTML = error_message;
       }
     };

     
     return false;
   
   } else {
     document.querySelector('.error-register').innerHTML = 'All fields are required.'
   };
   return false;
 };
   // **LOGIN**

 document.querySelector('#submit-login').onclick = () => {
   
   const username = document.querySelector('#username').value;
   const password = document.querySelector('#password').value;
   
   if (username !== '' && password !== '') {

     
     const request = new XMLHttpRequest();
     request.open('POST', '/login');
     const csrf_token = document.querySelector('#csrf').childNodes[0]['value'];
     request.setRequestHeader("X-CSRFToken", csrf_token);

     const login_data = new FormData();
     login_data.append('username', username);
     login_data.append('password', password);

    
     request.send(login_data);
     request.onload = () => {
       const response = request.responseText;
       const success = JSON.parse(response)['success'];
       const error_message = JSON.parse(response)['message'];


       if (success === true) {
         window.location.href = '/';
       } else {
         document.querySelector('.error-login').innerHTML = error_message;
       }
     };
     
     return false;

   
   } else {
     document.querySelector('.error-login').innerHTML = 'Both username and password are required.'
   };
   return false;
 };
})
