<template>
    <div id="app" class="app">
       <!-- El header -->
        <header>
            <div class="header">
                <!-- <h1>Sante Hospital App</h1> -->
                <img src='./assets/images/logo-slogan.png' height="90">
                <nav>
                    <button v-if="is_auth" v-on:click="loadHome"> Inicio </button>
                    <!-- <button v-if="is_auth" > Cuenta </button> -->
                    <button v-if="is_auth" v-on:click="logOut" > Cerrar Sesión </button>
                    <button v-if="!is_auth" v-on:click="loadLogIn" > Login </button>
                    <button v-if="!is_auth" v-on:click="loadSignUp" > Registrarse </button>
                </nav>
            </div>
        </header>

        <!-- El main component -->
       <div class="main-component" >
        <!-- Router-view muestra el componente asociado a el URL actual. -->
        <!-- - La logica"v-on:"" valida si el usuario esta loggeado o no y direccion al home o al login. -->
          <router-view
            v-on:completedLogIn="completedLogIn"
            v-on:completedSignUp="completedSignUp"
            v-on:logOut="logOut"
            >
            </router-view>
       </div>

       <!-- El footer -->
       <footer class="pie-pagina">
        <div class="grupo-1">
            <div class="box">
                <figure>
                    <a href="#">
                        <img src="./assets/images/logo-slogan.png" alt="Logo de SLee Dw">
                    </a>
                </figure>
            </div>
            <div class="box">
                <h2>REDES SOCIALES</h2>
                <p>Encuentra más información en nuestras redes sociales disponibles.</p>
                
            </div>

            <div class="box">
                <h2>¿Tienes alguna inquietud?</h2>

                <p>Déjanos tu correo electrónico para comunicarnos contigo</p>
                <input  class = "campotxt" type="text" name="correo electrónico" placeholder =" Ingresa tu correo electrónico"/>

                
                
            </div>
            <br>
            <br>
            <br>
            <br>
            <div class="box">
            
                <div class="red-social">
                    <a href="#" class="fa fa-facebook" ><img src="./assets/images/facebook2.png" alt="Logo de SLee Dw"></a>
                    <a href="#" class="fa fa-instagram"><img src="./assets/images/instagram.png" alt="Logo de SLee Dw"></a>
                    <a href="#" class="fa fa-twitter"><img src="./assets/images/twitter.png" alt="Logo de SLee Dw"></a>
                    <a href="#" class="fa fa-whatsapp"><img src="./assets/images/whatsapp.png" alt="Logo de SLee Dw"></a>
                </div>
            </div>
        </div>
        <div class="grupo-2">
            <small>&copy; 2022 <b>Santé</b> - Todos los Derechos Reservados.</small>
        </div>
    </footer>
    </div>
 </template>
<script >
    export default {
        name: 'App',
        data: function() {
            return {
                is_auth: false
            }
        },
        components: {},
        methods: {
            // Funcion que verifica si el usuario esta loggeado o no.
            verifyAuth: function() {
                this.is_auth = localStorage.getItem("isAuth") || false;
                if (this.is_auth == false)
                    this.$router.push({
                        name: "logIn"
                    });
                else
                    this.$router.push({
                        name: "home"
                    });
            },
            loadLogIn: function() {
                this.$router.push({
                    name: "logIn"
                })
            },
            loadSignUp: function() {
                this.$router.push({
                    name: "signUp"
                })
            },
            completedLogIn: function(data) {
                localStorage.setItem("isAuth", true);
                localStorage.setItem("username", data.username);
                localStorage.setItem("token_access", data.token_access);
                localStorage.setItem("token_refresh", data.token_refresh);
                alert("Autenticación Exitosa");
                this.verifyAuth();
            },
            completedSignUp: function(data) {
                alert("Registro Exitoso");
                this.completedLogIn(data);
            },
            loadHome: function() {
                this.$router.push({
                    name: "home"
                });
            },
            loadServicios: function() {
                this.$router.push({
                    name: "servicios"
                });
            },
            logOut: function() {
                localStorage.clear();
                alert("Sesión Cerrada");
                this.verifyAuth();
            },
        },
        created: function() {
            this.verifyAuth();
        }
    } 
    </script>
