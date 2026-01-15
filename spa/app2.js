const app = document.getElementById('app');


function navbar (){
    return`
    <nav>
    <button><a href="#/home">home</a></button>
    <button><a href="#/services">servicios</a></button>
    <button><a href="#/contact">contacto</a></button>
    <button><a href="#/counter">contador</a></button>
</nav>`;
}

function render(view){
    app.innerHTML = `
    ${navbar()}
    <main>
    ${view}
    </main>`
}


function Home() {
  return  '<h1>🏠 Home</h1><p>Bienvenido a nuestra spa</p>';
}

function Services() {
  return  '<h1>🛠️ Servicios</h1><p> fronted con js </p>';
}

function Contact() {
  return  '<h1>📩 Contacto</h1><p> clan@hamilton </p>';
}


let counter = 0;
function Counter(){
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


function increment() {
       document.getElementById('add').onclick = ()=> {
        counter++;
        Counter();
    }

    document.getElementById('dismin').onclick = ()=> {
        counter--;
        Counter();
    }
}

function router() {
  const route = location.hash;

  switch (route) {
    case '#/home':
      render(Home());
      break;
    case '#/services':
      render(Services());
      break;
    case '#/contact':
      render(Contact());
      break;
    case '#/counter':
        Counter();
        break;
    default:
      render(Home());
  }
}

window.addEventListener('hashchange', router);
window.addEventListener('load', router);


