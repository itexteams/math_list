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


def bt_dang47_p3_b6_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random các thông số bài toán
                # hp: chiều cao phần chóp ngập trong nước (SO)
                # k: mẫu số của phần thể tích nước còn lại (ví dụ k=3 thì nước chiếm 2/3)
                hp = random.choice([2, 3, 4, 5])
                k = random.choice([3, 4, 5])
                h = hp * k                # Chiều cao của ly nước
                tu_so = k - 1             # Tử số phần thể tích nước
                mau_so = k                # Mẫu số phần thể tích nước

                # Tính toán kết quả
                # Thể tích khối chóp S.ABC: V = (hp^3 * sqrt(3)) / 2
                V_val = (hp**3 * math.sqrt(3)) / 2
                kq_dec = Decimal(float(V_val)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                kq_str = str(kq_dec).replace('.', ',')
                kq_float = round(V_val, 1)

                # Các đáp án trắc nghiệm
                du = ['$%s$' % (kq_str)]
                da = random.choice(du)

                # Sinh các phương án nhiễu (sai)
                s = []
                offsets = [0.1, -0.1, 1.0, -1.0, 2.0, -2.0, 3.0]
                for off in offsets:
                    val = kq_float + off
                    if val > 0:
                        val_str = str(Decimal(float(val)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ',')
                        if '$%s$' % val_str not in s and val_str != kq_str:
                            s.append('$%s$' % val_str)

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                hinhve=r'''\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.46 ] (182.33,245.61) .. controls (182.33,237.88) and (202.53,231.62) .. (227.46,231.62) .. controls (252.39,231.62) and (272.6,237.88) .. (272.6,245.61) .. controls (272.6,253.34) and (252.39,259.6) .. (227.46,259.6) .. controls (202.53,259.6) and (182.33,253.34) .. (182.33,245.61) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.3 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (189.58,227.81) .. controls (223.53,224.4) and (241.4,226.08) .. (266.52,227.75) .. controls (265.85,233.74) and (265.73,238.87) .. (266.1,243.37) .. controls (258.71,256.79) and (195.63,257.53) .. (190.33,242.82) .. controls (190.2,238.08) and (190.01,233.13) .. (189.58,227.81) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.3 ][fill={rgb, 255:red, 216; green, 228; blue, 240 }  ,fill opacity=1 ] (183.89,142.79) .. controls (188.35,131.06) and (265.97,132.18) .. (272.11,141.11) .. controls (271.43,147.1) and (263.67,223.25) .. (264.03,227.75) .. controls (259.84,241.24) and (198.07,244.32) .. (192.37,229.15) .. controls (192.25,224.41) and (184.31,148.11) .. (183.89,142.79) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.3 ][fill={rgb, 255:red, 245; green, 186; blue, 35 }  ,fill opacity=0.54 ] (227.55,39.64) -- (281.6,76.99) -- (229.11,116.08) -- (172.72,76.44) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.3 ] (189.58,227.81) -- (197.96,236.59) -- (198.42,250.09) -- (190.33,242.82) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.3 ] (254.72,237.06) -- (265.63,229.88) -- (266.1,243.37) -- (254.72,250.09) -- cycle ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.3 ][line width=1.5]    (190.33,245.61) .. controls (197.49,257.53) and (257.52,256.13) .. (266.1,243.37) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (189.58,227.81) .. controls (191.44,244.97) and (257.03,247.85) .. (266.52,227.75) ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.3 ][fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (186.79,167.73) .. controls (191.26,156) and (263.01,155.54) .. (269.15,164.47) .. controls (268.48,170.46) and (263.67,223.25) .. (264.03,227.75) .. controls (259.84,241.24) and (198.07,244.32) .. (192.37,229.15) .. controls (192.25,224.41) and (187.22,173.05) .. (186.79,167.73) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.3 ][fill={rgb, 255:red, 245; green, 179; blue, 35 }  ,fill opacity=0.78 ] (172.72,76.44) -- (229.11,116.08) -- (228,165.21) -- (176.07,126.13) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.3 ][fill={rgb, 255:red, 245; green, 201; blue, 35 }  ,fill opacity=0.84 ] (281.6,76.99) -- (279.92,126.13) -- (228,165.21) -- (229.11,116.08) -- cycle ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.36 ]   (183.89,142.79) .. controls (185.75,159.95) and (262.62,161.21) .. (272.11,141.11) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.23 ]   (192.37,229.15) .. controls (199.82,224.49) and (257.98,224.03) .. (264.03,227.75) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.51 ] (205.77,231.71) .. controls (205.77,230.55) and (215.27,229.61) .. (226.99,229.61) .. controls (238.71,229.61) and (248.21,230.55) .. (248.21,231.71) .. controls (248.21,232.86) and (238.71,233.8) .. (226.99,233.8) .. controls (215.27,233.8) and (205.77,232.86) .. (205.77,231.71) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 210; green, 196; blue, 31 }  ,fill opacity=1 ] (263.57,172.85) -- (269.61,166.8) -- (264.03,227.75) -- (259.38,233.33) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 210; green, 196; blue, 31 }  ,fill opacity=1 ] (186.79,167.73) -- (192.37,174.24) -- (198.42,233.8) -- (192.37,229.15) -- cycle ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.53 ]   (186.79,167.73) .. controls (185.39,183.08) and (264.5,181.22) .. (269.61,166.8) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.14 ] (200.75,164.47) .. controls (208.31,160.69) and (252.53,158.16) .. (261.24,166.8) .. controls (257.52,225.89) and (269.15,243.11) .. (205.77,231.71) .. controls (203.54,233.33) and (203.08,199.83) .. (200.75,164.47) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=0.36 ] (249.79,158.89) .. controls (266.36,164.94) and (261.24,164.47) .. (261.24,166.8) .. controls (263.31,170.04) and (262.17,169.12) .. (255.65,172.85) .. controls (259.05,174.01) and (272.63,169.38) .. (269.61,166.8) .. controls (268.22,163.54) and (258.91,157.96) .. (249.79,158.89) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.41 ] (190.51,151.91) -- (196.56,154.7) -- (202.61,228.68) -- (197.03,228.22) -- cycle ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.5 ]   (270.54,145.86) -- (262.63,227.75) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.5 ]   (186.79,149.58) -- (194.24,230.54) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.61 ]   (184,145.86) .. controls (200.75,164.94) and (267.75,157.03) .. (270.54,144.46) ;
            	\draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.36 ][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.29 ] (228,169.03) .. controls (228.24,169.03) and (228.4,169.06) .. (228.53,169.11) .. controls (228.67,169.17) and (228.71,169.23) .. (228.62,169.31) .. controls (228.51,169.39) and (228.32,169.46) .. (228,169.51) .. controls (227.66,169.57) and (227.23,169.59) .. (226.76,169.58) .. controls (226.25,169.57) and (225.74,169.52) .. (225.31,169.43) .. controls (224.81,169.33) and (224.49,169.19) .. (224.27,169.03) .. controls (224.06,168.85) and (224.03,168.67) .. (224.24,168.47) .. controls (224.45,168.27) and (224.88,168.08) .. (225.52,167.93) .. controls (226.21,167.76) and (227.03,167.65) .. (228,167.6) .. controls (229.02,167.54) and (230.08,167.56) .. (231.1,167.65) .. controls (232.18,167.75) and (233.12,167.92) .. (233.91,168.16) .. controls (234.72,168.41) and (235.23,168.7) .. (235.44,169.03) .. controls (235.66,169.38) and (235.5,169.73) .. (234.98,170.06) .. controls (234.45,170.42) and (233.55,170.72) .. (232.34,170.96) .. controls (231.09,171.21) and (229.61,171.36) .. (228,171.42) .. controls (226.29,171.47) and (224.65,171.41) .. (223.03,171.23) .. controls (221.37,171.05) and (219.97,170.77) .. (218.86,170.38) .. controls (217.7,169.98) and (217.04,169.53) .. (216.83,169.03) .. controls (216.61,168.51) and (216.92,168.01) .. (217.79,167.52) .. controls (218.68,167.02) and (220,166.6) .. (221.79,166.28) .. controls (223.64,165.94) and (225.7,165.75) .. (228,165.69) .. controls (230.35,165.64) and (232.65,165.74) .. (234.82,166) .. controls (237.06,166.27) and (238.94,166.67) .. (240.36,167.2) .. controls (241.83,167.75) and (242.68,168.36) .. (242.89,169.03) .. controls (242.89,169.03) and (242.89,169.03) .. (242.89,169.03) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.5 ]   (174.12,75.04) -- (230.51,114.68) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.5 ]   (230.51,113.29) -- (281.6,75.6) ;
            	\draw [color={rgb, 255:red, 220; green, 217; blue, 217 }  ,draw opacity=1 ]   (227.72,116.08) -- (226.36,163.54) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.1 ]   (176.07,126.13) -- (207.26,101.66) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.1 ]   (279.92,126.13) -- (246.81,103.98) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.35 ] (227.55,39.64) -- (281.6,75.6) -- (198.42,94.21) -- (172.72,76.44) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.35 ] (172.72,76.44) -- (185.57,85.32) -- (202.03,145.67) -- (176.07,126.13) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.17 ] (229.11,116.08) -- (258.91,94.21) -- (246.35,151.44) -- (228,165.21) -- cycle ;
            	\draw [color={rgb, 255:red, 248; green, 196; blue, 114 }  ,draw opacity=0.39 ]   (174.12,75.04) -- (227.55,39.64) ;
            	\draw [color={rgb, 255:red, 248; green, 196; blue, 114 }  ,draw opacity=0.13 ]   (281.6,75.6) -- (227.55,39.64) ;
            \end{tikzpicture}'''
                # Câu hỏi
                noidungcauhoi = (r'''\immini{Một cái ly nước hình trụ có chiều cao $%s$ cm. Lượng nước trong ly chiếm $\frac{%s}{%s}$ thể tích ly nước. An đặt một viên đá hình lập phương vào miệng ly nước thì thấy một đỉnh của viên đá chạm vào mặt nước và đồng thời mô hình ly nước và đá cùng lấy trục ly nước làm trục đối xứng. Nếu ban đầu An đổ nước đầy ly thì sau khi đặt khối lập phương như trên thì lượng nước tràn ra là bao nhiêu cm$^3$? (Kết quả làm tròn đến hàng phần chục và bỏ qua độ dày của ly).}{%s}'''
                                 % (h, tu_so, mau_so, hinhve))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''\\begin{center}
            \\begin{tikzpicture}[scale=1, line width=1pt, line join=round, line cap=round]
            \\coordinate (A) at (-2.5, 0.8);
            \\coordinate (B) at (-0.5, -1.5);
            \\coordinate (C) at (2.5, 0.8);
            \\coordinate (H) at (1, -0.35);
            \\coordinate (O) at (0, 0.1);
            \\coordinate (S) at (0, 4);
            \\draw[dashed] (A) -- (C);
            \\draw[dashed] (A) -- (H);
            \\draw[dashed] (S) -- (O);
            \\draw (S) -- (A);
            \\draw (S) -- (B);
            \\draw (S) -- (C);
            \\draw (A) -- (B) -- (C);
            \\fill (A) circle (1.5pt) node[left] {$A$};
            \\fill (B) circle (1.5pt) node[below] {$B$};
            \\fill (C) circle (1.5pt) node[right] {$C$};
            \\fill (S) circle (1.5pt) node[above] {$S$};
            \\fill (H) circle (1.5pt) node[below right] {$H$};
            \\fill (O) circle (1.5pt) node[below] {$O$};
            \\draw[dashed] (0, 0.4) -- (0.25, 0.3) -- (0.25, 0);
            \\end{tikzpicture}
            \\end{center}
            Xét hình chóp tam giác đều $S.ABC$ trong đó $S$ là đỉnh của hình lập phương nằm bên trong ly nước và $A, B, C$ là các điểm chung của đá với miệng ly; $O$ là trọng tâm tam giác $ABC$ và $H$ là trung điểm $BC$.\\\\
            Đặt $x$ (cm) là cạnh đáy hình chóp thì $AO = \\frac{2}{3}AH = \\frac{2}{3} \\cdot \\frac{x\\sqrt{3}}{2} = \\frac{x\\sqrt{3}}{3}$.\\\\
            Vì hình chóp $S.ABC$ có $SA, SB, SC$ bằng nhau và đôi một vuông góc tại đỉnh $S$ nên độ dài cạnh $SA = SB = SC = \\frac{x}{\\sqrt{2}}$.\\\\
            Từ đó suy ra $SO = \\sqrt{SA^2 - OA^2} = \\sqrt{\\frac{x^2}{2} - \\frac{x^2}{3}} = \\frac{x\\sqrt{6}}{6}$.\\\\
            Theo giả thiết thì chiều cao hình chóp $S.ABC$ bằng $\\frac{1}{%s}$ chiều cao ly nước: $SO = \\frac{1}{%s} \\cdot %s = %s$ (cm).\\\\
            Suy ra chiều dài cạnh đáy của hình chóp: $\\frac{x\\sqrt{6}}{6} = %s \\Rightarrow x = %s\\sqrt{6}$ (cm).\\\\
            Vậy thể tích nước tràn ra bằng với thể tích khối chóp $S.ABC$.\\\\
            Thể tích đó là: $V = \\frac{1}{3}SO \\cdot S_{ABC} = \\frac{1}{3} \\cdot %s \\cdot \\frac{(%s\\sqrt{6})^2\\sqrt{3}}{4} = \\frac{%s\\sqrt{3}}{2} \\approx %s$ (cm$^3$).'''
                           % (mau_so, mau_so, h, hp, hp, hp, hp, hp, hp**3, kq_str))
                dapan='\\shortans[0]{$%s$}\n'%(kq_str)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                       '\\loigiai{'+str(loigiai)+'}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

