<template>
    <div id="app" class="app">
       <div class="header">
          <h1>Sante Hospital App</h1>
          <img src='./assets/images/LogoSante1.png'>
          <nav>
             <button v-if="is_auth" v-on:click="loadHome"> Inicio </button>
             <!-- <button v-if="is_auth" > Cuenta </button> -->
             <button v-if="is_auth" v-on:click="logOut" > Cerrar Sesión </button>
             <button v-if="!is_auth" v-on:click="loadLogIn" > Login </button>
             <button v-if="!is_auth" v-on:click="loadSignUp" > Registrarse </button>
          </nav>
       </div>
       <div class="main-component" >
          <router-view
            v-on:completedLogIn="completedLogIn"
            v-on:completedSignUp="completedSignUp"
            v-on:logOut="logOut"
            >
            </router-view>
       </div>
       <div class="footer">
          <h2>Sante Hospital 2022</h2>
       </div>
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
            logOut: function() {
                localStorage.clear();
                alert("Sesión Cerrada");
                this.verifyAuth();
            },
        },
        created: function() {
            this.verifyAuth()
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
    .header{
        margin: 0%;
        padding: 8px 16px;
        height: 10vh;
        min-height: 100px;
        background-color: #283747;
        color:#E5E7E9;
        display: flex;
        justify-content : space-between;
        align-items : center ;
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
     color : #E5E7E9 ;
     background : #283747 ;
     border : 1px solid #E5E7E9 ;
     border-radius : 5px ;
     padding : 10px 20px ;
}
 .header nav button:hover {
     color : #283747 ;
     background : #E5E7E9 ;
     border : 1px solid #E5E7E9 ;
}
 .main-component {
     height : 75vh ;
     margin : 0% ;
     padding : 0% ;
     background : #FDFEFE ;
}
 .footer {
     margin : 0 ;
     padding : 0 ;
     width: 100%;
     height: auto;
     min-height: 100px;
     background-color: #283747;
     color: #E5E7E9;
     bottom: 0;
     position: absolute;
}
 .footer h2{
     width: 100%;
     height: 100%;
     display: flex;
     justify-content: center;
     align-items: center;
}

</style>