<template>
  <div class="configurator">
    <h1>Конфигуратор Салона Красоты</h1>
    <p>Настройки салона красоты</p>

    <div class="input-container">
      <label for="treatmentCount">Количество процедур:</label>
      <input type="number" id="treatmentCount" v-model="treatmentCount" min="1" />
    </div>

    <div class="input-container">
      <label for="staffCount">Количество сотрудников:</label>
      <input type="number" id="staffCount" v-model="staffCount" min="1" />
    </div>

    <div class="input-container">
      <label for="equipmentCount">Количество оборудования:</label>
      <input type="number" id="equipmentCount" v-model="equipmentCount" min="1" />
    </div>

    <button @click="saveConfiguration" class="save-button">Сохранить конфигурацию</button>

    <!-- Модальное окно с формой -->
    <div v-if="showModal" class="modal">
      <div class="modal-content">
        <h2>Итоговая цена: {{ totalPrice }} руб.</h2>
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
  name: 'BeautySalonConfigurator',
  data() {
    return {
      treatmentCount: 1,
      staffCount: 1,
      equipmentCount: 1,
      showModal: false,
      customerName: '',
      customerSurname: '',
      customerPhone: '',
      customerEmail: '',
      basePrice: 100000,
    };
  },
  computed: {
    totalPrice() {
      let price = this.basePrice + this.treatmentCount * 20000 + this.staffCount * 30000 + this.equipmentCount * 25000;
      return price;
    }
  },
  methods: {
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
  background-color: #f9f9f9;
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
</style>
