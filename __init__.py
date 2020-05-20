from flask import Flask, redirect, url_for, render_template, request, session, flash, make_response
from datetime import date, datetime, timedelta
import wikipedia, random, math, holidays

app = Flask(__name__)
app.config['SECRET_KEY'] = "1-2/3/0-5Aa"
app.config['SERVER NAME'] = 'hmanyds.com'




@app.route('/home')
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/home/es')
def casa():
    return render_template('homeSpanish.html')

@app.route('/spanish', methods=["POST", "GET"])
def spanish():
    if request.method == "POST":
        date_input = request.form["date"]
        contar_fin_on = request.form.get("ContarFin")

        if date_input == "":
            return redirect(url_for("spanish"))
        else:
            if contar_fin_on:
                start = datetime.strptime(date_input, "%Y-%m-%d").date()
                end = date.today()
                Gap = (end - start).days
                final_result = str(Gap)
                session["final_result"] = final_result
                return redirect(url_for("final_result"))
            else:
                start = datetime.strptime(date_input, "%Y-%m-%d").date()
                end = date.today()
                Gap = (end - start).days
                N_semanas = Gap / 7
                fines_de_semana = (math.trunc(N_semanas)) * 2
                final_result = str((Gap) - fines_de_semana)
                session["final_result"] = final_result
                return redirect(url_for("final_result"))
    else:
        return render_template("indexSpanish.html")


@app.route("/spanish_result")
def final_result():
    if "final_result" in session:
        final_result = session["final_result"]
        integer_final = int(final_result)
        final_but_is_until = str(abs(integer_final))
        return render_template("resultSpanish.html", final_result=final_result, int_final=integer_final,
                               final_but_is_until=final_but_is_until)
    else:
        return redirect(url_for("spanish"))


@app.route('/english', methods=["POST", "GET"])
def eng():
    if request.method == "POST":
        date_input = request.values.get("dateEng")
        contar_fin_on = request.form.get("ContarFinEng")

        if date_input == "":
            return redirect(url_for("eng"))
        else:
            if contar_fin_on:
                start = datetime.strptime(date_input, "%Y-%m-%d").date()
                end = date.today()
                Gap = (end - start).days
                final_result_eng = str(Gap)
                session["final_result_eng"] = final_result_eng
                return redirect(url_for("final_result_eng"))
            else:
                start = datetime.strptime(date_input, "%Y-%m-%d").date()
                end = date.today()
                Gap = (end - start).days
                N_semanas = Gap / 7
                fines_de_semana = (math.trunc(N_semanas)) * 2
                final_result_eng = str((Gap) - fines_de_semana)
                session["final_result_eng"] = final_result_eng
                return redirect(url_for("final_result_eng"))
    else:
        return render_template("indexEnglish.html")


@app.route('/english_result')
def final_result_eng():
    if "final_result_eng" in session:
        final_result_eng = session["final_result_eng"]
        integer_final_eng = int(final_result_eng)
        final_but_is_until_eng = str(abs(integer_final_eng))
        return render_template("result.html", final_result=final_result_eng, int_final=integer_final_eng,
                               final_but_is_until=final_but_is_until_eng)
    else:
        return redirect(url_for("eng"))


@app.route('/addDays', methods=["POST", "GET"])
def addDays():
    if request.method == "POST":
        daysto = request.values.get("addForm")
        add_subs = request.form.get("AddCheck")
        if daysto == "":
            return redirect(url_for("addDays"))
        else:

            if add_subs:
                daystoAdd = int(daysto)
                date_today = date.today()
                result = date_today + timedelta(days=daystoAdd)
                add_result = result.strftime('%a, %d/%m/%Y')
                session["add_result"] = add_result
                return redirect(url_for("add_result"))
            else:
                daystoAdd = int(daysto)
                date_today = date.today()
                result = date_today - timedelta(days=daystoAdd)
                add_result = result.strftime('%a, %d/%m/%Y')
                session["add_result"] = add_result
                return redirect(url_for("add_result"))
    else:
        return render_template("AddDays.html")


@app.route('/add_result')
def add_result():
    if "add_result" in session:
        add_result = session["add_result"]
        return render_template("add_result.html", add_result=add_result)
    else:
        return redirect(url_for("addDays"))


