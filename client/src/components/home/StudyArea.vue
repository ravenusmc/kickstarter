<template>
  <div>
    <StudyForm />

    <!-- First Chart Area -->
    <div class='graphExplanationArea'>

      <GraphCard
       :typeOne='typeTwo'
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
       :data='successfulByCategory'
       :options='chartOptionsTwo'>
      </GraphCard>

     <div class='paragraphDiv'>
       <h2 class='center title'>Brief Explanation</h2>
       <p class='paragraphFormatting'>
         This chart will show the user what categories had the most successes in
         a given time frame. The <span>initial time frame</span> that the site uses
         is from <span>May 3rd, 2009 to February 17th, 2017</span>. As we can see,
         the top three kick starter campaigns in that time period were Music,
         Theater and Food.
       </p>
       <p class='paragraphFormatting'>
         The buttons below will allow the user to change the time frame year by year.
         When the first button is hit, the time frame will move forward by one year. Thus,
         the first year represented, after the year is increased is 2010.
       </p>

       <h3 class='center font'>Year: {{ chartTwoYear }}</h3>

         <div class='button_div'>

           <form v-on:click="decreaseYear($event, chartTwoYear, 2)">
             <button class='arrowButton'>
               <i class="fa fa-arrow-left fa-3x" aria-hidden="true" v-model="chartTwoYear"></i>
             </button>
           </form>

           <form v-on:click="increaseYear($event, chartTwoYear, 2)">
             <button class='arrowButton'>
               <i class="fa fa-arrow-right fa-3x" aria-hidden="true" v-model="chartTwoYear"></i>
             </button>
           </form>

         </div>

     </div>

    </div>
    <!-- End of Second Chart Area -->

    <!-- Third chart Area -->
    <div class='graphExplanationArea'>

      <GraphCard
       :typeOne='typeOne'
       :data='failuresByCategory'
       :options='chartOptionsThree'>
      </GraphCard>

     <div class='paragraphDiv'>
       <h2 class='center title'>Brief Explanation</h2>
       <p class='paragraphFormatting'>
         This chart will show the user what categories had the most failures in
         a given time frame. The <span>initial time frame</span> that the site uses
         is from <span>May 3rd, 2009 to February 17th, 2017</span>. As we can see,
         the top three kick starter campaigns in that time period were Music,
         Food and Film and Video.
       </p>
       <p class='paragraphFormatting'>
         The buttons below will allow the user to change the time frame year by year.
         When the first button is hit, the time frame will move forward by one year. Thus,
         the first year represented, after the year is increased is 2010.
       </p>

       <h3 class='center font'>Year: {{ chartThreeYear }}</h3>

         <div class='button_div'>

           <form v-on:click="decreaseYear($event, chartThreeYear, 3)">
             <button class='arrowButton'>
               <i class="fa fa-arrow-left fa-3x" aria-hidden="true" v-model="chartThreeYear"></i>
             </button>
           </form>

           <form v-on:click="increaseYear($event, chartThreeYear, 3)">
             <button class='arrowButton'>
               <i class="fa fa-arrow-right fa-3x" aria-hidden="true" v-model="chartThreeYear"></i>
             </button>
           </form>

         </div>

     </div>

    </div>
    <!-- End of third Chart Area -->

    <!-- Fourth chart Area -->
    <div class='graphExplanationArea'>

      <GraphCard
       :typeOne='typeThree'
       :data='successAndFailures'
       :options='chartOptionsFour'>
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

       <h3 class='center font'>Year: {{ chartFourYear }}</h3>

         <div class='button_div'>

           <form v-on:click="decreaseYear($event, chartFourYear, 3)">
             <button class='arrowButton'>
               <i class="fa fa-arrow-left fa-3x" aria-hidden="true" v-model="chartFourYear"></i>
             </button>
           </form>

           <form v-on:click="increaseYear($event, chartFourYear, 4)">
             <button class='arrowButton'>
               <i class="fa fa-arrow-right fa-3x" aria-hidden="true" v-model="chartFourYear"></i>
             </button>
           </form>

         </div>

     </div>

    </div>
    <!-- End of fourth Chart Area -->

    <!-- Fifth chart Area -->
    <div class='graphExplanationArea'>

      <GraphCard
       :typeOne='typeThree'
       :data='successAndFailures'
       :options='chartOptionsFour'>
      </GraphCard>

     <div class='paragraphDiv'>
       <h2 class='center title'>Brief Explanation</h2>
       <p class='paragraphFormatting'>
         This chart is a little bit different. It should have actually been moved
         to the front of the cards on this page - or at least near the top. The
         purpose of this card is to show the number of failed, successful and cancelled
         campaigns / category added together. This will give the user a much better
         sense of the most popular campaigns on kick starter.
       </p>
       <p class='paragraphFormatting'>
         The buttons below will allow the user to change the time frame year by year.
         When the first button is hit, the time frame will move forward by one year. Thus,
         the first year represented, after the year is increased is 2010. The <span>
         initial time frame</span> that the site uses is from <span>May 3rd, 2009
         to February 17th, 2017</span>.
       </p>

       <h3 class='center font'>Year: {{ chartFourYear }}</h3>

         <div class='button_div'>

           <form v-on:click="decreaseYear($event, chartFourYear, 3)">
             <button class='arrowButton'>
               <i class="fa fa-arrow-left fa-3x" aria-hidden="true" v-model="chartFourYear"></i>
             </button>
           </form>

           <form v-on:click="increaseYear($event, chartFourYear, 4)">
             <button class='arrowButton'>
               <i class="fa fa-arrow-right fa-3x" aria-hidden="true" v-model="chartFourYear"></i>
             </button>
           </form>

         </div>

     </div>

    </div>
    <!-- End of fifth Chart Area -->

  </div>
