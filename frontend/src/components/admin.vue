<template>
  <div class="admin-page">
    <h1>Admin Panel</h1>

    <div v-if="!authenticated" class="login-container">
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

    <div v-else class="form-container">
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
      try {
        const response = await this.$http.post('http://localhost:5000/api/authenticate', {
          username: this.username,
          password: this.password
        });
        if (response.data.success) {
          this.authenticated = true;
          this.errorMessage = '';
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
        this.plotName = '';
        this.plotLocation = '';
        this.plotSize = null;
        this.plotPrice = null;
        this.plotImageUrl = '';
        this.plotErrorMessage = '';
      } catch (error) {
        this.plotErrorMessage = 'Ошибка при добавлении участка. Попробуйте еще раз.';
        this.plotSuccessMessage = '';
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
  background-color: #f9f9f9;
  padding: 40px;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

h1 {
  color: #333;
  font-size: 2.5em;
  margin-bottom: 20px;
}

h2 {
  color: #555;
  margin-bottom: 20px;
}

.login-container, .form-container {
  width: 100%;
  max-width: 400px;
  background: white;
  padding: 30px;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

input[type="text"],
input[type="password"],
input[type="number"] {
  width: 100%;
  padding: 10px;
  margin-bottom: 15px;
  border: 1px solid #ddd;
  border-radius: 5px;
  font-size: 1em;
  transition: border 0.3s;
}

input[type="text"]:focus,
input[type="password"]:focus,
input[type="number"]:focus {
  border-color: #007bff;
  outline: none;
}

button {
  width: 100%;
  padding: 12px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 5px;
  font-size: 1em;
  cursor: pointer;
  transition: background-color 0.3s;
}

button:hover {
  background-color: #0056b3;
}

.error {
  color: red;
  margin-top: 10px;
  font-size: 0.9em;
}

.success {
  color: green;
  margin-top: 10px;
  font-size: 0.9em;
}
</style>
