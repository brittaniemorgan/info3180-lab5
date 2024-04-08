<template>
    <body>
        <h1>Movies</h1>
        <div class="container">        
            <div v-if="!movies.length" class="no-movies">
                You haven't added any movies.
            </div>
            <div class="movies">
                <div v-for="(movie) in movies" >
                    <div class="card">
                        <div>
                            <img :src="movie.poster" alt="Poster" />
                        </div>
                        <div class="card-body">     
                            <div>
                                <h5 class="card-title">{{ movie.title }}</h5>
                                <p class="card-text">{{ movie.description }}</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </body>
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

img {
    max-width: 300px;
    max-height: 300px; 
    object-fit: contain;
}

div{
    margin: 0px;
    padding: 0px;
}

.movies{
    display: grid;
    grid-template-columns: 1fr 1fr;
    grid-column-gap: 10%;
    grid-row-gap: 20px;
}

.card{
    display: grid;
    grid-template-columns: 1fr 1fr;
    box-shadow: none;
    transition: all 0.3s ease-in-out;
}

.card:hover {
    box-shadow: 0 3px 5px rgba(0, 0, 0, 0.2);
    transition: all 0.3s ease-in-out;
}

body{
    padding-top: 3%;
    padding-bottom: 4%;
    padding-left: 4%;
    padding-right: 4%;
}

.card-body{
    padding-left: 0px;
    margin-left:0px;
}

.no-movies {
    font-size: 32px;
    font-weight: bold;
    text-align: center;
}

</style>