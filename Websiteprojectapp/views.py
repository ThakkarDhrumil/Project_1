from django.shortcuts import redirect
from django.shortcuts import render
import mysql
from mysql.connector import Error
# Create your views here.
def get(request):
    return render(request, 'main/index.html')
def loginindex(request):
    return render(request,'login/index.html')
def regindex(request):
    return render(request,'register/index.html')

def regdata(request):
    try:
        con=mysql.connector.connect(host='localhost',database='project',user='root',password='root')
        cursor=con.cursor()
       # f_name=request.POST.get("firstname")
        #l_name=request.POST.get("lastname")
        email=request.POST.get("email")
        password=request.POST.get("password")
        query="insert into registiation(email,password)values('%s', '%s')" %(email,password)
        cursor.execute(query)
        con.commit()
        return redirect(contentpage)

    except Error as e:
        print(e)


    finally:
        cursor.close()
        con.close()

def feedback(request):
    try:
        fcon=mysql.connector.connect(host='localhost',database='project',user='root',password='root')
        fcursor=fcon.cursor()
        fname=request.POST.get("fname")
        faddress=request.POST.get("faddress")
        query="insert into feedback(name,feedback)values('%s','%s')" %(fname,faddress)
        fcursor.execute(query)
        fcon.commit()
        msg1="feedback inserted"
        return render(request,'main/index.html',{'feedback':msg1})

    except Error as e:
        print(e)


    finally:
        fcursor.close()
        fcon.close()

'''def logindata(request):
    try:
        lcon=mysql.connector.connect(host='localhost',database='project',user='root',password='root')
        lcursor=lcon.cursor()
        lname=request.POST.get("Username")
        lpassword=request.POST.get("Password")
        query="select * from login where lid='".rid."'
        lcursor.execute(query)
        lcon.commit()


    except Error as e:
        print(e)


    finally:
        lcursor.close()
        lcon.close()
        '''
def contentpage(request):
     return render(request, 'contentpage/index.html')
def showpage(request):
    return render(request, 'showpage/../templates/showdata.html')
def resume(request):
    try:
        ccon=mysql.connector.connect(host='localhost',database='project',user='root',password='root')
        ccursor=ccon.cursor()
        cf_name=request.POST.get("firstname")
        cl_name=request.POST.get("lastname")
        cemail=request.POST.get("email")
        caddress=request.POST.get("address")
        cphoneno=request.POST.get("phoneno")
        ceducation=request.POST.get("education")
        cworkexperience=request.POST.get("workexperience")
        query="insert into contentpage(firstname,lastname,email,address,phoneno,education,workexperience)values('%s', '%s', '%s', '%s','%s', '%s', '%s')" %(cf_name,cl_name,cemail,caddress,cphoneno,ceducation,cworkexperience)
        ccursor.execute(query)
        ccon.commit()
        print(cemail)
        qry = "select * from contentpage where email='%s'" %(cemail)
        ccursor.execute(qry)
        v = ccursor.fetchall()
        print(v)
        x = request.POST.get('submit')
        print(x)
        if(request.POST.get('submit')=='submit'):
            msg = 'data inserted succesfully'
            return render(request,'contentpage/index.html',{'datainserted': msg})
        elif(request.POST.get('print')=='print'):
            qry = "select * from contentpage where email='%s'" %(cemail)
            ccursor.execute(qry)
            v = ccursor.fetchall()
            return render(request, 'showpage/showdata.html', {'data': v})
        elif(request.POST.get('exit')=='exit'):
            return render(request, 'main/index.html')

    except Error as e:
        print(e)


    finally:
        ccursor.close()
        ccon.close()
