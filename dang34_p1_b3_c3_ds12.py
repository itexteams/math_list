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


def bt_dang34_p1_b3_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 1 & 3: Random tham số bán kính a (chọn a từ 2 đến 10)
                a_val = randint(2, 10)

                # Tính toán kết quả theo công thức V = 2a^3 / 3
                v_tu = 2 * (a_val**3)
                v_mau = 3
                ket_qua = Rational(v_tu, v_mau)

                # Đáp án đúng
                da = '$%s$' % latex(ket_qua)

                # Bước 4: Tạo các phương án sai (không trùng với đáp án đúng)
                # Các trường hợp sai phổ biến: thiếu hệ số 2, sai mẫu số, hoặc nhầm sang có pi
                s_list = [
                    '$%s$' % latex(Rational(a_val**3, 3)),
                    '$%s$' % latex(Rational(4 * a_val**3, 3)),
                    '$%s$' % latex(a_val**3),
                    '$%s\\pi$' % latex(ket_qua),
                    '$%s\\pi$' % latex(Rational(a_val**3, 3)),
                    '$%s$' % latex(Rational(2 * a_val**3, 5)),
                    '$%s$' % latex(Rational(5 * a_val**3, 3))
                ]

                # Loại bỏ giá trị nếu lỡ trùng với đáp án đúng (đề phòng)
                if da in s_list:
                    s_list.remove(da)

                random.shuffle(s_list)
                das1 = s_list[0]
                das2 = s_list[1]
                das3 = s_list[2]

                # Câu hỏi
                noidungcauhoi = (r'''Gọi $(H)$ là phần giao của hai khối $\frac{1}{4}$ hình trụ có cùng bán kính $a = %s$, hai trục hình trụ vuông góc với nhau.
                         		\begin{center}
            \begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            \draw    (169.33,27.67) -- (29.33,107.67) ; 
            \draw    (29.33,107.67) -- (29.33,167.67) ;
            \draw  [dash pattern={on 4.5pt off 4.5pt}]  (29.33,167.67) -- (169.33,87.67) ;
            \draw  [dash pattern={on 4.5pt off 4.5pt}]  (169.33,87.67) -- (349.33,147.67) ;
            \draw    (169.33,27.67) -- (349.33,87.67) ; 
            \draw  [dash pattern={on 4.5pt off 4.5pt}]  (169.33,27.67) -- (169.33,87.67) ;
            \draw    (349.33,87.67) -- (349.33,147.67) ; 
            \draw    (29.33,167.67) -- (81.03,184.8) ;
            \draw    (172.77,131.27) -- (81.03,184.8) ;
            \draw    (349.33,147.67) -- (306.4,172.8) ;
            \draw    (306.4,172.8) -- (178.69,129.46) ;
            \draw  [dash pattern={on 4.5pt off 4.5pt}]  (169.33,87.67) -- (178.69,129.46) ;
            \draw  [dash pattern={on 4.5pt off 4.5pt}]  (172.77,131.27) -- (221.03,104.8) ;
            \draw  [dash pattern={on 4.5pt off 4.5pt}]  (178.69,129.46) -- (129.62,110.33) ;
            \draw  [draw opacity=0] (31.72,108.19) .. controls (66.31,115.98) and (88.25,150.1) .. (81.03,184.8) -- (17.44,171.59) -- cycle ; \draw   (31.72,108.19) .. controls (66.31,115.98) and (88.25,150.1) .. (81.03,184.8) ;  
            \draw  [draw opacity=0] (306.54,172.79) .. controls (294.83,138.19) and (313.07,100.59) .. (347.46,88.32) -- (369.97,151.33) -- cycle ; \draw   (306.54,172.79) .. controls (294.83,138.19) and (313.07,100.59) .. (347.46,88.32) ;  
            \draw  [draw opacity=0][dash pattern={on 4.5pt off 4.5pt}] (171.72,28.19) .. controls (206.31,35.98) and (228.25,70.1) .. (221.03,104.8) -- (157.44,91.59) -- cycle ; \draw  [dash pattern={on 4.5pt off 4.5pt}] (171.72,28.19) .. controls (206.31,35.98) and (228.25,70.1) .. (221.03,104.8) ;  
            \draw  [draw opacity=0][dash pattern={on 4.5pt off 4.5pt}] (130.62,111.33) .. controls (119.37,78.08) and (136.61,41.97) .. (169.35,29.69) -- (192.19,90.5) -- cycle ; \draw  [dash pattern={on 4.5pt off 4.5pt}] (130.62,111.33) .. controls (119.37,78.08) and (136.61,41.97) .. (169.35,29.69) ;  
            \draw  [draw opacity=0] (171.72,28.19) .. controls (191.31,60.48) and (192.03,99) .. (176.96,130.82) -- (79.06,84.4) -- cycle ; \draw   (171.72,28.19) .. controls (191.31,60.48) and (192.03,99) .. (176.96,130.82) ;  
            \end{tikzpicture}
            \end{center} Thể tích của khối $(H)$ là'''
                                 % (latex(a_val)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải (Sử dụng \text{d}x theo yêu cầu)
                a2 = a_val**2
                a3 = a_val**3

                loigiai = (r'''\begin{center}
            				\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            					\draw  [dash pattern={on 4.5pt off 4.5pt}]  (170.46,72.29) -- (169.33,130.67) ; 
            					\draw  [dash pattern={on 4.5pt off 4.5pt}]  (169.33,130.67) -- (176.96,173.82) ;
            					\draw    (176.96,173.82) -- (221.03,147.8) ;
            					\draw    (176.96,173.82) -- (129.62,153.33) ;
            					\draw  [draw opacity=0] (171.72,71.19) .. controls (206.31,78.98) and (228.25,113.1) .. (221.03,147.8) -- (157.44,134.59) -- cycle ; \draw   (171.72,71.19) .. controls (206.31,78.98) and (228.25,113.1) .. (221.03,147.8) ;  
            					\draw  [draw opacity=0] (130.62,154.33) .. controls (119.24,120.7) and (137,84.16) .. (170.46,72.29) -- (192.19,133.5) -- cycle ; \draw   (130.62,154.33) .. controls (119.24,120.7) and (137,84.16) .. (170.46,72.29) ;  
            					\draw  [draw opacity=0] (171.72,71.19) .. controls (191.31,103.48) and (192.03,142) .. (176.96,173.82) -- (79.06,127.4) -- cycle ; \draw   (171.72,71.19) .. controls (191.31,103.48) and (192.03,142) .. (176.96,173.82) ;  
            					\draw    (221.03,147.8) -- (282.5,168.5) ;
            					\draw [shift={(284.4,169.13)}, rotate = 198.61] [color={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.75]    (10.93,-3.29) .. controls (6.95,-1.4) and (3.31,-0.3) .. (0,0) .. controls (3.31,0.3) and (6.95,1.4) .. (10.93,3.29)   ;
            					\draw  [dash pattern={on 4.5pt off 4.5pt}]  (169.33,130.67) -- (221.03,147.8) ;
            					\draw    (130.62,154.33) -- (77.48,184.15) ;
            					\draw [shift={(75.73,185.13)}, rotate = 330.7] [color={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.75]    (10.93,-3.29) .. controls (6.95,-1.4) and (3.31,-0.3) .. (0,0) .. controls (3.31,0.3) and (6.95,1.4) .. (10.93,3.29)   ;
            					\draw  [dash pattern={on 4.5pt off 4.5pt}]  (169.33,130.67) -- (130.62,154.33) ;
            					\draw    (170.46,72.29) -- (170.71,35.6) ;
            					\draw [shift={(170.72,33.6)}, rotate = 90.38] [color={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.75]    (10.93,-3.29) .. controls (6.95,-1.4) and (3.31,-0.3) .. (0,0) .. controls (3.31,0.3) and (6.95,1.4) .. (10.93,3.29)   ;
            					\draw  [dash pattern={on 4.5pt off 4.5pt}]  (170.32,104.4) -- (127.52,123.2) ;
            					\draw  [dash pattern={on 4.5pt off 4.5pt}]  (170.32,104.4) -- (221.52,123.2) ;
            					\draw    (186.72,142.4) -- (221.52,123.2) ;
            					\draw    (186.72,142.4) -- (127.52,123.2) ;
            					\draw (155,120) node [anchor=north west][inner sep=0.75pt]    {$O$};
            					\draw (151.2,37.24) node [anchor=north west][inner sep=0.75pt]    {$x$};
            					\draw (76.8,150.44) node [anchor=north west][inner sep=0.75pt]    {$y$};
            					\draw (262.8,139.44) node [anchor=north west][inner sep=0.75pt]    {$z$};
            				\end{tikzpicture}
            			\end{center}'''
                           '''Đặt hệ tọa độ $Oxyz$ như hình vẽ, xét mặt cắt song song với mặt phẳng $(Oyz)$ cắt trục $Ox$ tại $x$: thiết diện mặt cắt luôn là hình vuông có cạnh $\\sqrt{%s^2 - x^2} = \\sqrt{%s - x^2}$ ($0 \\leq x \\leq %s$).\\\\
                             Do đó thiết diện mặt cắt có diện tích: $S(x) = %s - x^2$.\\\\
                             Vậy $V_{(H)} = \\int_{0}^{%s} S(x) \\text{d}x = \\int_{0}^{%s} (%s - x^2) \\text{d}x = \\left( %s x - \\frac{x^3}{3} \\right) \\bigg|_{0}^{%s} = \\frac{2 \\cdot %s}{3} = %s$.'''
                           % (latex(a_val), latex(a2), latex(a_val), 
                              latex(a2), 
                              latex(a_val), latex(a_val), latex(a2), 
                              latex(a2), latex(a_val), 
                              latex(a3), latex(ket_qua)
                             ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) +
                       '\n\\choice \n'
                       '{' + str(list_1[0]) + '}\n'
                       '{' + str(list_1[1]) + '}\n'
                       '{' + str(list_1[2]) + '}\n'
                       '{' + str(list_1[3]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

