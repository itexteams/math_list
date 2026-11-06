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


def bt_dang13_p3_b2_c7_ds11(self):
            # Khai báo biến
            # Hàm hỗ trợ định dạng số theo chuẩn tiếng Việt (dấu phẩy cho số thập phân)
            def fmt(val):
                if isinstance(val, (int, float)) and val == int(val):
                    return str(int(val))
                return str(val).replace('.', ',')

            # Khai báo và random các biến số đảm bảo logic thực tế (đèn không đập xuống bàn)
            while True:
                H0 = random.randint(2, 5)                       # Độ cao ban đầu của đèn
                vh = random.choice([0.1, 0.2, 0.25, 0.4, 0.5])  # Tốc độ hạ đèn
                t_target = random.choice([1.5, 2, 2.5, 3, 4])   # Thời điểm cần xét
                H1 = round(H0 - vh * t_target, 2)               # Độ cao của đèn tại t_target
                if 0.5 < H1 < H0:                               # Đảm bảo H1 hợp lý
                    break

            vr = random.choice([0.2, 0.25, 0.4, 0.5, 0.6])      # Tốc độ của robot
            k = random.choice([4, 6, 8, 10, 12])                # Hằng số k trong biểu thức căn

            # Khởi tạo biến ký hiệu sympy để tính đạo hàm chính xác
            t = symbols('t')
            h_t = H0 - vh * t
            r_t = vr * t

            # Thiết lập hàm C(t) và tính đạo hàm
            expr_C = sp.sqrt(k) * h_t / ((h_t**2 + r_t**2)**Rational(3, 2))
            dC_dt = diff(expr_C, t)

            # Thay giá trị t_target vào đạo hàm để ra kết quả cuối cùng
            ans_exact = dC_dt.subs(t, t_target).evalf()
            ans_exact_4 = round(float(ans_exact), 4) # Lấy 4 chữ số thập phân mô phỏng bước trung gian
            ans_round = round(float(ans_exact), 1)   # Làm tròn đến hàng phần chục theo yêu cầu đề

            # Xử lý chuỗi hiển thị kết quả gần đúng trong lời giải
            if ans_exact_4 == ans_round:
                eval_str = "= %s" % fmt(ans_round)
            else:
                eval_str = "= %s \\approx %s" % (fmt(ans_exact_4), fmt(ans_round))

            # Xử lý đáp án đúng
            du = ['$%s$' % fmt(ans_round)]
            da = du[0]

            # Tạo các đáp án nhiễu sai khác logic
            s_pool = set()
            s_pool.add(round(-ans_round, 1) if ans_round != 0 else round(ans_round + 0.1, 1))
            s_pool.add(round(ans_round + 0.1, 1))
            s_pool.add(round(ans_round - 0.1, 1))
            s_pool.add(round(ans_round + 0.2, 1))
            s_pool.add(round(ans_round - 0.2, 1))

            # Xóa đáp án đúng khỏi tập nhiễu nếu bị trùng
            if ans_round in s_pool:
                s_pool.remove(ans_round)

            s_list = list(s_pool)
            random.shuffle(s_list)

            das1 = '$%s$' % fmt(s_list[0])
            das2 = '$%s$' % fmt(s_list[1])
            das3 = '$%s$' % fmt(s_list[2])
            hinhve=r'''\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.15 ] (107.4,232.2) .. controls (107.4,221.49) and (129.11,212.8) .. (155.9,212.8) .. controls (182.69,212.8) and (204.4,221.49) .. (204.4,232.2) .. controls (204.4,242.91) and (182.69,251.6) .. (155.9,251.6) .. controls (129.11,251.6) and (107.4,242.91) .. (107.4,232.2) -- cycle ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (151.79,49.73) -- (155.52,45.1) -- (158.08,45.1) -- (161.8,49.73) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (151.79,48) -- (161.8,48) -- (161.8,49.73) -- (151.79,49.73) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (151.79,49.73) -- (161.8,49.73) -- (161.8,51.45) -- (151.79,51.45) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (151.79,51.45) -- (161.8,51.45) -- (161.8,53.18) -- (151.79,53.18) -- cycle ;
            	\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (151.79,53.18) .. controls (156.97,52.84) and (157.21,53.08) .. (161.8,53.18) .. controls (159.38,59.85) and (176.07,67.34) .. (167.36,77.26) .. controls (161.8,82.82) and (151.89,82.34) .. (147.78,77.5) .. controls (138.35,68.31) and (155.03,59.37) .. (151.79,53.18) -- cycle ;
            	\draw    (157.11,53.76) -- (156.72,70) ;
            	\draw    (157.11,53.76) -- (153.58,69.52) ;
            	\draw    (157.11,53.76) -- (160.11,69.76) ;
            	\draw   (154.4,72.33) .. controls (154.4,71.04) and (155.44,70) .. (156.72,70) .. controls (158.01,70) and (159.05,71.04) .. (159.05,72.33) .. controls (159.05,73.61) and (158.01,74.65) .. (156.72,74.65) .. controls (155.44,74.65) and (154.4,73.61) .. (154.4,72.33) -- cycle ;
            	\draw   (157.79,69.76) .. controls (157.79,68.48) and (158.83,67.44) .. (160.11,67.44) .. controls (161.39,67.44) and (162.43,68.48) .. (162.43,69.76) .. controls (162.43,71.04) and (161.39,72.08) .. (160.11,72.08) .. controls (158.83,72.08) and (157.79,71.04) .. (157.79,69.76) -- cycle ;
            	\draw   (151.26,69.52) .. controls (151.26,68.24) and (152.3,67.2) .. (153.58,67.2) .. controls (154.86,67.2) and (155.9,68.24) .. (155.9,69.52) .. controls (155.9,70.8) and (154.86,71.84) .. (153.58,71.84) .. controls (152.3,71.84) and (151.26,70.8) .. (151.26,69.52) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.3 ][fill={rgb, 255:red, 188; green, 117; blue, 55 }  ,fill opacity=1 ] (164.9,198.52) -- (164.9,229.68) .. controls (164.9,232.4) and (160.78,234.6) .. (155.7,234.6) .. controls (150.62,234.6) and (146.5,232.4) .. (146.5,229.68) -- (146.5,198.52) .. controls (146.5,195.8) and (150.62,193.6) .. (155.7,193.6) .. controls (160.78,193.6) and (164.9,195.8) .. (164.9,198.52) .. controls (164.9,201.24) and (160.78,203.44) .. (155.7,203.44) .. controls (150.62,203.44) and (146.5,201.24) .. (146.5,198.52) ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.3 ][fill={rgb, 255:red, 188; green, 117; blue, 55 }  ,fill opacity=1 ] (92.9,183.85) .. controls (92.9,168.8) and (121.11,156.6) .. (155.9,156.6) .. controls (190.69,156.6) and (218.9,168.8) .. (218.9,183.85) .. controls (218.9,198.9) and (190.69,211.1) .. (155.9,211.1) .. controls (121.11,211.1) and (92.9,198.9) .. (92.9,183.85) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.3 ][fill={rgb, 255:red, 227; green, 167; blue, 114 }  ,fill opacity=1 ] (92.9,181.8) .. controls (92.9,167.88) and (121.11,156.6) .. (155.9,156.6) .. controls (190.69,156.6) and (218.9,167.88) .. (218.9,181.8) .. controls (218.9,195.72) and (190.69,207) .. (155.9,207) .. controls (121.11,207) and (92.9,195.72) .. (92.9,181.8) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.38 ] (137.45,182.19) .. controls (137.45,176.71) and (147.74,172.28) .. (160.43,172.28) .. controls (173.11,172.28) and (183.4,176.71) .. (183.4,182.19) .. controls (183.4,187.66) and (173.11,192.1) .. (160.43,192.1) .. controls (147.74,192.1) and (137.45,187.66) .. (137.45,182.19) -- cycle ;
            	\draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (136.45,171.15) .. controls (148.7,164.4) and (164.7,162.4) .. (176.7,173.25) .. controls (176.64,177.44) and (177.05,180.95) .. (175.45,182.65) .. controls (172.95,189.65) and (146.45,193.4) .. (137.45,182.9) .. controls (136.45,179.9) and (135.45,177.15) .. (136.45,171.15) -- cycle ;
            	\draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (135.95,173.25) .. controls (135.95,167.95) and (145.07,163.65) .. (156.33,163.65) .. controls (167.58,163.65) and (176.7,167.95) .. (176.7,173.25) .. controls (176.7,178.55) and (167.58,182.85) .. (156.33,182.85) .. controls (145.07,182.85) and (135.95,178.55) .. (135.95,173.25) -- cycle ;
            	\draw  [fill={rgb, 255:red, 211; green, 203; blue, 203 }  ,fill opacity=1 ] (138.95,172.78) .. controls (138.95,168.7) and (146.79,165.4) .. (156.45,165.4) .. controls (166.11,165.4) and (173.95,168.7) .. (173.95,172.78) .. controls (173.95,176.85) and (166.11,180.15) .. (156.45,180.15) .. controls (146.79,180.15) and (138.95,176.85) .. (138.95,172.78) -- cycle ;
            	\draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (148.7,172.28) .. controls (148.7,170.69) and (152.06,169.4) .. (156.2,169.4) .. controls (160.34,169.4) and (163.7,170.69) .. (163.7,172.28) .. controls (163.7,173.86) and (160.34,175.15) .. (156.2,175.15) .. controls (152.06,175.15) and (148.7,173.86) .. (148.7,172.28) -- cycle ;
            	\draw  [fill={rgb, 255:red, 80; green, 227; blue, 194 }  ,fill opacity=1 ] (152.2,172.28) .. controls (152.2,171.52) and (153.99,170.9) .. (156.2,170.9) .. controls (158.41,170.9) and (160.2,171.52) .. (160.2,172.28) .. controls (160.2,173.03) and (158.41,173.65) .. (156.2,173.65) .. controls (153.99,173.65) and (152.2,173.03) .. (152.2,172.28) -- cycle ;
            	\draw    (139.25,177.95) -- (139.95,185.4) ;
            	\draw    (163.5,181.95) -- (163.7,189.15) ;
            	\draw [line width=0.75]  [dash pattern={on 4.5pt off 4.5pt}]  (156.45,172.78) -- (156.45,65.6) ;
            	\draw [line width=0.75]  [dash pattern={on 4.5pt off 4.5pt}]  (156.45,172.78) -- (213.4,173.1) ;
            	\draw [line width=0.75]    (213.4,173.1) -- (156.9,71.6) ;
            	\draw    (156.8,47.41) -- (156.9,22.6) ;
            	\draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (89,15.4) -- (225.4,15.4) -- (225.4,22) -- (89,22) -- cycle ;
            	\draw    (196.4,172.4) .. controls (193.4,164.4) and (196.6,157.3) .. (204.4,156.9) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.26 ] (155.7,211.1) -- (163.4,211.1) -- (163.4,233.6) -- (155.7,233.6) -- cycle ;
            	\draw (112.2,110) node [anchor=north west][inner sep=0.75pt]    {$h( m)$};
            	\draw (190.2,94.5) node [anchor=north west][inner sep=0.75pt]    {$x( m)$};
            	\draw (182.2,141.5) node [anchor=north west][inner sep=0.75pt]    {$\alpha $};
            	\draw (182.7,174) node [anchor=north west][inner sep=0.75pt]    {$1m$};
            \end{tikzpicture}'''
            # Câu hỏi
            noidungcauhoi = (r'''\immini{Một bóng đèn được treo phía trên và chính giữa một cái bàn hình tròn có bán kính cố định bằng $1$ mét. Trên mặt bàn có một robot hút bụi hình tròn đang hoạt động. Tại thời điểm ban đầu ($t = 0$), bóng đèn ở độ cao $h = %s$ và bắt đầu được hạ xuống với tốc độ không đổi là $%s$ m/s. Cùng lúc đó, robot bắt đầu di chuyển từ tâm bàn ra phía mép bàn với tốc độ không đổi là $%s$ m/s. Cường độ sáng mà robot nhận được tại một thời điểm bất kỳ phụ thuộc vào góc nghiêng và khoảng cách từ đèn đến robot được cho bởi công thức $C(x) = \sqrt{%s} \cdot \frac{\\sin \alpha}{x^2}$. Hãy tính tốc độ thay đổi của cường độ sáng mà robot nhận được tại thời điểm bóng đèn ở độ cao $%s$ mét (Kết quả làm tròn đến hàng phần chục).}{%s}''' 
            % (fmt(H0), fmt(vh), fmt(vr), k, fmt(H1), hinhve))

            # Các đáp án trộn ngẫu nhiên
            da_d = ('\\True ' + str(da))
            da_s1 = str(das1)
            da_s2 = str(das2)
            da_s3 = str(das3)

            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Lời giải chi tiết
            loigiai = ('''Ta có: $r(t) = %st$ và $x(t) = \\sqrt{h^2(t) + r^2(t)}$ mà $h(t) = %s - %st$\\\\
            Theo bài ra: $h(t) = %s \\Leftrightarrow %s - %st = %s \\Rightarrow t = %s$ nên $C(t) = \\frac{\\sqrt{%s} \\cdot \\sin \\alpha}{x^2} = \\sqrt{%s} \\cdot \\frac{\\frac{h(t)}{x(t)}}{h^2(t) + r^2(t)}$\\\\
            $\\Leftrightarrow C(t) = \\sqrt{%s} \\cdot \\frac{\\frac{%s - %st}{\\sqrt{(%s - %st)^2 + (%st)^2}}}{(%s - %st)^2 + (%st)^2} = \\sqrt{%s} \\cdot \\frac{%s - %st}{\\left(\\sqrt{(%s - %st)^2 + (%st)^2}\\right)^3} \\\\= \\sqrt{%s} \\cdot \\frac{%s - %st}{\\left[ (%s - %st)^2 + (%st)^2 \\right]^{\\frac{3}{2}}}$\\\\
            Khi đó: $C'(%s) = \\frac{d}{dt} \\left[ \\sqrt{%s} \\cdot \\frac{%s - %st}{\\left[ (%s - %st)^2 + (%st)^2 \\right]^{\\frac{3}{2}}} \\right]_{t=%s} %s$\\\\
            Vậy tốc độ thay đổi của cường độ sáng mà robot nhận được tại thời điểm bóng đèn ở độ cao $%s$ mét bằng $%s$ (m/s).''' 
            % (fmt(vr), fmt(H0), fmt(vh), 
               fmt(H1), fmt(H0), fmt(vh), fmt(H1), fmt(t_target), k, k,
               k, fmt(H0), fmt(vh), fmt(H0), fmt(vh), fmt(vr), fmt(H0), fmt(vh), fmt(vr), k, fmt(H0), fmt(vh), fmt(H0), fmt(vh), fmt(vr), k, fmt(H0), fmt(vh), fmt(H0), fmt(vh), fmt(vr),
               fmt(t_target), k, fmt(H0), fmt(vh), fmt(H0), fmt(vh), fmt(vr), fmt(t_target), eval_str,
               fmt(H1), fmt(ans_round)))
            dapan='\\shortans[0]{$%s$}\n'%(fmt(ans_round))

            # Xuất kết quả
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content  

