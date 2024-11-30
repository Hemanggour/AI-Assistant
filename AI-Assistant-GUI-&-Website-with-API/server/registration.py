from database import Database as db
from authentication import Authentication as auth, Update
from . import Token as token, SendEMail, emailContent

class Register:
    def login(session, request):
        if 'loggedIn' in session and session['loggedIn']:
            return ['logout.html', None]
        elif request.method == 'POST':
            email = request.form.get('email')
            password = request.form.get('password')
            data = auth.authLogin(email=email, password=password)
            if data:
                if data == 'Incorrect Password!!':
                    return ['login.html', data]
                elif data == 'User Not Found!':
                    return ['sign-up.html', data]
            else:
                session.permanent = True
                session['loggedIn'] = True
                session['userId'] = db.getUserId(email=email)[0]
                return ['redirect', '/']
        else:
            return ['login.html', None]

    def logout(session):
        try:
            session.clear()
            session.permanent = False
            return ['redirect', '/']
        except:
            return ['redirect', '/login']
    
    def signUp(session, request):
        if 'loggedIn' in session and session['loggedIn']:
            return ['logout.html', None]
        token = request.args.get('token')
        if (request.method == 'POST') and (not token):
            mail = SendEMail()
            username = request.form.get('username')
            email = request.form.get('email')
            password = request.form.get('password')
            conPassword = request.form.get('confirmPassword')
            if conPassword != password:
                return ['sign-up.html', "Password Doesn't Match!!"]
            validPass = auth.authPass(password)
            if validPass != True:
                return ['sign-up.html', validPass]
            if auth.authSignUp(username=username, email=email, password=password):
                return ['sign-up.html', "User Already Exists!"]
            if token.checkUserInNotVerified(email=email):
                db.deleteNotVerifiedUser(email=email)
            token = token.generateSignUpToken(username=username, email=email, password=password)
            subject = emailContent.subject['emailSignUpVerification']
            body = (emailContent.body['emailSignUpVerification'].format(username, token))
            print(subject, "\n",body)
            if mail.send(recEmail=email, subject=subject, body=body):
                return ['sign-up.html', "Verification Mail has Been Sent!"]
            return ['sign-up.html', "Error Sending Email, Try Again!"]
        elif token:
            if data := token.isSignUpTokenValid(token=token):
                auth.signUp(data[0], data[1], data[2])
                db.deleteNotVerifiedUser(email=data[1])
                return ['login.html', "Sign Up Successfull!"]
            return ['sign-up.html', "Invalid or expired token."]
                # return ['verify-sign-up.html', token]
        return ['sign-up.html', None]


def forgotPassword(session, request):
    if request.method == 'POST':
        email = request.form.get('email')
        oldPassword = request.form.get('oldPassword')
        newPassword = request.form.get('newPassword')
        conNewPassword = request.form.get('confirmNewPassword')
        notVerified = auth.authLogin(email=email, password=oldPassword)
        if notVerified:
            if notVerified == 'Incorrect Password!!':
                return ['forgot-password.html', notVerified]
            elif notVerified == 'User Not Found!':
                return ['sign-up.html', notVerified]
        else:
            if conNewPassword != newPassword:
                return ['forgot-password.html', "Password Doesn't Match!!"]
            if newPassword == oldPassword:
                return ['forgot-password.html', "Current Password Can't Be Your New Password!"]
            validPass = auth.authPass(newPassword)
            if validPass != True:
                return ['forgot-password.html', validPass]
            else:
                Update.password(email=email, oldPassword=oldPassword, newPassword=newPassword)
                return ['login.html', "Password Reset Successfull!"]
    return ['forgot-password.html', None]


