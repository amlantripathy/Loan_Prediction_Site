const { response } = require("express");
const bodyParser = require("body-parser");
const express=require("express");
const { text } = require("body-parser");
const {spawn} = require("child_process");
const app=express();





app.use(bodyParser.urlencoded({extended: true}));


app.get("/", function(req, res){ 
    res.sendFile(__dirname+"/LOAN.html");
});

app.post("/", function(req,res){
    
    var Name = req.body.Name;
    var Gender= req.body.Gender;
    var Marital_Status= req.body.Marital_Status;
    var No_of_Dependents= req.body.No_of_Dependents;
    var Education= req.body.Education;
    var Self_Employed= req.body.Self_Employed;
    var Income= req.body.Income;
    var Coapplicant_Income= req.body.Coapplicant_Income;
    var Loan_Amount= req.body.Loan_Amount;
    var Loan_Amount_Term= req.body.Loan_Amount_Term;
    var Credit_History= req.body.Credit_History;
    var Property_Location= req.body.Property_Location;
    const py =spawn('python', ['updated code.py',Gender,Marital_Status,No_of_Dependents,Education,Self_Employed,Income,Coapplicant_Income,Loan_Amount,Loan_Amount_Term,Credit_History,Property_Location]);
    py.stdout.on('data', (data) =>{
        console.log(`stdout: ${data}`);
        res.send(`${data}`);
    });

    py.on('close' ,(code) =>{
        console.log(`code exited ${code}`);
    });

});





app.listen(3000, function(){
    console.log("ml model on the way")
});

