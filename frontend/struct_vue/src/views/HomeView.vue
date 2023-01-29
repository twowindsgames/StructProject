<template>
  <div className="home">
    <section className="hero is-medium is-dark ">

      <div className="button is-info " v-on:click="winter">Get Winter Only</div>
      <div className="hero-body has-text-centered ">

        <div className="column is-center">
          <table className="table table mx-auto">
            <thead>
            <tr>
              <th scope="col">Name</th>
              <th scope="col">Price</th>
              <th scope="col">Category</th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="product in latestProducts"
                v-bind:key="product.id">
              <td>{{ product.slug }}</td>

            </tr>
            </tbody>
          </table>
        </div>
        <h6 className="is-size-3">AllProducts</h6>


      </div>
    </section>


  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'HomeView',
  data() {
    return {
      latestProducts: []
    }
  },
  mounted() {
    this.getLatestProducts()

  },
  methods: {
    getLatestProducts() {

      axios
          .get('/api/group/all/')
          .then(response => {
            this.latestProducts = response.data
          })
          .catch(error => {
            console.log(error)
          })

    },
    winter: function () {

      axios
          .get('/api/v1/winter-products/', {params: {category: 2}})
          .then(response => {
            this.latestProducts = response.data
          })
          .catch(error => {
            console.log(error)
          })

    }
  }
}
</script>