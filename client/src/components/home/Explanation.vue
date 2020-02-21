<template>
  <div>

    <div class='explanationPageTitle center font'>
      <h1>KickStarter Study</h1>
    </div>

    <section>

      <div id='pic_div'>
      </div>

      <div id='purpose_div'>
        <h2 class='center fontColor font'>Purpose</h2>
        <p class='font paragraphFont'>
          The purpose of this project is to examine some Kick Starter Data from
          a basic level. I also have another goal with this project of using a
          few different charts from Google Charts and see what different
        </p>
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

/* Media Queries */
@media only all and (max-width: 900px){

  section {
    grid-template-columns: 1fr;
    margin-left: 5%;
    margin-right: 5%;
  }

}
</style>
