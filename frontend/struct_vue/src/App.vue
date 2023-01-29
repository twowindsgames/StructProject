<template >
  <nav class="navbar is-dark">
    <div class="navbar-brand">
      <router-link to="/" class="navbar-item"><strong>DjacketsApp</strong></router-link>



    </div>
    <div class="navbar-menu" id="navbar-menu">
      <div class="navbar-end">
        <router-link to="/api/group/all" class="navbar-item"><strong>Summer</strong></router-link>
        <router-link to="/winter" class="navbar-item"><strong>Winter</strong></router-link>

        <div class="navbar-item">
          <div class="buttons">


          </div>
        </div>

      </div>
    </div>
  </nav>
  <router-link to="/home" class="button is-info ">GetProductsAll</router-link>

  <section class="section">
  <router-view/>
  </section>
</template>

<style lang="scss">
@import '../node_modules/bulma';
</style>
