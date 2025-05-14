def call(){
   pipeline{
     agent any
     stages{
       stage("demo stage"){
          steps{
            echo "Hi I am demo stage - changes added by feature branch"
          }
       }
     }
   }
}
