<template>

      <q-menu  v-if="!root" transition-duration="0"
        touch-position
        >

        <q-list  dense style="min-width: 100px">

                  <q-item clickable v-close-popup @click="$emit('ShowEditTree','edit node')">
                     <q-item-section>Изменить информацию о подразделении </q-item-section>
                  </q-item>
                  <q-item clickable v-close-popup @click="$emit('ShowEditTree','add node')">
                     <q-item-section>Добавить подчиненное подразделение </q-item-section>
                  </q-item>

         <q-separator/>

              <q-item   clickable  v-close-popup  >
                <q-item-section  @click="$emit('ReadyDelete')"  >Удалить</q-item-section>
              </q-item>








          <q-separator />
        </q-list>
      </q-menu>


      <q-menu v-else transition-duration="0"
        touch-position
        context-menu>
        <q-list  dense style="min-width: 100px">
          <q-separator />
           <q-item clickable v-close-popup @click="$emit('ShowEditTree','add node')">
                   <q-item-section>Добавить корневое подразделение </q-item-section>
          </q-item>
          <q-separator />
          <q-item clickable v-close-popup>
            <q-item-section>Закрыть</q-item-section>
          </q-item>
        </q-list>
      </q-menu>


</template>

<script>
export default {
  name: "context_menu",
  props: [ 'group', 'readyToDelete','root'],
  }
</script>