from flask import Flask, render_template, request, session
from classes.person import Person
from datafile import filename
from classes.customer import Customer
from classes.product import Product
from classes.customerorder import CustomerOrder
from classes.orderproduct import OrderProduct
from classes.userlogin import Userlogin

app = Flask(__name__)

Person.read(filename + 'Person.db')
Customer.read(filename + 'business.db')
Product.read(filename + 'business.db')
CustomerOrder.read(filename + 'business.db')
OrderProduct.read(filename + 'business.db')
Userlogin.read(filename + 'business.db')
prev_option = ""
app.secret_key = 'BAD_SECRET_KEY'


@app.route("/")
def index():
    return render_template("index.html", ulogin=session.get("user"))
    
@app.route("/login")
def login():
    return render_template("login.html", user= "", password="", ulogin=session.get("user"),resul = "")

@app.route("/logoff")
def logoff():
    session.pop("user",None)
    return render_template("index.html", ulogin=session.get("user"))

@app.route("/chklogin", methods=["post","get"])
def chklogin():
    user = request.form["user"]
    password = request.form["password"]
    resul = Userlogin.chk_password(user, password)
    if resul == "Valid":
        session["user"] = user
        return render_template("index.html", ulogin=session.get("user"))
    return render_template("login.html", user=user, password = password, ulogin=session.get("user"),resul = resul)


@app.route("/gform/<cname>", methods=["post","get"])
def gform(cname=''):
    global prev_option
    ulogin=session.get("user")
    if (ulogin != None):
        cl = eval(cname)
        butshow = "enabled"
        butedit = "disabled"
        option = request.args.get("option")
        if prev_option == 'insert' and option == 'save':
            strobj = request.form[cl.att[0]]
            for i in range(1,len(cl.att)):
                strobj += ";" + request.form[cl.att[i]]
            obj = cl.from_string(strobj)
            cl.insert(getattr(obj, cl.att[0]))
            cl.last()
        elif prev_option == 'edit':
            obj = cl.current()
            for att in cl.att:
                setattr(obj, att, request.form[att])
            cl.update(getattr(obj, cl.att[0]))
        else:
            if option == "edit":
                butshow = "disabled"
                butedit = "enabled"
            elif option == "delete":
                obj = cl.current()
                cl.remove(obj.code)
                if not cl.previous():
                    cl.first()
                cl.write(filename)
            elif option == "insert":
                butshow = "disabled"
                butedit = "enabled"
            elif option == 'cancel':
                pass
            elif option == "first":
                cl.first()
            elif option == "previous":
                cl.previous()
            elif option == "next":
                cl.nextrec()
            elif option == "last":
                cl.last()
            elif option == 'exit':
                return render_template("index.html", ulogin=session.get("user"))
        prev_option = option
        obj = cl.current()
        if option == 'insert' or len(cl.lst) == 0:
            obj = dict()
            for att in cl.att:
                obj[att] = ""
        # else:
        #     for att in cl.att:
        #         dobj[att[1:]] = getattr(obj, att)
        # return render_template("gform.html", butshow=butshow, butedit=butedit, cname=cname, code=code,name = name,dob=dob,salary=salary)
        return render_template("gform.html", butshow=butshow, butedit=butedit, cname=cname, obj=obj,att=cl.att,des=cl.des,ulogin=session.get("user"))
    else:
        return render_template("index.html", ulogin=ulogin)

@app.route("/Person", methods=["post","get"])
def person():
    global prev_option
    ulogin=session.get("user")
    if (ulogin != None):
        butshow = "enabled"
        butedit = "disabled"
        option = request.args.get("option")
        if option == "edit":
            butshow = "disabled"
            butedit = "enabled"
        elif option == "delete":
            obj = Person.current()
            Person.remove(obj.code)
            if not Person.previous():
                Person.first()
            Person.write(filename)
        elif option == "insert":
            butshow = "disabled"
            butedit = "enabled"
        elif option == 'cancel':
            pass
        elif prev_option == 'insert':
            strobj = request.form["code"] + ';' + request.form["name"] + ';' + \
            request.form["dob"] + ';' + request.form["salary"]
            obj = Person.from_string(strobj)
            Person.insert(obj.code)
            Person.last()
        elif prev_option == 'edit':
            obj = Person.current()
            obj.code = request.form["code"]
            obj.name = request.form["name"]
            obj.dob = request.form["dob"]
            obj.salary = float(request.form["salary"])
            Person.update(obj.code)
        elif option == "first":
            Person.first()
        elif option == "previous":
            Person.previous()
        elif option == "next":
            Person.nextrec()
        elif option == "last":
            Person.last()
        elif option == 'exit':
            return render_template("index.html", ulogin=session.get("user"))
        prev_option = option
        obj = Person.current()
        if option == 'insert' or len(Person.lst) == 0:
            code = ""
            name = ""
            dob = ""
            salary = ""
        else:
            code = obj.code
            name = obj.name
            dob = obj.dob
            salary = obj.salary
        return render_template("person.html", butshow=butshow, butedit=butedit, code=code,name = name,dob=dob,salary=salary, ulogin=session.get("user"))
    else:
        return render_template("index.html", ulogin=ulogin)
        
