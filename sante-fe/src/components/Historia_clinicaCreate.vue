<template>
    <div class="left-sidebar">
        <img src = "./../assets/images/user.png" height="120" width="120">
        <span style="text-align:center; margin:30px; font-size:30px">Entrada Historia clinica</span> 
       
    </div>
    <div class="content formulario">
        <form id="create-ps-form" v-on:submit.prevent="processPsSignUp">
            <div class="form-group">
                <label>Diagnostico:</label> <input type="text" class="campo_texto diagnostico" v-model="ps.diagnostico">
            </div>
            <div class="form-group">
                <label>Evolucion:</label> 
                <input type="text" class="campo_texto evolucion" v-model="ps.evolucion">
            </div>
            <div class="form-group">
                <label>Sugerencias: </label>
                <input type="text" class="campo_texto sugerencias_cuidado" v-model="ps.sugerencias_cuidado">
            </div>
            <div class="form-group">
                <label>Paciente ( ID ): </label>  
                <input type="text" class="campo_texto paciente_id_id" v-model="ps.paciente_id_id">
            </div>
            <div class="form-group">
                <label>Medico Encargado ( ID ) </label>
                <input type="text" class="campo_texto ps_id_id" v-model="ps.ps_id_id">
            </div>
            
            
            <button type="submit" class="btn btn-primary">Registrar</button>
            <button class="btn btn-secondary" v-on:click="loadHome">Atras</button>
        </form>
    </div>
</template>
    
<script>
    import axios from 'axios';
    export default {
    name: "Historia_clinicaCreate",
    data: function() {
        return {
            ps: {
                historiaclinica_id: "",
                diagnostico: "",
                evolucion: "",
                sugerencias_cuidado:"",
                paciente_id: "",
                presion_arterial: "",
                ps_id:"",
                
            }
        }
    },
    components: {},
    methods: {
        loadHome: function() {
            console.log("Si funciona");
            this.$router.push({
                    name: "historiaclinica"
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
        // Funcion que conecta con el back en usando axios.post()
        // - Esta funcion recive dos parametros:
        // - 1. La url del backend
        // - 2. El json con el contenido a enviar.
        processPsSignUp: function() {
            axios.post(
                    "https://sane-hospital-vjoha.herokuapp.com/historiasclinicas/",
                    {
                        historiaclinica_id: this.ps.historiaclinica_id,
                        diagnostico:this.ps.diagnostico,
                        evolucion:this.ps. evolucion,
                        sugerencias_cuidado: this.ps.sugerencias_cuidado,
                        paciente_id: this.ps.paciente_id_id,
                        ps_id: this.ps.ps_id_id,
                    }
                       
                )
                .then((result) => {
                    alert("Registro exitoso.")
                    console.log(result);
                    this.$router.push({
                        name: "historiaclinica"
                    });

                })
                .catch((error) => {
                    console.log(error.response.data);
                    alert("Error en el registro. Uno de los IDs foraneos no existe.");
                    this.$router.push({
                        name: "historiaclinica"
                    });

                });
        }
    }
}
</script>

<style> 
    button{
        width: 100%;
        margin: auto;
        display: block;
    }
    form#create-ps-form {
        border: 1px solid black;
        display: block;
        margin: 144px 0;
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
        background: #005073;   
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
        z-index: 99;
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
    
        form{
            padding:16px;
            border-radius: 5px;
        }
        .title {
            padding:16px 0 0 8px;
        }
        .form-group{
            margin:0 0 16px 0;
        }
    }

</style>