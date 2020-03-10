<template>
  <div>
    <StudyForm />
    <GraphCard
     :typeOne='typeOne'
     :data='firstChartData'
     :options='chartOptionsOne'>
     </GraphCard>
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
  ]),
},
}
</script>

<style>
</style>
