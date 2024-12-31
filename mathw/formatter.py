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

    @staticmethod
    def add_separators(content, gap, page_capacity,
                       separator='-', sep_num=40, truncate=True):
        """
        TODO:REMOVE
        给内容列表按 “页” 添加分割符。每页的第一行和最后一行不添加分隔符。
        注意：添加分隔符后，每一页的行数等于content中元素的数量加上分隔符的数量。
        :param content: list of strings, e.g. [item1, item2, item3, ...]，每个item是一个字符串
        :param gap: int, 代表分隔符之间间隔的元素数量。换句话说，在每一页中，每隔gap个元素，插入一个分隔符。
        :param page_capacity: int, 每页元素数量。
        :param separator: str, 组成分隔符的单个字符
        :param sep_num: 每个分隔符中包含的字符数量。因此，插入的分隔符 sep_string = separator * sep_num。
        :param truncate: bool, True - 截断，不会改变 content 列表的长度；False - 不截断，直接返回结果，但是会增加 content 列表的长度。
        :return: list of strings
        """
        sep_string = separator * sep_num
        new_content = []
        num_elements = len(content)

        # 计算一页item的个数(page_item_num)
        # 页的元素数量(page_capacity) = 分隔符数量 (item_num / k - 1) + 元素数量 (item_num)
        page_item_num = int((page_capacity + 1) * gap / (gap + 1))

        for page_start in range(0, num_elements, page_item_num):
            page_end = min(page_start + page_item_num, num_elements)
            page_content = content[page_start:page_end]

            # Add elements in the page and separators
            page_size = len(page_content)
            for i in range(0, page_size):
                if page_size > i > 0 == i % gap:
                    new_content.append(sep_string)
                new_content.append(page_content[i])

        if truncate:
            return new_content[:num_elements]
        else:
            return new_content
