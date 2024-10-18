<template>
  <div class="configurator">
    <h1>Конфигуратор Мойки</h1>
    <p>Настройки мойки самообслуживания</p>

    <div class="input-container">
      <label for="boxCount">Количество боксов:</label>
      <input type="number" id="boxCount" v-model="boxCount" min="1" />
    </div>

    <div class="checkbox-container">
      <label>
        <input type="checkbox" v-model="vacuumStand" />
        Нужен стенд с пылесосами
      </label>
    </div>

    <div class="payment-methods">
      <h3>Тип оплаты:</h3>
      <button @click="setPaymentMethod('card')" :class="{ active: paymentMethod === 'card' }">Картой</button>
      <button @click="setPaymentMethod('token')" :class="{ active: paymentMethod === 'token' }">Жетонами</button>
    </div>

    <button @click="saveConfiguration" class="save-button">Сохранить конфигурацию</button>

    <div v-if="showModal" class="modal">
      <div class="modal-content">
        <h2>Итоговая цена: {{ totalPrice }} руб. + цена участка</h2>
        <form @submit.prevent="submitForm">
          <input type="text" v-model="customerName" placeholder="Имя" required />
          <input type="text" v-model="customerSurname" placeholder="Фамилия" required />
          <input type="tel" v-model="customerPhone" placeholder="Номер телефона" required />
          <input type="email" v-model="customerEmail" placeholder="Электронная почта" required />
          <button type="submit" class="submit-button">Отправить</button>
          <button type="button" class="close-button" @click="closeModal">Закрыть</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'CarWashConfigurator',
  data() {
    return {
      boxCount: 1,
      vacuumStand: false,
      paymentMethod: '',
      showModal: false,
      customerName: '',
      customerSurname: '',
      customerPhone: '',
      customerEmail: '',
      basePrice: 5000,
      plotPrice: 0, // Добавляем переменную для цены участка
    };
  },
  computed: {
    totalPrice() {
      // Итоговая цена складывается из базовой цены, цены боксов, пылесосов и цены участка
      let price = this.basePrice + this.boxCount * 100000;
      if (this.vacuumStand) {
        price += 200000;
      }
      return price + this.plotPrice; // Добавляем цену участка
    }
  },
  mounted() {
    // Получаем цену участка из параметров маршрута
    this.plotPrice = parseFloat(this.$route.query.plotPrice) || 0;
  },
  methods: {

    setPaymentMethod(method) {
      this.paymentMethod = method;
    },
    saveConfiguration() {
      this.showModal = true;
    },
    closeModal() {
      this.showModal = false;
    },
    submitForm() {
      const customerData = {
        name: this.customerName,
        surname: this.customerSurname,
        phone: this.customerPhone,
        email: this.customerEmail,
      };
      console.log('Данные клиента:', customerData);

      // Перенаправление на страницу спасибо
      this.$router.push({ name: 'thank-you' });

      this.closeModal();
      this.customerName = '';
      this.customerSurname = '';
      this.customerPhone = '';
      this.customerEmail = '';
    },
  },
};
</script>


<style scoped>
.configurator {
  text-align: center;
  padding: 40px;
  background-color: #f3f4f6;
  border-radius: 10px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  max-width: 500px;
  margin: auto;
}

h1 {
  color: #333;
  font-size: 2em;
  margin-bottom: 20px;
}

p {
  color: #555;
  font-size: 1.2em;
  margin-bottom: 30px;
}

.input-container {
  margin-bottom: 20px;
}

input[type="number"],
input[type="text"],
input[type="tel"],
input[type="email"] {
  width: 100%;
  padding: 10px;
  font-size: 1em;
  border: 1px solid #ddd;
  border-radius: 5px;
  transition: border 0.3s;
}

input[type="number"]:focus,
input[type="text"]:focus,
input[type="tel"]:focus,
input[type="email"]:focus {
  border: 1px solid #007bff;
  outline: none;
}

.save-button {
  background-color: #28a745;
  color: white;
  padding: 10px 20px;
  font-size: 1em;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.save-button:hover {
  background-color: #218838;
}

.modal {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
}

.modal-content {
  background: white;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
  width: 300px;
}

.submit-button {
  background-color: #007bff;
  color: white;
  padding: 10px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  width: 100%;
  transition: background-color 0.3s;
}

.submit-button:hover {
  background-color: #0056b3;
}

.close-button {
  background-color: #dc3545;
  color: white;
  padding: 10px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  width: 100%;
  margin-top: 10px;
}

.close-button:hover {
  background-color: #c82333;
}

.payment-methods {
  margin: 20px 0;
}

.payment-methods button {
  margin: 0 5px;
  padding: 10px 15px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.payment-methods .active {
  background-color: #007bff;
  color: white;
}
</style>
