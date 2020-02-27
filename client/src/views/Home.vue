<template>
  <div>
    <Explanation/>
    <StudyArea />
  </div>
</template>

<script>
// @ is an alias to /src
import Explanation from '@/components/home/Explanation.vue';
import StudyArea from '@/components/home/StudyArea.vue';

export default {
  name: 'Home',
  components: {
    Explanation,
    StudyArea,
  }
}
</script>
