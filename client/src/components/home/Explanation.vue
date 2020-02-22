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
          a basic level. Basic level meaning looking at some of the basic statistical
          aspects of the data as well as building some charts to go along with it.
          along the lines of charts, I also have another goal with this project
          of using a few different charts from Google Charts. I tend to only use pie
          and bar charts and want to break out and use a few other types.
        </p>
        <p class='font paragraphFont'>
          As for why I choose this dataset? The easiest reason is that I just did.
          I wanted anotheer dataset to play with and this caught my eye. I did attend
          a data science meeetup that worked with a similar dataset. I never helped
          much on that project but maybe this is a way to make up for that!
        </p>
        <p class='font paragraphFont'>
          Let's examine some data!
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
  margin-left: 5%;
  margin-right: 5%;
  margin-top: 50px;
  margin-bottom: 50px;
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
