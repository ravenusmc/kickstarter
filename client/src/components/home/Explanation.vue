<template>
  <div>

    <div class='explanationPageTitle center'>
      <h1>KickStarter Study</h1>
    </div>

    <section>

      <div id='pic_div'>
      </div>

      <div id='purpose_div'>
      </div>

    </section>

  </div>
</template>

<script>
import Header from '@/components/home/Explanation.vue'

export default {
  name: 'Explanation',
};
</script>

<style scoped>

.explanationPageTitle {
  margin-top: 50px;
  text-transform: uppercase;
  color: #656969;
}

section {
  margin-top: 50px;
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-gap: 2em;
}

#pic_div {
  background-image: url('../../assets/images/hardwork.jpg');
  height: 500px;
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
}
</style>
