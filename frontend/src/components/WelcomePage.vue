<template>
  <div class="welcome-page">
    <header class="header">
    <div class="logo-container">
        <img src="https://cdn-icons-png.flaticon.com/512/6302/6302780.png" class="logo"/>
      </div>
      <nav>
        <ul class="nav-list">
          <li class="nav-item">
            <router-link to="/" class="nav-link">Главная</router-link>
          </li>
          <li class="nav-item">
            <a href="#about" class="nav-link" @click.prevent="scrollToSection('about')">О нас</a>
          </li>
          <li class="nav-item">
            <a href="#advantages" class="nav-link" @click.prevent="scrollToSection('advantages')">Преимущества</a>
          </li>
          <li class="nav-item">
            <a href="#reviews" class="nav-link" @click.prevent="scrollToSection('reviews')">Отзывы</a>
          </li>
          <li class="nav-item">
            <a href="#contacts" class="nav-link" @click.prevent="scrollToSection('contacts')">Контакты</a>
          </li>
        </ul>
      </nav>
    </header>

    <div class="image-container">
      <img
        src="https://services.kontur.ru/Files/Modules/Article/articles-4598_l_md_1x.png?t=1606173150"
        alt="Business Builder"
        class="header-image"
      />
    </div>

    <div class="content">
      <h1>Добро пожаловать в конструктор бизнеса</h1>
      <p>С нами вы сможете легко и быстро построить свой успешный бизнес!</p>
      <button @click="start" class="continue-button">Начать сейчас</button>
    </div>

    <!-- О нас -->
    <section id="about" class="about-section">
      <h2>О нас</h2>
      <p>
        Мы – команда экспертов в сфере бизнес-консалтинга и технологий. Наша миссия – упростить процесс создания бизнеса, предлагая эффективные инструменты для моделирования и запуска проектов.
      </p>
      <p>
        В нашем арсенале – знания, опыт и технологии, которые помогут вам достичь успеха. С нами бизнес станет ближе, чем вы думали!
      </p>
    </section>

    <!-- Преимущества -->
    <section id="advantages" class="advantages-section">
      <h2>Наши Преимущества</h2>
      <div class="advantages-list">
        <div class="advantage-item">
          <h3>Простота</h3>
          <p>Интуитивно понятный интерфейс и удобные инструменты для создания вашего бизнеса.</p>
        </div>
        <div class="advantage-item">
          <h3>Гибкость</h3>
          <p>Мы предлагаем гибкие настройки для всех типов бизнеса – от автосервисов до ресторанов.</p>
        </div>
        <div class="advantage-item">
          <h3>Поддержка</h3>
          <p>Наши специалисты всегда готовы помочь вам на всех этапах развития вашего проекта.</p>
        </div>
      </div>
    </section>

    <!-- Отзывы -->
    <section id="reviews" class="reviews-section">
      <h2>Отзывы наших клиентов</h2>
      <div class="reviews-list">
        <div class="review-item">
          <p>"Конструктор бизнеса помог мне запустить автосервис за считанные недели. Отличный инструмент!"</p>
          <span>- Алексей Иванов</span>
        </div>
        <div class="review-item">
          <p>"Простота и доступность этого сервиса поразила меня. Теперь я рекомендую его всем своим друзьям!"</p>
          <span>- Мария Петрова</span>
        </div>
        <div class="review-item">
          <p>"С помощью этой платформы я смогла открыть свой ресторан с минимальными затратами. Спасибо!"</p>
          <span>- Анна Смирнова</span>
        </div>
      </div>
    </section>

    <!-- Контакты -->
    <section id="contacts" class="contacts-section">
      <h2>Контакты</h2>
      <p>
        Свяжитесь с нами для консультаций и поддержки:
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
    },
    scrollToSection(sectionId) {
      const element = document.getElementById(sectionId);
      if (element) {
        element.scrollIntoView({ behavior: 'smooth' });
      }
    }
  }
};
</script>

<style scoped>
.welcome-page {
  display: flex;
  flex-direction: column;
  align-items: center;
  background-color: #f5f5f5;
  font-family: Arial, sans-serif;
}

.header {
  width: 90%;
  max-width: 1000px;
  background-color: #007bff;
  padding: 15px;
  margin-top: 20px;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.logo-container {
  display: flex;
  align-items: center;
}

.logo {
  width: 50px;
  height: auto;
  margin-right: 20px;
}

.nav-list {
  display: flex;
  justify-content: center;
  list-style: none;
  padding: 0;
  margin: 0;
}

.nav-item {
  margin: 0 15px;
}

.nav-link {
  color: white;
  text-decoration: none;
  font-size: 18px;
  transition: color 0.3s ease;
}

.nav-link:hover {
  color: #ffde59;
}

.image-container {
  width: 100%;
  max-width: 800px; /* Limited width */
  margin: 20px auto;
  overflow: hidden;
}

.header-image {
  width: 100%;
  height: auto;
  border-radius: 10px;
}

.content {
  text-align: center;
  margin-top: 20px;
}

h1 {
  font-size: 2.5em;
  color: #333;
}

p {
  font-size: 1.2em;
  color: #666;
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

.about-section, .advantages-section, .reviews-section, .contacts-section {
  width: 100%;
  max-width: 800px;
  margin: 20px auto;
  padding: 20px;
  background-color: white;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

h2 {
  font-size: 2em;
  color: #007bff;
  margin-bottom: 10px;
}

.advantages-list {
  display: flex;
  justify-content: space-around;
  flex-wrap: wrap;
}

.advantage-item {
  width: 250px;
  margin: 10px;
  text-align: center;
}

.reviews-list {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.review-item {
  background-color: #f8f9fa;
  padding: 15px;
  border-radius: 5px;
  font-style: italic;
}

.review-item span {
  display: block;
  margin-top: 10px;
  font-weight: bold;
  text-align: right;
}

.contacts-section ul {
  list-style: none;
  padding: 0;
}

.contacts-section li {
  font-size: 1.1em;
  color: #333;
  margin: 10px 0;
}
</style>
