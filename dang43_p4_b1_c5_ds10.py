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


def bt_dang43_p4_b1_c5_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # B3: Random bài toán bằng cách thay đổi giá trị bắt đầu của dãy 6 số liên tiếp
                # Ví dụ: n=1 là dãy {1,2,3,4,5,6}, n=2 là dãy {2,3,4,5,6,7}
                n = randint(1, 2)
                d1, d2, d3, d4, d5, d6 = n, n+1, n+2, n+3, n+4, n+5
                digits = [d1, d2, d3, d4, d5, d6]

                # Tính toán logic bài toán
                tong_sau = (sum(digits) - 1) // 2 # S2: tổng 3 số cuối
                tong_dau = tong_sau + 1          # S1: tổng 3 số đầu

                chu_so_le = [d for d in digits if d % 2 != 0]

                # Giải thuật tìm số trường hợp
                so_truong_hop_bo_ba = 0
                chi_tiet_lg = ""

                for a6 in chu_so_le:
                    tap_con_lai = [d for d in digits if d != a6]
                    tong_hai_so = tong_sau - a6
                    pairs = []
                    for i in range(len(tap_con_lai)):
                        for j in range(i + 1, len(tap_con_lai)):
                            if tap_con_lai[i] + tap_con_lai[j] == tong_hai_so:
                                pairs.append((tap_con_lai[i], tap_con_lai[j]))

                    if pairs:
                        so_truong_hop_bo_ba += len(pairs)
                        # Tạo chuỗi lời giải cho từng trường hợp a6
                        line_lg = "O Với $a_6 = %s$ thì $\\left( a_1+a_2+a_3 \\right) - \\left( a_4+a_5 \\right) = %s \\Rightarrow " % (latex(a6), latex(tong_sau - a6 + 1))
                        cases = []
                        for p in pairs:
                            a45 = set(p)
                            a123 = set(tap_con_lai) - a45
                            cases.append("\\begin{cases} a_1,a_2,a_3 \\in \\{%s\\} \\\\ a_4,a_5 \\in \\{%s\\} \\end{cases}$" % (",".join(map(str, sorted(list(a123)))), ",".join(map(str, sorted(list(a45))))))
                        chi_tiet_lg += line_lg + " hoặc $".join(cases) + " \\\\ "

                # Kết quả
                # Mỗi bộ {a1,a2,a3} có 3! cách, {a4,a5} có 2! cách.
                kq_so = so_truong_hop_bo_ba * factorial(3) * factorial(2)

                # B4: Điều chỉnh các phương án sai không trùng đáp án đúng
                kq = int(kq_so)
                s_options = [kq + 12, kq - 12, kq + 24, kq - 24, kq // 2, kq + 36, 24, 32, 36, 48]
                s_options = list(set([x for x in s_options if x > 0 and x != kq]))
                random.shuffle(s_options)

                das1 = s_options[0]
                das2 = s_options[1]
                das3 = s_options[2]

                # Câu hỏi
                noidungcauhoi = ('''Từ các chữ số $%s, %s, %s, %s, %s, %s$ tìm số các số tự nhiên lẻ có $6$ chữ số khác nhau và trong mỗi số đó tổng của ba chữ số đầu lớn hơn tổng của ba chữ số cuối một đơn vị.'''
                                 %(latex(d1), latex(d2), latex(d3), latex(d4), latex(d5), latex(d6)))

                # Các đáp án
                da_d = ('\\True $%s$' % (latex(kq)))
                da_s1 = '$%s$' % (latex(das1))
                da_s2 = '$%s$' % (latex(das2)) 
                da_s3 = '$%s$' % (latex(das3)) 

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Gọi $\\overline{a_1a_2a_3a_4a_5a_6}$ là số cần tìm. \\\\
                            Ta có $a_6 \\in \\{%s\\}$ và $\\left( a_1+a_2+a_3 \\right) - \\left( a_4+a_5+a_6 \\right) = 1$. \\\\
                            Vì tổng của các chữ số từ $%s$ đến $%s$ là $%s$ nên: \\\\
                            $\\left( a_1+a_2+a_3 \\right) + \\left( a_4+a_5+a_6 \\right) = %s$. \\\\
                            Từ đó suy ra $a_1+a_2+a_3 = %s$ và $a_4+a_5+a_6 = %s$. \\\\
                            %s
                            Mỗi trường hợp bộ ba số và bộ hai số có $3! \\cdot 2! = 12$ số thỏa mãn yêu cầu. \\\\
                            Vậy có tất cả $%s \\cdot 12 = %s$ số cần tìm.'''
                            %( ", ".join([str(x) for x in chu_so_le]),
                               latex(d1), latex(d6), latex(sum(digits)),
                               latex(sum(digits)), latex(tong_dau), latex(tong_sau),
                               chi_tiet_lg,
                               latex(so_truong_hop_bo_ba), latex(kq)
                            ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

