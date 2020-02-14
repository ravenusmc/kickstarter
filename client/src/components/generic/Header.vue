<template>
  <div>

    <div class='section-padding'>

      <nav>

        <div class='logo'>
          KickStarter Study
        </div>

        <div>
          <router-link to="/" class='linkFix'>Home</router-link>
          <router-link to="/about" class='linkFix'>About</router-link>
        </div>

      </nav>

    </div>

  </div>
</template>

<script>
export default {
  name: 'Header',
  components: {

  }
}
</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
  outline: 0;
  box-sizing: border-box;;
}

body {
  height: 100vh;
}

.section-padding {
  padding-top: 25px;
  height: 650px;
  display: flex;
  justify-content: center;
  background-image: url('../../assets/images/donation.jpg');
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
}

nav {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  position: relative;
  width: calc(100%);
  margin: 10px 0;
  background: #138AEF;
  z-index: 1;
  text-align: right;
  padding-right: 2%;
  height: 80px;
}

.logo {
  width: 35%;
  float: left;
  text-transform: uppercase;
  color: #fff;
  font-size: 35px;
  text-align: left;
  padding-left: 2%;
}

.linkFix {
  text-decoration: none;
  color: #fff;
  font-size: 30px;
  text-transform: uppercase;
  margin-right: 15px;
}

.nav-area li {
  display: inline-block;
  list-style: none;
  font-weight: bold;
  letter-spacing: 1px;
  text-transform: uppercase;
  display: block;
  padding: 0 25px;
  font-size: 14px;
  line-height: 30px;
  position: relative;
  z-index: 1;
  text-decoration: none;
}

nav:before {
  position: absolute;
  content: '';
  border-top: 10px solid #333;
  border-right: 10px solid #333;
  border-left: 10px solid transparent;
  border-bottom: 10px solid transparent;
  top: 100%;
  left: 0;
}

nav:after {
  position: absolute;
  content: '';
  border-top: 10px solid #333;
  border-left: 10px solid #333;
  border-right: 10px solid transparent;
  border-bottom: 10px solid transparent;
  top: 100%;
  right: 0;
}
</style>





























<!-- -->
