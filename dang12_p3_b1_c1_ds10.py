import sys
from PyQt5.QtWidgets import QApplication, QColorDialog, QMainWindow, QSplitter, QTreeWidget, QSpacerItem, QSizePolicy, QTreeWidgetItem, QCheckBox, QFileDialog, QVBoxLayout, QTextEdit, QPushButton, QWidget, QLabel, QLineEdit, QDialog, QAction, QMessageBox, QScrollBar, QHeaderView, QMenu, QGridLayout
from sympy import *
from sympy.abc import x
import sympy as sp
from sympy import symbols,sqrt,evaluate,Subs,latex, Rational, expand, simplify, integrate
import random
import math
from sympy import Rational
from fractions import Fraction as frac
from random import randint
from PyQt5.QtGui import QTextCursor
from PyQt5.QtGui import QFont
import hashlib
import uuid
import os
from sympy import symbols, Eq, solve
import numpy as np
from PyQt5.QtGui import QIcon
from math import factorial
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextDocument
from subprocess import run, CalledProcessError
import shutil
from PyQt5.QtWidgets import QProgressBar
from docx import Document
from PyQt5 import QtGui
import re
import pandas as pd
from PyQt5.QtGui import QPixmap
import subprocess
import platform
import json
from decimal import Decimal, ROUND_HALF_UP
from PyQt5.QtWidgets import QComboBox, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSpinBox, QTreeWidget, QTreeWidgetItem, QCheckBox, QTextEdit, QPushButton, QHBoxLayout
from random import randint, choice, shuffle
from sympy import latex
from fractions import Fraction
from collections import Counter
from random import sample
import shutil
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
import qrcode
import json
import glob
import os
import platform
import subprocess
import hashlib
import base64
from datetime import datetime, timedelta
from PyQt5.QtWidgets import (QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox)
from sympy import symbols, solve, Lt
#from PyQt5.QtWebEngineWidgets import QWebEngineView
#from PyQt5.QtCore import QUrl
#from sympy import latex
import re
import pyperclip
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

import google.generativeai as genai
from sympy.abc import x, y, z, t
import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QMessageBox
)
from pdf2image import convert_from_path
from math import degrees
import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font
from openpyxl.utils import get_column_letter
from sympy import simplify, collect
from itertools import combinations
import itertools
from PyQt5.QtCore import QSettings
import sys
import os
import platform
import subprocess
import hashlib
import time
from datetime import datetime, timedelta
# Bổ sung các widget và core cho Splash Screen
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar  # <-- BỔ SUNG 2 CÁI NÀY
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal  # <-- BỔ SUNG QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea  # <-- Thêm mục này vào đây
)
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QPropertyAnimation, pyqtProperty
from functools import wraps
import re
import uuid
import json, base64
from datetime import datetime
from nacl.signing import VerifyKey
from nacl.encoding import HexEncoder
from nacl.exceptions import BadSignatureError
### CÔNG CỤ
import sys
import numpy as np
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QDialog, 
    QVBoxLayout, QHBoxLayout, QTabWidget, QWidget, 
    QLabel, QSlider, QDoubleSpinBox, QGroupBox
)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D  # Cần cho 3D


