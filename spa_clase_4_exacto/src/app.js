import { navbar } from './components/Navbar.js';
import { router } from './router/router.js';

const app = document.getElementById('app');

export function render(view){
    app.innerHTML = `
    ${navbar()}
    <main>
    ${view}
    </main>`
}

window.addEventListener('hashchange', router);
window.addEventListener('load', router);