def forgotEmail(session, request):
    token = request.args.get('token')
    if (request.method == 'POST') and (not token):
        dataBase = db.Database()
        mail = SendEMail()
        username = request.form.get('username')
        password = request.form.get('password')
        newEmail = request.form.get('newEmail')
        notVerified = auth.authLogin(email=newEmail, password=password)
        if notVerified:
            if notVerified == 'Incorrect Password!!':
                return ['forgot-email.html', "Email Already Exists!"]
            elif notVerified == 'User Not Found!':
                if auth.authUser(username=username, password=password) == "Invalid Username or Password!":
                    return ['forgot-email.html', "Invalid Username or Password!"]
                else:
                    if token.checkUserInNotVerified(email=newEmail):
                        dataBase.deleteNotVerifiedUser(email=newEmail)
                    token = token.generateSignUpToken(username=username, email=newEmail, password=password)
                    subject = emailContent.subject["newEmailVerification"]
                    body = (emailContent.body["newEmailVerification"].format(username, token))
                    print(subject, "\n", body)
                    if mail.send(newEmail, subject=subject, body=body):
                        return ['forgot-email.html', "Verification Mail has Been Sent To New Email!"]
                    return ['forgot-email.html', "Error Sending Email, Try Again!"]
        else:
            return ["forgot-email.html", 'Email Already Exists!']
        return ['forgot-email.html', None]
    elif token:
        if data := token.isSignUpTokenValid(token=token):
            dataBase = db.Database()
            if data:
                Update.email(username=data[0], newEmail=data[1], password=data[2])
                dataBase.deleteNotVerifiedUser(data[1])
                return ['login.html', 'Email Reset Successfull']
        return ["forgot-email.html", "Invalid or Expired Token!"]
    return ['forgot-email.html', None]

def forgotPasswordByEmail(session, request):
    token = request.args.get('token')
    if (request.method == 'POST') and (not token):
        mail = SendEMail()
        dataBase = db.Database()
        email = request.form.get('email')
        dbEmail = dataBase.getEmail(email=email)
        username = dataBase.getUserByEmail(email=email)
        message = "User Not Found!"
        if dbEmail:
            if dbEmail[0] == email:
                dbuserId = dataBase.getUserId(email=email)[0]
                if token.checkTokenExists(dbuserId):
                    dataBase.deleteTokenById(dbuserId)
                token = token.generateResetToken(dbuserId)
                subject = emailContent.subject['resetPassword']
                body = (emailContent.body['resetPassword'].format(username[0], token))
                print(subject, "\n",body)
                if mail.send(recEmail=email, subject=subject, body=body):
                    return ['forgot-password-byEmail.html', "Verification Mail has Been Sent!"]
                message = "Error Sending Email, Try Again!"
        return ['forgot-password-byEmail.html', message]
    elif token:
        userId = token.isTokenValid(token=token)
        print(f"UserId: {userId}")
        if userId:
            return ['reset-password.html', token, userId]
        return ['forgot-password-byEmail.html', "Invalid or expired token!"]
    return ['forgot-password-byEmail.html', None]

def resetPassword(session, request):
    dataBase = db.Database()
    userId = request.form.get('userId')
    token = request.form.get('token')
    newPassword = request.form.get('newPassword')
    confirmPassword = request.form.get('confirmNewPassword')
    if newPassword != confirmPassword:
        return ['reset-password.html', "Passwords do not match", userId, token]
    if dbPass := dataBase.getPassById(userId=userId):
        if newPassword == dbPass[0]:
            return ['reset-password.html', "Current Password Can't be your New Password!", userId, token]
    if tUserId := token.isTokenValid(token=token):
        if int(tUserId) == int(userId):
            validPass = auth.authPass(newPassword)
            if validPass != True:
                return ['reset-password.html', validPass, userId, token]
            # hashedPassword = a.hashPassword(newPassword)
            Update.passById(userId=userId, newPassword=newPassword)
            Update.deleteTokenById(userId=userId)
        return ['login.html', "Password has been successfully reset!"]
    else:
        return ['forgot-password-byEmail.html', "Invalid or expired token!"]