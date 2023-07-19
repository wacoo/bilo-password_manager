import { registerUser, loginUser,loadUserData } from "./modules/data.js";
import { Navigation } from "./modules/navigation.js";
import { fillHome } from "./modules/nodes.js";

const notes = document.getElementById('notes');
const credentials = document.getElementById('credentials');

const nav = new Navigation();

registerUser();
loginUser();

nav.showHome();
fillHome();
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
