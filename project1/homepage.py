from flask import Flask,render_template,url_for,request,redirect
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///test.db'
db=SQLAlchemy(app)

@app.route('/',methods=['GET','POST'])
def homepagefn():
        if(request.method=='POST'):
            mailid=request.form.get('emailid')
            name=request.form.get('Name')
            new_task=user(email=mailid,name=name)
            try:
                db.session.add(new_task)
                db.session.commit()
                return redirect('/')
            except:
                return "There is db issue"
        else:
                return render_template('website.html')
        return render_template('website.html')

class interested(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String(80),unique=True)
    name=db.Column(db.String(32),nullable=False)
    def __repr__(self):
        return '<User %r>'%self.id
class user(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String(80),unique=True)
    name=db.Column(db.String(32),nullable=False)
    def __repr__(self):
        return '<User %r>'%self.id
@app.route('/listofusers')
def interestedpeople():
    inter=user.query.all()
    return render_template('interested.html',inter=inter)

if __name__ == '__main__':
    app.run(debug=True)
