from flask import Flask, render_template, request, session
from classes.store import Store

prev_option = ""

def apps_store():
    global prev_option
    ulogin=session.get("user")
    if (ulogin != None):
        butshow = "enabled"
        butedit = "disabled"
        option = request.args.get("option")
        if option == "edit":
            butshow, butedit = "disabled", "enabled"
        elif option == "delete":
            obj = Store.current()
            Store.remove(obj.id)
            if not Store.previous():
                Store.first()
        elif option == "insert":
            butshow, butedit = "disabled", "enabled"
        elif option == 'cancel':
            pass
        elif prev_option == 'insert' and option == 'save':
            strobj = str(Store.get_id(0))
            strobj = strobj + ';' + request.form["name"] + ';' + \
            request.form["location"]
            obj = Store.from_string(strobj)
            Store.insert(obj.id)
            Store.last()
        elif prev_option == 'edit' and option == 'save':
            obj = Store.current()
            obj.name = request.form["name"]
            obj.location = request.form["location"]
            Store.update(obj.id)
        elif option == "first":
            Store.first()
        elif option == "previous":
            Store.previous()
        elif option == "next":
            Store.nextrec()
        elif option == "last":
            Store.last()
        elif option == 'exit':
            return render_template("index.html", ulogin=session.get("user"))
        prev_option = option
        obj = Store.current()
        if option == 'insert' or len(Store.lst) == 0:
            id = 0
            id = Store.get_id(id)
            name = location= ""
        else:
            id = obj.id
            name = obj.name
            location = obj.location
        return render_template("store.html", butshow=butshow, butedit=butedit, 
                        id=id,name = name,location=location,
                        ulogin=session.get("user"))
    else:
        return render_template("index.html", ulogin=ulogin)
# -*- coding: utf-8 -*-

