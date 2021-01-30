from django.shortcuts import render, redirect
import pymysql


def classes(request):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='1qa2ws3ed', db='exercise', charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute('select cid, title from class')
    class_list = cursor.fetchall()
    cursor.close()
    conn.close()

    return render(request, 'classes.html', {'class_list': class_list})


def add_class(request):
    if request.method == 'GET':
        return render(request, 'add_class.html')
    else:
        title = request.POST.get('title')
        if len(title.strip()) == 0:
            print('this is post')
            return render(request, 'add_class.html', {'msg': '提交的内容不能为空'})
        else:
            conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='1qa2ws3ed', db='exercise', charset='utf8')
            cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
            cursor.execute('insert into class (title) values (%s)', title)
            conn.commit()
            cursor.close()
            conn.close()
            return redirect('/classes/')


def del_class(request):
    cid = request.GET.get('cid')
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='1qa2ws3ed', db='exercise', charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute('delete from class where cid=%s', cid)
    conn.commit()
    cursor.close()
    conn.close()
    return redirect('/classes/')


def edit_class(request):
    if request.method == 'GET':
        cid = request.GET.get('cid')
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='1qa2ws3ed', db='exercise', charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute('select cid, title from class where cid=%s', cid)
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return render(request, 'edit_class.html', {'result': result})
    else:
        cid = request.GET.get('cid')
        title = request.POST.get('title')
        print(cid)
        print(title)
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='1qa2ws3ed', db='exercise', charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute('update class set title=%s where cid=%s',[title, cid,])
        conn.commit()
        cursor.close()
        conn.close()
        return redirect('/classes/')


def teachers(request):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='1qa2ws3ed', db='exercise',charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute('select tid, name from teacher')
    teacher_list = cursor.fetchall()
    return render(request, 'teachers.html', {'teacher_list': teacher_list})


def add_teahcer(request):
    if request.method == 'GET':
        return render(request, 'add_teacher.html')
    else:
        name = request.POST.get('name')
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='1qa2ws3ed', db='exercise',charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute('insert into teacher (name) values (%s)', name)
        conn.commit()
        cursor.close()
        conn.close()
        return redirect('/teachers/')


def del_teacher(request):
    tid = request.GET.get('tid')
    print(tid)
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='1qa2ws3ed', db='exercise',charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute('delete from teacher where tid=%s', tid)
    conn.commit()
    cursor.close()
    conn.close()
    return redirect('/teachers/')


def edit_teacher(request):
    if request.method == 'GET':
        tid = request.GET.get('tid')
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='1qa2ws3ed', db='exercise',charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute('select tid,name from teacher where tid=%s', tid)
        result = cursor.fetchone()
        return render(request, 'edit_teacher.html', {'result': result})
    else:
        tid = request.GET.get('tid')
        name = request.POST.get('name')
        print(tid)
        print(name)
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='1qa2ws3ed', db='exercise',charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute('update teacher set name=%s where tid=%s', [name,tid,])
        conn.commit()
        cursor.close()
        conn.close()
        return redirect('/teachers/')