@app.route('/convert', methods=["POST", "GET"])
def convert():
    if request.method == "POST":
        numb = request.values.get("numberT")
        session['value'] = str(numb)
        radio_value = request.form["radio"]
        if session['value'] == "":
            session['convert'] = "surprise! what would you expect? 420"
            session['timStp'] = "Ha ha so funny, I didn't input anything"
            return redirect(url_for('convert_res'))
        else:
            if radio_value == "year":
                result = int(numb)*365
                session['convert'] = str(result)
                session['timStp'] = "years"
                return redirect(url_for('convert_res'))

            elif radio_value == "month":
                result = int(numb)*30
                session['convert'] = str(result)
                session['timStp'] = "months"
                return redirect(url_for('convert_res'))

            elif radio_value == "week":
                result = int(numb)*7
                session['convert'] = str(result)
                session['timStp'] = "weeks"
                return redirect(url_for('convert_res'))

            else:
                number = int(numb)
                result = number/24
                session['convert'] = str(result)
                session['timStp'] = "hours"
                return redirect(url_for('convert_res'))
    else:
        return render_template('conversor.html')

@app.route('/convert_result')
def convert_res():
    if "convert" in session:
        convert = session['convert']
        value = session['value']
        timStp = session['timStp']
        flash(f"{value} {timStp} is about {convert} days")

    return redirect(url_for('convert'))

