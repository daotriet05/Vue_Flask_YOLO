<template>
    <div class="container-fluid">
        <div class="description-block">
            <div class="title">
                <h1>YOLO Object Detection</h1>
            </div>
            <div class="description">
                <p>YOLO (You Only Look Once) is a real-time object detection algorithm developed by Joseph Redmon and Ali Farhadi in 2015. It is a single-stage object detector that uses a convolutional neural network (CNN) to predict the bounding boxes and class probabilities of objects in input images. YOLO was first implemented using the Darkent framework.</p>
            </div>
            
        </div>
        <div class="options-block">
            <div class="title">
                <h1>Choose version to use</h1>
            </div>
            <div class="options">
                <a
                    @click.prevent="$router.push('/yolov8')"
                >YOLOv8</a>

                <a
                    @click.prevent="$router.push('/yolov9')"
                >YOLOv9</a>

                <a
                    @click.prevent="$router.push('/yolov10')"
                >YOLOv10</a>
            </div>
        </div>
    </div>
    
</template>

<script>
export default {
    
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
    .options-block .options{
        width: 50%;
        display: flex;
        justify-content: space-around;
    }
    .options a{
        padding: 1% 1.5%;
        background-color: #808185;
        border-radius: 15px;
        transition: 0.2s ease;
        border: none;
    }
    .options a:hover{
        cursor: pointer;
        background-color: #5B565C;
    }
</style>
