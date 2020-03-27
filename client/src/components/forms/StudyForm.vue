<template>
  <div>

    <section id='formArea'>

      <form @submit="submitForm">

        <div class='datePicker'>
          <h3 class='font'>Enter Date Range:</h3>
          <input class='dateInput' v-model="startDate">&nbsp;&nbsp;
          <input class='dateInput' v-model="endDate">
        </div>

        <div class='moreParametersArea'>
          <div>
            <label class='font'>Category:</label>&nbsp;
            <select v-model="category" name="category">
              <option v-for="category in categories" v-bind:key="category" :value="category">
                {{ category }}
              </option>
            </select>
          </div>

          <div>
            <label class='font'>State:</label>&nbsp;
            <select v-model="state" name="state">
              <option v-for="state in states" v-bind:key="state" :value="state">
                {{ state }}
              </option>
            </select>
          </div>

          <div>
            <label class='font'>Money Goal:</label>&nbsp;
            <input v-model="moneyGoal">
          </div>

          <div>
            <label class='font'>Number of Backers:</label>&nbsp;
            <input v-model="backers">
          </div>
        </div>

        <div class='selectionFix'>
          <button class='font'>Submit</button>
        </div>

      </form>

      <div class='formParagraphArea'>
        <p class='font'>
          This form will allow the user to select different parameters to see
          how the data will change on the cards below. I will admit that only the
          first chart do all the parameters work. I never set them up for the other
          cards - mainly because I felt that I did not need to. The date is the
          one parameter that will affect all the cards. Please also not the
          starting date which is what all the cards are set to.
        </p>
      </div>

    </section>

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

#formArea {
  display: grid;
  grid-template-columns: 1fr 1fr;
}

form {
  margin-left: 5%;
  border: 2px solid black;
  box-shadow: 5px 10px #888888;
  border-radius: 10px;
  margin-bottom: 50px;
  display: flex;
  flex-direction: column;
  padding-bottom: 25px;
  /* justify-content: center;
  align-items: center; */
  text-align: left;
}

.datePicker {
  display: flex;
  flex-direction: row;
  margin-left: 3%;
}

.dateInput {
  margin-top: 22px;
  margin-left: 5px;
  margin-right: 5px;
  height: 15px;
}

.moreParametersArea {
  margin-left: 3%;
  margin-top: -18px;
}


.formParagraphArea {
  margin-left: 5%;
  margin-right: 5%;
  font-size: 20px;
  /* background-color: #05ce78; */
  line-height: 25px;
}

.selectionFix {
  margin-top: 20px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

@media only all and (max-width: 900px) {

  #formArea {
    display: grid;
    grid-template-columns: 1fr;
  }

}

</style>
