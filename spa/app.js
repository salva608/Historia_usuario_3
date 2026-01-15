const app = document.getElementById('app');

function renderHome() {
  app.innerHTML = '<h1>🏠 Home</h1><p>Bienvenido a nuestra spa</p>';
}

function renderServices() {
  app.innerHTML = '<h1>🛠️ Servicios</h1><p> fronted con js </p>';
}

function renderContact() {
  app.innerHTML = '<h1>📩 Contacto</h1><p> clan@hamilton </p>';
}

let counter = 0;
function renderCounter(){
    app.innerHTML = `
    <h1>Contador</h1>
    <p>${counter}</p>
    <button id = 'add' >+</button>
    <button id = 'dismin' >-</button>
    `;

    document.getElementById('add').onclick = ()=> {
        counter++;
        renderCounter();
    }

    document.getElementById('dismin').onclick = ()=> {
        counter--;
        renderCounter();
    }
}



function router() {
  const route = location.hash;

  switch (route) {
    case '#/home':
      renderHome();
      break;
    case '#/services':
      renderServices();
      break;
    case '#/contact':
      renderContact();
      break;
    case '#/counter':
        renderCounter();
        break;
    default:
      renderHome();
  }
}

window.addEventListener('hashchange', router);
window.addEventListener('load', router);


