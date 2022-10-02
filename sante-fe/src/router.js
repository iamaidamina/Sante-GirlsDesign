import {
  createRouter,
  createWebHistory
} from "vue-router";
import App from './App.vue';
import LogIn from './components/LogIn.vue'
import SignUp from './components/SignUp.vue'
import Home from './components/Home.vue'
import Personalsalud from './components/Personalsalud.vue'
import CreatePs from './components/CreatePs.vue'
import SearchPs from './components/SearchPs.vue'
import Familiar from './components/Familiar.vue'
import Historia_clinica from './components/Historia_clinica.vue'
import Signos_vitales from './components/Signos_Vitales.vue'
import Paciente from './components/Paciente.vue'

const routes = [{
      path: '/',
      name: 'root',
      component: App
  },
  {
      path: '/user/logIn',
      name: "logIn",
      component: LogIn
  },
  {
      path: '/user/signUp',
      name: "signUp",
      component: SignUp
  },
  {
    path: '/user/home',
    name: "home",
    component: Home
    },
    {
      path: '/user/Personalsalud',
      name: "personalsalud",
      component: Personalsalud
  },
  {
    path: '/user/Personalsalud/create',
    name: "createPs",
    component: CreatePs
  },
  {
    path: '/user/Personalsalud/Search',
    name: "searchPs",
    component: SearchPs
  },
  {
    path: '/user/Paciente',
    name: "paciente",
    component: Paciente
  },
  {
    path: '/user/familiar',
    name: "familiar",
    component: Familiar
  },
  {
    path: '/user/Signosvitales',
    name: "signosvitales",
    component: Signos_vitales
  },
  {
    path: '/user/Historiaclinica',
    name: "historiaclinica",
    component: Historia_clinica
  },
  
];
const router = createRouter({
  history: createWebHistory(),
  routes,
});
export default router;