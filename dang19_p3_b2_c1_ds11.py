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


def bt_dang19_p3_b2_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random khoảng cách chân cột OH (m)
                OH = random.choice([12, 15, 18, 20])

                # Random chiều cao gắn cáp S (BH) và cáp R (AH) sao cho AH > BH
                BH = random.choice([8, 10, 12])
                AH = BH + random.choice([2, 3, 4, 5])

                # Tính toán lượng giác bằng SymPy để tìm tan(AOB)
                tan_AOH = Rational(AH, OH)
                tan_BOH = Rational(BH, OH)

                # Công thức hiệu tan: tan(AOB) = (tan_AOH - tan_BOH) / (1 + tan_AOH * tan_BOH)
                tu_so = tan_AOH - tan_BOH
                mau_so = 1 + tan_AOH * tan_BOH
                tan_AOB = Rational(tu_so, mau_so)

                # Tính giá trị góc alpha theo độ
                alpha_rad = math.atan(float(tan_AOB))
                alpha_deg = math.degrees(alpha_rad)

                # Làm tròn đến hàng đơn vị theo đơn vị độ
                kq_dec = Decimal(str(alpha_deg)).quantize(Decimal('1'), rounding=ROUND_HALF_UP)
                kq = '%s^\\circ' % kq_dec

                # Các đáp án trắc nghiệm
                du = ['$%s$' % (kq)]
                da = random.choice(du)

                # Tạo các phương án sai xung quanh kết quả đúng
                s = []
                val_int = int(kq_dec)
                phi_sai = [val_int + 1, val_int + 2, val_int + 3, val_int - 1, val_int - 2, val_int - 3]
                for v_sai in phi_sai:
                    if v_sai > 0:
                        sai_str = '$%s^\\circ$' % v_sai
                        if sai_str != da and sai_str not in s:
                            s.append(sai_str)

                while len(s) < 3:
                    v_rand = val_int + random.randint(-5, 5)
                    sai_str = '$%s^\\circ$' % v_rand
                    if sai_str != da and sai_str not in s and v_rand > 0:
                        s.append(sai_str)

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]
                hinhve=r'''\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            	\draw  [fill={rgb, 255:red, 74; green, 144; blue, 226 }  ,fill opacity=1 ][line width=1]  (180.6,65) -- (187.5,65) -- (187.5,204.4) -- (180.6,204.4) -- cycle ;
            	\draw [line width=1]    (184.05,65) -- (137.6,83.9) ;
            	\draw [line width=1]    (183.05,102) -- (136.6,120.9) ;
            	\draw [line width=1]    (180.6,204.4) -- (136.6,232.4) ;
            	\draw  [fill={rgb, 255:red, 74; green, 144; blue, 226 }  ,fill opacity=1 ][line width=1]  (128.6,84.4) -- (136,84.4) -- (136,231.9) -- (128.6,231.9) -- cycle ;
            	\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=1]    (137.5,84.7) -- (314.6,234.4) ;
            	\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=1]    (136.6,120.9) -- (314.6,234.4) ;
            	\draw [line width=1]    (140.6,232.44) -- (310.6,234.36) ;
            	\draw [shift={(314.6,234.4)}, rotate = 180.64] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (8.75,-4.2) -- (0,0) -- (8.75,4.2) -- (5.81,0) -- cycle    ;
            	\draw [shift={(136.6,232.4)}, rotate = 0.64] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (8.75,-4.2) -- (0,0) -- (8.75,4.2) -- (5.81,0) -- cycle    ;
            	\draw [line width=1]    (252.1,233.9) .. controls (247.6,221.9) and (252.1,200.4) .. (267.6,194.4) ;
            	\draw [line width=1]    (270.6,204.9) -- (276,202) ;
            	\draw (122,63) node [anchor=north west][inner sep=0.75pt]    {$A$};
            	\draw (112,109) node [anchor=north west][inner sep=0.75pt]    {$B$};
            	\draw (108.5,228.5) node [anchor=north west][inner sep=0.75pt]    {$H$};
            	\draw (316.5,224) node [anchor=north west][inner sep=0.75pt]    {$O$};
            	\draw (200.5,117) node [anchor=north west][inner sep=0.75pt]    {$R$};
            	\draw (196,168) node [anchor=north west][inner sep=0.75pt]    {$S$};
            	\draw (233,207) node [anchor=north west][inner sep=0.75pt]    {$\beta $};
            	\draw (285.5,188) node [anchor=north west][inner sep=0.75pt]    {$\alpha $};
            \end{tikzpicture}'''
                # Câu hỏi
                noidungcauhoi = (r'''\immini{Một sợi cáp R được gắn vào một cột thẳng đứng ở vị trí cách mặt đất $%sm$. Một sợi cáp S khác cũng được gắn vào cột đó ở vị trí cách mặt đất $%sm$. Biết rằng hai sợi cáp trên cũng được gắn với mặt đất tại một vị trí cách chân cột $%sm$ (như hình vẽ). Giá trị góc $\alpha$ bằng bao nhiêu? làm tròn kết quả đến hàng đơn vị theo đơn vị độ.}{%s}'''
                                 % (latex(AH), latex(BH), latex(OH), hinhve))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Ta có: \\\\
                             + Góc $\\alpha = \\widehat{AOB}$. Mà theo hình ta thấy: $\\widehat{AOB} = \\widehat{AOH} - \\widehat{BOH}$ \\\\
                             + Ta có: $\\tan AOB = \\tan (AOH - BOH) = \\frac{\\tan AOH - \\tan BOH}{1 + \\tan AOH \\cdot \\tan BOH}$ (*) \\\\
                             + Xét $\\Delta AHO$ vuông tại H có: $\\tan AOH = \\frac{AH}{OH} = \\frac{%s}{%s}$ (1) \\\\
                             + Xét $\\Delta BHO$ vuông tại H có: $\\tan BOH = \\frac{BH}{OH} = \\frac{%s}{%s}$ (2) \\\\
                             Thay (1), (2) vào (*) ta tính được: $\\tan AOB = \\frac{%s}{%s} \\Rightarrow \\alpha = \\widehat{AOB} \\approx %s$.'''
                           % (latex(AH), latex(OH), latex(BH), latex(OH), latex(tan_AOB.p), latex(tan_AOB.q), kq))
                dapan='\\shortans[0]{$%s$}\n'%(kq_dec)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + dapan+
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

