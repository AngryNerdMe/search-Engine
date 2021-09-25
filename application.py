import flask
from flask import render_template
import requests
import json
import js2py
from flask import Flask ,request
 
application = Flask(__name__ ,static_folder="app/static",template_folder="app/static")

@application.route("/icaisearch")
def icaisearch():
   return  render_template("webpage.html")

@application.route("/grab_data",methods=['GET'])
def grab_data():
    #return "hello"
    print("done")
    query=request.args.get("user_data")
    drop_down_data=request.args.get("cars")
    chooose_dict={"0":"pulkit","1":"testing"}
    var=str(chooose_dict[drop_down_data])
    
    # taking user drop down data



   
    
    #query = "what ic CA?"
    user_query = "https://eolrvhhdn1.execute-api.ap-southeast-1.amazonaws.com/testing-stage/kendra-config?user_name="+query+"&se_para="+var
    json_data = requests.get(user_query)
    #content=json.load(json_data)
    new_data=json_data.json()
    content=new_data["user_data"]["Content"]
    filtered_list=[]
    for data in content:
       filtered_list.append(''.join(data))
  

    links=new_data["user_data"]["Links"]
    page_numbers=new_data["user_data"]["page_numbers"]
    filtered_page_numbers=[]
    for  items in  page_numbers:
        filtered_page_numbers.append("Page Number.."+" "+str(items))



    filtered_links=[]
    for items in links:
       filtered_links.append(items.split('/')[-1])
    title=new_data["user_data"]["Doctitle"]
    return render_template("page_redirect.html",filtered_links=filtered_links,title=title,content=content,query=query,filtered_page_numbers=filtered_page_numbers)
    #user_data = request.form['user_data']
    #print(user_data)
    #return "hello"
    
    
    #user_query = "https://eolrvhhdn1.execute-api.ap-southeast-1.amazonaws.com/testing-stage/kendra-config?user_name="+"what ic icai?"
    #json_data = requests.get(user_query)
   
    #data=request.form["user_data"]

'''
@app.route('/dropdown_data',methods=['POST','GET'])
def dropdown_data():
   word=requests.args.get('icai')
   print("helllo")
'''
   


    


if __name__ == "__main__":
    application.run(debug=True)




    #json_data=requests.get(search_query)
    #refined_json_data=json.dumps(json_data)
    #links=
    #titles=
    #content=[]
    #return render_template("page_redirect.html",links=links,titles=titles,content=content)





