import Vue from 'vue'
import App from './App'
import * as Api from './config/api.js'

import * as Common from './config/common.js'
import * as Db from './config/db.js'
import * as Config from './config/config.js'

import store from './store'

Vue.config.productionTip = false
Vue.prototype.$api = Api;
Vue.prototype.$common = Common;
Vue.prototype.$db = Db;
Vue.prototype.$config = Config;
Vue.prototype.$store = store

App.mpType = 'app'

const app = new Vue({
    store,
    ...App
})
app.$mount()
