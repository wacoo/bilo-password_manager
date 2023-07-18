import { loadUserData } from "./data.js";
const register = document.querySelector('.register');
const login = document.querySelector('.login');
const userHome = document.querySelector('.user_home');
const linkToRegister = document.getElementById('link_register');

export class Navigation {
    showLogin() {
        login.style.display = 'flex';
        register.style.display = 'none';
        userHome.style.display = 'none';
    }
    
    showRegister() {
        login.style.display = 'none';
        register.style.display = 'flex';
        userHome.style.display = 'none';
    }
    
    showHome() {
        login.style.display = 'none';
        register.style.display = 'none';
        userHome.style.display = 'flex';
        loadUserData();
    }
    
    addRegLinkListener = () => {
        linkToRegister.addEventListener('click', (event) => {
            event.preventDefault();
            this.showRegister();
        });
    }
}
