import { Home, Services, Contact, Counter } from '../views/views.js';
import { render } from '../app.js';

export function router() {
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
