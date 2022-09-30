<template>
    <div class="left-sidebar">
            <div class="logIn_user">
            <div class="container_logIn_user">
                <img src = "./../assets/images/user.png" height="90" width="90">
                <h2>Iniciar sesión</h2>
                <form v-on:submit.prevent="processLogInUser" >
                    <input type="text" v-model="user.username" placeholder="Username">
                    <br>
                    <input type="password" v-model="user.password" placeholder="Password">
                    <br>
                    <button type="submit" v-on:click="processLogInUser" >Iniciar Sesion</button>
                </form>
            </div>
        </div>
    </div>
    <div class="content sau">
        <div class="box-container">
            <img class="image_home" src="./../assets/images/medicos.jpg">
        </div>
    </div>
</template>
 <script>
    import axios from 'axios';
    export default {
        name: "LogIn",
        data: function() {
            return {
                user: {
                    username: "",
                    password: ""
                }
            }
        },
        methods: {
            // Funcion que conecta con el back en usando axios.post()
            processLogInUser: function() {
                console.log('Si funciona!');
                axios.post(
                        "https://sane-hospital-vjoha.herokuapp.com/login/",
                        {
                            "username":this.user.username,
                            "password":this.user.password,
                        }
                        
                    )
                    // Si el resultado es correcto hacer esto.
                    .then((result) => {
                        console.log('OMG!!!!!');
                        let dataLogIn = {
                            username: this.user.username,
                            token_access: result.data.access,
                            token_refresh: result.data.refresh,
                        }

                        this.$emit('completedLogIn', dataLogIn)

                    })
                    // Si el resultado es incorrecto hacer esto.
                    .catch((error) => {
                        if (error.response.status == "401")
                            alert("ERROR 401: Credenciales Incorrectas.");
                    });
            }
        }
    }
 </script>
<style>
    .logIn_user{
     margin: 0;
     padding: 0%;
     height: 100%;
     width: 100%;
     display: flex;
     justify-content: center;
     align-items: center;
     margin-top: 100px;
}
 .container_logIn_user {
     border-radius: 10px;
     width: 25%;
     height: auto;
     display: flex;
     flex-direction: column;
     justify-content: center;
     align-items: center;
     min-width: 250px;
     min-height: 350px;
}
 .logIn_user h2{
     color: #283747;
}
.logIn_user form{
     width: 70%;
}
 .logIn_user input{
     height: 40px;
     width: 100%;
     box-sizing: border-box;
     padding: 10px 20px;
     margin: 5px 0;
     border: 1px solid #283747;
}
 .logIn_user button{
     width: 100%;
     height: 40px;
     color: #E5E7E9;
     background: #283747;
     border-radius: 5px;
     padding: 10px 25px;
     margin: 5px 0;
}
 .logIn_user button:hover{
     color: #E5E7E9;
     background: crimson;
     border: 1px solid #283747;
}
.left-sidebar{
    width:28%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: flex-start;
    align-items: center;
    margin: 100px 0;
}
@media (max-width: 768px) {


    img.image_home{
        display: none;
    }
}

</style>