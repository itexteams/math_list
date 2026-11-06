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


def bt_dang4_p3_b2_c7_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random các thông số của bài toán
                r_val = random.choice([2, 3, 4, 5])

                # Đảm bảo chiều dài thanh truyền lớn hơn bán kính quay một khoảng hợp lý
                l_val = random.choice([7, 8, 9, 10, 11, 12])
                while l_val <= r_val + 2:
                    l_val = random.choice([7, 8, 9, 10, 11, 12])

                v_rpm = random.choice([100, 150, 200, 250, 300])

                # Chọn ngẫu nhiên một góc đẹp để tính toán exact math
                theta_choices = [
                    ('\\frac{\\pi}{6}', pi/6),
                    ('\\frac{\\pi}{4}', pi/4),
                    ('\\frac{\\pi}{3}', pi/3)
                ]
                theta_val_str, theta_sym = random.choice(theta_choices)

                # Sử dụng Sympy để thiết lập và tính đạo hàm chính xác
                theta = sp.Symbol('theta')
                # Phương trình vị trí x của pít-tông
                x_expr = r_val * sp.cos(theta) + sp.sqrt(l_val**2 - r_val**2 * sp.sin(theta)**2)
                # Đạo hàm của x theo theta
                dxdtheta_expr = sp.diff(x_expr, theta)

                # Tốc độ góc d(theta)/dt = v_rpm * 2pi
                dthetadt = v_rpm * 2 * pi
                # Vận tốc của pít-tông
                v_expr = dxdtheta_expr * dthetadt

                # Thay giá trị cụ thể của theta vào
                dxdtheta_at_val = sp.simplify(dxdtheta_expr.subs(theta, theta_sym))
                v_at_val = sp.simplify(v_expr.subs(theta, theta_sym))

                # Tính giá trị xấp xỉ và làm tròn đến hàng đơn vị
                final_speed = abs(v_at_val.evalf())
                kq_int = int(sp.Number(final_speed).round())
                kq = str(kq_int).replace('.', ',')

                # Các đáp án trắc nghiệm
                du = ['$%s$' % (kq)]
                da = random.choice(du)

                # Tạo các phương án sai (đảm bảo không trùng với đáp án đúng)
                s_raw = [
                    kq_int + random.randint(10, 50),
                    abs(kq_int - random.randint(15, 60)),
                    kq_int + random.randint(100, 250),
                    abs(kq_int - random.randint(80, 200)),
                    kq_int + random.randint(1, 9),
                    abs(kq_int - random.randint(1, 9))
                ]

                s = []
                for val in s_raw:
                    s.append('$%s$' % (str(val).replace('.', ',')))

                # Lọc trùng lặp và loại bỏ đáp án đúng nếu vô tình bị trùng
                s = list(set(s))
                if f"${kq}$" in s:
                    s.remove(f"${kq}$")

                random.shuffle(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                hinhve=r'''\tikzset {_q85v5nl0y/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{-122 }  \pgftransformscale{2 }  }}}
            \pgfdeclarehorizontalshading{_g3kq4n1v0}{150bp}{rgb(0bp)=(0.5,0.5,0.5);
            	rgb(43.3749989100865bp)=(0.5,0.5,0.5);
            	rgb(50bp)=(1,1,1);
            	rgb(54.53571319580078bp)=(0.5,0.5,0.5);
            	rgb(100bp)=(0.5,0.5,0.5)}
            \tikzset {_4tmqz12pm/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{-30 }  \pgftransformscale{2 }  }}}
            \pgfdeclarehorizontalshading{_fgrb6muqf}{150bp}{rgb(0bp)=(0.61,0.61,0.61);
            	rgb(37.5bp)=(0.61,0.61,0.61);
            	rgb(50bp)=(1,1,1);
            	rgb(62.5bp)=(0.61,0.61,0.61);
            	rgb(100bp)=(0.61,0.61,0.61)}
            \tikzset {_7iiahu01b/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{-40 }  \pgftransformscale{2 }  }}}
            \pgfdeclarehorizontalshading{_uscupb3nw}{150bp}{rgb(0bp)=(0.61,0.61,0.61);
            	rgb(37.5bp)=(0.61,0.61,0.61);
            	rgb(43.28571319580078bp)=(0.61,0.61,0.61);
            	rgb(50bp)=(1,1,1);
            	rgb(57.571427481515066bp)=(0.61,0.61,0.61);
            	rgb(100bp)=(0.61,0.61,0.61)}
            \tikzset {_ej4bwnxiv/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{-88 }  \pgftransformscale{2 }  }}}
            \pgfdeclarehorizontalshading{_hfbk8dt17}{150bp}{rgb(0bp)=(0.61,0.61,0.61);
            	rgb(42.1249989100865bp)=(0.61,0.61,0.61);
            	rgb(53.28571319580078bp)=(1,1,1);
            	rgb(62.5bp)=(0.5,0.5,0.5);
            	rgb(100bp)=(0.5,0.5,0.5)}
            \tikzset {_5v8h91i80/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{-45 }  \pgftransformscale{2 }  }}}
            \pgfdeclarehorizontalshading{_gsyl1qzel}{150bp}{rgb(0bp)=(0.5,0.5,0.5);
            	rgb(46.99887956891741bp)=(0.5,0.5,0.5);
            	rgb(49.141736711774556bp)=(1,1,1);
            	rgb(51.641736711774556bp)=(0.29,0.29,0.29);
            	rgb(100bp)=(0.29,0.29,0.29)}
            \tikzset {_esykvp8n3/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{-55 }  \pgftransformscale{2 }  }}}
            \pgfdeclarehorizontalshading{_65rror0zy}{150bp}{rgb(0bp)=(0.5,0.5,0.5);
            	rgb(37.5bp)=(0.5,0.5,0.5);
            	rgb(47.035718645368306bp)=(1,1,1);
            	rgb(57.660718645368306bp)=(0.29,0.29,0.29);
            	rgb(100bp)=(0.29,0.29,0.29)}
            \tikzset {_3qffkkd2g/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{-134 }  \pgftransformscale{2 }  }}}
            \pgfdeclarehorizontalshading{_py55kddps}{150bp}{rgb(0bp)=(0.29,0.29,0.29);
            	rgb(47.24888392857143bp)=(0.29,0.29,0.29);
            	rgb(50.40960039411272bp)=(1,1,1);
            	rgb(53.71428353445871bp)=(0,0,0);
            	rgb(100bp)=(0,0,0)}
            \tikzset{_6n8od2btq/.code = {\pgfsetadditionalshadetransform{\pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{-134 }  \pgftransformscale{2 } }}}
            \pgfdeclarehorizontalshading{_3j2f8g6bg} {150bp} {color(0bp)=(transparent!0);
            	color(47.24888392857143bp)=(transparent!0);
            	color(50.40960039411272bp)=(transparent!0);
            	color(53.71428353445871bp)=(transparent!10);
            	color(100bp)=(transparent!10) } 
            \pgfdeclarefading{_4s35ookjn}{\tikz \fill[shading=_3j2f8g6bg,_6n8od2btq] (0,0) rectangle (50bp,50bp); } 
            \tikzset {_4bq5t5hg1/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{-127 }  \pgftransformscale{2 }  }}}
            \pgfdeclarehorizontalshading{_1tuey5r88}{150bp}{rgb(0bp)=(0.5,0.5,0.5);
            	rgb(37.5bp)=(0.5,0.5,0.5);
            	rgb(46.94643293108259bp)=(1,1,1);
            	rgb(62.5bp)=(0.29,0.29,0.29);
            	rgb(100bp)=(0.29,0.29,0.29)}
            \tikzset {_cikqsdnwp/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{-92 }  \pgftransformscale{2 }  }}}
            \pgfdeclarehorizontalshading{_6lubq78c0}{150bp}{rgb(0bp)=(0.29,0.29,0.29);
            	rgb(37.5bp)=(0.29,0.29,0.29);
            	rgb(46.232147216796875bp)=(1,1,1);
            	rgb(57.83929007393973bp)=(0.29,0.29,0.29);
            	rgb(100bp)=(0.29,0.29,0.29)}
            \tikzset {_fw3f9e54c/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{-86 }  \pgftransformscale{2 }  }}}
            \pgfdeclarehorizontalshading{_nxzh27fwg}{150bp}{rgb(0bp)=(0.61,0.61,0.61);
            	rgb(37.5bp)=(0.61,0.61,0.61);
            	rgb(37.5bp)=(0.33,0.36,0.38);
            	rgb(47.01673780168806bp)=(1,1,1);
            	rgb(56.23214176722935bp)=(0.29,0.29,0.29);
            	rgb(100bp)=(0.29,0.29,0.29)}
            \tikzset {_fm3dj65c6/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{-92 }  \pgftransformscale{2 }  }}}
            \pgfdeclarehorizontalshading{_fcumkky18}{150bp}{rgb(0bp)=(0.5,0.5,0.5);
            	rgb(37.5bp)=(0.5,0.5,0.5);
            	rgb(47.66071319580078bp)=(1,1,1);
            	rgb(59.17857033865792bp)=(0.29,0.29,0.29);
            	rgb(100bp)=(0.29,0.29,0.29)}
            \tikzset {_z2k3v6jgt/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{-90 }  \pgftransformscale{2 }  }}}
            \pgfdeclarehorizontalshading{_0w8tzg21e}{150bp}{rgb(0bp)=(0.61,0.61,0.61);
            	rgb(37.5bp)=(0.61,0.61,0.61);
            	rgb(46.67857033865792bp)=(1,1,1);
            	rgb(57.66071319580078bp)=(0.29,0.29,0.29);
            	rgb(61.57031467982701bp)=(0.29,0.29,0.29);
            	rgb(62.5bp)=(0.29,0.29,0.29);
            	rgb(100bp)=(0.29,0.29,0.29)}
            \tikzset{every picture/.style={line width=0.75pt}} 
            \begin{center} \begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            	\draw  [fill={rgb, 255:red, 187; green, 192; blue, 193 }  ,fill opacity=1 ] (89.49,138.16) .. controls (89.49,115.14) and (108.16,96.48) .. (131.18,96.48) .. controls (154.2,96.48) and (172.86,115.14) .. (172.86,138.16) .. controls (172.86,161.18) and (154.2,179.85) .. (131.18,179.85) .. controls (108.16,179.85) and (89.49,161.18) .. (89.49,138.16) -- cycle ;
            	\draw  [fill={rgb, 255:red, 237; green, 234; blue, 201 }  ,fill opacity=1 ] (152.36,122.2) -- (199.75,122.2) -- (199.75,156.48) -- (152.36,156.48) -- cycle ;
            	\draw  [fill={rgb, 255:red, 187; green, 192; blue, 193 }  ,fill opacity=1 ] (250.24,70.11) -- (249.69,122.2) -- (163.36,122.03) -- (156.51,103.82) -- (157.58,101.64) -- (172.57,101.88) -- (172.57,107.02) -- (175.36,107.02) -- (175.36,102.31) -- (183.92,102.09) -- (183.84,106.31) -- (186.92,106.38) -- (187.14,102.31) -- (194.42,102.31) -- (194.33,106.52) -- (198.28,106.38) -- (198.28,102.52) -- (205.99,102.74) -- (205.99,106.59) -- (209.63,106.38) -- (209.63,102.52) -- (217.68,102.67) -- (217.77,106.81) -- (221.11,106.95) -- (221.2,102.74) -- (229.12,102.52) -- (229.12,106.81) -- (232.46,106.95) -- (232.46,102.45) -- (244.89,102.24) -- (245.53,70.11) -- cycle ;
            	\draw  [fill={rgb, 255:red, 187; green, 192; blue, 193 }  ,fill opacity=1 ] (250.33,156.48) -- (250.37,207.2) -- (245.02,207.2) -- (244.8,175.5) -- (231.83,175.56) -- (231.83,171.07) -- (227.97,170.85) -- (227.97,175.35) -- (221.12,175.35) -- (220.9,171.07) -- (217.05,170.85) -- (216.83,175.35) -- (209.16,175.29) -- (209.16,170.74) -- (205.09,170.74) -- (205.3,175.24) -- (197.59,175.18) -- (197.59,170.74) -- (193.73,170.74) -- (193.73,175.45) -- (186.45,175.24) -- (186.45,170.74) -- (183.02,170.74) -- (182.81,174.81) -- (175.31,174.84) -- (175.53,171.17) -- (172.31,171.17) -- (172.1,174.81) -- (157.68,174.9) -- (155.65,172.37) -- (162.07,156.95) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 237; green, 234; blue, 201 }  ,fill opacity=1 ] (161.97,155.62) .. controls (155.81,165.99) and (144.32,172.97) .. (131.18,172.97) .. controls (111.53,172.97) and (95.6,157.38) .. (95.6,138.16) .. controls (95.6,118.94) and (111.53,103.35) .. (131.18,103.35) .. controls (144.98,103.35) and (156.94,111.03) .. (162.84,122.26) -- cycle ;
            	\draw  [draw opacity=0] (161.35,156.58) .. controls (155.1,166.3) and (144.01,172.76) .. (131.37,172.76) .. controls (111.85,172.76) and (96.03,157.35) .. (96.03,138.35) .. controls (96.03,119.35) and (111.85,103.95) .. (131.37,103.95) .. controls (145.09,103.95) and (156.99,111.56) .. (162.85,122.69) -- (131.37,138.35) -- cycle ; \draw   (161.35,156.58) .. controls (155.1,166.3) and (144.01,172.76) .. (131.37,172.76) .. controls (111.85,172.76) and (96.03,157.35) .. (96.03,138.35) .. controls (96.03,119.35) and (111.85,103.95) .. (131.37,103.95) .. controls (145.09,103.95) and (156.99,111.56) .. (162.85,122.69) ;  
            	\draw  [draw opacity=0][fill={rgb, 255:red, 187; green, 192; blue, 193 }  ,fill opacity=1 ] (152.79,105.92) -- (163.29,103.57) -- (163.07,122.03) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 187; green, 192; blue, 193 }  ,fill opacity=1 ] (153.22,171.04) -- (161.79,172.76) -- (161.79,156.95) -- cycle ;
            	\draw  [fill={rgb, 255:red, 187; green, 192; blue, 193 }  ,fill opacity=1 ] (267.46,95.35) .. controls (275.65,100.57) and (281.82,116.45) .. (282.18,135.34) .. controls (282.57,155.46) and (276.24,172.42) .. (267.42,176.8) -- cycle ;
            	\draw  [fill={rgb, 255:red, 187; green, 192; blue, 193 }  ,fill opacity=1 ] (262.07,70.31) -- (267.85,70.31) -- (267.85,207.12) -- (262.07,207.12) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 187; green, 192; blue, 193 }  ,fill opacity=1 ] (265.07,92.66) -- (271.49,100.59) -- (272.14,169.13) -- (264.21,182.41) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.36 ] (250.24,83.17) -- (249.69,122.2) -- (163.36,122.03) -- (232.46,106.95) -- (232.46,102.45) -- (244.89,102.24) -- (245.42,85.33) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.24 ] (172.7,156.65) -- (250.33,156.48) -- (172.31,171.17) -- (172.1,174.81) -- (157.68,174.9) -- cycle ;
            	\path  [shading=_g3kq4n1v0,_q85v5nl0y] (134.07,118.27) -- (203.62,135.17) -- (201.82,142.58) -- (132.27,125.69) -- cycle ; 
            	\draw   (134.07,118.27) -- (203.62,135.17) -- (201.82,142.58) -- (132.27,125.69) -- cycle ;  
            	\path  [shading=_fgrb6muqf,_4tmqz12pm] (118.34,121.09) .. controls (118.34,114.56) and (123.64,109.26) .. (130.17,109.26) .. controls (136.7,109.26) and (141.99,114.56) .. (141.99,121.09) .. controls (141.99,127.62) and (136.7,132.91) .. (130.17,132.91) .. controls (123.64,132.91) and (118.34,127.62) .. (118.34,121.09) -- cycle ; 
            	\draw   (118.34,121.09) .. controls (118.34,114.56) and (123.64,109.26) .. (130.17,109.26) .. controls (136.7,109.26) and (141.99,114.56) .. (141.99,121.09) .. controls (141.99,127.62) and (136.7,132.91) .. (130.17,132.91) .. controls (123.64,132.91) and (118.34,127.62) .. (118.34,121.09) -- cycle ; 
            	\path  [shading=_uscupb3nw,_7iiahu01b] (114.11,142.57) .. controls (111.58,140.76) and (110.99,137.25) .. (112.79,134.72) -- (125.64,116.7) .. controls (127.44,114.17) and (130.95,113.58) .. (133.48,115.38) -- (133.48,115.38) .. controls (136.01,117.19) and (136.6,120.7) .. (134.8,123.23) -- (121.95,141.25) .. controls (120.15,143.78) and (116.64,144.37) .. (114.11,142.57) -- cycle ; 
            	\draw   (114.11,142.57) .. controls (111.58,140.76) and (110.99,137.25) .. (112.79,134.72) -- (125.64,116.7) .. controls (127.44,114.17) and (130.95,113.58) .. (133.48,115.38) -- (133.48,115.38) .. controls (136.01,117.19) and (136.6,120.7) .. (134.8,123.23) -- (121.95,141.25) .. controls (120.15,143.78) and (116.64,144.37) .. (114.11,142.57) -- cycle ; 
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (113.46,137.37) .. controls (113.46,135.24) and (115.18,133.51) .. (117.31,133.51) .. controls (119.44,133.51) and (121.17,135.24) .. (121.17,137.37) .. controls (121.17,139.5) and (119.44,141.22) .. (117.31,141.22) .. controls (115.18,141.22) and (113.46,139.5) .. (113.46,137.37) -- cycle ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (125.74,120.8) .. controls (125.74,118.67) and (127.47,116.95) .. (129.6,116.95) .. controls (131.72,116.95) and (133.45,118.67) .. (133.45,120.8) .. controls (133.45,122.93) and (131.72,124.66) .. (129.6,124.66) .. controls (127.47,124.66) and (125.74,122.93) .. (125.74,120.8) -- cycle ;
            	\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ]   (119.66,133.51) -- (126.23,123.52) ;
            	\path  [shading=_hfbk8dt17,_ej4bwnxiv] (199.46,122.2) -- (240.38,122.2) -- (240.38,156.48) -- (199.46,156.48) -- cycle ; 
            	\draw   (199.46,122.2) -- (240.38,122.2) -- (240.38,156.48) -- (199.46,156.48) -- cycle ; 
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (199.94,125.63) -- (240.04,125.29) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.56 ]   (200.28,134.2) -- (240.04,133.85) ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (203.71,137.97) .. controls (203.71,136.07) and (205.25,134.54) .. (207.14,134.54) .. controls (209.03,134.54) and (210.57,136.07) .. (210.57,137.97) .. controls (210.57,139.86) and (209.03,141.4) .. (207.14,141.4) .. controls (205.25,141.4) and (203.71,139.86) .. (203.71,137.97) -- cycle ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.56 ]   (199.94,151.33) -- (239.7,150.99) ;
            	\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=0.33 ]   (199.94,148.59) -- (239.7,148.25) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.31 ] [dash pattern={on 0.84pt off 2.51pt}]  (226.97,127.94) -- (233.82,128.16) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.31 ] [dash pattern={on 0.84pt off 2.51pt}]  (226.97,132.66) -- (233.82,132.87) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.31 ] [dash pattern={on 0.84pt off 2.51pt}]  (226.97,148.94) -- (233.82,149.15) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.31 ] [dash pattern={on 0.84pt off 2.51pt}]  (227.25,125.09) -- (234.11,125.3) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.31 ] [dash pattern={on 0.84pt off 2.51pt}]  (234.96,144.51) -- (223.34,144.65) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.26 ] (151.67,174.1) .. controls (145.54,177.75) and (138.39,179.85) .. (130.76,179.85) .. controls (107.97,179.85) and (89.49,161.18) .. (89.49,138.16) .. controls (89.49,115.14) and (107.97,96.48) .. (130.76,96.48) .. controls (132.78,96.48) and (134.77,96.62) .. (136.71,96.91) -- (130.76,138.16) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.31 ] (262.35,101.81) -- (276.63,113.23) -- (262.07,207.12) -- cycle ;
            	\path  [shading=_gsyl1qzel,_5v8h91i80] (278.81,98.47) -- (281.88,101.66) -- (258.87,123.81) -- (255.79,120.62) -- cycle ; 
            	\draw   (278.81,98.47) -- (281.88,101.66) -- (258.87,123.81) -- (255.79,120.62) -- cycle ; 
            	\path  [shading=_65rror0zy,_esykvp8n3] (254.04,118.51) -- (261.48,126.24) -- (258.03,129.56) -- (250.59,121.83) -- cycle ; 
            	\draw   (254.04,118.51) -- (261.48,126.24) -- (258.03,129.56) -- (250.59,121.83) -- cycle ; 
            	\path  [shading=_py55kddps,_3qffkkd2g,path fading= _4s35ookjn ,fading transform={xshift=2}] (281.66,176.36) -- (278.61,179.58) -- (255.42,157.61) -- (258.47,154.39) -- cycle ; 
            	\draw   (281.66,176.36) -- (278.61,179.58) -- (255.42,157.61) -- (258.47,154.39) -- cycle ; 
            	\path  [shading=_1tuey5r88,_4bq5t5hg1] (261.78,152.54) -- (254.4,160.33) -- (250.93,157.04) -- (258.31,149.25) -- cycle ; 
            	\draw   (261.78,152.54) -- (254.4,160.33) -- (250.93,157.04) -- (258.31,149.25) -- cycle ;  
            	\path  [shading=_6lubq78c0,_cikqsdnwp] (254.93,138.67) -- (306.59,138.67) -- (306.59,141.88) -- (254.93,141.88) -- cycle ; 
            	\draw   (254.93,138.67) -- (306.59,138.67) -- (306.59,141.88) -- (254.93,141.88) -- cycle ; 
            	\path  [shading=_nxzh27fwg,_fw3f9e54c] (267.99,131.17) -- (273.99,131.17) -- (273.99,149.81) -- (267.99,149.81) -- cycle ; 
            	\draw   (267.99,131.17) -- (273.99,131.17) -- (273.99,149.81) -- (267.99,149.81) -- cycle ; 
            	\draw    (268.18,139.44) -- (273.99,139.31) ;
            	\path  [shading=_fcumkky18,_fm3dj65c6] (268.26,146.24) -- (257.97,144.73) -- (257.9,135.28) -- (268.17,133.61) -- cycle ; 
            	\draw   (268.26,146.24) -- (257.97,144.73) -- (257.9,135.28) -- (268.17,133.61) -- cycle ; 
            	\path  [shading=_0w8tzg21e,_z2k3v6jgt] (274.05,146.81) -- (301.66,144.44) -- (301.59,136.1) -- (273.95,134.17) -- cycle ; 
            	\draw   (274.05,146.81) -- (301.66,144.44) -- (301.59,136.1) -- (273.95,134.17) -- cycle ; 
            	\draw    (268.18,135.58) -- (273.99,135.45) ;
            	\draw    (268.18,143.51) -- (273.99,143.38) ;
            	\draw    (268.24,146.94) -- (274.05,146.81) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (275.97,136.83) -- (299.28,138.02) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (259.18,137.17) -- (265.69,136.48) ;
            	\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ]   (121.85,137.71) -- (203.71,137.97) ;
            	\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ]   (133.77,122.72) -- (203.71,137.97) ;
            	\draw    (90.41,99.58) -- (110.29,126.35) ;
            	\draw    (201.46,85.87) -- (223.4,133.85) ;
            	\draw    (144,188.3) -- (155.33,135.64) ;
            	\draw    (309.08,107.81) -- (295.03,130.08) ;
            	\draw    (124,132.83) -- (128.8,147.91) ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (373.03,167.82) .. controls (373.03,164.97) and (375.34,162.67) .. (378.18,162.67) .. controls (381.03,162.67) and (383.33,164.97) .. (383.33,167.82) .. controls (383.33,170.66) and (381.03,172.97) .. (378.18,172.97) .. controls (375.34,172.97) and (373.03,170.66) .. (373.03,167.82) -- cycle ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (543.7,164.82) .. controls (543.7,161.97) and (546,159.67) .. (548.85,159.67) .. controls (551.69,159.67) and (554,161.97) .. (554,164.82) .. controls (554,167.66) and (551.69,169.97) .. (548.85,169.97) .. controls (546,169.97) and (543.7,167.66) .. (543.7,164.82) -- cycle ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (409.7,110.15) .. controls (409.7,107.31) and (412,105) .. (414.85,105) .. controls (417.69,105) and (420,107.31) .. (420,110.15) .. controls (420,113) and (417.69,115.3) .. (414.85,115.3) .. controls (412,115.3) and (409.7,113) .. (409.7,110.15) -- cycle ;
            	\draw    (382,163.64) -- (411.33,114.97) ; 
            	\draw    (545.33,162.3) -- (420,111.15) ;
            	\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ] [dash pattern={on 4.5pt off 4.5pt}]  (383.33,167.82) -- (543.7,165.82) ;
            	\draw  [draw opacity=0] (387.31,155.42) .. controls (392.25,158.62) and (393.89,164.88) .. (390.97,169.42) -- (382,163.64) -- cycle ; \draw  [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ] (387.31,155.42) .. controls (392.25,158.62) and (393.89,164.88) .. (390.97,169.42) ;  
            	\draw (452,172) node [anchor=north west][inner sep=0.75pt]    {$x$};
            	\draw (378.67,119.33) node [anchor=north west][inner sep=0.75pt]    {$%s$};
            	\draw (485.33,117.33) node [anchor=north west][inner sep=0.75pt]    {$%s$};
            	\draw (393.33,146) node [anchor=north west][inner sep=0.75pt]    {$\theta $};
            	\draw (46.26,81.49) node [anchor=north west][inner sep=0.75pt]  [font=\small] [align=left] {Crankshaft};
            	\draw (179.19,67.44) node [anchor=north west][inner sep=0.75pt]  [font=\small] [align=left] {Piston};
            	\draw (99.92,186.71) node [anchor=north west][inner sep=0.75pt]  [font=\small] [align=left] {Connecting rod};
            	\draw (279.73,88) node [anchor=north west][inner sep=0.75pt]  [font=\small] [align=left] {Spark plug};
            	\draw (123.2,143.11) node [anchor=north west][inner sep=0.75pt]    {$\theta $};
            \end{tikzpicture} \end{center}'''% (latex(r_val),  latex(l_val))

                # Câu hỏi
                noidungcauhoi = (r'''Hình vẽ dưới là sơ đồ của một động cơ pít-tông, bao gồm trục khuỷu (Crankshaft), pít-tông (Piston), thanh truyền (Connecting rod) và bugi (Spark plug). Có một góc $\theta$ được đánh dấu tại trục khuỷu. Khoảng cách từ tâm trục khuỷu đến điểm gắn thanh truyền là $%s$ inch (bán kính tay quay). Chiều dài thanh truyền là $%s$ inch. Khoảng cách từ tâm trục khuỷu đến đầu pít-tông theo phương ngang là $x$. %s Trục khuỷu quay ngược chiều kim đồng hồ với tốc độ không đổi là $%s$ vòng mỗi phút. Tốc độ của pít-tông khi $\theta = %s$ radian bằng bao nhiêu? (làm tròn kết quả đến hàng đơn vị).'''
                                 % (latex(r_val),  latex(l_val), hinhve, latex(v_rpm), theta_val_str))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Gọi $x$ là khoảng cách từ tâm trục khuỷu đến đầu pít-tông. Từ hình vẽ và áp dụng định lý hàm số cô-sin (hoặc hệ thức lượng), ta có phương trình vị trí của pít-tông là:
                $$x = r \\cos\\theta + \\sqrt{l^2 - r^2 \\sin^2\\theta}$$
                Thay số $r = %s$ và $l = %s$, ta có:
                $$x = %s \\cos\\theta + \\sqrt{%s - %s \\sin^2\\theta}$$
                Đạo hàm hai vế theo thời gian $t$, chú ý $\\frac{dx}{dt}$ là vận tốc của pít-tông và $\\frac{d\\theta}{dt}$ là tốc độ góc của trục khuỷu:
                $$\\frac{dx}{dt} = \\left( -%s \\sin\\theta - \\frac{%s \\sin\\theta \\cos\\theta}{\\sqrt{%s - %s \\sin^2\\theta}} \\right) \\cdot \\frac{d\\theta}{dt}$$
                Theo giả thiết, tốc độ góc của trục khuỷu là:
                $$\\frac{d\\theta}{dt} = %s \\cdot 2\\pi = %s\\pi \\text{ (rad/phút)}$$
                Khi $\\theta = %s$, ta thay vào biểu thức đạo hàm:
                $$\\frac{dx}{dt} = \\left( -%s \\sin\\left(%s\\right) - \\frac{%s \\sin\\left(%s\\right) \\cos\\left(%s\\right)}{\\sqrt{%s - %s \\sin^2\\left(%s\\right)}} \\right) \\cdot %s\\pi$$
                $$\\frac{dx}{dt} = \\left(%s\\right) \\cdot %s\\pi = %s$$
                Tốc độ của pít-tông là độ lớn của vận tốc:
                $$v = \\left| \\frac{dx}{dt} \\right| \\approx %s \\text{ (inch/phút)}.$$'''
                           % (
                               latex(r_val), latex(l_val),
                               latex(r_val), latex(l_val**2), latex(r_val**2),
                               latex(r_val), latex(r_val**2), latex(l_val**2), latex(r_val**2),
                               latex(v_rpm), latex(v_rpm*2),
                               theta_val_str,
                               latex(r_val), theta_val_str, latex(r_val**2), theta_val_str, theta_val_str, latex(l_val**2), latex(r_val**2), theta_val_str, latex(v_rpm*2),
                               latex(dxdtheta_at_val), latex(v_rpm*2), latex(v_at_val),
                               kq
                           ))
                dapan='\\shortans[0]{$%s$}\n'%(kq)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                       '\\loigiai{\n' + str(loigiai) + '\n}\n'
                       '\\end{ex}\n\\end{minipage} \n\n')
            return content    