@app.route('/anadir+dias', methods=['POST', 'GET'])
def anadirdias():
    if request.method == "POST":
        daystoadd = request.values.get("AnForm")
        session["daystoadd"] = daystoadd
        omitN = request.form.get("cnt")
        comunidades = request.form.get("comunidades")
        dateVal = request.form.get("dateAn")
        if str(daystoadd) == "":
            return redirect(url_for("anadirdias"))
        else:
            if omitN:

                # holiday database

                days_to_skipPV = holidays.ES(prov='PV', years=2020)
                days_to_skipAND = holidays.ES(prov='AN', years=2020)
                days_to_skipARG = holidays.ES(prov='AR', years=2020)
                days_to_skipAST = holidays.ES(prov='AS', years=2020)
                days_to_skipCN = holidays.ES(prov='CB', years=2020)
                days_to_skipCM = holidays.ES(prov='CM', years=2020)
                days_to_skipCL = holidays.ES(prov='CL', years=2020)
                days_to_skipCAT = holidays.ES(prov='CT', years=2020)
                days_to_skipVA = holidays.ES(prov='CVA', years=2020)
                days_to_skipEXT = holidays.ES(prov='EX', years=2020)
                days_to_skipGA = holidays.ES(prov='GA', years=2020)
                days_to_skipIBA = holidays.ES(prov='IB', years=2020)
                days_to_skipICA = holidays.ES(prov='CN', years=2020)
                days_to_skipMAD = holidays.ES(prov='MD', years=2020)
                days_to_skipMUR = holidays.ES(prov='MC', years=2020)
                days_to_skipNAV = holidays.ES(prov='NC', years=2020)
                days_to_skipRIO = holidays.ES(prov='RI', years=2020)

                # declaración de variables

                weekendsSkip = 0
                skipped = 0
                if dateVal == "":
                    start = date.today()
                else:
                    start = datetime.strptime(dateVal, "%Y-%m-%d").date()
                xres = start

                # if para comunidades

                #andalusia

                if comunidades == 'and':
                    # checkeo de fines
                    for days in range(int(daystoadd) + 1):

                        xres += timedelta(days=1)
                        weekday = xres.weekday()
                        if weekday >= 5:
                            weekendsSkip += 1
                    finalWeek = weekendsSkip

                    # checkeo de fiestas
                    for days_add in range(int(daystoadd) + 1):
                        if start + timedelta(days=days_add) in days_to_skipAND:
                            skipped += 1


                    resultAn = start + timedelta(days=int(daystoadd)) + timedelta(days=skipped) + timedelta(days=finalWeek)
                    if resultAn.weekday() >= 5:
                        resultAn += timedelta(days=2)

                    weekDayResult = resultAn.strftime('%a, %d/%m/%Y')
                    session["an_result"] = weekDayResult
                    return redirect(url_for('an_result'))

                if comunidades == 'ar':
                    # checkeo de fines
                    for days in range(int(daystoadd) + 1):

                        xres += timedelta(days=1)
                        weekday = xres.weekday()
                        if weekday >= 5:
                            weekendsSkip += 1
                    finalWeek = weekendsSkip

                    # checkeo de fiestas
                    for days_add in range(int(daystoadd) + 1):
                        if start + timedelta(days=days_add) in days_to_skipARG:
                            skipped += 1


                    resultAn = start + timedelta(days=int(daystoadd)) + timedelta(days=skipped) + timedelta(days=finalWeek)
                    if resultAn.weekday() >= 5:
                        resultAn += timedelta(days=2)

                    weekDayResult = resultAn.strftime('%a, %d/%m/%Y')
                    session["an_result"] = weekDayResult
                    return redirect(url_for('an_result'))

                if comunidades == 'as':
                    # checkeo de fines
                    for days in range(int(daystoadd) + 1):

                        xres += timedelta(days=1)
                        weekday = xres.weekday()
                        if weekday >= 5:
                            weekendsSkip += 1
                    finalWeek = weekendsSkip

                    # checkeo de fiestas
                    for days_add in range(int(daystoadd) + 1):
                        if start + timedelta(days=days_add) in days_to_skipAST:
                            skipped += 1


                    resultAn = start + timedelta(days=int(daystoadd)) + timedelta(days=skipped) + timedelta(days=finalWeek)
                    if resultAn.weekday() >= 5:
                        resultAn += timedelta(days=2)

                    weekDayResult = resultAn.strftime('%a, %d/%m/%Y')
                    session["an_result"] = weekDayResult
                    return redirect(url_for('an_result'))

                if comunidades == 'can':
                    # checkeo de fines
                    for days in range(int(daystoadd) + 1):

                        xres += timedelta(days=1)
                        weekday = xres.weekday()
                        if weekday >= 5:
                            weekendsSkip += 1
                    finalWeek = weekendsSkip

                    # checkeo de fiestas
                    for days_add in range(int(daystoadd) + 1):
                        if start + timedelta(days=days_add) in days_to_skipCN:
                            skipped += 1


                    resultAn = start + timedelta(days=int(daystoadd)) + timedelta(days=skipped) + timedelta(days=finalWeek)
                    if resultAn.weekday() >= 5:
                        resultAn += timedelta(days=2)

                    weekDayResult = resultAn.strftime('%a, %d/%m/%Y')
                    session["an_result"] = weekDayResult
                    return redirect(url_for('an_result'))

                if comunidades == 'cm':
                    # checkeo de fines
                    for days in range(int(daystoadd) + 1):

                        xres += timedelta(days=1)
                        weekday = xres.weekday()
                        if weekday >= 5:
                            weekendsSkip += 1
                    finalWeek = weekendsSkip

                    # checkeo de fiestas
                    for days_add in range(int(daystoadd) + 1):
                        if start + timedelta(days=days_add) in days_to_skipCM:
                            skipped += 1


                    resultAn = start + timedelta(days=int(daystoadd)) + timedelta(days=skipped) + timedelta(days=finalWeek)
                    if resultAn.weekday() >= 5:
                        resultAn += timedelta(days=2)

                    weekDayResult = resultAn.strftime('%a, %d/%m/%Y')
                    session["an_result"] = weekDayResult
                    return redirect(url_for('an_result'))

                if comunidades == 'cl':
                    # checkeo de fines
                    for days in range(int(daystoadd) + 1):

                        xres += timedelta(days=1)
                        weekday = xres.weekday()
                        if weekday >= 5:
                            weekendsSkip += 1
                    finalWeek = weekendsSkip

                    # checkeo de fiestas
                    for days_add in range(int(daystoadd) + 1):
                        if start + timedelta(days=days_add) in days_to_skipCL:
                            skipped += 1


                    resultAn = start + timedelta(days=int(daystoadd)) + timedelta(days=skipped) + timedelta(days=finalWeek)
                    if resultAn.weekday() >= 5:
                        resultAn += timedelta(days=2)

                    weekDayResult = resultAn.strftime('%a, %d/%m/%Y')
                    session["an_result"] = weekDayResult
                    return redirect(url_for('an_result'))

                if comunidades == 'cat':
                    # checkeo de fines
                    for days in range(int(daystoadd) + 1):

                        xres += timedelta(days=1)
                        weekday = xres.weekday()
                        if weekday >= 5:
                            weekendsSkip += 1
                    finalWeek = weekendsSkip

                    # checkeo de fiestas
                    for days_add in range(int(daystoadd) + 1):
                        if start + timedelta(days=days_add) in days_to_skipCAT:
                            skipped += 1


                    resultAn = start + timedelta(days=int(daystoadd)) + timedelta(days=skipped) + timedelta(days=finalWeek)
                    if resultAn.weekday() >= 5:
                        resultAn += timedelta(days=2)

                    weekDayResult = resultAn.strftime('%a, %d/%m/%Y')
                    session["an_result"] = weekDayResult
                    return redirect(url_for('an_result'))

                if comunidades == 'va':
                    # checkeo de fines
                    for days in range(int(daystoadd) + 1):

                        xres += timedelta(days=1)
                        weekday = xres.weekday()
                        if weekday >= 5:
                            weekendsSkip += 1
                    finalWeek = weekendsSkip

                    # checkeo de fiestas
                    for days_add in range(int(daystoadd) + 1):
                        if start + timedelta(days=days_add) in days_to_skipVA:
                            skipped += 1


                    resultAn = start + timedelta(days=int(daystoadd)) + timedelta(days=skipped) + timedelta(days=finalWeek)
                    if resultAn.weekday() >= 5:
                        resultAn += timedelta(days=2)

                    weekDayResult = resultAn.strftime('%a, %d/%m/%Y')
                    session["an_result"] = weekDayResult
                    return redirect(url_for('an_result'))

                if comunidades == 'ex':
                    # checkeo de fines
                    for days in range(int(daystoadd) + 1):

                        xres += timedelta(days=1)
                        weekday = xres.weekday()
                        if weekday >= 5:
                            weekendsSkip += 1
                    finalWeek = weekendsSkip

                    # checkeo de fiestas
                    for days_add in range(int(daystoadd) + 1):
                        if start + timedelta(days=days_add) in days_to_skipEXT:
                            skipped += 1


                    resultAn = start + timedelta(days=int(daystoadd)) + timedelta(days=skipped) + timedelta(days=finalWeek)
                    if resultAn.weekday() >= 5:
                        resultAn += timedelta(days=2)

                    weekDayResult = resultAn.strftime('%a, %d/%m/%Y')
                    session["an_result"] = weekDayResult
                    return redirect(url_for('an_result'))

                if comunidades == 'ga':
                    # checkeo de fines
                    for days in range(int(daystoadd) + 1):

                        xres += timedelta(days=1)
                        weekday = xres.weekday()
                        if weekday >= 5:
                            weekendsSkip += 1
                    finalWeek = weekendsSkip

                    # checkeo de fiestas
                    for days_add in range(int(daystoadd) + 1):
                        if start + timedelta(days=days_add) in days_to_skipGA:
                            skipped += 1


                    resultAn = start + timedelta(days=int(daystoadd)) + timedelta(days=skipped) + timedelta(days=finalWeek)
                    if resultAn.weekday() >= 5:
                        resultAn += timedelta(days=2)

                    weekDayResult = resultAn.strftime('%a, %d/%m/%Y')
                    session["an_result"] = weekDayResult
                    return redirect(url_for('an_result'))

                if comunidades == 'ba':
                    # checkeo de fines
                    for days in range(int(daystoadd) + 1):

                        xres += timedelta(days=1)
                        weekday = xres.weekday()
                        if weekday >= 5:
                            weekendsSkip += 1
                    finalWeek = weekendsSkip

                    # checkeo de fiestas
                    for days_add in range(int(daystoadd) + 1):
                        if start + timedelta(days=days_add) in days_to_skipIBA:
                            skipped += 1


                    resultAn = start + timedelta(days=int(daystoadd)) + timedelta(days=skipped) + timedelta(days=finalWeek)
                    if resultAn.weekday() >= 5:
                        resultAn += timedelta(days=2)

                    weekDayResult = resultAn.strftime('%a, %d/%m/%Y')
                    session["an_result"] = weekDayResult
                    return redirect(url_for('an_result'))

                if comunidades == 'canarias':
                    # checkeo de fines
                    for days in range(int(daystoadd) + 1):

                        xres += timedelta(days=1)
                        weekday = xres.weekday()
                        if weekday >= 5:
                            weekendsSkip += 1
                    finalWeek = weekendsSkip

                    # checkeo de fiestas
                    for days_add in range(int(daystoadd) + 1):
                        if start + timedelta(days=days_add) in days_to_skipICA:
                            skipped += 1


                    resultAn = start + timedelta(days=int(daystoadd)) + timedelta(days=skipped) + timedelta(days=finalWeek)
                    if resultAn.weekday() >= 5:
                        resultAn += timedelta(days=2)

                    weekDayResult = resultAn.strftime('%a, %d/%m/%Y')
                    session["an_result"] = weekDayResult
                    return redirect(url_for('an_result'))

                if comunidades == 'rio':
                    # checkeo de fines
                    for days in range(int(daystoadd) + 1):

                        xres += timedelta(days=1)
                        weekday = xres.weekday()
                        if weekday >= 5:
                            weekendsSkip += 1
                    finalWeek = weekendsSkip

                    # checkeo de fiestas
                    for days_add in range(int(daystoadd) + 1):
                        if start + timedelta(days=days_add) in days_to_skipRIO:
                            skipped += 1


                    resultAn = start + timedelta(days=int(daystoadd)) + timedelta(days=skipped) + timedelta(days=finalWeek)
                    if resultAn.weekday() >= 5:
                        resultAn += timedelta(days=2)

                    weekDayResult = resultAn.strftime('%a, %d/%m/%Y')
                    session["an_result"] = weekDayResult
                    return redirect(url_for('an_result'))

                if comunidades == 'mad':
                    # checkeo de fines
                    for days in range(int(daystoadd) + 1):

                        xres += timedelta(days=1)
                        weekday = xres.weekday()
                        if weekday >= 5:
                            weekendsSkip += 1
                    finalWeek = weekendsSkip

                    # checkeo de fiestas
                    for days_add in range(int(daystoadd) + 1):
                        if start + timedelta(days=days_add) in days_to_skipMAD:
                            skipped += 1


                    resultAn = start + timedelta(days=int(daystoadd)) + timedelta(days=skipped) + timedelta(days=finalWeek)
                    if resultAn.weekday() >= 5:
                        resultAn += timedelta(days=2)

                    weekDayResult = resultAn.strftime('%a, %d/%m/%Y')
                    session["an_result"] = weekDayResult
                    return redirect(url_for('an_result'))

                if comunidades == 'mur':
                    # checkeo de fines
                    for days in range(int(daystoadd) + 1):

                        xres += timedelta(days=1)
                        weekday = xres.weekday()
                        if weekday >= 5:
                            weekendsSkip += 1
                    finalWeek = weekendsSkip

                    # checkeo de fiestas
                    for days_add in range(int(daystoadd) + 1):
                        if start + timedelta(days=days_add) in days_to_skipMUR:
                            skipped += 1


                    resultAn = start + timedelta(days=int(daystoadd)) + timedelta(days=skipped) + timedelta(days=finalWeek)
                    if resultAn.weekday() >= 5:
                        resultAn += timedelta(days=2)

                    weekDayResult = resultAn.strftime('%a, %d/%m/%Y')
                    session["an_result"] = weekDayResult
                    return redirect(url_for('an_result'))

                if comunidades == 'nav':
                    # checkeo de fines
                    for days in range(int(daystoadd) + 1):

                        xres += timedelta(days=1)
                        weekday = xres.weekday()
                        if weekday >= 5:
                            weekendsSkip += 1
                    finalWeek = weekendsSkip

                    # checkeo de fiestas
                    for days_add in range(int(daystoadd) + 1):
                        if start + timedelta(days=days_add) in days_to_skipNAV:
                            skipped += 1


                    resultAn = start + timedelta(days=int(daystoadd)) + timedelta(days=skipped) + timedelta(days=finalWeek)
                    if resultAn.weekday() >= 5:
                        resultAn += timedelta(days=2)

                    weekDayResult = resultAn.strftime('%a, %d/%m/%Y')
                    session["an_result"] = weekDayResult
                    return redirect(url_for('an_result'))

                if comunidades == 'euskadi':
                    # checkeo de fines
                    for days in range(int(daystoadd) + 1):

                        xres += timedelta(days=1)
                        weekday = xres.weekday()
                        if weekday >= 5:
                            weekendsSkip += 1
                    finalWeek = weekendsSkip

                    # checkeo de fiestas
                    for days_add in range(int(daystoadd) + 1):
                        if start + timedelta(days=days_add) in days_to_skipPV:
                            skipped += 1


                    resultAn = start + timedelta(days=int(daystoadd)) + timedelta(days=skipped) + timedelta(days=finalWeek)
                    if resultAn.weekday() >= 5:
                        resultAn += timedelta(days=2)

                    weekDayResult = resultAn.strftime('%a, %d/%m/%Y')
                    session["an_result"] = weekDayResult
                    return redirect(url_for('an_result'))


            else:
                daystoAdd = int(daystoadd)
                date_today = date.today()
                result = date_today + timedelta(days=daystoAdd)
                add_result = result.strftime('%a, %d/%m/%Y')
                session["an_result"] = add_result
                return redirect(url_for("an_result"))
    else:
        return render_template("anadirDias.html")

