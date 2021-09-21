   
import React from "react";





const ShowComments=(props)=>{
    return(
        <div>
           
            <div>
                        {
                        comment.map((display, index)=> <p key={index} className= "commentsShown"> {display.comment} </p>)
                        }   
                    </div>
                
        </div>
        
   
    )
    
    
}

export default ShowComments
