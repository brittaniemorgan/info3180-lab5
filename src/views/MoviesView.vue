<template>
    <div>
        <div v-if="!movies.length" class="no-movies">
            You haven't added any movies.
        </div>
        <div class="movies">
            <div v-for="(movie, index) in movies" :key="index" class="col-md-6">
                <div class="card mb-4">
                    <div class="card-body">
                        <div>
                            <img :src="movie.poster" alt="Poster" />
                        </div>
                        <div>
                            <h5 class="card-title">{{ movie.title }}</h5>
                            <p class="card-text">{{ movie.description }}</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
  

<script setup> 
    import { ref, onMounted } from "vue"; 
    let movies = ref([]); 

    const fetchMovies = () => {
        fetch("/api/v1/movies", { 
            method: 'GET'
            }) 
            .then(function (response) { 
                return response.json(); 
            }) 
            .then(function (data) { 
                // display a success message 
                console.log(data); 
                movies.value = data.movies;
            }) 
            .catch(function (error) { 
                console.log(error); 
        });
    };

    onMounted(() => { 
        fetchMovies(); 
    }); 
</script> 

<style>
img{
    width: 200px;
}

.movies{
    display: grid;
    grid-template-columns: 1fr 1fr;
    grid-gap: 70px;
    width: 50%;
}
</style>