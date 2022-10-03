<template>
    <div class="left-sidebar">
        <img src = "./../assets/images/user.png" height="120" width="120">
        <span style="text-align:center; margin:30px; font-size:30px">Bienvenido: <br>{{username}}</span> 
    </div>
    <div class="content sau">
        <div class="box-container">
           
            <div class="box">
                <a class="box-item" v-on:click="loadPersonaSalud" >
                    <br>
                    <img src = "./../assets/images/personalsalud1.png" height="90" width="90">
                    <br>
                    <h3>Personal Salud</h3>
                </a>
            </div>

            <div class="box">
                <a class="box-item" v-on:click="loadHistoriaclinica" >
                    <br>
                    <img src = "./../assets/images/historiaclinica2.png" height="90" width="90">
                    <br>
                    <h3>Historia Clínica</h3>
                </a>
            </div>

            <div class="box">
                <a class="box-item" v-on:click="loadSignosvitales" >
                    <br>
                    <img src = "./../assets/images/signosvitales2.png" height="90" width="90">
                    <br>
                    <h3>Signos Vitales</h3>
                </a>
            </div>

            <div class="box">

                <a class="box-item" v-on:click="loadPaciente" >
                    <br>
                    <img src = "./../assets/images/paciente2.png" height="90" >
                    <br>
                    <h3>Paciente</h3>

                </a>

            </div>
            <div class="box">
                <a class="box-item" v-on:click="loadfamiliar" >
            
                    <br>
                    <img src = "./../assets/images/familiar2.png" height="90" width="90">
                    <br>
                    <h3>Familiar</h3>
                </a>
            </div>
        </div>
    </div>
</template>
    
<script>
    export default {
    name: "Home",
    data: function() {
        return {
            username: localStorage.getItem('username') || "none"
        }
    },
    components: {},
    methods: {
        loadPaciente: function() {
            console.log("Si funciona");
            this.$router.push({
                    name: "paciente"
                });
        },
        loadfamiliar: function() {
            console.log("Si funciona");
            this.$router.push({
                    name: "familiar"
                });
        },
        loadHistoriaclinica: function() {
            console.log("Si funciona");
            this.$router.push({
                    name: "historiaclinica"
                });
        },
        loadSignosvitales: function() {
            console.log("Si funciona");
            this.$router.push({
                    name: "signosvitales"
                });
        },
        loadPersonaSalud: function() {
            console.log("Si funciona");
            this.$router.push({
                    name: "personalsalud"
                });
        },
    }
}
</script>
<style> 
    
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
        justify-content: center !important;
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

        img{display: none;}
    }
</style>