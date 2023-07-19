import { Navigation } from "./navigation.js";
import { fillHome } from "./nodes.js";

const form_register = document.getElementById('frm_register');
const form_login = document.getElementById('frm_login');
const btnRegister = document.getElementById('btn_register');
const notifyReg = document.querySelector('.info_register');
const notifyLog = document.querySelector('.info_login');
const url_reg = 'http://localhost:5000/auth/register';
const url_log = 'http://localhost:5000/auth/login';
const url_home = 'http://localhost:5000/view/';

const nav = new Navigation();
function registerUser() {
  form_register.addEventListener('submit', (event) => {
    event.preventDefault();
    const data = {
      fname: form_register.elements['fname'].value,
      lname: form_register.elements['lname'].value,
      email: form_register.elements['email'].value,
      passwd: form_register.elements['passwd'].value,
      confirm: form_register.elements['confirm'].value
    };

    if (data.passwd === data.confirm) {
      postInputData(url_reg, data).then(
        (response) => {
          notifyReg.innerHTML = response.message;

        })
        .catch((err) => {
          console.log('Error:', err);
          notifyReg.innerHTML = `Error:, ${err}`;
          
        });
    } else {
      notify.innerHTML = 'Password doesn\'t match!';
    }
  });
}

function loginUser(type='passwd') {
  form_login.addEventListener('submit', (event) => {
    event.preventDefault();
    const data = {
      email: form_login.elements['email_login'].value,
      passwd: form_login.elements['passwd_login'].value
    };
    let headers = new Headers();
    if (type === 'passwd') {
      console.log('pass');
      headers.append('Content-Type', 'application/json');

    } else if (type === 'token'){
      console.log('token');
      const token = sessionStorage.getItem('token');
      headers.append('Authorization', `Bearer ${token}`);
    }
    console.log('Headers:', headers);
    console.log('Data:', data);
    postInputData(url_log, headers, data).then(
      (response) => {
        notifyLog.innerHTML = response.token;
        sessionStorage.setItem('token', response.token);
        sessionStorage.setItem('email', response.email);
        nav.showHome();
        fillHome();        
      })
      .catch((err) => {
        console.log('Error:', err);
        notifyLog.innerHTML = `Error:, ${err}`;
      });
    

  });
}

async function postInputData(url = '', headers, data) {
  const res = await fetch(url, {
    method: 'POST',
    headers: headers,
    body: JSON.stringify(data)
  });
  return await res.json();
}

function loadUserData() {
  let tkn = sessionStorage.getItem('token');
  let email = sessionStorage.getItem('email');
  let headers = new Headers();
  if(tkn) {
    const data = {
      email: email 
    };
    headers.append('Authorization', `Bearer ${tkn}`)
    postInputData(url_home, headers, data).then(
      (response) => {
        //notifyLog.innerHTML = response.token;
        console.log(response);
        sessionStorage.setItem('data', JSON.stringify(response));     
      })
      .catch((err) => {
        console.log('Error:', err);
        notifyLog.innerHTML = `Error:, ${err}`;
      });
    }
}

export {registerUser, loginUser, loadUserData};