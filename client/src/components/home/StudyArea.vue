<template>
  <div>
    <StudyForm />

    <!-- First Chart Area -->
    <div class='graphExplanationArea'>

      <GraphCard
       :typeOne='typeOne'
       :data='firstChartData'
       :options='chartOptionsOne'>
       </GraphCard>

       <div class='paragraphDiv'>
         <h2 class='center title'>Brief Explanation</h2>
         <p class='paragraphFormatting'>
           The purpose of the first chart is to show the user the number of charts
           that have failed, succeeded or been cancelled in a given time frame. The
           user can also select a money goal that they want to go up to as well as
           the number of backers who want to support a project.
         </p>
         <p class='paragraphFormatting'>
           The reason why I created this chart is that I wanted the users to get
           just a basic information from the kickstarter data that I have. I also
           want to say that some of the filters from above will not be used to build
           this first chart.
         </p>
         <p class='paragraphFormatting'>
           This first chart has the money goal set to 1000 and the number of
           backers set to 100.
         </p>
       </div>

    </div>
    <!-- End of First Chart Area -->

    <!-- Second Chart Area -->
    <div class='graphExplanationArea'>

      <GraphCard
       :typeOne='typeOne'
       :data='firstChartData'
       :options='chartOptionsOne'>
       </GraphCard>

       <div class='paragraphDiv'>
         <h2 class='center title'>Brief Explanation</h2>
         <p class='paragraphFormatting'>
           The purpose of the first chart is to show the user the number of charts
           that have failed, succeeded or been cancelled in a given time frame. The
           user can also select a money goal that they want to go up to as well as
           the number of backers who want to support a project.
         </p>
         <p class='paragraphFormatting'>
           The reason why I created this chart is that I wanted the users to get
           just a basic information from the kickstarter data that I have. I also
           want to say that some of the filters from above will not be used to build
           this first chart.
         </p>
       </div>

    </div>
    <!-- End of Second Chart Area -->

  </div>
</template>

<script scoped>
import { mapGetters } from 'vuex';
import StudyForm from '@/components/forms/StudyForm.vue';
import GraphCard from '@/components/charts/GraphCard.vue';

export default {
  name: 'StudyArea',
  components: {
    StudyForm,
    GraphCard,
  },
  data() {
    return {
      typeOne: 'BarChart',
      chartOptionsOne: {
        title: 'First Chart',
        legend: { position: 'top' },
        height: 500,
        vAxis: {
          viewWindow: {
            min: 0,
          },
        },
      },
    }
  },
  computed: {
  ...mapGetters([
    'firstChartData',
    'successfulByCategory',
  ]),
},
}
</script>

<style scoped>

.graphExplanationArea {
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-gap: 2em;
  margin-bottom: 50px;
}

.title {
  text-transform: uppercase;
}

.paragraphDiv {
  margin-left: 8%;
  margin-right: 8%;
}

.paragraphFormatting {
  font-size: 18px;
}

</style>
