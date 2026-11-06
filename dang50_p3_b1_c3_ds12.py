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


def bt_dang50_p3_b1_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến và Random các số liệu đảm bảo logic bài toán
            while True:
                T_env = random.choice([20, 22, 24, 25, 26, 28, 30])  # Nhiệt độ môi trường
                A = random.choice([30, 40, 50, 60])                  # Chênh lệch nhiệt độ lúc t=0
                T0 = T_env + A                                       # Nhiệt độ tại t=0

                R_num = random.choice([10, 15, 20, 25, 30])          # Chênh lệch nhiệt độ lúc t=1
                if R_num >= A:                                       # Nhiệt độ sau 1 giờ phải giảm
                    continue
                T1 = T_env + R_num                                   # Nhiệt độ tại t=1

                T_init = random.choice([85, 90, 95, 100])            # Nhiệt độ lúc mới pha
                if T_init <= T0:                                     # Lúc mới pha phải nóng hơn lúc t=0
                    continue

                t_hour = random.choice([8, 9, 10, 14, 15])           # Giờ bắt đầu đo
                break

            # Tính toán các hệ số (sử dụng số thực để tính toán toán học)
            e_k_val = R_num / A
            target_val = (T_init - T_env) / A
            t_val = math.log(target_val, e_k_val)

            # Chuyển đổi các hệ số sang định dạng phân số cho chuỗi LaTeX
            e_k_tex = latex(Rational(R_num, A))
            target_tex = latex(Rational(T_init - T_env, A))

            # Làm tròn thời gian theo chuẩn lời giải mẫu
            t_approx = round(t_val, 6)
            abs_t_approx = abs(t_approx)
            t_mins_approx = round(abs_t_approx * 60, 2)
            ans_round = round(t_mins_approx)

            # Hàm hỗ trợ hiển thị số có dấu phẩy cho số thập phân và bỏ phần thập phân nếu là số nguyên
            def fmt(x):
                if int(x) == x:
                    return str(int(x))
                return str(x).replace('.', ',')

            # Các đáp án trắc nghiệm
            du = ['$%s$' % (ans_round)]
            da = du[0]

            # Tạo các đáp án nhiễu sai khác với đáp án đúng
            s_pool = set()
            while len(s_pool) < 3:
                sai = ans_round + random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
                if sai > 0 and sai != ans_round:
                    s_pool.add(sai)

            s_list = list(s_pool)
            random.shuffle(s_list)

            das1 = '$%s$' % s_list[0]
            das2 = '$%s$' % s_list[1]
            das3 = '$%s$' % s_list[2]

            # Đưa các đáp án vào danh sách chọn ngẫu nhiên
            list_1 = ['\\True ' + str(da), str(das1), str(das2), str(das3)]
            random.shuffle(list_1)
            hinhve=r'''\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.53 ] (199.44,238.34) .. controls (199.44,227.97) and (223.53,219.56) .. (253.24,219.56) .. controls (282.95,219.56) and (307.04,227.97) .. (307.04,238.34) .. controls (307.04,248.71) and (282.95,257.12) .. (253.24,257.12) .. controls (223.53,257.12) and (199.44,248.71) .. (199.44,238.34) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.45 ][fill={rgb, 255:red, 201; green, 223; blue, 227 }  ,fill opacity=0.4 ] (198.5,228.1) .. controls (199.31,211.88) and (297.05,233.2) .. (298.35,228.9) .. controls (296.3,227.2) and (297.9,204.6) .. (297.29,236.28) .. controls (297.35,253.65) and (198.85,258.15) .. (198.5,236.28) .. controls (198.9,212.1) and (198.35,236.4) .. (198.5,228.1) -- cycle ;
            	\draw  [fill={rgb, 255:red, 234; green, 245; blue, 247 }  ,fill opacity=1 ] (198.5,228.1) .. controls (198.5,221.2) and (220.62,215.6) .. (247.9,215.6) .. controls (275.18,215.6) and (297.29,221.2) .. (297.29,228.1) .. controls (297.29,235) and (275.18,240.6) .. (247.9,240.6) .. controls (220.62,240.6) and (198.5,235) .. (198.5,228.1) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.51 ][fill={rgb, 255:red, 201; green, 223; blue, 227 }  ,fill opacity=0.4 ] (199.09,127.32) .. controls (199.9,111.1) and (298.9,111.1) .. (297.88,127.32) .. controls (297.9,162.6) and (297.9,196.1) .. (297.29,227.78) .. controls (296.9,243.6) and (198.9,246.1) .. (198.5,227.78) .. controls (199.4,195.1) and (198.4,158.6) .. (199.09,127.32) -- cycle ;
            	\draw  [fill={rgb, 255:red, 254; green, 3; blue, 31 }  ,fill opacity=1 ] (302.83,67.31) .. controls (303.88,65) and (306.61,63.98) .. (308.92,65.03) -- (312.74,66.77) .. controls (315.06,67.82) and (316.08,70.55) .. (315.03,72.86) -- (307.17,90.14) .. controls (307.17,90.14) and (307.17,90.14) .. (307.17,90.14) -- (294.98,84.6) .. controls (294.98,84.6) and (294.98,84.6) .. (294.98,84.6) -- cycle ;
            	\draw  [fill={rgb, 255:red, 237; green, 233; blue, 233 }  ,fill opacity=1 ] (294.98,84.6) -- (307.17,90.14) -- (265.98,180.79) -- (253.78,175.24) -- cycle ;
            	\draw  [fill={rgb, 255:red, 237; green, 233; blue, 233 }  ,fill opacity=1 ] (265.98,180.79) -- (251.45,203.04) -- (246.57,200.83) -- (253.78,175.24) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (245.58,216.15) .. controls (244.96,217.51) and (243.35,218.12) .. (241.98,217.5) -- (241.98,217.5) .. controls (240.61,216.88) and (240.01,215.26) .. (240.63,213.9) -- (246.57,200.83) .. controls (246.57,200.83) and (246.57,200.83) .. (246.57,200.83) -- (251.52,203.08) .. controls (251.52,203.08) and (251.52,203.08) .. (251.52,203.08) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 247; green, 7; blue, 36 }  ,fill opacity=1 ] (298.5,91.32) -- (300.16,92.07) -- (250.03,202.4) -- (248.36,201.64) -- cycle ;
            	\draw    (280.48,132.69) -- (286.2,135.51) ;
            	\draw    (270.04,156.45) -- (275.76,159.26) ;
            	\draw    (290.4,110.87) -- (296.11,113.68) ;
            	\draw    (280.07,117.72) -- (285.79,120.53) ;
            	\draw    (269.17,140.9) -- (274.89,143.72) ;
            	\draw  [draw opacity=0] (295.35,93.13) -- (301.33,95.85) -- (263.18,179.8) -- (257.2,177.09) -- cycle ; \draw   (295.35,93.13) -- (257.2,177.09)(300.73,95.58) -- (262.58,179.53) ; \draw   (295.35,93.13) -- (301.33,95.85)(292.91,98.52) -- (298.89,101.23)(290.46,103.9) -- (296.44,106.62)(288.02,109.28) -- (293.99,112)(285.57,114.66) -- (291.55,117.38)(283.12,120.04) -- (289.1,122.76)(280.68,125.42) -- (286.66,128.14)(278.23,130.81) -- (284.21,133.52)(275.79,136.19) -- (281.77,138.9)(273.34,141.57) -- (279.32,144.29)(270.9,146.95) -- (276.87,149.67)(268.45,152.33) -- (274.43,155.05)(266,157.71) -- (271.98,160.43)(263.56,163.09) -- (269.54,165.81)(261.11,168.48) -- (267.09,171.19)(258.67,173.86) -- (264.65,176.58) ; \draw    ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (304.67,66.76) -- (281.07,117.72) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 238; green, 248; blue, 28 }  ,fill opacity=0.43 ] (198.9,165.6) .. controls (203.21,152.38) and (297.42,152.38) .. (296.9,164.6) .. controls (296.92,199.88) and (297.9,196.1) .. (297.29,227.78) .. controls (293.9,240.6) and (213.9,251.1) .. (198.5,227.78) .. controls (199.4,195.1) and (198.21,196.88) .. (198.9,165.6) -- cycle ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.51 ]   (199.09,127.32) .. controls (199.9,147.6) and (298.4,148.1) .. (297.88,127.32) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.52 ]   (199.09,168.82) .. controls (199.9,189.1) and (298.4,189.6) .. (297.88,168.82) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.38 ] (208.24,137.52) -- (201.44,133.76) -- (201.84,242.72) -- (208.24,245.52) -- cycle ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (199.49,128.42) .. controls (200.3,148.7) and (299.16,148.7) .. (298.64,127.92) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (200.04,131.52) -- (199.5,228.1) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (295.83,132.52) -- (295.29,229.1) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.24 ] (212.9,228.1) .. controls (212.9,223.89) and (228.57,220.48) .. (247.9,220.48) .. controls (267.23,220.48) and (282.9,223.89) .. (282.9,228.1) .. controls (282.9,232.31) and (267.23,235.72) .. (247.9,235.72) .. controls (228.57,235.72) and (212.9,232.31) .. (212.9,228.1) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.3 ] (239.64,169.74) .. controls (243.56,168.17) and (246.57,166.59) .. (276.71,167.59) .. controls (252.75,166.84) and (230.15,170.23) .. (252.75,177.92) .. controls (237.83,176.27) and (233.31,172.63) .. (239.64,169.74) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.18 ] (297.04,230.72) -- (285.44,236.32) -- (284.64,246.32) -- (295.83,240.52) -- cycle ;
            \end{tikzpicture}'''
            # Câu hỏi
            noidungcauhoi = (r'''\immini{Trong giờ sinh hoạt STEM, các bạn học sinh thực hiện một thí nghiệm về sự tỏa nhiệt. Một ly trà nóng vừa được pha xong với nhiệt độ ban đầu là $%s^\circ\text{C}$ và đặt lên bàn trong phòng thí nghiệm có nhiệt độ không đổi là $%s^\circ\text{C}$. Các bạn bắt đầu bấm đồng hồ đo đạc lúc $%s$ giờ đúng. Lúc này nhiệt độ của ly trà đo được là $%s^\circ\text{C}$. Đúng 1 giờ sau, nhiệt độ của ly trà đo được giảm xuống còn $%s^\circ\text{C}$. Biết rằng tốc độ thay đổi nhiệt độ của vật thể tỉ lệ thuận với sự chênh lệch nhiệt độ giữa vật thể và môi trường. Hỏi cốc trà được pha trước lúc các bạn học sinh bắt đầu bấm giờ bao nhiêu phút (Kết quả làm tròn đến hàng đơn vị).}{%s}'''
            % (fmt(T_init), fmt(T_env), t_hour, fmt(T0), fmt(T1),hinhve))

            # Nội dung lời giải (Đã bọc \left( \right) quanh các biến phân số để LaTeX hiển thị đẹp hơn)
            loigiai = ('''Gọi $T(t)$ là nhiệt độ của ly trà tại thời điểm $t$ (giờ) và nhiệt độ của môi trường là $%s^\\circ\\text{C}$\\\\
            Tốc độ thay đổi nhiệt độ của vật thể tỉ lệ thuận với sự chênh lệch nhiệt độ giữa vật thể và môi trường nên $\\frac{T'(t)}{(T(t)-%s)} = k \\Leftrightarrow T'(t) = k(T(t)-%s)$ (trong đó $k$ là hằng số tỷ lệ)\\\\
            Ta đã biết $T'(t) = \\frac{dT}{dt}$ nên phương trình trở thành $\\frac{dT}{dt} = k(T-%s)$\\\\
            Lấy nguyên hàm hai vế: \\\\ $\\int \\frac{1}{(T-%s)} \\text{d}(T) = \\int k \\text{d}t \\Rightarrow \\ln|T-%s| = kt + C \\Leftrightarrow |T-%s| = e^{kt+C} = e^{kt} \\cdot e^C$\\\\
            Do nhiệt độ của ly trà luôn hơn hoặc bằng nhiệt độ của môi trường nên $T - %s \\ge 0$ nên ta có thể phá dấu trị tuyệt đối: $T - %s = e^C \\cdot e^{kt}$\\\\
            Đặt $A = e^C$ (Với $A$ là một hằng số dương tùy ý) suy ra $T(t) - %s = A \\cdot e^{kt} \\Leftrightarrow T(t) = %s + A \\cdot e^{kt}$\\\\
            Tại $t = 0$ ($%s$ giờ) thì $T = %s$ nên $%s = %s + A \\cdot e^{k \\cdot 0} \\Rightarrow %s = %s + A \\Rightarrow A = %s$\\\\
            Tại $t = 1$ ($%s$ giờ) thì $T = %s$ nên $%s = %s + %s \\cdot e^{k \\cdot 1} \\Rightarrow %s = %s + %s \\cdot e^k \\Leftrightarrow %s = %s \\cdot e^k \\Rightarrow e^k = %s$\\\\
            Vậy lúc này phương trình $T(t) = %s + %s \\cdot (e^k)^t = %s + %s \\cdot \\left(%s\\right)^t$\\\\
            Nhiệt độ lúc pha trà là $%s^\\circ\\text{C}$ nên $%s = %s + %s \\cdot \\left(%s\\right)^t \\Rightarrow \\left(%s\\right)^t = %s \\Rightarrow t = \\log_{%s}\\left(%s\\right)$\\\\
            Khi $t = \\log_{%s}\\left(%s\\right) \\approx %s$ (dấu âm thể hiện thời điểm pha trà nằm trước mốc thời gian $t = 0$, tức là trước $%s$ giờ)\\\\
            Đổi sang phút ta có $%s \\cdot 60 \\approx %s$ (phút) nên cốc trà được pha trước lúc bấm giờ $%s$ phút.'''
            % (fmt(T_env), 
               fmt(T_env), fmt(T_env), 
               fmt(T_env), 
               fmt(T_env), fmt(T_env), fmt(T_env), 
               fmt(T_env), fmt(T_env), 
               fmt(T_env), fmt(T_env), 
               t_hour, fmt(T0), fmt(T0), fmt(T_env), fmt(T0), fmt(T_env), fmt(A), 
               t_hour + 1, fmt(T1), fmt(T1), fmt(T_env), fmt(A), fmt(T1), fmt(T_env), fmt(A), fmt(R_num), fmt(A), e_k_tex, 
               fmt(T_env), fmt(A), fmt(T_env), fmt(A), e_k_tex, 
               fmt(T_init), fmt(T_init), fmt(T_env), fmt(A), e_k_tex, e_k_tex, target_tex, e_k_tex, target_tex, 
               e_k_tex, target_tex, fmt(t_approx), t_hour, 
               fmt(abs_t_approx), fmt(t_mins_approx), ans_round))
            dapan='\\shortans[0]{$%s$}\n'%(ans_round)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content  

