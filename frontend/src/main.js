import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import axios from 'axios'; // Импортируем Axios

const app = createApp(App);

app.config.globalProperties.$http = axios; // Добавляем Axios в глобальные свойства

app.use(router).mount('#app');