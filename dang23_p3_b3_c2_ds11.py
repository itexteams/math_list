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


def bt_dang23_p3_b3_c2_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Các giá trị cạnh hình vuông a có thể được chọn ngẫu nhiên
                list_a = [30, 40, 50, 60, 80, 100]
                a = random.choice(list_a)

                # Tính toán
                S1 = a**2
                # Tổng diện tích tô màu S = 2 * S1 * (1 - pi/4)
                exact_val = 2 * S1 * (1 - math.pi / 4)

                # Làm tròn đến hàng đơn vị
                kq_int = int(Decimal(float(exact_val)).quantize(Decimal('1'), rounding=ROUND_HALF_UP))
                kq = str(kq_int)

                # Các đáp án trắc nghiệm
                du = ['$%s$'%(kq)]
                da = random.choice(du)

                # Tạo các đáp án gây nhiễu, cộng trừ một số đơn vị
                s = ['$%s$'%(latex(kq_int+10)),
                     '$%s$'%(latex(kq_int+15)),
                     '$%s$'%(latex(kq_int+5)),
                     '$%s$'%(latex(kq_int-5)),
                     '$%s$'%(latex(kq_int-10)),
                     '$%s$'%(latex(kq_int-15)),
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi (Bao gồm hình vẽ mẫu TikZ)
                noidungcauhoi = ('''\\immini{Một loại gạch men có kích thước hình vuông $%s \\times %s$ cm. Người ta thiết kế hoa văn cho viên gạch bằng cách tạo đường tròn $(C_1)$ nội tiếp hình vuông ban đầu, phần nằm ngoài đường tròn $(C_1)$ mà thuộc viên gạch thì được tô màu đậm. Tiếp theo họ tạo ra một hình vuông nội tiếp đường tròn $(C_1)$, bên trong hình vuông này lại có một đường tròn nội tiếp $(C_2)$; và họ tiếp tục tô màu đậm cho phần nằm ngoài đường tròn $(C_2)$ mà thuộc hình vuông này. Quy luật này cứ thế tiếp tục vô hạn lần (tham khảo hình vẽ). Hỏi tổng diện tích thuộc về viên gạch được tô màu đậm là bao nhiêu cm vuông? (Kết quả được làm tròn đến hàng đơn vị của cm vuông).}
                                 {\\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            	\\draw  [fill={rgb, 255:red, 144; green, 19; blue, 254 }  ,fill opacity=1 ][line width=1]  (39.4,41) -- (199,41) -- (199,200.6) -- (39.4,200.6) -- cycle ;
            	\\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ][line width=1]  (39.4,120.8) .. controls (39.4,76.73) and (75.13,41) .. (119.2,41) .. controls (163.27,41) and (199,76.73) .. (199,120.8) .. controls (199,164.87) and (163.27,200.6) .. (119.2,200.6) .. controls (75.13,200.6) and (39.4,164.87) .. (39.4,120.8) -- cycle ;
            	\\draw  [fill={rgb, 255:red, 144; green, 19; blue, 254 }  ,fill opacity=1 ][line width=1]  (63.1,64.7) -- (175.3,64.7) -- (175.3,176.9) -- (63.1,176.9) -- cycle ;
            	\\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ][line width=1]  (63.1,120.8) .. controls (63.1,89.82) and (88.22,64.7) .. (119.2,64.7) .. controls (150.18,64.7) and (175.3,89.82) .. (175.3,120.8) .. controls (175.3,151.78) and (150.18,176.9) .. (119.2,176.9) .. controls (88.22,176.9) and (63.1,151.78) .. (63.1,120.8) -- cycle ;
            	\\draw  [fill={rgb, 255:red, 144; green, 19; blue, 254 }  ,fill opacity=1 ][line width=1]  (79.6,81.2) -- (158.8,81.2) -- (158.8,160.4) -- (79.6,160.4) -- cycle ;
            	\\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ][line width=1]  (79.6,120.8) .. controls (79.6,98.93) and (97.33,81.2) .. (119.2,81.2) .. controls (141.07,81.2) and (158.8,98.93) .. (158.8,120.8) .. controls (158.8,142.67) and (141.07,160.4) .. (119.2,160.4) .. controls (97.33,160.4) and (79.6,142.67) .. (79.6,120.8) -- cycle ;
            	\\draw  [fill={rgb, 255:red, 144; green, 19; blue, 254 }  ,fill opacity=1 ][line width=1]  (91.6,93.2) -- (146.8,93.2) -- (146.8,148.4) -- (91.6,148.4) -- cycle ;
            	\\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ][line width=1]  (91.6,120.8) .. controls (91.6,105.56) and (103.96,93.2) .. (119.2,93.2) .. controls (134.44,93.2) and (146.8,105.56) .. (146.8,120.8) .. controls (146.8,136.04) and (134.44,148.4) .. (119.2,148.4) .. controls (103.96,148.4) and (91.6,136.04) .. (91.6,120.8) -- cycle ;
            \\end{tikzpicture}}'''
                                 %(latex(a), latex(a)))

                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai=('''Gọi hình vuông ban đầu là hình vuông thứ nhất, có cạnh $a_1 = %s$ cm. Diện tích là $S_1 = %s^2 = %s$. \\\\
                Đường tròn $(C_1)$ nội tiếp hình vuông thứ nhất có bán kính $R_1 = \\frac{a_1}{2} = \\frac{%s}{2}$. Diện tích đường tròn $(C_1)$ là $S_{(C_1)} = \\pi R_1^2 = \\frac{\\pi}{4} %s^2 = \\frac{\\pi}{4} S_1$. \\\\
                Diện tích phần tô màu đậm ở bước 1 là: $u_1 = S_1 - S_{(C_1)} = S_1 - \\frac{\\pi}{4}S_1 = %s\\left(1 - \\frac{\\pi}{4}\\right)$. \\\\
                Hình vuông thứ 2 nội tiếp đường tròn $(C_1)$ nên có đường chéo bằng đường kính của $(C_1)$, do đó đường chéo bằng $a_1$. \\\\
                Cạnh của hình vuông thứ 2 là $a_2 = \\frac{a_1}{\\sqrt{2}}$. Diện tích hình vuông thứ 2 là $S_2 = a_2^2 = \\frac{a_1^2}{2} = \\frac{1}{2}S_1$. \\\\
                Đường tròn $(C_2)$ nội tiếp hình vuông thứ 2 có diện tích $S_{(C_2)} = \\frac{\\pi}{4} S_2 = \\frac{1}{2} S_{(C_1)}$. \\\\
                Diện tích phần tô màu đậm ở bước 2 là: $u_2 = S_2 - S_{(C_2)} = \\frac{1}{2}S_1 - \\frac{1}{2}S_{(C_1)} = \\frac{1}{2}(S_1 - S_{(C_1)}) = \\frac{1}{2}u_1$. \\\\
                Quá trình này lặp lại vô hạn lần, các phần diện tích tô màu đậm lập thành một cấp số nhân lùi vô hạn với số hạng đầu $u_1 = %s\\left(1 - \\frac{\\pi}{4}\\right)$ và công bội $q = \\frac{1}{2}$. \\\\
                Tổng diện tích phần tô màu đậm là: \\\\
                $S = \\frac{u_1}{1 - q} = \\frac{%s\\left(1 - \\frac{\\pi}{4}\\right)}{1 - \\frac{1}{2}} = 2 \\cdot %s\\left(1 - \\frac{\\pi}{4}\\right) = %s\\left(1 - \\frac{\\pi}{4}\\right) \\approx %s$ (cm$^2$).'''
                         %(latex(a), latex(a), latex(S1), latex(a), latex(a), latex(S1), latex(S1), latex(S1), latex(S1), latex(2*S1), kq))
            dapan='\\shortans[0]{$%s$}\n'%(kq)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

