import { render } from '../app.js';

export function Home() {
  return  '<h1>🏠 Home</h1><p>Bienvenido a nuestra spa</p>';
}

export function Services() {
  return  '<h1>🛠️ Servicios</h1><p> fronted con js </p>';
}

export function Contact() {
  return  '<h1>📩 Contacto</h1><p> clan@hamilton </p>';
}

let counter = 0;

export function Counter(){
    render(`
    <h1>Contador</h1><p>${counter}</p>
    <button id = 'add' >+</button>
    <button id = 'dismin' >-</button>
    `);

    document.getElementById('add').onclick = ()=> {
        counter++;
        Counter();
    }

    document.getElementById('dismin').onclick = ()=> {
        counter--;
        Counter();
    }
}
