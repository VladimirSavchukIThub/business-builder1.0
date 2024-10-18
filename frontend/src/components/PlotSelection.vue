<template>
  <div class="plot-selection">
    <h1>Выберите участок</h1>
    <div class="plots-container">
      <div
        v-for="plot in plots"
        :key="plot.id"
        class="plot-card"
        @click="selectPlot(plot.id)"
      >
        <img :src="plot.image_url" alt="Участок" class="plot-image" />
        <div class="plot-info">
          <h2>{{ plot.name }}</h2>
          <p>{{ plot.location }}</p>
          <p>{{ plot.size }} м²</p>
          <p class="plot-price">Цена: {{ plot.price }} руб.</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'PlotSelection',
  data() {
    return {
      plots: []  // Изначально пустой массив для участков
    };
  },
  created() {
    this.fetchPlots();  // Получение данных при создании компонента
  },
  methods: {
    async fetchPlots() {
      try {
        const response = await axios.get('http://localhost:5000/plots');  // Замените на ваш адрес API
        this.plots = response.data;  // Обновление массива plots данными из API
      } catch (error) {
        console.error('Ошибка при получении участков:', error);
      }
    },
    selectPlot(plotId) {
      console.log('Выбран участок с ID:', plotId);
      this.$router.push('/business-type-selection'); // Перенаправление на выбор типа бизнеса
    }
  }
};
</script>

<style>
.plot-selection {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
  background-color: #f5f5f5;
}

.plots-container {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 20px;
  width: 100%;
  max-width: 1200px; /* Максимальная ширина контейнера */
}

.plot-card {
  background: white;
  border: 1px solid #ccc;
  border-radius: 8px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  cursor: pointer;
  transition: transform 0.2s;
}

.plot-card:hover {
  transform: scale(1.05); /* Увеличение карточки при наведении */
}

.plot-image {
  width: 100%;
  height: 200px; /* Высота изображения */
  object-fit: cover; /* Подгонка изображения под размеры карточки */
  border-top-left-radius: 8px;
  border-top-right-radius: 8px;
}

.plot-info {
  padding: 15px;
}

.plot-price {
  font-weight: bold;
  color: #007bff; /* Цвет цены */
}
</style>
