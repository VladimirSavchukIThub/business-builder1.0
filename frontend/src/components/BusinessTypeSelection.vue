<template>
  <div class="business-type-selection">
    <h1>Выберите тип бизнеса</h1>
    <div class="business-types-container">
      <div
        v-for="businessType in businessTypes"
        :key="businessType.id"
        class="business-type-card"
        @click="selectBusinessType(businessType.id)"
      >
        <img :src="businessType.image_url" alt="Тип бизнеса" class="business-type-image" />
        <div class="business-type-info">
          <h2>{{ businessType.name }}</h2>
          <p>{{ businessType.description }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'; // Не забудьте установить axios, если еще не сделали это

export default {
  name: 'BusinessTypeSelection',
  data() {
    return {
      businessTypes: [] // Массив для хранения типов бизнеса
    };
  },
  mounted() {
    this.fetchBusinessTypes(); // Вызов метода для получения типов бизнеса
  },
  methods: {
    async fetchBusinessTypes() {
      try {
        const response = await axios.get('http://localhost:5000/business_types'); // Замените на ваш адрес API
        this.businessTypes = response.data; // Сохранение полученных данных
      } catch (error) {
        console.error('Ошибка при получении типов бизнеса:', error);
      }
    },
    selectBusinessType(businessTypeId) {
      // Перенаправление на конфигуратор в зависимости от типа бизнеса
      console.log('Выбран тип бизнеса с ID:', businessTypeId);
      switch (businessTypeId) {
        case 1:
          this.$router.push('/car-wash-configurator'); // Для автомойки
          break;
        case 2:
          this.$router.push('/restaurant-configurator'); // Для ресторана
          break;
        case 3:
          this.$router.push('/beauty-salon-configurator'); // Для салона красоты
          break;
        default:
          console.error('Неизвестный тип бизнеса');
      }
    }
  }
};
</script>

<style>
.business-type-selection {
  text-align: center;
  padding: 20px;
}

.business-types-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}

.business-type-card {
  background: #f9f9f9;
  border: 1px solid #ddd;
  border-radius: 10px;
  margin: 15px;
  padding: 20px;
  width: 200px;
  cursor: pointer;
  transition: transform 0.2s;
}

.business-type-card:hover {
  transform: scale(1.05);
}

.business-type-image {
  width: 100%;
  border-radius: 10px;
}

.business-type-info {
  margin-top: 10px;
}

.business-type-info h2 {
  font-size: 1.2em;
  margin: 10px 0;
}

.business-type-info p {
  font-size: 0.9em;
  color: #555;
}
</style>
