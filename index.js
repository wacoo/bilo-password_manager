import { registerUser, loginUser,loadUserData } from "./modules/data.js";
import { Navigation } from "./modules/navigation.js";
import { createBox } from "./modules/nodes.js";

const notes = document.getElementById('notes');
const credentials = document.getElementById('credentials');

const nav = new Navigation();

registerUser();
loginUser();
let tkn = sessionStorage.getItem('token');
console.log(tkn);
if(tkn) {
    nav.showHome();
    let data = sessionStorage.getItem('data');
    const ud = {
        title: ['Credentials', 'Notes'],
        image: ['static/images/default-icon.png', 'static/images/notepad.png'],
        data: data
    }
    //console.log(data);
    createBox(credentials, ud, 0);
    createBox(notes, ud, 1);
} else {
    nav.showLogin();
    loginUser('passwd');
}

nav.addRegLinkListener();
/*
const cred_data = {
    title: 'Credentials',
    p1: 'https://facebook.com',
    image: 'static/images/default-icon.png'
}

const note_data = {
    title: 'Secure Notes',
    p1: 'Tomorrow\'s presidential schedule',
    image: 'static/images/notepad.png'
}*/
//const data = sessionStorage.getItem(data);
