<template>
  <div class="admin-page">
    <h1>Admin Panel</h1>
    <div v-if="!authenticated">
      <h2>Enter Username and Password</h2>
      <form @submit.prevent="checkCredentials">
        <input
          type="text"
          v-model="username"
          placeholder="Введите имя пользователя"
          required
        />
        <input
          type="password"
          v-model="password"
          placeholder="Введите пароль"
          required
        />
        <button type="submit">Войти</button>
      </form>
      <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
    </div>

    <div v-else>
      <h2>Добавить Участок</h2>
      <form @submit.prevent="addPlot">
        <input
          type="text"
          v-model="plotName"
          placeholder="Название участка"
          required
        />
        <input
          type="text"
          v-model="plotLocation"
          placeholder="Расположение участка"
          required
        />
        <input
          type="number"
          v-model="plotSize"
          placeholder="Размер участка"
          required
        />
        <input
          type="number"
          v-model="plotPrice"
          placeholder="Цена участка"
          required
        />
        <input
          type="text"
          v-model="plotImageUrl"
          placeholder="Ссылка на изображение"
          required
        />
        <button type="submit">Добавить Участок</button>
      </form>
      <p v-if="plotSuccessMessage" class="success">{{ plotSuccessMessage }}</p>
      <p v-if="plotErrorMessage" class="error">{{ plotErrorMessage }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'AdminPage',
  data() {
    return {
      username: '',
      password: '',
      authenticated: false,
      errorMessage: '',
      plotName: '',
      plotLocation: '',
      plotSize: null,
      plotPrice: null,
      plotImageUrl: '',
      plotSuccessMessage: '',
      plotErrorMessage: ''
    };
  },
  methods: {
    async checkCredentials() {
    console.log('Button clicked, attempting to authenticate...'); // Логируем нажатие кнопки
    try {
      const response = await this.$http.post('http://localhost:5000/api/authenticate', {
        username: this.username,
        password: this.password
      });
      console.log('Response:', response.data);
        if (response.data.success) {
          this.authenticated = true;
          this.errorMessage = ''; // Clear error message on successful authentication
        } else {
          this.errorMessage = 'Неверные учетные данные';
        }
      } catch (error) {
        this.errorMessage = 'Ошибка при аутентификации. Попробуйте еще раз.';
      }
    },
    async addPlot() {
      try {
        await this.$http.post('http://localhost:5000/api/plots', {
            name: this.plotName,
            location: this.plotLocation,
            size: this.plotSize,
            price: this.plotPrice,
            image_url: this.plotImageUrl
        });
        this.plotSuccessMessage = 'Участок добавлен успешно';
        // Clear fields and messages
        this.plotName = '';
        this.plotLocation = '';
        this.plotSize = null;
        this.plotPrice = null;
        this.plotImageUrl = '';
        this.plotErrorMessage = '';
      } catch (error) {
        this.plotErrorMessage = 'Ошибка при добавлении участка. Попробуйте еще раз.';
        this.plotSuccessMessage = ''; // Clear success message if there's an error
      }
    }
  }
};
</script>

<style scoped>
.admin-page {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.error {
  color: red;
}

.success {
  color: green;
}
</style>
