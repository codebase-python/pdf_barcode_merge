"""
Reportlab sandbox.
"""
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter, landscape

from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image,Table
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

from reportlab.lib.units import inch,cm,mm
from reportlab.lib.utils import ImageReader
from reportlab.lib import pagesizes,colors
from reportlab.pdfgen.canvas import Canvas
from reportlab.graphics.barcode import createBarcodeDrawing
from reportlab.graphics.shapes import Drawing
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.graphics import renderPDF
from pdf_to_image import pdf_to_image
# from wand.image import Image as WandImage


class BarcodeRender(Drawing):
    def __init__(self, data, barHeight=10, barWidth=10,*args, **kw):
        barcode = createBarcodeDrawing('Code128', value=data,  barHeight=barHeight*mm, barWidth = barWidth*mm,humanReadable=True)
        Drawing.__init__(self,barcode.width,barcode.height,*args,**kw)
        self.add(barcode, name='barcode')

    def asBinary(self,format="gif"):
        return self.asString(format=format)



def sampleTablePDF():
    logo = "cimpress_sample.png"
    cup = "coffee-cup.jpg"
    imCup = Image(cup)

    im = Image(logo)

    im.hAlign = "CENTER"
    doc = SimpleDocTemplate("cimpress_sample_print_order.pdf",pagesize=(im.drawWidth+400,im.drawHeight+400))
    content = []
    barcodeObject1 = BarcodeRender("Hello", barHeight=20, barWidth=1)
    barcodeObject2 = BarcodeRender("Hello", barHeight=20, barWidth=1)
    imCup.drawHeight = barcodeObject1.height
    imCup.drawWidth = barcodeObject1.height
    tTableStyle = [
                   # ('BACKGROUND', (-1, 0), (-1, 0), colors.red),
                   # ('BACKGROUND', (0, 0), (0, 0), colors.yellow),
                    ('ALIGN', (0, 0), (0, 0), "RIGHT"),

                    ('ALIGN', (-1, 0), (-1, 0), "LEFT"),
                    ('ALIGN', (1, 0), (1, 0), "CENTER"),
                    ('VALIGN', (0, 0), (0, 0), "MIDDLE"),
                    ('VALIGN', (1, 0), (1, 0), "MIDDLE"),
                    ('VALIGN', (-1, 0), (-1, 0), "MIDDLE"),
                    # ('BACKGROUND', (0, 0), (0, 0), colors.orange),
                    # ('BACKGROUND', (-1, 0), (-1, 0), colors.red),
                    # ('BACKGROUND', (1, 0), (1, 0), colors.yellow),

                   # ('SPAN', (0, -1), (-1, -1)),
                   #  ('BACKGROUND', (0, -1), (-1, -1), colors.black),
                   #  ('ALIGN', (0, -1), (-1, -1), "CENTER")
                   ]
    styles = getSampleStyleSheet()
    styleHeading = ParagraphStyle('title', fontSize=20, leading=24,alignment=TA_LEFT)
    productDelivery = ParagraphStyle('title', fontSize=12, leading=24, alignment=TA_LEFT,textColor=colors.green)


    paras = []
    paras.append(Paragraph("SP: 01/27 Q: 1 <br/> SKU: 343434 <br/> ",styleHeading))
    paras.append(Paragraph("FAYA dwfdf dsfdsf sfdsf dsf sd fdsfds sdfdsfds sdfdsf f", productDelivery))
    tableData = [[paras,imCup,barcodeObject2]]
    spacer = Spacer(0,2*cm)
    table = Table(data=tableData,colWidths=[300,imCup.drawWidth,barcodeObject2.width])
    table.setStyle(tblstyle=tTableStyle)
    content.append(table)
    content.append(spacer)
    content.append(im)
    doc.build(content)


pdf_to_image()
sampleTablePDF()