<style>
    @import url('https://fonts.googleapis.com/css?family=Montserrat&display=swap');
    @import url('https://fonts.googleapis.com/css?family=Quicksand&display=swap');
    body{
     margin: 0 0 0 0;
     font-family: 'Montserrat', sans-serif;
    }

    p{
        padding: 0 !important;
    }
    header {
        width: 100%;
        display: flex;
        justify-content: center;
    }
    .header{
        margin: 0%;
        padding: 8px 16px;
        height: 050px;
        min-height: 100px;
        background-color: #fff;
        color:#E5E7E9;
        display: flex;
        justify-content : space-between;
        align-items : center ;
        border-bottom: 1px solid rgb(185, 183, 183);
        position:fixed;
        width: 100%;
        max-width: 1300px;
        margin: auto;
    }
    .header h1 {
        width : 20% ;
        text-align : center ;
        min-width: 355px;
    }
    .header nav {
        height : 100% ;
        width : 20% ;
        display : flex ;
        justify-content : flex-end ;
        align-items : center ;
        font-size : 20px ;
        gap: 22px;
    }
    .header nav button {
        color : white;
        background : #71c7ec ;
        border : 1px solid #E5E7E9 ;
        border-radius : 5px ;
        padding : 10px 20px ;
        font-size: 18px;
        font-weight: bold;
        cursor: pointer;
    }
    .header nav button:hover {
        background : 	#107dac ;
        border : 1px solid #E5E7E9 ;
    }
    .main-component {
        margin : 0% ;
        padding : 0% ;
        background : #FDFEFE ;
        display: flex;
        overflow:scroll;
        min-height: 350px;
        max-width: 1250px;
        margin: auto;
    }
    a{
        cursor: pointer;
    }

    .buscar,.atras{
        max-width: 150px;
        color: white !important;
        margin: 16px;
        font-weight: bold;
        font-size: 16px;
    }
    @import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;700&display=swap');
    *{
        margin: 0;
        padding: 0;
        box-sizing: border-box;
        font-family: 'Open Sans', sans-serif;
    }

    .pie-pagina{
        width: 100%;
        background-color: #b6ddff;
    }
    .pie-pagina .grupo-1{
        width: 100%;
        max-width: 1200px;
        margin: auto;
        display:grid;
        grid-template-columns: repeat(3, 1fr);
        grid-gap:50px;
        padding: 45px 0px;
    }
    .pie-pagina .grupo-1 .box figure{
        width: 100%;
        height: 100%;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .pie-pagina .grupo-1 .box figure img{
        width: 120px;
    }
    .pie-pagina .grupo-1 .box h2{
        color: rgb(0, 0, 0);
        margin-bottom: 25px;
        font-size: 20px;
    }
    .pie-pagina .grupo-1 .box p{
        color: #000000;
        margin-bottom: 10px;
    }
    .pie-pagina .grupo-1 .red-social a{
        display: inline-block;
        text-decoration: none;
        width: 50px;
        height: 50px;
        line-height: 45px;
        color: #fff;
        margin-right: 10px;
        text-align: center;
        transition: all 300ms ease;
    }

    .campotxt{

        width: 80%;
        height: 40px;
        border: 1px solid #134F5C;
        border-radius: 4px;
    }

    .pie-pagina .grupo-1 .red-social a:hover{
        color: #134F5C ;
    }
    .pie-pagina .grupo-2{
        background-color: #6FA8DC;
        padding: 15px 10px;
        text-align: center;
        color: rgb(0, 0, 0);
    }
    .pie-pagina .grupo-2 small{
        font-size: 15px;
    }

    .input{

        height: 20px;
        width: 50px;
    }

    .content {width: 70%}

    .content.formulario form {
        border: 1px solid #000;
        display: block;
        margin: 144px 0;
        width: 70%;
        padding: 10px;
        font-size: 27px;
        border: 2px solid #189ad3;

    }

    form button.btn {
        font-size: 24px;
        color: white;
    }

    .form-group {
        margin: 16px;
        height: 40px;
        display: flex;
        justify-content: flex-start;
        gap: 29px;
    }

    .form-group input, .form-group select {
        border: 2px solid #189ad3;
        border-radius: 5px;
    }

    form#FormularioSerchPs {
        display: block;
    }
    form#FormularioSerchPs .form-group{
        display: block;
    }
    .buttons {
        display: flex;
    }
    @media screen and (max-width:800px){
        .pie-pagina .grupo-1{
            width: 90%;
            grid-template-columns: repeat(1, 1fr);
            grid-gap:30px;
            padding: 35px 0px;
        }
        .main-component{
            flex-direction: column;
        }
        .left-sidebar{
            width: 100% !important;
        }
    }

</style>