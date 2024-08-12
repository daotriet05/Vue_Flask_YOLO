import { createRouter, createWebHashHistory } from "vue-router";

import Home from '../components/Home.vue'
import Yolov8 from '../components/Yolov8.vue'
import Yolov9 from '../components/Yolov9.vue'
import Yolov10 from '../components/Yolov10.vue'

const router = createRouter({
    history: createWebHashHistory(),
    routes: [
        {
            path: '/',
            component: Home, 
        },
        {
            path: '/yolov8',
            component: Yolov8, 
        },
        {
            path: '/yolov9',
            component: Yolov9, 
        },
        {
            path: '/yolov10',
            component: Yolov10, 
        },
    ]
})

export default router