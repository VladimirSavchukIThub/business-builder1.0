<template>
  <div class="thank-you">
    <h1>Спасибо за заказ!</h1>
    <p>Мы с вами свяжемся в ближайшее время.</p>
    <router-link to="/" class="back-link">Вернуться на главную</router-link>
  </div>
</template>

<script>
export default {
  name: 'ThankYou',
};
</script>

<style scoped>
.thank-you {
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

.back-link {
  color: #007bff;
  text-decoration: none;
}

.back-link:hover {
  text-decoration: underline;
}
</style>
