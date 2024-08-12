<template>
    <div class="container-fluid">
        <div class="description-block">
            <div class="title">
                <h1>YOLOv9</h1>
            </div>
            <div class="description">
                <p>On February 21st, 2024, Chien-Yao Wang, I-Hau Yeh, and Hong-Yuan Mark Liao released the “YOLOv9: Learning What You Want to Learn Using Programmable Gradient Information'' paper, which introduces a new computer vision model architecture: YOLOv9. The source code was made available, allowing anyone to train their own YOLOv9 models. <br> According to the project research team, the YOLOv9 achieves a higher mAP than existing popular YOLO models such as YOLOv8, YOLOv7, and YOLOv5, when benchmarked against the MS COCO dataset.</p>
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

                const path = 'http://127.0.0.1:5000/yolov9'
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
