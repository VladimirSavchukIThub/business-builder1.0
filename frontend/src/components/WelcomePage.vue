<template>
  <div class="welcome-page">
    <header class="header">
      <nav>
        <ul class="nav-list">
          <li class="nav-item">
            <router-link to="/" class="nav-link">Главная</router-link>
          </li>
          <li class="nav-item">
            <a href="#about" class="nav-link">О нас</a> <!-- Anchor link to About -->
          </li>
          <li class="nav-item">
            <a href="#contacts" class="nav-link">Контакты</a> <!-- Anchor link to Contacts -->
          </li>
        </ul>
      </nav>
    </header>

    <!-- Updated image container -->
    <div class="image-container">
      <img
        src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRb4o08sB1kzDT5_ax1AMHgY4xGwm5lf0PoxA&s"
        alt="Business Builder"
        class="header-image"
      />
    </div>

    <div class="content">
      <h1>Добро пожаловать в конструктор бизнеса</h1>
      <button @click="start" class="continue-button">Продолжить</button>
    </div>

    <section id="about" class="about-section">
      <h2>О нас</h2>
      <p>
        Мы команда профессионалов, готовая помочь вам создать успешный бизнес. Наша цель - сделать процесс
        создания бизнеса простым и удобным для вас.
      </p>
    </section>

    <section id="contacts" class="contacts-section">
      <h2>Контакты</h2>
      <p>
        Вы можете связаться с нами по следующим каналам:
      </p>
      <ul>
        <li>Email: info@businessbuilder.com</li>
        <li>Телефон: +7 (123) 456-7890</li>
        <li>Адрес: г. Москва, ул. Примерная, д. 1</li>
      </ul>
    </section>
  </div>
</template>

<script>
export default {
  name: 'WelcomePage',
  methods: {
    start() {
      this.$router.push('/plot-selection');
    }
  }
};
</script>

<style scoped>
.welcome-page {
  display: flex;
  flex-direction: column;
  justify-content: flex-start; /* Changed to flex-start for better stacking */
  height: auto; /* Changed height to auto to fit content */
  background-color: #f5f5f5;
}

.header {
  max-width: 800px; /* Set a maximum width for the header */
  margin: 0 auto; /* Center the header */
  padding: 10px 20px;
  background-color: #007bff;
  border-radius: 10px; /* Rounded corners */
}

.nav-list {
  display: flex;
  justify-content: center; /* Center the navigation items */
  list-style: none;
  margin: 0;
  padding: 0;
}

.nav-item {
  margin-left: 20px;
}

.nav-link {
  color: white;
  text-decoration: none;
  font-size: 16px;
}

.nav-link:hover {
  text-decoration: underline;
}

/* Updated styles for the image container */
.image-container {
  width: 100%; /* Full width */
  overflow: hidden; /* Prevent overflow */
}

.header-image {
  width: 100%; /* Make the image full width */
  height: auto; /* Maintain aspect ratio */
}

.content {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  flex-grow: 1;
  margin-top: 20px; /* Added margin to separate from image */
}

.continue-button {
  padding: 15px 30px;
  font-size: 20px;
  color: white;
  background-color: #007bff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.continue-button:hover {
  background-color: #0056b3;
}

.about-section {
  padding: 20px;
  background-color: #e9ecef; /* Light background for the about section */
  margin-top: 20px; /* Spacing above the section */
  text-align: center;
}

.contacts-section {
  padding: 20px;
  background-color: #f8f9fa; /* Light background for the contacts section */
  margin-top: 20px; /* Spacing above the section */
  text-align: center;
}
</style>
