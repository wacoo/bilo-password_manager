import { Navigation } from "./navigation.js";
import { loginUser } from "./data.js";

function createElement(type, cls, id) {
    const element = document.createElement(type);
    if(cls) {
        for(let i = 0; i < cls.length; i += 1) {
            element.classList.add(cls[i]);
        }        
    }
    if(id) {
        element.id = id;
    }
        
    return element;    
}


function createBox(parent, data,idx) {
    const topBar = createElement('div', ['top-bar'], null);
    const h3 = createElement('h3', null, null);
    const cred_wrapper = createElement('div', ['cred_wrapper'], null);
    h3.innerHTML = data.title[idx];

    topBar.appendChild(h3);
    parent.appendChild(topBar);
    for(let i = 0; i < 3; i += 1) {
        const box = createElement('div', ['box'], null);
        const img = createElement('img', null, null);
        const p1 = createElement('p', null, null);
        const p2 = createElement('p', null, null);
        const p3 = createElement('p', null, null);
        const p4 = createElement('p', null, null);

        img.src = data.image[idx];
        if (idx === 0) {
            p1.innerHTML = data.data['credentials'][i].url;
            p2.innerHTML = data.data['credentials'][i].username;
            p3.innerHTML = data.data['credentials'][i].password;
            p3.innerHTML = data.data['credentials'][i].auto_fill;
            //console.log(data);
        } else {
            p1.innerHTML = data.data['notes'][0].description;
            //console.log(data.data['notes'][0].description);
        }
        

        box.appendChild(img);
        box.append(p1, p2, p3, p4);
        cred_wrapper.appendChild(box);        
    }
    parent.appendChild(cred_wrapper);
}

function fillHome() {
    const nav = new Navigation();
    let tkn = sessionStorage.getItem('token');
    console.log(tkn);
    if(tkn) {
        let data = JSON.parse(sessionStorage.getItem('data'));
        const ud = {
            title: ['Credentials', 'Notes'],
            image: ['static/images/default-icon.png', 'static/images/notepad.png'],
            data: data
        }
        //console.log(data);
        //console.log(data['credentials'][0].url);
        createBox(credentials, ud, 0);
        createBox(notes, ud, 1);
    } else {
        nav.showLogin();
        loginUser('passwd');
    }
}

export { createBox, fillHome };
    