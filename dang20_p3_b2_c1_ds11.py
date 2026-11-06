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


def bt_dang20_p3_b2_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Chọn ngẫu nhiên bộ ba số Pythagore cho tam giác OXA vuông tại X (cạnh huyền OA)
                triplets = [(6, 8, 10), (8, 6, 10)]
                ox, xa, oa = random.choice(triplets)

                # Chọn ngẫu nhiên độ dài đoạn AY
                ay = random.choice([7, 8, 9, 11, 12])

                # Tính toán các giá trị hình học bằng SymPy
                oy2 = oa**2 + ay**2
                oy = sqrt(oy2)

                # Tính sin và cos của các góc thành phần
                sin_aoy = Rational(ay, 1) / oy
                cos_aoy = Rational(oa, 1) / oy

                cos_xoa = Rational(ox, oa)
                sin_xoa = Rational(xa, oa)

                # Đáp án đúng dạng giá trị chính xác trước khi làm tròn
                kq_chinhxac = sin_xoa * cos_aoy + cos_xoa * sin_aoy

                # Chuyển đổi và làm tròn đến hàng phần chục theo yêu cầu bằng Decimal
                kq_float = float(kq_chinhxac)
                kq_decimal = Decimal(str(kq_float)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                kq_str = str(kq_decimal).replace('.', ',')

                # Các phương án trắc nghiệm (làm tròn đến hàng phần chục và dùng dấu phẩy)
                da = '$%s$' % kq_str

                # Tạo các phương án nhiễu dựa trên kết quả đúng
                val_da = float(kq_decimal)
                val_s1 = round(val_da + 0.2, 1)
                val_s2 = round(val_da - 0.2, 1)
                val_s3 = round(val_da + 0.4, 1)

                das1 = '$%s$' % str(val_s1).replace('.', ',')
                das2 = '$%s$' % str(val_s2).replace('.', ',')
                das3 = '$%s$' % str(val_s3).replace('.', ',')

                # Chuỗi mã TikZ cho hình vẽ (Tuyệt đối không dùng raw string r''')
                hinhve = '''\\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            	\\draw  [fill={rgb, 255:red, 202; green, 220; blue, 240 }  ,fill opacity=1 ][line width=1]  (353.7,187.4) -- (352.7,122.4) -- (244.2,78.4) -- (83.2,144.4) -- (114.7,195.4) -- (244.2,141.9) -- cycle ;
            	\\draw [line width=1]    (84,109) -- (244.2,45.4) ;
            	\\draw [line width=1]    (352.2,89.9) -- (244.2,45.4) ;
            	\\draw [line width=1]    (84,120.5) -- (244.2,56.9) ;
            	\\draw [line width=1]    (83.5,132.5) -- (243.7,68.9) ;
            	\\draw [line width=1]    (352.2,101.4) -- (244.2,56.9) ;
            	\\draw [line width=1]    (351.7,113.4) -- (243.7,68.9) ;
            	\\draw [line width=1]    (84.2,141.9) -- (84,109) ;
            	\\draw [line width=1]    (121.7,127.4) -- (121.5,94.5) ;
            	\\draw [line width=1]    (152.7,115.4) -- (152.5,82.5) ;
            	\\draw [line width=1]    (183.2,102.4) -- (183,69.5) ;
            	\\draw [line width=1]    (209.7,92.9) -- (209.5,60) ;
            	\\draw [line width=1]    (244.2,78.4) -- (244,45.5) ;
            	\\draw [line width=1]    (268.2,87.9) -- (268.5,56) ;
            	\\draw [line width=1]    (291.7,97.9) -- (291.5,65) ;
            	\\draw [line width=1]    (319.7,109.4) -- (319.5,76.5) ;
            	\\draw [line width=1]    (352.7,122.4) -- (352.5,89.5) ;
            	\\draw  [fill={rgb, 255:red, 194; green, 207; blue, 223 }  ,fill opacity=1 ][line width=1]  (83.2,117.3) -- (86.4,117.3) -- (86.4,144.4) -- (83.2,144.4) -- cycle ;
            	\\draw  [fill={rgb, 255:red, 194; green, 207; blue, 223 }  ,fill opacity=1 ][line width=1]  (120.1,100.3) -- (123.3,100.3) -- (123.3,127.4) -- (120.1,127.4) -- cycle ;
            	\\draw  [fill={rgb, 255:red, 194; green, 207; blue, 223 }  ,fill opacity=1 ][line width=1]  (151.1,88.3) -- (154.3,88.3) -- (154.3,115.4) -- (151.1,115.4) -- cycle ;
            	\\draw  [fill={rgb, 255:red, 194; green, 207; blue, 223 }  ,fill opacity=1 ][line width=1]  (181.6,75.3) -- (184.8,75.3) -- (184.8,102.4) -- (181.6,102.4) -- cycle ;
            	\\draw  [fill={rgb, 255:red, 194; green, 207; blue, 223 }  ,fill opacity=1 ][line width=1]  (208.1,65.8) -- (211.3,65.8) -- (211.3,92.9) -- (208.1,92.9) -- cycle ;
            	\\draw  [fill={rgb, 255:red, 194; green, 207; blue, 223 }  ,fill opacity=1 ][line width=1]  (242.6,51.3) -- (245.8,51.3) -- (245.8,78.4) -- (242.6,78.4) -- cycle ;
            	\\draw  [fill={rgb, 255:red, 194; green, 207; blue, 223 }  ,fill opacity=1 ][line width=1]  (266.6,60.8) -- (269.8,60.8) -- (269.8,87.9) -- (266.6,87.9) -- cycle ;
            	\\draw  [fill={rgb, 255:red, 194; green, 207; blue, 223 }  ,fill opacity=1 ][line width=1]  (290.1,70.8) -- (293.3,70.8) -- (293.3,97.9) -- (290.1,97.9) -- cycle ;
            	\\draw  [fill={rgb, 255:red, 194; green, 207; blue, 223 }  ,fill opacity=1 ][line width=1]  (318.1,82.3) -- (321.3,82.3) -- (321.3,109.4) -- (318.1,109.4) -- cycle ;
            	\\draw  [fill={rgb, 255:red, 194; green, 207; blue, 223 }  ,fill opacity=1 ][line width=1]  (351.1,95.3) -- (354.3,95.3) -- (354.3,122.4) -- (351.1,122.4) -- cycle ;
            	\\draw [line width=1]    (244.2,78.4) -- (244.2,141.9) ;
            	\\draw [line width=1]    (84.8,144.4) -- (244.2,141.9) ;
            	\\draw  [line width=1]  (118.2,184.07) -- (122.87,192.4) -- (114.7,195.4) -- (109.53,187.73) -- cycle ;
            	\\draw  [line width=1]  (243.87,132.73) -- (244.2,141.9) -- (235.53,142.07) -- (234.87,133.07) -- cycle ;
            	\\draw (61.33,130.13) node [anchor=north west][inner sep=0.75pt]    {$O$};
            	\\draw (102,196.47) node [anchor=north west][inner sep=0.75pt]    {$X$};
            	\\draw (228,88) node [anchor=north west][inner sep=0.75pt]    {$Y$};
            	\\draw (233.33,144.8) node [anchor=north west][inner sep=0.75pt]    {$A$};
            	\\draw (152.67,119.47) node [anchor=north west][inner sep=0.75pt]    {$%s\\text{ m}$};
            	\\draw (249.33,98.8) node [anchor=north west][inner sep=0.75pt]    {$%s\\text{ m}$};
            	\\draw (78.67,160.47) node [anchor=north west][inner sep=0.75pt]    {$%s\\text{ m}$};
            \\end{tikzpicture}''' % (latex(oa), latex(ay), latex(ox))

                # Câu hỏi kèm hình vẽ TikZ
                noidungcauhoi = ('''\\immini{Sơ đồ cho thấy một phần cấu trúc kim loại của một cây cầu. Giá trị của $\\sin \\widehat{XOY}$ bằng bao nhiêu? (Kết quả làm tròn đến hàng phần chục).}{%s}'''
                                 % (hinhve))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Chuẩn bị hiển thị chuỗi biểu thức số thập phân dấu phẩy cho lời giải
                val_sin_aoy = str(round(float(sin_aoy), 4)).replace('.', ',')
                val_cos_aoy = str(round(float(cos_aoy), 4)).replace('.', ',')
                val_cos_xoa = str(round(float(cos_xoa), 4)).replace('.', ',')
                val_sin_xoa = str(round(float(sin_xoa), 4)).replace('.', ',')

                # Nội dung lời giải đầy đủ, chi tiết từng bước không viết tắt
                loigiai = ('''Gọi $A$ là chân đường vuông góc hạ từ $Y$ xuống đường thẳng $OA$. Do đó tam giác $OAY$ vuông tại $A$.\\\\
                           Ta có $OY = \\sqrt{OA^2 + AY^2} = \\sqrt{%s^2 + %s^2} = \\sqrt{%s}$.\\\\
                           Mặt khác ta có:\\\\
                           $\\sin \\widehat{AOY} = \\frac{%s}{\\sqrt{%s}} \\approx %s \\Rightarrow \\cos \\widehat{AOY} = \\sqrt{1 - \\sin^2 \\widehat{AOY}} \\approx %s$ (vì góc $\\widehat{AOY}$ là góc nhọn nên $\\cos \\widehat{AOY} > 0$).\\\\
                           Trong tam giác $OXA$ vuông tại $X$, ta có:\\\\
                           $\\cos \\widehat{XOA} = \\frac{%s}{%s} = %s \\Rightarrow \\sin \\widehat{XOA} = \\sqrt{1 - \\left(%s\\right)^2} = %s$ (vì góc $\\widehat{XOA}$ là góc nhọn nên $\\sin \\widehat{XOA} > 0$).\\\\
                           Ta lại có $\\sin \\widehat{XOY} = \\sin\\left(\\widehat{XOA} + \\widehat{AOY}\\right) = \\sin \\widehat{XOA} \\cdot \\cos \\widehat{AOY} + \\cos \\widehat{XOA} \\cdot \\sin \\widehat{AOY}$\\\\
                           $\\approx %s \\cdot %s + %s \\cdot %s \\approx %s$.'''
                           % (latex(oa), latex(ay), latex(oy2),
                              latex(ay), latex(oy2), val_sin_aoy, val_cos_aoy,
                              latex(ox), latex(oa), val_cos_xoa, val_cos_xoa, val_sin_xoa,
                              val_sin_xoa, val_cos_aoy, val_cos_xoa, val_sin_aoy, kq_str))
                dapan='\\shortans[0]{$%s$}\n'%(kq_str)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