@app.route("/subform/<cname>", methods=["post","get"])
def subform(cname=""):
    global prev_option
    tlist = cname.split('_')
    cnames = tlist[0]
    scname = tlist[1]
    ulogin=session.get("user")
    if (ulogin != None):
        cl = eval(cnames)
        sbl = eval(scname)
        butshow = "enabled"
        butedit = "disabled"
        option = request.args.get("option")
        if prev_option == 'insert':
            strobj = request.form[cl.att[0]]
            for i in range(1,len(cl.att)):
                strobj += ";" + request.form[cl.att[i]]
            obj = cl.from_string(strobj)
            cl.insert(getattr(obj, cl.att[0]))
            cl.last()
        elif prev_option == 'edit':
            obj = cl.current()
            for att in cl.att:
                setattr(obj, att, request.form[att])
            cl.update(getattr(obj, cl.att[0]))
        else:
            if option == "edit":
                butshow = "disabled"
                butedit = "enabled"
            elif option == "delete":
                obj = cl.current()
                lines = sbl.getlines(getattr(obj, cl.att[0]))
                for line in lines:
                    sbl.remove(line)
                cl.remove(obj.code)
                if not cl.previous():
                    cl.first()
            elif option == "insert":
                butshow = "disabled"
                butedit = "enabled"
            elif option == 'cancel':
                pass
            elif option == "first":
                cl.first()
            elif option == "previous":
                cl.previous()
            elif option == "next":
                cl.nextrec()
            elif option == "last":
                cl.last()
            elif option[:6] == "delrow":
                row = int(option.split("_")[1])
                obj = cl.current()
                lines = sbl.getlines(getattr(obj, cl.att[0]))
                print(row,lines[row])
                sbl.remove(lines[row])
            elif option == "addrow":
                butshow = "disabled"
                butedit = "disabled"
            elif option == "saverow":
                obj = cl.current()
                strobj = getattr(obj, cl.att[0])
                for i in range(1,len(sbl.att)):
                    strobj += ";" + request.form[sbl.att[i]]
                objl = sbl.from_string(strobj)
                code = str(getattr(objl, sbl.att[0])) + str(getattr(objl, sbl.att[1]))
                print(code, objl)
                sbl.insert(code)
            elif option == 'exit':
                return render_template("index.html", ulogin=session.get("user"))
        prev_option = option
        obj = cl.current()
        headers = list()
        objl = list()
        if option == 'insert' or len(cl.lst) == 0:
            obj = dict()
            for att in cl.att:
                obj[att] = ""
        else:
            for i in range(1, len(sbl.att)):
                    headers.append(sbl.att[i][1:])        
            lines = sbl.getlines(getattr(obj, cl.att[0]))
            for line in lines:
                objl.append(sbl.obj[line])
        # return render_template("gform.html", butshow=butshow, butedit=butedit, cname=cname, code=code,name = name,dob=dob,salary=salary)
        return render_template("subform.html", butshow=butshow, butedit=butedit, cname=cname, obj=obj,att=cl.att,des=cl.des, ulogin=session.get("user"),objl=objl,desl=sbl.des, attl=sbl.att)
    else:
        return render_template("index.html", ulogin=ulogin)


@app.route("/Userlogin", methods=["post","get"])
def userlogin():
    global prev_option
    ulogin=session.get("user")
    if (ulogin != None):
        group = Userlogin.obj[ulogin].usergroup
        if group != "admin":
            Userlogin.current(ulogin)
        butshow = "enabled"
        butedit = "disabled"
        option = request.args.get("option")
        if option == "edit":
            butshow = "disabled"
            butedit = "enabled"
        elif option == "delete":
            obj = Userlogin.current()
            Userlogin.remove(obj.user)
            if not Userlogin.previous():
                Userlogin.first()
        elif option == "insert":
            butshow = "disabled"
            butedit = "enabled"
        elif option == 'cancel':
            pass
        elif prev_option == 'insert' and option == 'save':
            obj = Userlogin(request.form["user"],request.form["usergroup"], \
                            Userlogin.set_password(request.form["password"]))
            Userlogin.insert(obj.user)
            Userlogin.last()
        elif prev_option == 'edit':
            obj = Userlogin.current()
            if group == "admin":
                obj.usergroup = request.form["usergroup"]
            if request.form["password"] != "":
                obj.password = Userlogin.set_password(request.form["password"])
                print(obj.password)
            Userlogin.update(obj.user)
        elif option == "first":
            Userlogin.first()
        elif option == "previous":
            Userlogin.previous()
        elif option == "next":
            Userlogin.nextrec()
        elif option == "last":
            Userlogin.last()
        elif option == 'exit':
            return render_template("index.html", ulogin=session.get("user"))
        prev_option = option
        obj = Userlogin.current()
        if option == 'insert' or len(Userlogin.lst) == 0:
            user = ""
            usergroup = ""
            password = ""
        else:
            user = obj.user
            usergroup = obj.usergroup
            password = ""
        return render_template("userlogin.html", butshow=butshow, butedit=butedit, user=user,usergroup = usergroup,password=password, ulogin=session.get("user"), group=group)
    else:
        return render_template("index.html", ulogin=ulogin)


if __name__ == '__main__':
    app.run()