<template>
    <div class="left-sidebar">
        <img src = "./../assets/images/user.png" height="120" width="120">
        <span style="text-align:center; margin:30px; font-size:30px">Familiar paciente</span> 
       
    </div>
    <div class="content">
        <div class="ps_data">
            <ul>
                <li><span>Nombre: </span>{{nombre}}</li>
                <li><span>Apellido: </span>{{apellido}}</li>
                <li><span>Tipo Documento: </span>{{tipo_documento}}</li>
                <li><span>Numero Documento: </span>{{numero_documento}}</li>
                <li><span>Parentesco: </span>{{parentesco}}</li>
                <li><span>Genero: </span>{{genero}}</li>
                <li><span>Telefono: </span>{{telefono}}</li>
                <li><span>Correo Electronico: </span>{{correo_electronico}}</li>
                <li><span>ID paciente</span>: {{paciente_id}}</li>
            </ul>
            <button v-on:click="loadHome" class="btn"> Atras </button>
        </div>

    </div>
</template>
    
<script>

    export default {
    name: "FamiliarDetail",
    data: function() {
        return {
            nombre: localStorage.getItem("nombre"),
            apellido:localStorage.getItem("apellido"),
            tipo_documento:localStorage.getItem("tipo_documento"),
            numero_documento:localStorage.getItem("numero_documento"),
            parentesco: localStorage.getItem("parentesco"),
            genero: localStorage.getItem("genero"),
            telefono:  localStorage.getItem("telefono"),
            correo_electronico:  localStorage.getItem("correo_electronico"),
            User_id: localStorage.getItem("User_id"),
            paciente_id: localStorage.getItem("paciente_id"),
        }
    },
    components: {},
    methods: {
        loadHome: function() {
            console.log("Si funciona");
            this.$router.push({
                    name: "familiar"
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
        }
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