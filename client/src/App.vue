<template>
  <div>
    <Header/>
    <router-view/>
    <Footer/>
  </div>
</template>

<script>
import Header from '@/components/generic/Header.vue';
import Footer from '@/components/generic/Footer.vue'

export default {
  components: {
    Header,
    Footer,
  }
}
</script>

<style>

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

</style>
