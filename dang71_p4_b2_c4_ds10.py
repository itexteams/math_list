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


def bt_dang71_p4_b2_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # B3: Suy nghĩ tìm cách random bài toán
                # Chốt các thông số ngẫu nhiên để bài toán luôn có nghiệm đẹp hoặc hợp lý
                # Chieu rong cong (w) nen la so chan de tinh toan de dang
                w = random.randrange(10, 22, 2)  # Ví dụ: 10, 12, 14...
                # Chieu cao cong (H)
                H = random.randint(6, 10)
                # Chieu ngang xe tai (w_xe), phai nho hon chieu rong cong
                w_xe = random.randrange(4, w-2, 2) 

                # Tọa độ các điểm dựa trên hệ trục: Gốc O tại chân cột trái (0,0)
                # Parabol đi qua (0,0), (w, 0) và đỉnh (w/2, H)
                # Phương trình y = ax^2 + bx
                # 1) a(w)^2 + b(w) = 0  => b = -aw
                # 2) a(w/2)^2 + b(w/2) = H

                a_val = Rational(-4 * H, w**2)
                b_val = Rational(4 * H, w)

                # Tính chiều cao tối đa của xe tại vị trí biên (cách tâm 1 khoảng w_xe/2)
                # Vị trí x của mép xe: x1 = w/2 - w_xe/2 và x2 = w/2 + w_xe/2
                x_edge = Rational(w - w_xe, 2)
                h_max = a_val * (x_edge**2) + b_val * x_edge

                # Đáp án đúng
                kq = h_max
                da = '$0 < h < %s$' % (latex(kq))

                # B4: Điều chỉnh các phương án sai
                s = [
                    '$0 < h < %s$' % (latex(kq + 1)),
                    '$0 < h < %s$' % (latex(kq + 2)),
                    '$0 < h < %s$' % (latex(kq - 1)),
                    '$0 < h < %s$' % (latex(kq / 2)),
                    '$h < %s$' % (latex(kq)),
                    '$h > %s$' % (latex(kq))
                ]

                # Loại bỏ trường hợp trùng đáp án đúng (nếu có)
                s = [i for i in s if i != da]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # B2: Viết lại đề bài
                noidungcauhoi = ('''Một chiếc cổng hình parabol có chiều rộng $%s$ m và chiều cao $%s$ m. Giả sử một chiếc xe tải có chiều ngang $%s$ m đi vào vị trí chính giữa cổng. 
                                 \\begin{center} \\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-0.8,xscale=0.8]
            \\draw   (316.74,171.08) .. controls (245.01,12.87) and (172.67,12.59) .. (99.73,170.25) ;
            \\draw   (311.04,171) .. controls (242.95,20.84) and (174.3,20.58) .. (105.06,170.21) ;
            \\end{tikzpicture} \\end{center}
                                 Tìm điều kiện chiều cao $h$ của xe tải để có thể đi vào cổng mà không chạm tường.'''
                                 %(latex(w), latex(H), latex(w_xe)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết theo ảnh
                loigiai = ('''\\begin{center}
            	\\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-0.8,xscale=0.8]
            		\\draw   (316.74,171.08) .. controls (245.01,12.87) and (172.67,12.59) .. (99.73,170.25) ;
            		\\draw   (311.04,171) .. controls (242.95,20.84) and (174.3,20.58) .. (105.06,170.21) ; 
            		\\draw    (68.47,170.73) -- (360.47,170.73) ;
            		\\draw [shift={(362.47,170.73)}, rotate = 180] [color={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.75]    (10.93,-3.29) .. controls (6.95,-1.4) and (3.31,-0.3) .. (0,0) .. controls (3.31,0.3) and (6.95,1.4) .. (10.93,3.29)   ;
            		\\draw    (99.47,204.73) -- (101.44,29.73) ;
            		\\draw [shift={(101.47,27.73)}, rotate = 90.65] [color={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.75]    (10.93,-3.29) .. controls (6.95,-1.4) and (3.31,-0.3) .. (0,0) .. controls (3.31,0.3) and (6.95,1.4) .. (10.93,3.29)   ;
            		\\draw (78,171.33) node [anchor=north west][inner sep=0.75pt]    {$O$};
            		\\draw (337,177.33) node [anchor=north west][inner sep=0.75pt]    {$x$};
            		\\draw (80,29.33) node [anchor=north west][inner sep=0.75pt]    {$y$};
            	\\end{tikzpicture}
            \\end{center}Chọn hệ trục tọa độ sao cho chân cổng bên trái trùng với gốc tọa độ $O(0;0)$. Parabol có phương trình dạng $y = ax^2 + bx$. \\\\
                             Vì chiếc cổng hình parabol có chiều rộng $%s$ m và chiều cao $%s$ m, theo hình vẽ ta có parabol đi qua các điểm $(%s;0)$ và đỉnh $(%s;%s)$, suy ra: \\\\
                             $\\begin{cases} %s a + %s b = 0 \\\\ %s a + %s b = %s \\end{cases} \\Leftrightarrow \\begin{cases} a = %s \\\\ b = %s \\end{cases}$. \\\\
                             Suy ra parabol có phương trình $y = %s x^2 + %s x$. \\\\
                             Do chiếc xe tải có chiều ngang $%s$ m đi vào vị trí chính giữa cổng nên mép xe sẽ ở vị trí $x = \\frac{%s - %s}{2} = %s$. \\\\
                             Thay $x = %s$ vào phương trình parabol ta được $y = %s$. Khi đó chiều cao tối đa của xe là $%s$. \\\\
                             Vậy điều kiện để xe tải có thể đi vào cổng mà không chạm tường là $0 < h < %s$.'''
                          %(latex(w), latex(H), latex(w), latex(w/2), latex(H),
                            latex(w**2), latex(w), latex((Rational(w,2))**2), latex(Rational(w,2)), latex(H),
                            latex(a_val), latex(b_val),
                            latex(a_val), latex(b_val),
                            latex(w_xe), latex(w), latex(w_xe), latex(x_edge),
                            latex(x_edge), latex(kq), latex(kq), latex(kq)
                          ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

