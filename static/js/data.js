const form = document.getElementById('frm');
const btnRegister = document.getElementById('btn_register');
const notify = document.querySelector('.info');
const url = 'http://localhost:5000/auth/register';
//const data = new FormData(form);
function registerUser() {
    form.addEventListener('submit', (event) => {
        event.preventDefault();
        //console.log('data2');
        data = {
            fname: form.elements['fname'].value,
            lname: form.elements['lname'].value,
            email: form.elements['email'].value,
            passwd: form.elements['passwd'].value,
            confirm: form.elements['confirm'].value
        };

        if (data.passwd === data.confirm) {
            postInputData(url, data).then(
                (response) => {
                    console.log(response);
                })
                .catch((err) => {
                    console.log('Error:', err);
                });
        } else {
            notify.innerHTML = 'Password doesn\'t match!';
        }        
    });
}
async function postInputData(url='', data) {
    const res = await fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    });
    return await res.json();
}



registerUser();