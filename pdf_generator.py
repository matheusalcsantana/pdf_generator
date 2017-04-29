from reportlab.pdfgen import canvas
from reportlab.lib.units import inch, cm
def hello(c):
    c.drawString(240, 780, "Recibo - Concretize JR")
    c.drawString(240, 400, "Recibo - Concretize JR")
    c.line(0, 800, 595.27, 800)
    c.line(0, 420, 595.27, 420)
    c.line(0, 40, 595.27, 40)
    c.drawImage('concjr.png', 40, 760, width=120, height=30, mask=None)
    c.drawImage('concjr.png', 40, 380, width=120, height=30, mask=None)
c = canvas.Canvas("hello.pdf")
hello(c)
c.showPage()
c.save()