import { createRouter, createWebHistory } from 'vue-router';
import WelcomePage from '../components/WelcomePage.vue';
import PlotSelection from '../components/PlotSelection.vue';
import BusinessTypeSelection from '../components/BusinessTypeSelection.vue';
import CarWashConfigurator from '../components/CarWashConfigurator.vue';
import RestaurantConfigurator from '../components/RestaurantConfigurator.vue';
import BeautySalonConfigurator from '../components/BeautySalonConfigurator.vue';
import ThankYou from '../components/ThankYou.vue'; // Импортируйте компонент ThankYou
import admin from '../components/admin.vue'; // Импортируйте компонент Admin

const routes = [
  { path: '/', component: WelcomePage },
  { path: '/plot-selection', component: PlotSelection },
  { path: '/business-type-selection', component: BusinessTypeSelection },
  { path: '/car-wash-configurator', component: CarWashConfigurator },
  { path: '/restaurant-configurator', component: RestaurantConfigurator },
  { path: '/beauty-salon-configurator', component: BeautySalonConfigurator },
  { path: '/thank-you', component: ThankYou, name: 'thank-you' }, // Добавлено имя маршрута
  { path: '/admin', component: admin }, // Добавлено новый маршрут для Admin
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
