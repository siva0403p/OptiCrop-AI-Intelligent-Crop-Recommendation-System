// ======================================
// OptiCrop AI
// Frontend Interactions
// ======================================

document.addEventListener("DOMContentLoaded", () => {

    console.log("🌱 OptiCrop AI Loaded Successfully");

    const form = document.querySelector("form");

    if(form){

        form.addEventListener("submit", ()=>{

            const button=document.querySelector(".predict-btn");

            button.disabled=true;

            button.innerHTML="⏳ Predicting...";

        });

    }

});