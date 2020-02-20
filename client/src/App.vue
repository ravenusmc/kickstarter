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
</style>