def bt_dang12_p3_b1_c1_ds10(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        # Sinh các giá trị số ngẫu nhiên cho các phát biểu toán học
        d1 = random.randint(3, 9)
        d2 = random.randint(11, 19)
        d3 = d1 + d2 # khẳng định đúng câu d

        e1 = random.randint(4, 8)
        e2 = random.randint(21, 89)
        e3 = random.randint(15, 30) # khẳng định sai câu e

        g1 = random.randint(1, 5)
        g2 = random.randint(8, 15) # mệnh đề chứa biến câu g

        h_pow = random.randint(5, 10)
        h_div = random.randint(3, 11) # câu h

        k_num = random.choice([15, 17, 19, 21]) # câu k

        # Định nghĩa danh sách các câu từ ảnh gốc, phân loại xem có phải "mệnh đề toán học" không
        # Mỗi phần tử: (Chuỗi hiển thị, Có phải mệnh đề toán học không? (True/False), Chuỗi giải thích)
        pool = [
            ("Huế là một thành phố của Việt Nam", False, "là một mệnh đề thông thường về địa lý, không phải là mệnh đề toán học."),
            ("Sông Hương chảy ngang qua thành phố Huế", False, "là một mệnh đề thông thường về địa lý, không phải là mệnh đề toán học."),
            ("Hãy trả lời câu hỏi này !", False, "là một câu mệnh lệnh, không phải là mệnh đề."),
            ("%s + %s = %s" % (latex(d1), latex(d2), latex(d3)), True, "là một khẳng định số học (đúng), do đó đây là một mệnh đề toán học."),
            ("%s + %s = %s" % (latex(e1), latex(e2), latex(e3)), True, "là một khẳng định số học (sai), do đó đây là một mệnh đề toán học."),
            ("Bạn có rỗi tối nay không ?", False, "là một câu hỏi, không phải là mệnh đề."),
            ("x + %s = %s" % (latex(g1), latex(g2)), False, "là một mệnh đề chứa biến, chưa thể khẳng định tính đúng sai ngay lập tức nên không phải là mệnh đề toán học."),
            ("2^{%s} - 1 \\text{ chia hết cho } %s" % (latex(h_pow), latex(h_div)), True, "là một khẳng định về tính chất chia hết trong toán học, do đó đây là một mệnh đề toán học."),
            ("%s \\text{ là hợp số}" % latex(k_num), True, "là một khẳng định về lý thuyết số trong toán học, do đó đây là một mệnh đề toán học.")
        ]

        # Chọn ngẫu nhiên từ 7 đến 9 phát biểu để tạo sự đa dạng cho bài toán
        num_select = random.randint(7, 9)
        chosen_items = random.sample(pool, num_select)

        # Đếm số lượng câu là mệnh đề toán học
        kq_num = sum(1 for item in chosen_items if item[1] is True)
        da = '$%s$' % latex(kq_num)

        # Tạo các phương án sai xung quanh đáp án đúng (từ 0 đến num_select và không trùng với kq_num)
        s_candi = list(range(0, num_select + 1))
        if kq_num in s_candi:
            s_candi.remove(kq_num)

        s = []
        for val in random.sample(s_candi, 3):
            s.append('$%s$' % latex(val))

        das1 = s[0]
        das2 = s[1]
        das3 = s[2]

        # Các ký tự đầu dòng (a, b, c, d...)
        labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'k', 'l', 'm']

        # Tạo chuỗi danh sách các phát biểu trong câu hỏi
        list_str_statements = ""
        for i, item in enumerate(chosen_items):
            stmt_text = item[0] if "x" not in item[0] and "2^{" not in item[0] and "+" not in item[0] else "$%s$" % item[0]
            list_str_statements += "%s) %s. \\\\" % (labels[i], stmt_text)
        list_str_statements = list_str_statements.rstrip(" \\\\")

        # Câu hỏi
        noidungcauhoi = ('''Trong các câu sau, có bao nhiêu câu là mệnh đề toán học? \\\\ %s'''
                            % (list_str_statements))

        # Các đáp án
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2) 
        da_s3 = str(das3) 

        # Đưa các đáp án vào danh sách chọn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Tạo chuỗi lời giải chi tiết từng bước
        loigiai_chi_tiet = ""
        for i, item in enumerate(chosen_items):
            stmt_text = item[0] if "x" not in item[0] and "2^{" not in item[0] and "+" not in item[0] else "$%s$" % item[0]
            type_str = "là một mệnh đề toán học" if item[1] else "không phải là một mệnh đề toán học"
            loigiai_chi_tiet += "Câu %s) %s %s. %s \\\\" % (labels[i], stmt_text, type_str, item[2])
        loigiai_chi_tiet = loigiai_chi_tiet.rstrip(" \\\\")

        loigiai = ('''Mệnh đề toán học là những mệnh đề khẳng định một sự kiện toán học rõ ràng và có tính đúng hoặc sai. Các câu cảm thán, câu hỏi, mệnh đề chứa biến hoặc mệnh đề thuộc các lĩnh vực khác (như địa lý, đời sống) không được coi là mệnh đề toán học. \\\\
    Xét từng câu ta có: \\\\ %s \\\\ Kết luận: Có tất cả $%s$ câu là mệnh đề toán học.'''
                    % (loigiai_chi_tiet, latex(kq_num)))
        dapan='\\shortans[0]{$%s$}\n'%(latex(kq_num))
    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + dapan+
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
    return content

