<template>
    <div class="left-sidebar">
        <img src = "./../assets/images/user.png" height="120" width="120">
        <span style="text-align:center; margin:30px; font-size:30px">Crear Personal Salud</span> 
       
    </div>
    <div class="content sau">
        <form id="create-ps-form" v-on:submit.prevent="processPsSignUp">
        <div class="form-group">
            <label>Nombre:</label> <input type="text" class="campo_texto nombre" v-model="ps.nombre">
        </div>
        <div class="form-group">
            <label>Apellido:</label> <input type="text" class="campo_texto apellido" v-model="ps.apellido">
        </div>
        <div class="form-group">
            <label>Tipo de Documento: </label>
            <select type="text" class="campo_texto " v-model="ps.tipo_documento">
                <option>   </option>
                <option>T.I</option>
                <option>C.C</option>
            </select> 
        </div>
        <div class="form-group">
            <label>Numero de Documento: </label>  <input type="text" class="campo_texto " v-model="ps.numero_documento">
        </div>
        <div class="form-group">
            <label>Genero: </label>
            <select type="text" class="campo_texto " v-model="ps.genero">
                <option>   </option>
                <option>M</option>
                <option>F</option>
            </select>
         </div>
         <div class="form-group">
            <label>Tipo: </label>
            <select type="text" class="campo_texto " v-model="ps.tipo">
                <option>   </option>
                <option>Medico</option>
                <option>Enfermera</option>
            </select>
        </div>
        <div class="form-group">
            <label>Ciudad:</label> <input type="text" class="campo_texto " v-model="ps.ciudad">
       </div>
       <div class="form-group">
            <label>Telefono:</label> <input type="text" class="campo_texto " v-model="ps.telefono">
       </div>
       <div class="form-group">
            <label>Email:</label> <input type="text" class="campo_texto " v-model="ps.correo_electronico">
       </div>
        <div class="form-group">
            <label>Fecha Nacimiento:</label> <input type="date" class="campo_texto " v-model="ps.fecha_nacimiento">
       </div>
        <div class="form-group">
            <label>Especialidad: </label>
            <select type="text" class="campo_especialidad" v-model="ps.especialidad_id">
                <option>   </option>
                <option>1</option>
                <option>2</option>
            </select>
         </div>
        <div class="form-group">
        <label>Registro: </label> <input type="text" class="campo_registro" v-model="ps.registro">
        </div>
        <button type="submit" class="btn btn-primary">Registrar</button>
        <button type="submit" class="btn btn-secondary" v-on:click="loadHome">Atras</button>
    </form>
    </div>
</template>
    
<script>
    import axios from 'axios';
    export default {
    name: "CreatePs",
    data: function() {
        return {
            ps: {
                nombre: "",
                apellido: "",
                tipo_documento: "",
                numero_documento: "",
                genero: "",
                tipo: "",
                ciudad: "",
                fecha_nacimiento: "",
                especialidad_id: "",
                registro: "",
                telefono: "",
                correo_electronico: "",
                User_id: 1,
            }
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
        // Funcion que conecta con el back en usando axios.post()
        // - Esta funcion recive dos parametros:
        // - 1. La url del backend
        // - 2. El json con el contenido a enviar.
        processPsSignUp: function() {
            axios.post(
                    "https://sane-hospital-vjoha.herokuapp.com/ps/",
                    {
                        nombre: this.ps.nombre,
                        apellido: this.ps.apellido,
                        tipo_documento: this.ps.tipo_documento,
                        numero_documento: this.ps.numero_documento,
                        genero: this.ps.genero,
                        tipo: this.ps.tipo,
                        ciudad: this.ps.ciudad,
                        fecha_nacimiento: "2009-09-09",
                        especialidad_id: this.ps.especialidad_id,
                        registro: this.ps.registro,
                        telefono: this.ps.telefono,
                        correo_electronico: this.ps.correo_electronico,
                        User_id: 1
                    }
                )
                .then((result) => {
                    console.log("Registro exitoso.")
                    this.$router.push({
                        name: "personalsalud"
                    });

                })
                .catch((error) => {
                    console.log(error.response.data);
                    alert("ERROR: Fallo en el registro.");

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