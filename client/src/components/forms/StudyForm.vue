<template>
  <div>

    <form @submit="submitForm">

      <div class="">
        <select v-model="category" name="category">
          <option v-for="category in categories" v-bind:key="category" :value="category">
            {{ category }}
          </option>
        </select>
      </div>

      <div class='selectionFix'>
        <button>Submit</button>
      </div>

    </form>

  </div>
</template>

<script>
export default {
  name: "StudyForm",
  data() {
    return {
      category: 'Publishing',
      categories: ['Publishing', 'Film & Video', 'Music', 'Food', 'Design', 'Crafts', 'Games',
      'Comics', 'Fashion', 'Theater', 'Art', 'Photography', 'Technology', 'Dance',
      'Journalism'],
    }
  },
  methods: {
    submitForm(evt) {
      evt.preventDefault();
      console.log(this.category)
      // const payload = {
      //   question: this.question,
      //   answer: this.answer,
      //   sex: this.sex,
      // };
      // this.fetchMapData({ payload });
    }
  }
}
</script>

<style scoped>

.selectionFix {
  margin-top: 20px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

</style>
