<template>
    <div class="container-fluid">
        <div class="description-block">
            <div class="title">
                <h1>YOLOv10</h1>
            </div>
            <div class="description">
                <p>Released on May 23, 2024, YOLOv10 is a real-time object detection model developed by researchers from Tsinghua University. YOLOv10 represents the state of the art in object detection, achieving lower latency than previous YOLO models with fewer parameters. <br> In terms of performance, the YOLOv10 paper notes “our YOLOv10-S is 1.8× faster than RT-DETR-R18 under the similar AP on COCO, meanwhile enjoying 2.8× smaller number of parameters and FLOPs. Compared with YOLOv9-C, YOLOv10-B has 46\% less latency and 25\% fewer parameters for the same performance.”</p>
            </div>
            
        </div>
        <div class="options-block">
            <div class="title">
                <h1>Choose image to run inference</h1>
            </div>
            <div class="form">
                <input type="file" accept="image/*" @change="onFileChange">
                <button @click.prevent="uploadImage">Upload</button>
            </div>

        </div>
        <div class="result-block">
            <div class="title">
                <h1>Result</h1>
            </div>
            <div class="result">
                <img v-if="receivedImage" :src="receivedImage" alt="Processed Image">
            </div>
        </div>
            
    </div>
    
</template>

<script>
import axios from 'axios'

export default {
    data(){
        return {
            selectedFile: null,
            receivedImage: null
        }
    },
    methods: {
        onFileChange(e){
            this.selectedFile=e.target.files[0]
        },
        uploadImage(){
            if (this.selectedFile != null){
                const formData = new FormData()
                formData.append('image',this.selectedFile)

                const path = 'http://127.0.0.1:5000/yolov10'
                axios.post(path, formData, {
                    headers: {
                        'Content-Type': 'multipart/form-data'
                    },
                    responseType: 'blob'
                })
                .then(response => {
                    console.log('got it');
                    
                    const url = window.URL.createObjectURL(new Blob([response.data]))
                    this.receivedImage = url
                    this.selectedFile = null
                })
                .catch(error => {
                    console.log('failed');
                    
                    console.log(error);
                })
            }
                
        }

    }
}
</script>

<style scoped>
    .container-fluid{
        margin-top: 10%;
        width: 100%;
        display: flex;
        flex-direction: column;
    }
    .container-fluid .description-block{
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    .description-block .description{
        width: 50%;
    }
    .container-fluid .options-block{
        margin-top: 5%;
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    .options-block .form{
        width: 50%;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .form button{
        padding: 1% 1.5%;
        background-color: #808185;
        border-radius: 15px;
        transition: 0.2s ease;
        border: none;
    }
    .form button:hover{
        cursor: pointer;
        background-color: #5B565C;
    }
    .container-fluid .result-block{
        margin-top: 5%;
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    .result-block img{
        max-width: 720px;
        width: 100%;
    }
</style>
