<template>
    <h1>Upload Form</h1>
    <div v-if="flashMessage" v-bind:class="[isSuccess ? alertSuccessClass : alertErrorClass]" class="alert">
        <div v-if="!Array.isArray(flashMessage)">
            {{ flashMessage }}
        </div>
        <div v-else>
            <ul>
                <li v-for="error in flashMessage">{{ error }}</li>
            </ul>
        </div>
    </div>
    <div>   
        <form id="movieForm" @submit.prevent="saveMovie">
            <div class="form-group mb-3">
                <label for="title" class="form-label">Movie Title</label>
                <input type="text" name="title" v-model="title" class="form-control" />
            </div>
            <div class="form-group mb-3">
                <label for="description" class="form-label">Description</label>
                <textarea name="description" v-model="description" class="form-control"></textarea>
            </div>
            <div class="form-group mb-3">
                <label for="poster" class="form-label">Photo Upload</label>
                <br>
                <input type="file" name="poster" @change="onFileChange" class="form-control-file" />
            </div>
            <button type="submit" class="btn btn-primary">Submit</button>
        </form>
    </div>
</template>

<script setup>
    import { ref, onMounted } from 'vue';

    const alertSuccessClass = 'alert-success';
    const alertErrorClass = 'alert-danger';

    let title = ref(""); 
    let description = ref(""); 
    let csrf_token = ref(""); 
    let poster = ref(null)
    let flashMessage = ref('')
    let displayFlash = ref(false);
    let isSuccess = ref(false);

    function getCsrfToken() { 
        fetch('/api/v1/csrf-token') 
            .then((response) => response.json()) 
            .then((data) => { 
                console.log(data); 
                csrf_token.value = data.csrf_token; 
        }) 
    }

    const saveMovie = () => {
        let movieForm = document.getElementById('movieForm'); 
        let form_data = new FormData(movieForm);
        fetch("/api/v1/movies", { 
            method: 'POST', 
            body: form_data,
            headers: { 
                'X-CSRFToken': csrf_token.value 
            } 
            }) 
            .then(function (response) { 
                return response.json(); 
            }) 
            .then(function (data) { 
                console.log(data); 
                displayFlash = true;
                if (data.errors){
                    isSuccess = false;
                    flashMessage.value = data.errors;
                }
                else{
                    isSuccess = true;
                    flashMessage.value = 'Movie added successfully!';
                }
            }) 
            .catch(function (error) { 
                console.log(error); 
                displayFlash = true;
                isSuccess = false;
                flashMessage.value = error;
        });
    };

    onMounted(() => { 
        getCsrfToken(); 
    }); 
</script>
