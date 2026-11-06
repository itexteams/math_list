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


def bt_dang11_p3_b1_c1_ds10(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        # Sinh ngẫu nhiên các số cho các câu toán học để tạo sự đa dạng
        n1 = random.randint(11, 29) # Số tự nhiên trong câu 1 (ví dụ gốc: 19)
        n2 = random.randint(3, 7)   # Số chia trong câu 1 (ví dụ gốc: 5)
        year_prime = random.choice([2023, 2025, 2027, 2029]) # Năm trong câu 2 (ví dụ gốc: 2027)
        n3 = random.randint(2, 6)   # Hệ số của x trong câu 3 (ví dụ gốc: 5)
        n4 = random.randint(1, 5)   # Hệ số tự do câu 3 (ví dụ gốc: 3)
        n5 = random.randint(2, 5)   # Số hạng đầu câu 4 (ví dụ gốc: 4)
        n6 = random.randint(5, 7)   # Vế phải câu 4 (ví dụ gốc: 6)

        # Định nghĩa danh sách 8 phát biểu đã được SỬA LỖI FONT CHỮ thành tiếng Việt chuẩn
        # Mỗi phần tử: (Chuỗi phát biểu, Có phải mệnh đề không? (True/False), Chuỗi giải thích)
        pool = [
            ("Số %s chia hết cho %s" % (latex(n1), latex(n2)), True, "là một khẳng định toán học có tính đúng sai rõ ràng. Do đó, đây là một mệnh đề."),
            ("%s là số nguyên tố" % latex(year_prime), True, "là một khẳng định có tính đúng sai rõ ràng trong số học. Do đó, đây là một mệnh đề."),
            ("%sx - %s < 0" % (latex(n3), latex(n4)), False, "là một khẳng định chứa biến $x$, tính đúng sai chưa được xác định rõ ràng mà phụ thuộc vào giá trị của biến. Do đó, đây không phải là một mệnh đề."),
            ("%s + \\pi > %s" % (latex(n5), latex(n6)), True, "là một bất đẳng thức số học có tính đúng sai rõ ràng. Do đó, đây là một mệnh đề."),
            ("Cầu Trường Tiền bắc qua sông Hương", True, "là một khẳng định về địa lý thực tế có tính đúng sai rõ ràng (đây là khẳng định đúng). Do đó, đây là một mệnh đề."),
            ("London là thủ đô của Pháp", True, "là một khẳng định về địa lý có tính đúng sai rõ ràng (đây là khẳng định sai). Do đó, đây là một mệnh đề."),
            ("Hình thoi có hai đường chéo vuông góc", True, "là một khẳng định hình học có tính đúng sai rõ ràng (đây là khẳng định đúng). Do đó, đây là một mệnh đề."),
            ("Hôm nay thời tiết mát!", False, "là một câu cảm thán biểu lộ cảm xúc cá nhân, không thể xác định tính đúng sai. Do đó, đây không phải là một mệnh đề.")
        ]

        # Chọn ngẫu nhiên toàn bộ hoặc một phần các phát biểu từ pool để trộn đề bài
        num_select = random.randint(7, 8)
        chosen_items = random.sample(pool, num_select)

        # Đếm số lượng phát biểu là mệnh đề
        kq_num = sum(1 for item in chosen_items if item[1] is True)
        da = '$%s$' % latex(kq_num)

        # Tạo các phương án sai (từ 0 đến num_select và không trùng với kq_num)
        s_candi = list(range(0, num_select + 1))
        if kq_num in s_candi:
            s_candi.remove(kq_num)

        s = []
        for val in random.sample(s_candi, 3):
            s.append('$%s$' % latex(val))

        das1 = s[0]
        das2 = s[1]
        das3 = s[2]

        # Tạo chuỗi danh sách hiển thị các phát biểu trong câu hỏi
        list_str_statements = ""
        for i, item in enumerate(chosen_items):
            list_str_statements += "%s. %s \\\\" % (latex(i + 1), item[0] if "x" not in item[0] and "\\pi" not in item[0] else "$%s$" % item[0])
        list_str_statements = list_str_statements.rstrip(" \\\\")

        # Câu hỏi
        noidungcauhoi = ('''Trong các phát biểu sau, có bao nhiêu phát biểu là mệnh đề? \\\\ %s'''
                            % (list_str_statements))

        # Các đáp án
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2) 
        da_s3 = str(das3) 

        # Đưa các đáp án vào danh sách và trộn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Tạo chuỗi lời giải chi tiết sửa lỗi font hoàn chỉnh
        loigiai_chi_tiet = ""
        for i, item in enumerate(chosen_items):
            stmt_display = item[0] if "x" not in item[0] and "\\pi" not in item[0] else "$%s$" % item[0]
            tr_fa = "là một mệnh đề" if item[1] else "không phải là một mệnh đề"
            loigiai_chi_tiet += "Phát biểu %s: %s %s. %s \\\\" % (latex(i + 1), stmt_display, tr_fa, item[2])
        loigiai_chi_tiet = loigiai_chi_tiet.rstrip(" \\\\")

        loigiai = ('''Mệnh đề lôgich là một khẳng định có tính đúng hoặc sai rõ ràng. Câu hỏi, câu cảm thán hoặc khẳng định có chứa biến chưa xác định giá trị thì không phải là mệnh đề. \\\\
    Xét từng phát biểu ta có: \\\\ %s \\\\ Kết luận: Có tất cả $%s$ phát biểu là mệnh đề.'''
                    % (loigiai_chi_tiet, latex(kq_num)))
        dapan='\\shortans[0]{$%s$}\n'%(latex(kq_num))
    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + dapan+
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
    return content

