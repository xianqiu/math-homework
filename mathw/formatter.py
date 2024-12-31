from reportlab.platypus import BaseDocTemplate, Paragraph, Frame, PageTemplate
from reportlab.lib.styles import ParagraphStyle
from functools import partial


class Formatter(object):

    _config = {
        'pageCapacity': 10,  # 每页的题目数（行数）
        'paperHeight': 841.89,  # A4纸高 pt
        'paperWidth': 595.27,  # A4纸宽 pt
        'topMargin': 72,
        'bottomMargin': 36,
        'leftMargin': 72,
        'rightMargin': 12,
        'fontName': 'Helvetica',  # Helvetica, Times-Roman, Courier
        'outputName': 'math-work.pdf',
        'headerInfo': '',
    }

    def __init__(self, items, **kwargs):
        """
        :param items: str list
        """
        self._items = items
        for k, v in self._config.items():
            if k in kwargs:
                self._config[k] = kwargs[k]
            setattr(self, k, self._config[k])

        self._content = []

    def _calculate_font_size(self):
        h = self.paperHeight - self.topMargin - self.bottomMargin - 72
        s = h / (2 * self.pageCapacity - 1)
        return s

    def _format_content(self):
        font_size = self._calculate_font_size()  # 字号
        line_space = 2 * font_size  # 行距
        style = ParagraphStyle(name='Normal',
                               fontName=self._config['fontName'],
                               fontSize=font_size,
                               leading=line_space)
        self._content = [Paragraph(it, style) for it in self._items]

    @staticmethod
    def _header(canvas, doc, content):
        canvas.saveState()
        w, h = content.wrap(doc.width, doc.topMargin)
        content.drawOn(canvas,
                       doc.leftMargin + doc.width - w,
                       doc.height + doc.topMargin - h)
        canvas.restoreState()

    def save(self):
        """ 把结果保存成 PDF 文件
        """
        doc = BaseDocTemplate(
            self.outputName,
            pagesize=(self.paperWidth, self.paperHeight),
            topMargin=self.topMargin,
            bottomMargin=self.bottomMargin,
            leftMargin=self.leftMargin,
            rightMargin=self.rightMargin
        )
        # add header
        frame = Frame(doc.leftMargin,
                      doc.bottomMargin,
                      doc.width,
                      doc.height - 20,
                      id='normal')
        template = PageTemplate(frames=frame,
                                onPage=partial(self._header,
                                               content=Paragraph(self.headerInfo))
                                )
        doc.addPageTemplates([template])
        # add header done
        # add content
        self._format_content()
        doc.build(self._content)
