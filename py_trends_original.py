from flask import Flask, request, render_template, session, redirect, Response
from pytrends.request import TrendReq
import os

pytrend = TrendReq()
app = Flask(__name__)
app.config["CACHE_TYPE"] = "null"
kw_list = list()
PEOPLE_FOLDER = os.path.join('static')
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER

df = pytrend.trending_searches()

def pyload(posted):
    kw_list = list()
    posted = posted.split(",")
    for word in posted:
        kw_list.append(word)
    tb = pytrend.build_payload(
        kw_list,
        cat=0,
        timeframe='today 5-y',  # This can be changed to have a new timeline
        geo='',  # This needs to change if you want not to use Spain (ES)
        gprop='')
    return tb

def related(tb):
    rq = pytrend.related_queries()
    for word in rq:
        top = rq.get(word).get('top')
        return top

def rising(tb):
    rq = pytrend.related_queries()
    for word in rq:
        rising = rq.get(word).get('rising')
        return rising

def graph(tb):
    data = pytrend.interest_over_time()
    data = data.drop(labels=['isPartial'], axis='columns')
    image = data.plot(title='Comparing the words: {}'.format(tb))
    fig = image.get_figure()
    fig.savefig('static/iot.png')
    #fig.savefig('iot.png')
    #return image

@app.route('/', methods=("POST", "GET"))
def html_table():
    return render_template('simple.html',  tables=[df.to_html(classes='data')])

@app.route('/trend', methods=("POST", "GET"))
def trend():
    if request.method == 'POST':
        ld = pyload(request.form['fname'])
        rel = related(ld)
        ris = rising(ld)
        #img = graph(ld)
        return render_template('trend.html', content=rel, tables=[rel.to_html(classes='data')],
                           tables2=[ris.to_html(classes='data')])
        #content=request.form['fname'])
    else:
        return render_template('trend.html')

if __name__ == '__main__':
    app.run()