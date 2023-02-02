<template >
  <nav class="navbar is-dark">
    <div class="navbar-brand">
      <router-link to="/" class="navbar-item"><strong>DjacketsApp</strong></router-link>



    </div>

  </nav>


  <section class="section">
  <router-view/>
  </section>
</template>

<style lang="scss">
@import '../node_modules/bulma';
</style>
