<template>
  <div>
    <Header/>
    <router-view/>
    <Footer/>
  </div>
</template>

<script>
import Header from '@/components/generic/Header.vue';
import Footer from '@/components/generic/Footer.vue';

export default {
  components: {
    Header,
    Footer,
  }
}
</script>

<style>
/* This code is here for possible use of route transitions */
/* @import "https://cdn.jsdelivr.net/npm/animate.css@3.5.1"; */

/* .page {
  position: fixed;
  width: inherit;
} */
/* End route transition code */

.center {
  text-align: center;
}

.fontColor {
  color: #656969;
  text-transform: uppercase;
}

.font {
  font-family: 'Source Sans Pro';
}

.paragraphFont {
  color: #656969;
  font-size: 18px;
  line-height: 1.5em;
}

button {
  background-color: #05ce78;
  border-color: #05ce78;
  padding: 15px;
  border-radius: 12px;
}

button:hover {
  background-color: #ce055b;
  border-color: #ce055b;
}

</style>