</template>

<script>
import moment from 'moment';
import { mapGetters, mapActions } from 'vuex';
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
      test: 'HI MIKE',
      typeOne: 'BarChart',
      typeTwo: 'ColumnChart',
      typeThree: 'PieChart',
      typeFour: 'TreeMap',
      chartTwoYear: 'Initial Time Frame',
      chartThreeYear: 'Initial Time Frame',
      chartFourYear: 'Initial Time Frame',
      chartOptionsOne: {
        title: 'First Chart',
        legend: { position: 'top' },
        colors:['#05ce78'],
        height: 500,
        vAxis: {
          viewWindow: {
            min: 0,
          },
        },
      },
      chartOptionsTwo: {
        title: 'Successful By Category Chart',
        legend: { position: 'top' },
        colors:['#05ce78'],
        height: 500,
        animation:{
          duration: 1000,
          easing: 'linear',
        },
        vAxis: {
          viewWindow: {
            min: 0,
          },
        },
      },
      chartOptionsThree: {
        title: 'Failures By Category Chart',
        legend: { position: 'top' },
        colors:['#05ce78'],
        height: 500,
        animation:{
          duration: 1000,
          easing: 'linear',
        },
        vAxis: {
          viewWindow: {
            min: 0,
          },
        },
      },
      chartOptionsFour: {
        title: 'Success and Failures Chart',
        legend: { position: 'top' },
        height: 500,
        animation:{
          duration: 1000,
          easing: 'linear',
        },
      }, // End chartOptionsFour
    }
  },
  computed: {
    ...mapGetters([
      'firstChartData',
      'successfulByCategory',
      'failuresByCategory',
      'successAndFailures',
    ]),
  }, // End Computed properties
  methods: {
    ...mapActions([
      'fireActionsIndividualChart',
      'fetchSuccessfulByCategory',
      'fetchFailuresByCategory',
      'fetchSuccessAndFailures',
    ]),
    decreaseYear(event, year, graphNumber) {
      event.preventDefault();

      if (year == 'Initial Time Frame') {
        year = 2010
      }else {
        year -= 1
      }

      if (year < 2009){
        alert('There is no data below 2009')
        year = 2009
      }

      let startDate = moment(`01/01/${year}`).format('M/D/YYYY h:mm:ss A');
      let endDate = moment(`12/31/${year}`).format('M/D/YYYY h:mm:ss A');

      const payload = {
        startDate: startDate,
        endDate: endDate,
      };

      if (graphNumber == 1) {
        this.chartOneYear = year
      } else if (graphNumber === 2) {
        this.chartTwoYear = year
        this.fetchSuccessfulByCategory({ payload });
      } else if (graphNumber === 3) {
        this.chartThreeYear = year
        this.fetchFailuresByCategory({ payload });
      } else if (graphNumber === 4) {
        this.chartFourYear = year
        this.fetchSuccessAndFailures({ payload })
      }

    }, // End decreaseYear method
    increaseYear(event, year, graphNumber) {
      event.preventDefault();

      if (year == 'Initial Time Frame') {
        year = 2010
      }else {
        year += 1
      }

      if (year < 2009){
        alert('There is no data below 2009')
        year = 2009
      }

      let startDate = moment(`01/01/${year}`).format('M/D/YYYY h:mm:ss A');
      let endDate = moment(`12/31/${year}`).format('M/D/YYYY h:mm:ss A');

      const payload = {
        startDate: startDate,
        endDate: endDate,
      };

      if (graphNumber == 1) {
        this.chartOneYear = year
      } else if (graphNumber == 2) {
        this.chartTwoYear = year
        this.fetchSuccessfulByCategory({ payload });
      } else if (graphNumber == 3) {
        this.chartThreeYear = year
        this.fetchFailuresByCategory({ payload });
      }else if (graphNumber === 4) {
        this.chartFourYear = year
        this.fetchSuccessAndFailures({ payload })
      }

    }, // End increaseYear method
  } // End methods
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

span {
  font-weight: bold;
}

.button_div {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
}

.arrowButton {
  margin-left: 5px;
  margin-right: 5px;
}

</style>
