from flask import Flask,render_template,url_for,request,redirect
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///test.db'
db=SQLAlchemy(app)

@app.route('/',methods=['GET','POST'])
def homepagefn():
        if(request.method=='POST'):
            mailid=request.form.get('emailid')
            new_task=interested(email=mailid)
            try:
                db.session.add(new_task)
                db.session.commit()
                return redirect('/listofinterested')
            except:
                return "There is db issue"
        else:
                return render_template('website.html')
        return render_template('website.html')

class interested(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String(80),nullable=False)

    def __repr__():
        return '<User %r>'%self.id
@app.route('/listofinterested')
def interestedpeople():
    inter=interested.query.all()
    return render_template('interested.html',inter)

if __name__ == '__main__':
    app.run(debug=True)
