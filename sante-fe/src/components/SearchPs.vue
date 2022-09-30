<template>
    <div class="left-sidebar">
        <img src = "./../assets/images/user.png" height="120" width="120">
        <span style="text-align:center; margin:30px; font-size:30px">Buscar Personal Salud</span> 
       
    </div>
    <div class="content sau">
        <form id="FormularioSerchPs">
            <div class="form-group">
                <span>Busque personal de salud ingresando el ID</span><br><br>
                <label>ID Ps:</label> <input type="text" class="campo_texto searchId">
            </div>
        </form>
        <a v-on:click="loadHome">Atras</a>
    </div>
</template>
    
<script>
    export default {
    name: "SearchPs",
    data: function() {
        return {
            username: localStorage.getItem('username') || "none"
        }
    },
    components: {},
    methods: {
        loadHome: function() {
            console.log("Si funciona");
            this.$router.push({
                    name: "personalsalud"
                });
        },
        loadSearchPs: function() {
            console.log("Si funciona");
            this.$router.push({
                    name: "home"
                });
        },
        loadCreatePs: function() {
            console.log("Si funciona");
            this.$router.push({
                    name: "home"
                });
        },
    }
}
</script>
<style> 
    #FormularioSerchPs input{
        height: 30px;
        width: 100%;
        border-radius: 5px;
        text-align: center;
        font-size: 16px;
    }
    #FormularioSerchPs div span{
        height: 30px;
        width: 100%;
        border-radius: 5px;
        text-align: center;
        font-size: 16px;
        display: block;
    }
    #FormularioSerchPs div label{
        height: 30px;
        margin: auto;
        border-radius: 5px;
        text-align: center;
        font-size: 24px;
        font-weight: bold;
        display: block;
    }
     .form-group {
        margin: 16px;
    }
    .greetings{
        margin: 0;
        padding: 0%;
        height: 100%;
        width: 100%;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .greetings h1{
        font-size: 50px;
        color: #283747;
    }
    .greetings span{
        color: #396fd5;
        font-weight: bold;
    }
    .logo {
    margin-left: 30px;
    }

    .logo a {
        text-decoration: none;
        color:rgb(3, 33, 62);
        text-transform: uppercase;
        font-size: 20px;
    }

    .title {
        margin-bottom: 40px;
        font-size: 60px;
        font-weight: 600;
        text-transform: uppercase;
        color: rgb(0, 0, 0)
        
    
    }

    .title{
        background-color:rgba(111, 167, 220, 0.504) ;
    }

    p {
        margin-bottom: 40px;
        font-size: 18px;
        color: #fff;
        padding: 0 100px;
    }

    .btn {
        display: inline-block;
        margin-top: 15px;
        padding: 10px 40px;
        border: 2px solid rgb(111, 168, 220);
        color: rgb(0, 0, 0);
        text-decoration: none;
        background: rgb(111, 168, 220);

        
    }

    .btn:hover {
        background: none;
    
        
    }

    .content {
        height: auto;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
    .left-sidebar{
        width:28%;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: flex-start;
        align-items: center;
        margin: 100px 0;
        padding: 16px 0;
    }
    .sau {
        padding: 30px;
        background: #fff;
        width: 70%
    }

    .box-container {
        display: flex;
        justify-content: center;
        flex-wrap: wrap;
        text-align: center;

    }

    .box-container .box {
        height: 14rem;
        width: 17rem;
        background: rgb(217, 233, 247);
        text-align: center;
        border-radius: 1rem;
        box-shadow: 0 .3rem 5rem rgba(0, 0 , 0, .5);
        margin: 2rem;   
    }



    .box-container .box h3 {
        font-size: 20px;
        color:rgb(19,79,92);

    }

    @media (max-width: 768px) {

        .title {
            margin-bottom: 0;
            font-size: 40px;
        }

        .sau {
            height: auto;
        }

        .navbar {
            display: none;
        }
    
        
    }

</style>