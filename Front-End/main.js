var nav=document.querySelectorAll(".navclass a");
for (var i = 0; i < nav.length; i++) {
    nav[i].addEventListener("mouseover",function(){
        this.classList.add("selected")
    });
    nav[i].addEventListener("mouseout",function()
    {
        this.classList.remove("selected");
    });
    nav[i].addEventListener("click",function(){
    	this.classList.toggle("done");
    })
    
}