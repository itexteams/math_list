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


def bt_dang51_p3_b6_c2_hh11(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)

    if dang=='1':
        # Random tham số bài toán
        k = random.choice([1, 2, 3, 4])
        a_val = random.choice([2, 3, 4, 5, 6])
        c_val = 1 * k
        L_val = a_val + 5 * k

        # Tính toán các giá trị trung gian
        h1_val = Rational(L_val - a_val, 2)
        b_val = L_val - 2 * c_val
        dr_val = Rational(b_val - a_val, 2)
        h_val = int(math.sqrt(float(h1_val**2 - dr_val**2)))

        # Hàm định dạng số thập phân dùng dấu phẩy
        def fmt_num(val):
            if isinstance(val, (int, Integer)):
                return str(val)
            elif isinstance(val, (float, Rational)):
                f_val = float(val)
                if f_val.is_integer():
                    return str(int(f_val))
                return str(f_val).replace('.', ',')
            return str(val).replace('.', ',')

        str_L = fmt_num(L_val)
        str_a = fmt_num(a_val)
        str_c = fmt_num(c_val)
        str_b = fmt_num(b_val)
        str_h1 = fmt_num(h1_val)
        str_dr = fmt_num(dr_val)
        str_h1_sq = fmt_num(h1_val**2)
        str_dr_sq = fmt_num(dr_val**2)
        str_diff_sq = fmt_num(h1_val**2 - dr_val**2)
        str_h = fmt_num(h_val)

        # Đáp án đúng
        kq = str_h
        du = ['$%s$' % (kq)]
        da = random.choice(du)

        # Tạo danh sách đáp án sai không trùng nhau và không trùng đáp án đúng
        candidate_vals = [
            h_val + 1,
            h_val + 2,
            h_val - 1 if h_val > 1 else h_val + 3,
            float(h1_val),
            float(dr_val),
            h_val + 0.5
        ]

        s = []
        for c_v in candidate_vals:
            c_str = '$%s$' % (fmt_num(c_v))
            if c_str != da and c_str not in s:
                s.append(c_str)

        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)

        # Nội dung câu hỏi
        noidungcauhoi = ('''Để chuẩn bị cho hội chợ "Ý tưởng xanh", bạn Nam dự định làm một chiếc khay trồng rau mầm thủy canh dạng hình chóp cụt đều không có nắp. Từ một tấm vật liệu tái chế hình vuông có cạnh $%s\\text{ dm}$, Nam cắt bỏ bốn phần giống nhau ở bốn góc, sau đó gấp tạo hình rồi hàn các mép lại để được chiếc khay như hình vẽ bên dưới. Biết đáy khay là hình vuông có cạnh bằng $%s\\text{ dm}$ và đoạn cắt ở mỗi góc có độ dài $%s\\text{ dm}$. Hỏi chiều cao của chiếc khay trồng rau này bằng bao nhiêu đề-xi-mét?
    \\begin{center}
    	\\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
    		\\draw  [fill={rgb, 255:red, 80; green, 227; blue, 194 }  ,fill opacity=1 ][line width=0.75]  (325.6,184) -- (411.6,184) -- (411.6,270) -- (325.6,270) -- cycle ;
    		\\draw  [fill={rgb, 255:red, 80; green, 227; blue, 194 }  ,fill opacity=1 ][line width=1]  (51.1,173.9) -- (158.1,173.9) -- (158.1,280.9) -- (51.1,280.9) -- cycle ;
    		\\draw  [fill={rgb, 255:red, 80; green, 227; blue, 194 }  ,fill opacity=1 ][line width=1]  (81.6,204.4) -- (127.6,204.4) -- (127.6,250.4) -- (81.6,250.4) -- cycle ;
    		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (51.1,173.9) -- (81.6,204.4) ;
    		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (127.6,204.4) -- (158.1,173.9) ;
    		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (127.6,250.4) -- (158.1,280.9) ;
    		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (51.1,280.9) -- (81.6,250.4) ;
    		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (63.6,173.9) -- (81.6,204.4) ;
    		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (51.1,186.4) -- (81.6,204.4) ;
    		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (127.6,204.4) -- (158.1,186.4) ;
    		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (127.6,204.4) -- (145.6,173.9) ;
    		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (127.6,250.4) -- (158.1,268.4) ;
    		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (127.6,250.4) -- (145.6,280.9) ;
    		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (51.1,268.4) -- (81.6,250.4) ;
    		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (81.6,250.4) -- (63.6,280.9) ;
    		\\draw  [fill={rgb, 255:red, 80; green, 227; blue, 194 }  ,fill opacity=1 ][line width=1]  (188.1,173.5) -- (295.1,173.5) -- (295.1,280.5) -- (188.1,280.5) -- cycle ;
    		\\draw  [fill={rgb, 255:red, 80; green, 227; blue, 194 }  ,fill opacity=1 ][line width=1]  (218.6,204) -- (264.6,204) -- (264.6,250) -- (218.6,250) -- cycle ;
    		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (188.1,173.5) -- (218.6,204) ;
    		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (264.6,204) -- (295.1,173.5) ;
    		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (264.6,250) -- (295.1,280.5) ;
    		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (188.1,280.5) -- (218.6,250) ;
    		\\draw [line width=1]    (200.6,173.5) -- (218.6,204) ;
    		\\draw [line width=1]    (188.1,186) -- (218.6,204) ;
    		\\draw [line width=1]    (264.6,204) -- (295.1,186) ;
    		\\draw [line width=1]    (264.6,204) -- (282.6,173.5) ;
    		\\draw [line width=1]    (264.6,250) -- (295.1,268) ;
    		\\draw [line width=1]    (264.6,250) -- (282.6,280.5) ;
    		\\draw [line width=1]    (188.1,268) -- (218.6,250) ;
    		\\draw [line width=1]    (218.6,250) -- (200.6,280.5) ;
    		\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (197.6,170.4) -- (218.6,204) -- (184.1,182.4) -- (185.85,170.4) -- cycle ;
    		\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (300.1,181.4) -- (264.6,204) -- (285.6,170.4) -- (297.1,171.4) -- cycle ;
    		\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (298.1,271.4) -- (264.6,250) -- (285.1,282.4) -- (297.1,284.9) -- cycle ;
    		\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (185.6,270.9) -- (218.6,250) -- (197.1,283.9) -- (188.1,280.5) -- cycle ;
    		\\draw  [fill={rgb, 255:red, 65; green, 181; blue, 155 }  ,fill opacity=1 ][line width=1]  (345.6,204) -- (391.6,204) -- (391.6,250) -- (345.6,250) -- cycle ;
    		\\draw    (325.6,184) -- (345.6,204) ;
    		\\draw    (391.6,204) -- (411.6,184) ;
    		\\draw    (391.6,250) -- (411.6,270) ;
    		\\draw    (325.6,270) -- (345.6,250) ;
    		\\draw   (485.16,227.6) -- (544.8,227.6) -- (519.24,249.2) -- (459.6,249.2) -- cycle ;
    		\\draw  [fill={rgb, 255:red, 80; green, 227; blue, 194 }  ,fill opacity=1 ] (469.3,199.6) -- (485.16,227.6) -- (459.6,249.2) -- (442.8,221.6) -- cycle ;
    		\\draw  [fill={rgb, 255:red, 80; green, 227; blue, 194 }  ,fill opacity=1 ] (560.36,199) -- (544.8,227.6) -- (485.16,227.6) -- (469.3,199.6) -- cycle ;
    		\\draw  [fill={rgb, 255:red, 80; green, 227; blue, 194 }  ,fill opacity=1 ] (534.8,220.6) -- (519.24,249.2) -- (459.6,249.2) -- (442.8,221.6) -- cycle ;
    		\\draw  [fill={rgb, 255:red, 80; green, 227; blue, 194 }  ,fill opacity=1 ] (560.36,199) -- (544.8,227.6) -- (519.24,249.2) -- (534.8,220.6) -- cycle ;
    	\\end{tikzpicture}
    \\end{center}'''
        %(str_L, str_a, str_c)
        )

        # Các đáp án
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)

        # Trộn ngẫu nhiên đáp án
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Lời giải chi tiết
        loigiai = ('''Chiều cao của hình thang cân ở mỗi mặt bên khi trải phẳng (trung đoạn của khay) là: \\\\
    $%s = \\frac{%s - %s}{2} = %s\\text{ (dm)}$. \\\\
    Độ dài cạnh đáy lớn của chiếc khay (cạnh đáy trên $A'B'C'D'$) là: \\\\
    $%s = %s - 2 \\cdot %s = %s\\text{ (dm)}$. \\\\
    Xét thiết diện qua trục của hình chóp cụt đều, khoảng cách từ chân đường cao mặt bên đến tâm đáy lớn là: \\\\
    $%s = \\frac{%s - %s}{2} = %s\\text{ (dm)}$. \\\\
    Chiều cao $h$ của chiếc khay trồng rau hình chóp cụt đều là: \\\\
    $h = \\sqrt{%s^2 - %s^2} = \\sqrt{%s - %s} = \\sqrt{%s} = %s\\text{ (dm)}$.'''
        %(str_h1, str_L, str_a, str_h1,
          str_b, str_L, str_c, str_b,
          str_dr, str_b, str_a, str_dr,
          str_h1, str_dr, str_h1_sq, str_dr_sq, str_diff_sq, str_h)
        )
    dapan='\\shortans[0]{$%s$}\n'%(str_h)
    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
        '\\loigiai{'+str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n')
    return content

