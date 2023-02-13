<template>
  <q-dialog>
    <q-card>
      <q-card-section class="row items-center q-pb-none ">
        <div class="text-h6  ">{{ title }}</div>
        <q-space/>
        <q-btn icon="close" flat round dense v-close-popup/>
      </q-card-section>
      <q-card-section>
        <slot></slot>
      </q-card-section>
    </q-card>
  </q-dialog>
</template>
<script>
export default {
  props: ['title'],
  name: 'ModalMenu',
}</script>