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


def bt_dang16_p3_b2_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random các thông số cho bài toán
                d = random.choice([16, 18, 20, 22, 24]) # Đường kính AH
                h_val = random.choice([3.8, 4.0, 4.2, 4.3, 4.5, 4.8]) # Chiều cao BK

                R = d / 2.0

                # Tính toán chính xác
                sin_alpha = h_val / R
                cos_alpha = math.sqrt(1 - sin_alpha**2)
                CM_val = 2 * h_val * cos_alpha

                # Làm tròn đến phần trăm (2 chữ số thập phân)
                kq_exact = CM_val
                kq_dec = Decimal(str(kq_exact)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                kq_str = str(kq_dec).replace('.', ',')

                # Tạo phương án sai
                alpha = math.asin(sin_alpha)
                wrong1 = R * math.sin(3 * alpha)
                wrong2 = 2 * h_val
                wrong3 = kq_exact + 1.15
                wrong4 = kq_exact - 0.85
                wrong5 = kq_exact + 0.45

                s_vals = [wrong1, wrong2, wrong3, wrong4, wrong5]
                s_formatted = [str(Decimal(str(w)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)).replace('.', ',') for w in s_vals]

                # Đảm bảo các phương án sai khác nhau và không trùng đáp án đúng
                s_formatted = list(set(s_formatted))
                if kq_str in s_formatted:
                    s_formatted.remove(kq_str)

                das1, das2, das3 = random.sample(s_formatted, 3)

                # Chuyển đổi các số thành chuỗi để format hiển thị cho đẹp
                d_str = str(d)
                R_str = str(R).replace('.0', '').replace('.', ',')
                h_str = str(h_val).replace('.', ',')

                R_sq = R**2
                h_sq = h_val**2
                diff_sq = R_sq - h_sq
                diff_sq_str = str(round(diff_sq, 4)).replace('.0', '').replace('.', ',')

                # Vẽ hình TikZ minh họa bài toán
                tikz_code = ('''\\begin{center} 
                             \\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
                             	\\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (41.1,116.9) -- (329.6,116.9) -- (329.6,137.9) -- (41.1,137.9) -- cycle ;
                             	\\draw  [fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (329.6,222.4) -- (246.6,190.4) -- (113.1,190.4) -- (41.1,220.4) -- cycle ;
                             	\\draw  [fill={rgb, 255:red, 179; green, 174; blue, 174 }  ,fill opacity=1 ] (41.1,137.9) -- (329.6,137.9) -- (329.6,190.4) -- (41.1,190.4) -- cycle ;
                             	\\draw  [draw opacity=0][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ][line width=5.25]  (121.1,190.81) .. controls (121.15,157.44) and (147.77,130.4) .. (180.6,130.4) .. controls (213.43,130.4) and (240.05,157.44) .. (240.1,190.81) -- (180.6,190.9) -- cycle ; \\draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ][line width=5.25]  (121.1,190.81) .. controls (121.15,157.44) and (147.77,130.4) .. (180.6,130.4) .. controls (213.43,130.4) and (240.05,157.44) .. (240.1,190.81) ;  
                             	\\draw [color={rgb, 255:red, 248; green, 231; blue, 28 }  ,draw opacity=1 ]   (178.6,180.4) -- (180.6,220.4) ;
                             	\\draw [color={rgb, 255:red, 248; green, 231; blue, 28 }  ,draw opacity=1 ]   (178.6,180.4) -- (183.1,220.9) ;
                             	\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (124.85,190.9) -- (58.1,220.4) ;
                             	\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (236.85,190.9) -- (314.1,221.4) ;
                             	\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (240.1,190.81) -- (319.1,221.4) ;
                             	\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (121.1,190.81) -- (51.1,220.4) ;
                             	\\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (113.1,190.4) -- (41.1,190.4) -- (41.1,220.4) -- cycle ;
                             	\\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (329.6,190.4) -- (246.6,190.4) -- (329.6,222.4) -- cycle ;
                             	\\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (324.1,167.4) -- (327.6,184.4) -- (277.6,184.9) -- (279.1,168.4) -- cycle ;
                             	\\draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (327.6,184.4) -- (327.1,197.9) -- (276.6,197.9) -- (277.6,184.9) -- cycle ;
                             	\\draw  [fill={rgb, 255:red, 65; green, 117; blue, 5 }  ,fill opacity=1 ] (95.6,190.4) -- (101.6,190.4) -- (40.6,216.4) -- (41.1,211.4) -- cycle ;
                             	\\draw  [fill={rgb, 255:red, 65; green, 117; blue, 5 }  ,fill opacity=1 ] (255.1,190.2) -- (261.1,190.2) -- (330.6,212.4) -- (330.6,217.4) -- cycle ;
                             	\\draw  [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (249.5,169.95) .. controls (249.5,167.44) and (251.54,165.4) .. (254.05,165.4) .. controls (256.56,165.4) and (258.6,167.44) .. (258.6,169.95) .. controls (258.6,172.46) and (256.56,174.5) .. (254.05,174.5) .. controls (251.54,174.5) and (249.5,172.46) .. (249.5,169.95) -- cycle ;
                             	\\draw  [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (243.5,177.45) .. controls (243.5,174.94) and (245.54,172.9) .. (248.05,172.9) .. controls (250.56,172.9) and (252.6,174.94) .. (252.6,177.45) .. controls (252.6,179.96) and (250.56,182) .. (248.05,182) .. controls (245.54,182) and (243.5,179.96) .. (243.5,177.45) -- cycle ;
                             	\\draw  [color={rgb, 255:red, 74; green, 144; blue, 226 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (253.5,179.9) .. controls (253.04,177.39) and (254.71,175.35) .. (257.23,175.35) .. controls (259.74,175.35) and (262.14,177.39) .. (262.6,179.9) .. controls (263.06,182.41) and (261.39,184.45) .. (258.88,184.45) .. controls (256.36,184.45) and (253.96,182.41) .. (253.5,179.9) -- cycle ;
                             	\\draw  [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (115,176.95) .. controls (115,174.44) and (117.04,172.4) .. (119.55,172.4) .. controls (122.06,172.4) and (124.1,174.44) .. (124.1,176.95) .. controls (124.1,179.46) and (122.06,181.5) .. (119.55,181.5) .. controls (117.04,181.5) and (115,179.46) .. (115,176.95) -- cycle ;
                             	\\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (248.05,182) -- (257.5,182) -- (257.5,186.65) -- (248.05,186.65) -- cycle ;
                             	\\draw [color={rgb, 255:red, 248; green, 231; blue, 28 }  ,draw opacity=1 ] [dash pattern={on 0.84pt off 2.51pt}]  (163.6,168.4) .. controls (162.1,162.4) and (152.6,154.9) .. (142.6,152.9) ;
                             	\\draw [color={rgb, 255:red, 248; green, 231; blue, 28 }  ,draw opacity=1 ] [dash pattern={on 0.84pt off 2.51pt}]  (215.6,151.4) .. controls (213.6,157.4) and (196.6,176.9) .. (161.6,170.9) ;
                             	\\draw [color={rgb, 255:red, 128; green, 128; blue, 128 }  ,draw opacity=1 ][line width=1.5]    (124.85,190.9) .. controls (134.6,114.9) and (226.6,118.4) .. (236.85,190.9) ;
                             	\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ] [dash pattern={on 4.5pt off 4.5pt}]  (191.6,177.9) -- (248.6,222.4) ;
                             	\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ] [dash pattern={on 4.5pt off 4.5pt}]  (164.1,179.4) -- (119.1,220.4) ;
                             	\\draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.14 ][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.18 ] (192.1,175.4) -- (236.85,190.9) -- (124.85,190.9) -- (154.6,176.4) -- cycle ;
                             \\end{tikzpicture} \\hspace*{2cm}
                \\scalebox{0.6}{ \\begin{tikzpicture}[scale=0.4, line width=1pt]
                \\def\\R{9}
                \\def\\ang{28.56}
                \\draw[<->] (-\\R-0.5, -1.2) -- (\\R+0.5, -1.2) node[midway, below] {$%s$ m};
                \\draw (-\\R-1, 0) -- (\\R+1, 0);
                \\draw (\\R, 0) arc (0:180:\\R);
                \\coordinate (O) at (0,0);
                \\node[below] at (O) {$O$};
                \\coordinate (A) at (\\R, 0); \\node[above right] at (A) {$A$};
                \\coordinate (H) at (-\\R, 0); \\node[above left] at (H) {$H$};
                \\coordinate (B) at ({\\R*cos(\\ang)}, {\\R*sin(\\ang)}); \\node[above right] at (B) {$B$};
                \\coordinate (C) at ({\\R*cos(2*\\ang)}, {\\R*sin(2*\\ang)}); \\node[above right] at (C) {$C$};
                \\coordinate (D) at ({\\R*cos(3*\\ang)}, {\\R*sin(3*\\ang)}); \\node[above right] at (D) {$D$};
                \\coordinate (G) at ({-\\R*cos(\\ang)}, {\\R*sin(\\ang)}); \\node[above left] at (G) {$G$};
                \\coordinate (F) at ({-\\R*cos(2*\\ang)}, {\\R*sin(2*\\ang)}); \\node[above left] at (F) {$F$};
                \\coordinate (E) at ({-\\R*cos(3*\\ang)}, {\\R*sin(3*\\ang)}); \\node[above left] at (E) {$E$};
                \\foreach \\p in {A,B,C,D,E,F,G,H,O} \\fill (\\p) circle (3pt);
                \\draw (O) -- (B); \\draw (O) -- (C); \\draw (O) -- (D);
                \\draw (O) -- (E); \\draw (O) -- (F); \\draw (O) -- (G);
                \\coordinate (K) at ({\\R*cos(\\ang)}, 0); \\node[below] at (K) {$K$};
                \\draw (B) -- (K) node[midway, right] {$%s$ m};
                \\draw ({\\R*cos(\\ang)}, 0.4) -- ({\\R*cos(\\ang)-0.4}, 0.4) -- ({\\R*cos(\\ang)-0.4}, 0);
                \\coordinate (M) at ({\\R*cos(2*\\ang)}, 0); \\node[below] at (M) {$M$};
                \\coordinate (N) at ({-\\R*cos(2*\\ang)}, 0); \\node[below] at (N) {$N$};
                \\draw[red] (M) -- (C) -- (F) -- (N) -- cycle;
                \\draw ({\\R*cos(2*\\ang)}, 0.4) -- ({\\R*cos(2*\\ang)-0.4}, 0.4) -- ({\\R*cos(2*\\ang)-0.4}, 0);
                \\draw (2,0) arc (0:\\ang:2);
                \\node at ({\\ang/2}:2.5) {$\\alpha$};
                \\end{tikzpicture} }
                \\end{center}''' % (d_str, h_str))

                # Các đáp án trắc nghiệm
                du = ['$%s$'%(kq_str)]
                da = random.choice(du)

                # Câu hỏi
                noidungcauhoi = ('''Đèo Hải Vân là ranh giới tự nhiên của thành phố Đà Nẵng và tỉnh Thừa Thiên-Huế. Hầm được khởi công ngày 27/8/2000 và khánh thành ngày 5/6/2005. Đây là hầm đường bộ dài nhất, hiện đại nhất Đông Nam Á và là một trong 30 đường hầm dài nhất trên thế giới. Trong kiến trúc, có hình nửa đường tròn để có thể chịu lực tốt. Trong hình bên, cổng Đèo Hải Vân được ghép bởi sáu cung vật liệu chịu lực tốt hai bên tạo thành các cung $AB, BC, CD, EF, FG, GH$ bằng nhau và một cung vật liệu chốt ở đỉnh. Cho $AH = %s$ m, $BK = %s$ m. Biết rằng hình chữ nhật $MNFC$ có $MN$ là khoảng cách hai làn xe, $CM$ là chiều cao cho phép của các xe lưu thông (Xem hình minh họa). Chiều cao $CM$ cho phép của các xe lưu thông bằng bao nhiêu? (Kết quả làm tròn đến hàng phần trăm). %s''' 
                                 % (d_str, h_str, tikz_code))

                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = '$' + str(das1) + '$'
                da_s2 = '$' + str(das2) + '$' 
                da_s3 = '$' + str(das3) + '$' 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai=('''Gọi $O$ là tâm của nửa đường tròn, bán kính $R = \\frac{AH}{2} = \\frac{%s}{2} = %s$ m.\\\\
                Từ giả thiết ta có các cung $AB, BC, CD, EF, FG, GH$ bằng nhau nên $\\widehat{AOB} = \\widehat{BOC} = \\widehat{COD} = \\alpha$.\\\\
                Suy ra $\\widehat{AOC} = \\widehat{AOB} + \\widehat{BOC} = 2\\alpha$.\\\\
                Xét $\\triangle OBK$ vuông tại $K$, ta có: $\\sin \\alpha = \\frac{BK}{OB} = \\frac{%s}{%s}$.\\\\
                Suy ra $\\cos \\alpha = \\sqrt{1 - \\sin^2 \\alpha} = \\sqrt{1 - \\left(\\frac{%s}{%s}\\right)^2} = \\frac{\\sqrt{%s}}{%s}$.\\\\
                Xét $\\triangle OCM$ vuông tại $M$, ta có chiều cao $CM$ là:\\\\
                $CM = OC \\cdot \\sin(2\\alpha) = R \\cdot 2 \\sin \\alpha \\cos \\alpha = %s \\cdot 2 \\cdot \\frac{%s}{%s} \\cdot \\frac{\\sqrt{%s}}{%s} \\approx %s$ m.''' 
                         % (d_str, R_str, h_str, R_str, h_str, R_str, diff_sq_str, R_str, R_str, h_str, R_str, diff_sq_str, R_str, kq_str))
                dapan='\\shortans[0]{$%s$}\n'%(kq_str)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content  

