<template>
  <div>

    <form @submit="submitForm">

      <div>
        <select v-model="category" name="category">
          <option v-for="category in categories" v-bind:key="category" :value="category">
            {{ category }}
          </option>
        </select>
      </div>

      <div>
        <select v-model="state" name="state">
          <option v-for="state in states" v-bind:key="state" :value="state">
            {{ state }}
          </option>
        </select>
      </div>

      <div class='datePicker'>
        <h3>Enter the Date:</h3>
        <label>Start Date:</label>
        <input v-model="startDate">
        <label>End Date:</label>
        <input  v-model="endDate">
      </div>

      <div>
        <input v-model="moneyGoal">
      </div>

      <div>
        <input v-model="backers">
      </div>


      <div class='selectionFix'>
        <button>Submit</button>
      </div>

    </form>

  </div>
</template>

<script>
import moment from 'moment';
import { mapActions } from 'vuex';

export default {
  name: "StudyForm",
  data() {
    return {
      startDate: '05/03/2009',
      endDate: '02/17/2017',
      category: 'Publishing',
      categories: ['Publishing', 'Film & Video', 'Music', 'Food', 'Design', 'Crafts', 'Games',
      'Comics', 'Fashion', 'Theater', 'Art', 'Photography', 'Technology', 'Dance',
      'Journalism'],
      state: 'successful',
      states: ['failed', 'successful'],
      moneyGoal: 0,
      backers: 0,
    }
  },
  methods: {
    ...mapActions([
      'fireActions',
    ]),
    submitForm(evt) {
      evt.preventDefault();
      this.startDate = moment(this.startDate).format('M/D/YYYY h:mm:ss A');
      this.endDate = moment(this.endDate).format('M/D/YYYY h:mm:ss A');
      const payload = {
        category: this.category,
        state: this.state,
        currency: 'USD',
        country: 'US',
        startDate: this.startDate,
        endDate: this.endDate,
        moneyGoal: this.moneyGoal,
        backers: this.backers,
      };
      this.fireActions({ payload });
    }
  }
}
</script>

<style scoped>

form {
  border: 2px solid red;
  margin-bottom: 50px;
}

.selectionFix {
  margin-top: 20px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

</style>
