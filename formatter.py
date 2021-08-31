from reportlab.platypus import BaseDocTemplate, Paragraph, Frame, PageTemplate
from reportlab.lib.styles import ParagraphStyle
from functools import partial


class Formatter(object):

    _config = {
        'pageCapacity': 10,  # 每页的题目数
        'paperHeight': 297,  # 纸高 mm
        'paperWidth': 210,  # 纸宽 mm
        'topMargin': 25.4,
        'bottomMargin': 12.7,
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

        self._inch_to_mm = 25.4  # 英寸 -> 毫米 换算
        self._pt_to_mm = self._inch_to_mm / 72  # 字号一磅 -> 毫米 换算
        self._content = []

    def _calculate_font_size(self):
        # 两倍行距
        h = self.paperHeight - self.topMargin - self.bottomMargin
        s_pt = h / (2 * self.pageCapacity + 1)
        return s_pt / self._pt_to_mm

    def _format_content(self):
        s = self._calculate_font_size()
        style = ParagraphStyle(name='Normal',
                               fontSize=s,
                               leading=2*s)
        self._content = [Paragraph(it, style) for it in self._items]

    @staticmethod
    def header(canvas, doc, content):
        canvas.saveState()
        w, h = content.wrap(doc.width, doc.topMargin)
        content.drawOn(canvas, doc.leftMargin + doc.width - w, doc.height + doc.topMargin - h)
        canvas.restoreState()

    def save(self):
        """ 把结果保存成 PDF 文件
        """
        doc = BaseDocTemplate(
            self.outputName,
            topMargin=self.topMargin/self._pt_to_mm,
            bottomMargin=self.bottomMargin/self._pt_to_mm
        )
        # add header
        frame = Frame(doc.leftMargin,
                      doc.bottomMargin,
                      doc.width,
                      doc.height - 20,
                      id='normal')
        template = PageTemplate(frames=frame,
                                onPage=partial(self.header,
                                               content=Paragraph(self.headerInfo))
                                )
        doc.addPageTemplates([template])
        # add header done
        # add content
        self._format_content()
        doc.build(self._content)
