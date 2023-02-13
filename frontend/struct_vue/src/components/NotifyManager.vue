<script>
import {Notify} from "quasar";

export default {
  name: "NotifyManager",
  methods: {

    pushResponceNotify(response) {
      Notify.create({message: response.data, color: 'positive', position: 'top'})
    },

    pushErrorNotify(error) {
      Notify.create({message: error.message, color: 'negative', position: 'top'})
    },

    pushPostErrorNotify(error) {
      let message_details = Object.keys(error.response.data).toString()
      if (message_details) {
        message_details = " ошибка в: " + message_details
      }
      Notify.create({message: error.message + message_details, color: 'negative', position: 'top'})
    },
  }
}
</script>


<style scoped>

</style>