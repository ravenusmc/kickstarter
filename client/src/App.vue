<template>
  <div>
    <Header/>
    <router-view/>
  </div>
</template>

<script>
import Header from '@/components/generic/Header.vue'

export default {
  components: {
    Header,
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
  font-size: 15px;
  line-height: 1.5em;
}

</style>
