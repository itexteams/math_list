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


def bt_dang8_p3_b1_c1_ds10(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        # Sinh các giá trị số ngẫu nhiên cho bài toán để tạo sự đa dạng
        num_p1 = random.randint(2, 5) # số nguyên tố cho câu 4
        n1 = random.randint(2, 6) # số thứ nhất câu 7
        n2 = random.randint(3, 6) # số thứ hai câu 7
        n3 = n1 + n2 + random.choice([-2, -1, 1, 2]) # kết quả sai cho câu 7
        num_p2 = random.choice([2, 5, 10]) # số chia hết ở câu 10

        # Danh sách các câu phát biểu và thuộc tính của chúng: (Chuỗi hiển thị, IsMệnhĐề, LờiGiảiChiTiết)
        statements_pool = [
            ("Bình phương của một số thực bất kì là số âm", True, "là một khẳng định có tính đúng sai rõ ràng (đây là khẳng định sai). Do đó, đây là một mệnh đề."),
            ("Số $\\pi$ là một số hữu tỉ hay số vô tỉ?", False, "là một câu hỏi, không thể xác định được tính đúng sai. Do đó, đây không phải là một mệnh đề."),
            ("$2x + 1$ là số lẻ", False, "là một khẳng định chứa biến $x$, tính đúng sai chưa được xác định rõ ràng mà phụ thuộc vào giá trị của biến. Do đó, đây là mệnh đề chứa biến chứ không phải là mệnh đề."),
            ("$%s$ là số nguyên tố" % latex(num_p1), True, "là một khẳng định có tính đúng sai rõ ràng. Do đó, đây là một mệnh đề."),
            ("Hôm nay, cả lớp đều học bài", True, "là một khẳng định có tính đúng sai rõ ràng (tùy thuộc vào thực tế ngày hôm đó). Do đó, đây là một mệnh đề."),
            ("Có bạn nào chưa làm bài tập không?", False, "là một câu hỏi, không thể xác định được tính đúng sai. Do đó, đây không phải là một mệnh đề."),
            ("$%s + %s = %s$" % (latex(n1), latex(n2), latex(n3)), True, "là một đẳng thức số học, có tính đúng sai rõ ràng (đây là khẳng định sai). Do đó, đây là một mệnh đề."),
            ("Thời tiết hôm nay nóng quá!", False, "là một câu cảm thán, bộc lộ cảm xúc, không thể xác định đúng sai. Do đó, đây không phải là một mệnh đề."),
            ("Chu vi hình chữ nhật bằng tích của chiều dài và chiều rộng của nó", True, "là một khẳng định về hình học có tính đúng sai rõ ràng (đây là khẳng định sai). Do đó, đây là một mệnh đề."),
            ("Nếu một số tự nhiên có tận cùng bằng $0$ thì số đó chia hết cho $%s$" % latex(num_p2), True, "là một mệnh đề kéo theo có tính đúng sai rõ ràng. Do đó, đây là một mệnh đề.")
        ]

        # Chọn ngẫu nhiên từ 8 đến 10 câu để tạo sự thay đổi cấu trúc đề
        num_select = random.randint(8, 10)
        chosen_items = random.sample(statements_pool, num_select)

        # Đếm số lượng phát biểu là mệnh đề
        kq_num = sum(1 for item in chosen_items if item[1] is True)
        da = '$%s$' % latex(kq_num)

        # Tạo các phương án sai xung quanh đáp án đúng (từ 1 đến 10 và không trùng với kq_num)
        s_candi = list(range(1, 11))
        if kq_num in s_candi:
            s_candi.remove(kq_num)

        s = []
        for val in random.sample(s_candi, 3):
            s.append('$%s$' % latex(val))

        das1 = s[0]
        das2 = s[1]
        das3 = s[2]

        # Tạo chuỗi nội dung câu hỏi
        list_str_statements = ""
        for i, item in enumerate(chosen_items):
            list_str_statements += "%s) %s. \\\\" % (latex(i + 1), item[0])
        list_str_statements = list_str_statements.rstrip(" \\\\")

        # Câu hỏi
        noidungcauhoi = ('''Trong các phát biểu sau, có bao nhiêu phát biểu là mệnh đề? \\\\ %s'''
                            % (list_str_statements))

        # Các đáp án
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2) 
        da_s3 = str(das3) 

        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Tạo chuỗi lời giải chi tiết
        loigiai_chi_tiet = ""
        for i, item in enumerate(chosen_items):
            loigiai_chi_tiet += "Phát biểu %s) \"%s\" %s \\\\" % (latex(i + 1), item[0], item[2])
        loigiai_chi_tiet = loigiai_chi_tiet.rstrip(" \\\\")

        loigiai = ('''Mệnh đề là một khẳng định có tính đúng hoặc sai rõ ràng. Câu hỏi, câu cảm thán hoặc câu chứa biến chưa xác định giá trị không phải là mệnh đề. \\\\
    Xét từng phát biểu ta có: \\\\ %s \\\\ Kết luận: Có tất cả $%s$ phát biểu là mệnh đề.'''
                    % (loigiai_chi_tiet, latex(kq_num)))
        dapan='\\shortans[0]{$%s$}\n'%(latex(kq_num))
    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) +dapan+
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
    return content