@app.route('/an_result')
def an_result():
    if "an_result" in session:
        an_result = session["an_result"]
        daystoadd = session["daystoadd"]
        return render_template("an_result.html", an_result=an_result, daystoadd=daystoadd)
    else:
        return redirect(url_for("anadirdias"))


@app.route('/daywasit', methods=['POST', 'GET'])
def daywasit():
    if request.method == 'POST':
        dateInput = request.form['dateWas']

        if dateInput == "":
            return redirect(url_for("daywasit"))
        else:
            # wikipedia
            dateRaw = datetime.strptime(dateInput, "%Y-%m-%d").date()
            date = dateRaw.strftime("%B-%d")
            wiki = wikipedia.page(date)
            longStr = wiki.section('Events')
            strArr = longStr.split("\n")
            numStrArr = len(strArr)
            randomInt = random.randint(0, numStrArr)
            finalWikiArt = strArr[randomInt]
            session['wikiArt'] = finalWikiArt
            session['link'] = wiki.url

            #getting day of the week
            session['dateWe'] = dateRaw.strftime("%A")
            session['dateRes'] = dateRaw.strftime("%B %d, %Y")

            return redirect(url_for("resultDay"))
    else:
        return render_template('dayswasit.html')

@app.route('/resultDay')
def resultDay():
    if "dateWe" in session:
        finalWikiArt = session['wikiArt']
        wikiUrl = session['link']
        dateWe = session['dateWe']
        dateRes = session['dateRes']

        return render_template('dayswasitRes.html', finalWikiArt=finalWikiArt, wikiUrl=wikiUrl,
                               dateWe=dateWe, dateRes=dateRes)

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contactUs.html')


