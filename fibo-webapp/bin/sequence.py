#!/usr/bin/python

import web
import fibo

urls = (
  '/numbers', 'Index'
)

app = web.application(urls, globals())

render = web.template.render('templates/')

class Index(object):
    def GET(self):
        return render.input_form()
    
    def POST(self):
        form = web.input(numbers = None)

        if form.numbers:
            num = int(form.numbers)
            sequence = fibo.fib(num)
            return render.index(sequence = sequence)
        else:
            return "Error. A numeric value is required"

if __name__ == "__main__":
    app.run()
