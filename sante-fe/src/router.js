import {
  createRouter,
  createWebHistory
} from "vue-router";
import App from './App.vue';
import LogIn from './components/LogIn.vue'
import SignUp from './components/SignUp.vue'
import Home from './components/Home.vue'

// Imports Paciente
import Paciente from './components/Paciente.vue'
import PacienteCreate from './components/PacienteCreate.vue'
import PacienteSearch from './components/PacienteSearch.vue'
import PacienteDetail from './components/PacienteDetail.vue'

// Imports personal salud
import Personalsalud from './components/Personalsalud.vue'
import PersonalSaludCreate from './components/PersonalSaludCreate.vue'
import PersonalSaludSearch from './components/PersonalSaludSearch.vue'
import PersonalSaludDetail from './components/PersonalSaludDetail.vue'


// Imorts Familiar
import Familiar from './components/Familiar.vue'
import FamiliarCreate from './components/FamiliarCreate.vue'
import FamiliarSearch from './components/FamiliarSearch.vue'
import FamiliarDetail from './components/FamiliarDetail.vue'

// Imorts Historia clinica
import Historia_clinica from './components/Historia_clinica.vue'
import Historia_clinicaCreate from './components/Historia_clinicaCreate.vue'
import Historia_clinicaDetail from './components/Historia_clinicaDetail.vue'
import Historia_clinicaSearch from './components/Historia_clinicaSearch.vue'





// //Imports Signos vitales
import SignosVitales from './components/Signos_Vitales.vue'
import Signos_VitalesCreate from './components/Signos_VitalesCreate.vue'

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
    path: '/user/Paciente',
    name: "paciente",
    component: Paciente
  },
  {
    path: '/user/Paciente/create',
    name: "pacientecreate",
    component: PacienteCreate
  },
  {
    path: '/user/Paciente/search',
    name: "pacientesearch",
    component: PacienteSearch
  },
  {
    path: '/user/Paciente/detail',
    name: "pacientedetail",
    component: PacienteDetail
  },
  {
    path: '/user/familiar',
    name: "familiar",
    component: Familiar
  },
  {
    path: '/user/familiar/search',
    name: "FamiliarSearch",
    component: FamiliarSearch
  },
  {
    path: '/user/familiar/create',
    name: "FamiliarCreate",
    component: FamiliarCreate
  },
  {
    path: '/user/familiar/detail',
    name: "FamiliarDetail",
    component: FamiliarDetail
  },
  {
    path: '/user/Signosvitales',
    name: "signosvitales",
    component: SignosVitales
  },
  {
    path: '/user/Historiaclinica',
    name: "historiaclinica",
    component: Historia_clinica
  },
  {
    path: '/user/Historiaclinica/create',
    name: "historiaclinicacreate",
    component: Historia_clinicaCreate
  },
  {
    path: '/user/Historiaclinica/search',
    name: "historiaclinicasearch",
    component: Historia_clinicaSearch
  },
  {
    path: '/user/Historiaclinica/detail',
    name: "historiaclinicadetail",
    component: Historia_clinicaDetail
  },
  {
    path: '/user/Personalsalud',
    name: "personalsalud",
    component: Personalsalud
  },
{
  path: '/user/Personalsalud/create',
  name: "createPs",
  component: PersonalSaludCreate
},
{
  path: '/user/Personalsalud/Search',
  name: "searchPs",
  component: PersonalSaludSearch
},
{
  path: '/user/personalsalud/detail',
  name: "pssingle",
  component: PersonalSaludDetail
},
  
];
const router = createRouter({
  history: createWebHistory(),
  routes,
});
export default router;