@app.route('/help')
def help():
    return render_template('help.html')


@app.route('/legal')
def legal():
    return render_template('legal.html')

@app.route('/legal_in_spanish')
def legalSpanish():
    return render_template('legalSpanish.html')


@app.route('/sitemap')
def sitemap_html():
    return render_template('sitemap.html')

@app.route('/FAQ')
def FAQ():
    return render_template('FAQ.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route('/sitemap.xml', methods=['GET'])
def sitemap():
    try:
        """Generate sitemap.xml. Makes a list of urls and date modified."""
        pages = []
        ten_days_ago = (datetime.now() - timedelta(days=7)).date().isoformat()
        # static pages
        for rule in app.url_map.iter_rules():
            if "GET" in rule.methods and len(rule.arguments) == 0:
                pages.append(
                    ["http://hmanyds.com" + str(rule.rule), ten_days_ago]
                )

        sitemap_xml = render_template('sitemap.xml', pages=pages)
        response = make_response(sitemap_xml)
        response.headers["Content-Type"] = "application/xml"

        return response
    except Exception as e:
        return (str(e))

@app.route('/robots.txt')
def robots():
    return render_template('robots.txt')

@app.route('/sobreNosotros')
def sobreNosotros():
    return render_template('aboutEs.html')

@app.route('/blog/history+of+time')
def blogpost1():
    return render_template('blogpost 1.html')

@app.route('/anadir+dias/explicacion')
def anDExplicación():
    return render_template('festividades.html')


@app.route('/ads.txt')
def adstxt():
    return render_template('ads.txt')

if __name__ == '__main__':
    app.run(debug=True)
