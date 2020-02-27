<template>
  <div>
    <footer>
      <div class='footer_fix'>
        <h2 class='footerTitle font'>Copyright &copy; 2020 Double Sun Productions<br></h2>
          <div>
            <a href="https://www.linkedin.com/in/mcuddy1/"><i class="fa fa-linkedin-square fa-3x" aria-hidden="true"></i></a>
            <a href="https://twitter.com/mcuddy7"><i class="fa fa-twitter-square fa-3x" aria-hidden="true"></i></a>
            <a href="https://codingsaga.wordpress.com/"><i class="fa fa-pencil fa-3x" aria-hidden="true"></i></a>
            <a href="https://github.com/ravenusmc"><i class="fa fa-github-square fa-3x" aria-hidden="true"></i></a>
          </div>
      </div>
    </footer>
  </div>
</template>

<script>
export default {
  name: 'Footer',
};
</script>

<style scoped>
.fa-linkedin-square, .fa-twitter-square, .fa-pencil, .fa-github-square {
  color: black;
  margin: 5px;
}
footer {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background: #05ce78;
  height: 300px;
}
.footer_fix {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  margin-bottom: 50px;
  padding-top: 50px;
}
.footerTitle {
  font-size: 20px;
  text-transform: uppercase;
}
</style>
