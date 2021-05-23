<template>
  <div id="app">
    <h1>Appname: {{ ssr.appName }}</h1>
    <h2>User: {{ ssr.user }}</h2>
  </div>
</template>

<script>
export default {
  name: 'app2',
  data () {
    return {
      counter: 1,
      /*global ssr:true*/
      ssr: {...ssr},
    }
  }
}
</script>

