from flask import Flask

app = Flask(__name__)

@app.route('/home') 
def home(): 
    return '''<html>
     <h1>Welcome! Dive into our adventure! </h1> 
     <body> <p> We will be exploring different pets, foods and outer space! </p>  
     <img src = "https://www.chefspencil.com/wp-content/uploads/DISHES-OF-ARABIAN-CUISINE.jpeg" width = "400"> 
      <img src = "https://t3.ftcdn.net/jpg/04/81/85/46/360_F_481854656_gHGTnBscKXpFEgVTwAT4DL4NXXNhDKU9.jpg" width = "715">  
      <img src = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQAWRpInBBIezN3V57bCHII9sLUXgV_mlfA3A&s" width = "600"> 
      <a href = "/food1"> CLICK HERE </a>   
      <a href = "fav_pet"> FAVORITE PET </a> 
      <a href = "/outer_space"> OUTER SPACE </a> 
      </body> 
      </html> '''

@app.route('/food1') 
def food1 () : 
    return ''' <html> <h1> Go to the first food photo </h1> 
      <a href = "/home"> HOME PAGE  </a>   
      <a href = "/fav_food"> FAVORITE FOOD </a> 
    </html> ''' 
    

@app.route ('/fav_food') 
def fav_food () : 
    return ''' <html>  
      <img src = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRYPgkKVWotfIIZwSoI7lFxTgFntFjhK9a-Vg&s" width = "400">     
      <a href = "/home"> HOME PAGE </a>  
      <a href = "/fav_food1"> FOOD 2  </a>
    </html> ''' 

@app.route ('/fav_food1') 
def fav_food1 () :
    return ''' <html>  
      <img src = "https://www.themediterraneandish.com/wp-content/uploads/2023/02/Cauliflower-Shawarma_8-500x500.jpg" width = "400">  
      <a href = "/home"> HOME PAGE </a> 
      <a href = "/fav_food2"> FOOD 3  </a>
      
    </html> ''' 

@app.route ('/fav_food2') 
def fav_food2 () : 
    return ''' <html>  
      <img src = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT9UjKooD4BTb5DCHiLvNGU-MtLw6Wg1lnYWg&s" width = "400"> 
      <a href = "/home"> HOME PAGE </a> 
    </html> ''' 

    

@app.route ('/fav_pet') 
def fav_pet () : 
    return ''' <html>  
      <img src = "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcTeydP73x0Bvoe27Z8-N4idn2sUsOwPxNFIPuPll6YR8kyEqEaw" width = "400">     
      <a href = "/home"> HOME PAGE </a>  
      <a href = "/fav_pet2"> PET 2  </a>
    </html> ''' 

@app.route ('/fav_pet2') 
def fav_pet2 () :
    return ''' <html>  
      <img src = "https://cdn.britannica.com/30/150930-120-D3D93F1E/lion-Namibia.jpg" width = "400">  
      <a href = "/home"> HOME PAGE </a> 
      <a href = "/fav_pet3"> PET 3  </a>
      
    </html> ''' 

@app.route ('/fav_pet3') 
def fav_pet3 () : 
    return ''' <html>  
        <img src = "https://i.natgeofe.com/k/e7ba8001-23ac-457f-aedb-abd5f2fdda62/moms5_4x3.png" width = "400"> 
        <a href = "/home"> HOME PAGE  </a>   
        </html> ''' 


@app.route ('/outer_space') 
def outer_space () : 
    return ''' <html>  
      <img src = "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/Webb%27s_First_Deep_Field.jpg/1200px-Webb%27s_First_Deep_Field.jpg" width = "400">     
      <a href = "/home"> HOME PAGE </a>  
      <a href = "/outer_space1"> SPACE 1  </a>
    </html> ''' 

@app.route ('/outer_space1') 
def outer_space1 () :
    return ''' <html>  
      <img src = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSgTc2V1FngTfLoX526H97RWBP68sOQE7BJ6Q&s" width = "400">  
      <a href = "/home"> HOME PAGE </a> 
      <a href = "/outer_space2"> SPACE 2  </a>
      
    </html> ''' 

@app.route ('/outer_space2') 
def outer_space2 () : 
    return ''' <html>  
        <img src = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRnOPOwI4YtncLBPLdXZIZsWAMBUbC9CSeqMg&s" width = "400"> 
        <a href = "/home"> HOME PAGE  </a>   
        </html> ''' 

if __name__ == '__main__': 
    app.run(debug=True) 

