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


def bt_dang28_p3_b1_c4_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            # Hàm hỗ trợ làm tròn đến hàng phần trăm và đổi dấu chấm thành phẩy
            def to_dec_str(val):
                v = float(val)
                # quantize('0.01') để làm tròn đúng 2 chữ số thập phân
                s = str(Decimal(v).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))
                # Loại bỏ số 0 vô nghĩa ở đuôi nếu có (ví dụ 0.50 -> 0.5), nếu bạn muốn giữ nguyên 0.50 thì xóa 2 hàm rstrip
                s = s.rstrip('0').rstrip('.')
                return s.replace('.', ',')

            if dang=='1':
                # Số lượng bi ban đầu
                xanh = random.randint(8, 12)
                do = random.randint(5, 9)
                tong = xanh + do

                # Xác suất Hòa
                P_A = Rational(xanh, tong)
                P_A_bar = Rational(do, tong)

                # Nếu Hòa lấy xanh, Bình lấy 2 bi. Cùng màu => 2 xanh
                tu_B_bar_A = math.comb(xanh - 1, 2)
                mau_B_bar_A = math.comb(tong - 1, 2)
                P_B_bar_A = Rational(tu_B_bar_A, mau_B_bar_A)
                P_B_A = 1 - P_B_bar_A

                # Nếu Hòa lấy đỏ, Bình lấy 3 bi. Cùng màu => 3 đỏ
                tu_B_bar_A_bar = math.comb(do - 1, 3)
                mau_B_bar_A_bar = math.comb(tong - 1, 3)
                P_B_bar_A_bar = Rational(tu_B_bar_A_bar, mau_B_bar_A_bar)
                P_B_A_bar = 1 - P_B_bar_A_bar

                # Tính các xác suất tổng hợp
                P_AB = P_B_A * P_A
                P_B = P_B_A * P_A + P_B_A_bar * P_A_bar

                # Kết quả cuối cùng (Phân số và Thập phân làm tròn)
                kq_frac = P_AB / P_B
                kq_dec = to_dec_str(kq_frac)

                # Đáp án đúng
                da = f"${kq_dec}$"

                # Tập hợp các đáp án sai được làm tròn đến hàng phần trăm
                wrong_options = [P_B, P_AB, 1 - kq_frac, P_A, P_B_A]
                s_set = []
                for w in wrong_options:
                    w_dec = to_dec_str(w)
                    if w_dec != kq_dec and f"${w_dec}$" not in s_set:
                        s_set.append(f"${w_dec}$")

                # Đảm bảo đủ 3 phương án sai
                while len(s_set) < 3:
                    random_val = to_dec_str(random.uniform(0.1, 0.9))
                    if random_val != kq_dec and f"${random_val}$" not in s_set:
                        s_set.append(f"${random_val}$")

                das1 = s_set[0]
                das2 = s_set[1]
                das3 = s_set[2]

                hinhve=r'''\tikzset {_g4p2u74jw/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{89.1 bp } { -108.9 bp }  }  \pgftransformscale{1.32 }  }}}
            \pgfdeclareradialshading{_40wdjb0f2}{\pgfpoint{-72bp}{88bp}}{rgb(0bp)=(1,1,1);
            	rgb(0bp)=(1,1,1);
            	rgb(12.087059020996094bp)=(0.99,0.02,0.13);
            	rgb(22.73102351597377bp)=(0.19,0.01,0.03);
            	rgb(400bp)=(0.19,0.01,0.03)}
            \tikzset {_m79jdknx3/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{89.1 bp } { -108.9 bp }  }  \pgftransformscale{1.32 }  }}}
            \pgfdeclareradialshading{_dvqaby3dq}{\pgfpoint{-72bp}{88bp}}{rgb(0bp)=(1,1,1);
            	rgb(0bp)=(1,1,1);
            	rgb(12.087059020996094bp)=(0.99,0.02,0.13);
            	rgb(22.73102351597377bp)=(0.19,0.01,0.03);
            	rgb(400bp)=(0.19,0.01,0.03)}
            \tikzset {_gw4qoh6rd/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{89.1 bp } { -108.9 bp }  }  \pgftransformscale{1.32 }  }}}
            \pgfdeclareradialshading{_es3sdihw7}{\pgfpoint{-72bp}{88bp}}{rgb(0bp)=(1,1,1);
            	rgb(0bp)=(1,1,1);
            	rgb(12.087059020996094bp)=(0.49,0.83,0.13);
            	rgb(22.73102351597377bp)=(0.19,0.01,0.03);
            	rgb(400bp)=(0.19,0.01,0.03)}
            \tikzset {_8xufb4hv9/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{89.1 bp } { -108.9 bp }  }  \pgftransformscale{1.32 }  }}}
            \pgfdeclareradialshading{_46bly8urq}{\pgfpoint{-72bp}{88bp}}{rgb(0bp)=(1,1,1);
            	rgb(0bp)=(1,1,1);
            	rgb(12.087059020996094bp)=(0.99,0.02,0.13);
            	rgb(22.73102351597377bp)=(0.19,0.01,0.03);
            	rgb(400bp)=(0.19,0.01,0.03)}
            \tikzset {_8nrhoo6sm/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{89.1 bp } { -108.9 bp }  }  \pgftransformscale{1.32 }  }}}
            \pgfdeclareradialshading{_9jpdryjtx}{\pgfpoint{-72bp}{88bp}}{rgb(0bp)=(1,1,1);
            	rgb(0bp)=(1,1,1);
            	rgb(12.087059020996094bp)=(0.49,0.83,0.13);
            	rgb(22.73102351597377bp)=(0.19,0.01,0.03);
            	rgb(400bp)=(0.19,0.01,0.03)}
            \tikzset {_f6rgls948/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{89.1 bp } { -108.9 bp }  }  \pgftransformscale{1.32 }  }}}
            \pgfdeclareradialshading{_jepxc8gk1}{\pgfpoint{-72bp}{88bp}}{rgb(0bp)=(1,1,1);
            	rgb(0bp)=(1,1,1);
            	rgb(12.087059020996094bp)=(0.49,0.83,0.13);
            	rgb(22.73102351597377bp)=(0.19,0.01,0.03);
            	rgb(400bp)=(0.19,0.01,0.03)}
            \tikzset {_hvxgfmix6/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{89.1 bp } { -108.9 bp }  }  \pgftransformscale{1.32 }  }}}
            \pgfdeclareradialshading{_zgolsul3s}{\pgfpoint{-72bp}{88bp}}{rgb(0bp)=(1,1,1);
            	rgb(0bp)=(1,1,1);
            	rgb(12.087059020996094bp)=(0.99,0.02,0.13);
            	rgb(22.73102351597377bp)=(0.19,0.01,0.03);
            	rgb(400bp)=(0.19,0.01,0.03)}
            \tikzset {_08f3gd1r9/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{89.1 bp } { -108.9 bp }  }  \pgftransformscale{1.32 }  }}}
            \pgfdeclareradialshading{_z9l2hd6b8}{\pgfpoint{-72bp}{88bp}}{rgb(0bp)=(1,1,1);
            	rgb(0bp)=(1,1,1);
            	rgb(12.087059020996094bp)=(0.49,0.83,0.13);
            	rgb(22.73102351597377bp)=(0.19,0.01,0.03);
            	rgb(400bp)=(0.19,0.01,0.03)}
            \tikzset {_efbctp1mv/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{89.1 bp } { -108.9 bp }  }  \pgftransformscale{1.32 }  }}}
            \pgfdeclareradialshading{_c889qlf3z}{\pgfpoint{-72bp}{88bp}}{rgb(0bp)=(1,1,1);
            	rgb(0bp)=(1,1,1);
            	rgb(12.087059020996094bp)=(0.49,0.83,0.13);
            	rgb(22.73102351597377bp)=(0.19,0.01,0.03);
            	rgb(400bp)=(0.19,0.01,0.03)}
            \tikzset {_0s4gsuo1m/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{89.1 bp } { -108.9 bp }  }  \pgftransformscale{1.32 }  }}}
            \pgfdeclareradialshading{_qpgi75qlm}{\pgfpoint{-72bp}{88bp}}{rgb(0bp)=(1,1,1);
            	rgb(0bp)=(1,1,1);
            	rgb(12.087059020996094bp)=(0.99,0.02,0.13);
            	rgb(22.73102351597377bp)=(0.19,0.01,0.03);
            	rgb(400bp)=(0.19,0.01,0.03)}
            \tikzset {_wxk5uzbxt/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{89.1 bp } { -108.9 bp }  }  \pgftransformscale{1.32 }  }}}
            \pgfdeclareradialshading{_2jaimmkfh}{\pgfpoint{-72bp}{88bp}}{rgb(0bp)=(1,1,1);
            	rgb(0bp)=(1,1,1);
            	rgb(12.087059020996094bp)=(0.99,0.02,0.13);
            	rgb(22.73102351597377bp)=(0.19,0.01,0.03);
            	rgb(400bp)=(0.19,0.01,0.03)}
            \tikzset {_057kuimsq/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{89.1 bp } { -108.9 bp }  }  \pgftransformscale{1.32 }  }}}
            \pgfdeclareradialshading{_qvdbejarw}{\pgfpoint{-72bp}{88bp}}{rgb(0bp)=(1,1,1);
            	rgb(0bp)=(1,1,1);
            	rgb(12.087059020996094bp)=(0.99,0.02,0.13);
            	rgb(22.73102351597377bp)=(0.19,0.01,0.03);
            	rgb(400bp)=(0.19,0.01,0.03)}
            \tikzset {_7mikztv3r/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{89.1 bp } { -108.9 bp }  }  \pgftransformscale{1.32 }  }}}
            \pgfdeclareradialshading{_3bkvylu9b}{\pgfpoint{-72bp}{88bp}}{rgb(0bp)=(1,1,1);
            	rgb(0bp)=(1,1,1);
            	rgb(12.087059020996094bp)=(0.49,0.83,0.13);
            	rgb(22.73102351597377bp)=(0.19,0.01,0.03);
            	rgb(400bp)=(0.19,0.01,0.03)}
            \tikzset{every picture/.style={line width=0.75pt}} 
            \begin{center} \begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.29 ] (124,129.33) -- (296.76,105.15) -- (315.47,105) -- (284.45,138.84) -- (136.13,137.67) -- cycle ;
            	\draw  [color={rgb, 255:red, 180; green, 177; blue, 177 }  ,draw opacity=1 ][fill={rgb, 255:red, 199; green, 220; blue, 240 }  ,fill opacity=0.48 ] (272.68,129.31) -- (296.76,105.15) -- (296.68,48.88) -- (147.59,49.09) -- (123.51,73.24) -- (123.59,129.51) -- cycle ; \draw  [color={rgb, 255:red, 180; green, 177; blue, 177 }  ,draw opacity=1 ] (296.68,48.88) -- (272.6,73.03) -- (272.68,129.31) ; \draw  [color={rgb, 255:red, 180; green, 177; blue, 177 }  ,draw opacity=1 ] (272.6,73.03) -- (123.51,73.24) ;
            	\draw [color={rgb, 255:red, 180; green, 177; blue, 177 }  ,draw opacity=1 ]   (148.13,105.33) -- (296.76,105.15) ;
            	\draw [color={rgb, 255:red, 180; green, 177; blue, 177 }  ,draw opacity=1 ]   (147.59,49.09) -- (149.19,122.9) ;
            	\draw [color={rgb, 255:red, 180; green, 177; blue, 177 }  ,draw opacity=1 ]   (155.93,97.4) -- (122.8,129.23) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 186; green, 180; blue, 180 }  ,fill opacity=0.67 ] (184.35,109.15) .. controls (184.35,107.03) and (189.29,105.31) .. (195.38,105.31) .. controls (201.47,105.31) and (206.41,107.03) .. (206.41,109.15) .. controls (206.41,111.28) and (201.47,113) .. (195.38,113) .. controls (189.29,113) and (184.35,111.28) .. (184.35,109.15) -- cycle ;
            	\path  [shading=_40wdjb0f2,_g4p2u74jw] (179.53,98.45) .. controls (179.53,91.46) and (185.2,85.8) .. (192.18,85.8) .. controls (199.17,85.8) and (204.83,91.46) .. (204.83,98.45) .. controls (204.83,105.43) and (199.17,111.1) .. (192.18,111.1) .. controls (185.2,111.1) and (179.53,105.43) .. (179.53,98.45) -- cycle ; 
            	\draw   (179.53,98.45) .. controls (179.53,91.46) and (185.2,85.8) .. (192.18,85.8) .. controls (199.17,85.8) and (204.83,91.46) .. (204.83,98.45) .. controls (204.83,105.43) and (199.17,111.1) .. (192.18,111.1) .. controls (185.2,111.1) and (179.53,105.43) .. (179.53,98.45) -- cycle ; 
            	\draw  [draw opacity=0] (181.73,98.95) .. controls (181.72,98.78) and (181.72,98.62) .. (181.72,98.45) .. controls (181.72,92.67) and (186.43,87.98) .. (192.25,87.97) -- (192.26,98.45) -- cycle ; \draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ] (181.73,98.95) .. controls (181.72,98.78) and (181.72,98.62) .. (181.72,98.45) .. controls (181.72,92.67) and (186.43,87.98) .. (192.25,87.97) ;  
            	\draw  [draw opacity=0][fill={rgb, 255:red, 186; green, 180; blue, 180 }  ,fill opacity=0.67 ] (157.75,108.95) .. controls (157.75,106.83) and (162.69,105.11) .. (168.78,105.11) .. controls (174.87,105.11) and (179.81,106.83) .. (179.81,108.95) .. controls (179.81,111.08) and (174.87,112.8) .. (168.78,112.8) .. controls (162.69,112.8) and (157.75,111.08) .. (157.75,108.95) -- cycle ;
            	\path  [shading=_dvqaby3dq,_m79jdknx3] (152.93,98.25) .. controls (152.93,91.26) and (158.6,85.6) .. (165.58,85.6) .. controls (172.57,85.6) and (178.23,91.26) .. (178.23,98.25) .. controls (178.23,105.23) and (172.57,110.9) .. (165.58,110.9) .. controls (158.6,110.9) and (152.93,105.23) .. (152.93,98.25) -- cycle ; 
            	\draw   (152.93,98.25) .. controls (152.93,91.26) and (158.6,85.6) .. (165.58,85.6) .. controls (172.57,85.6) and (178.23,91.26) .. (178.23,98.25) .. controls (178.23,105.23) and (172.57,110.9) .. (165.58,110.9) .. controls (158.6,110.9) and (152.93,105.23) .. (152.93,98.25) -- cycle ; 
            	\draw  [draw opacity=0] (155.13,98.75) .. controls (155.12,98.58) and (155.12,98.42) .. (155.12,98.25) .. controls (155.12,92.47) and (159.83,87.78) .. (165.65,87.77) -- (165.66,98.25) -- cycle ; \draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ] (155.13,98.75) .. controls (155.12,98.58) and (155.12,98.42) .. (155.12,98.25) .. controls (155.12,92.47) and (159.83,87.78) .. (165.65,87.77) ;  
            	\draw  [draw opacity=0][fill={rgb, 255:red, 186; green, 180; blue, 180 }  ,fill opacity=0.67 ] (211.49,109.84) .. controls (211.49,107.66) and (216.58,105.88) .. (222.85,105.88) .. controls (229.12,105.88) and (234.2,107.66) .. (234.2,109.84) .. controls (234.2,112.03) and (229.12,113.8) .. (222.85,113.8) .. controls (216.58,113.8) and (211.49,112.03) .. (211.49,109.84) -- cycle ;
            	\path  [shading=_es3sdihw7,_gw4qoh6rd] (206.53,98.82) .. controls (206.53,91.63) and (212.36,85.8) .. (219.55,85.8) .. controls (226.75,85.8) and (232.57,91.63) .. (232.57,98.82) .. controls (232.57,106.01) and (226.75,111.84) .. (219.55,111.84) .. controls (212.36,111.84) and (206.53,106.01) .. (206.53,98.82) -- cycle ; 
            	\draw   (206.53,98.82) .. controls (206.53,91.63) and (212.36,85.8) .. (219.55,85.8) .. controls (226.75,85.8) and (232.57,91.63) .. (232.57,98.82) .. controls (232.57,106.01) and (226.75,111.84) .. (219.55,111.84) .. controls (212.36,111.84) and (206.53,106.01) .. (206.53,98.82) -- cycle ; 
            	\draw  [draw opacity=0] (208.8,99.34) .. controls (208.79,99.17) and (208.78,98.99) .. (208.78,98.82) .. controls (208.78,92.87) and (213.63,88.04) .. (219.62,88.04) -- (219.64,98.82) -- cycle ; \draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ] (208.8,99.34) .. controls (208.79,99.17) and (208.78,98.99) .. (208.78,98.82) .. controls (208.78,92.87) and (213.63,88.04) .. (219.62,88.04) ;  
            	\draw  [draw opacity=0][fill={rgb, 255:red, 186; green, 180; blue, 180 }  ,fill opacity=0.67 ] (238.55,108.95) .. controls (238.55,106.83) and (243.49,105.11) .. (249.58,105.11) .. controls (255.67,105.11) and (260.61,106.83) .. (260.61,108.95) .. controls (260.61,111.08) and (255.67,112.8) .. (249.58,112.8) .. controls (243.49,112.8) and (238.55,111.08) .. (238.55,108.95) -- cycle ;
            	\path  [shading=_46bly8urq,_8xufb4hv9] (233.73,98.25) .. controls (233.73,91.26) and (239.4,85.6) .. (246.38,85.6) .. controls (253.37,85.6) and (259.03,91.26) .. (259.03,98.25) .. controls (259.03,105.23) and (253.37,110.9) .. (246.38,110.9) .. controls (239.4,110.9) and (233.73,105.23) .. (233.73,98.25) -- cycle ; 
            	\draw   (233.73,98.25) .. controls (233.73,91.26) and (239.4,85.6) .. (246.38,85.6) .. controls (253.37,85.6) and (259.03,91.26) .. (259.03,98.25) .. controls (259.03,105.23) and (253.37,110.9) .. (246.38,110.9) .. controls (239.4,110.9) and (233.73,105.23) .. (233.73,98.25) -- cycle ; 
            	\draw  [draw opacity=0] (235.93,98.75) .. controls (235.92,98.58) and (235.92,98.42) .. (235.92,98.25) .. controls (235.92,92.47) and (240.63,87.78) .. (246.45,87.77) -- (246.46,98.25) -- cycle ; \draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ] (235.93,98.75) .. controls (235.92,98.58) and (235.92,98.42) .. (235.92,98.25) .. controls (235.92,92.47) and (240.63,87.78) .. (246.45,87.77) ;  
            	\draw  [draw opacity=0][fill={rgb, 255:red, 186; green, 180; blue, 180 }  ,fill opacity=0.67 ] (266.09,110.04) .. controls (266.09,107.86) and (271.18,106.08) .. (277.45,106.08) .. controls (283.72,106.08) and (288.8,107.86) .. (288.8,110.04) .. controls (288.8,112.23) and (283.72,114) .. (277.45,114) .. controls (271.18,114) and (266.09,112.23) .. (266.09,110.04) -- cycle ;
            	\path  [shading=_9jpdryjtx,_8nrhoo6sm] (261.13,99.02) .. controls (261.13,91.83) and (266.96,86) .. (274.15,86) .. controls (281.35,86) and (287.17,91.83) .. (287.17,99.02) .. controls (287.17,106.21) and (281.35,112.04) .. (274.15,112.04) .. controls (266.96,112.04) and (261.13,106.21) .. (261.13,99.02) -- cycle ; 
            	\draw   (261.13,99.02) .. controls (261.13,91.83) and (266.96,86) .. (274.15,86) .. controls (281.35,86) and (287.17,91.83) .. (287.17,99.02) .. controls (287.17,106.21) and (281.35,112.04) .. (274.15,112.04) .. controls (266.96,112.04) and (261.13,106.21) .. (261.13,99.02) -- cycle ; 
            	\draw  [draw opacity=0] (263.4,99.54) .. controls (263.39,99.37) and (263.38,99.19) .. (263.38,99.02) .. controls (263.38,93.07) and (268.23,88.24) .. (274.22,88.24) -- (274.24,99.02) -- cycle ; \draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ] (263.4,99.54) .. controls (263.39,99.37) and (263.38,99.19) .. (263.38,99.02) .. controls (263.38,93.07) and (268.23,88.24) .. (274.22,88.24) ;  
            	\draw  [draw opacity=0][fill={rgb, 255:red, 186; green, 180; blue, 180 }  ,fill opacity=0.67 ] (139.89,120.64) .. controls (139.89,118.46) and (144.98,116.68) .. (151.25,116.68) .. controls (157.52,116.68) and (162.6,118.46) .. (162.6,120.64) .. controls (162.6,122.83) and (157.52,124.6) .. (151.25,124.6) .. controls (144.98,124.6) and (139.89,122.83) .. (139.89,120.64) -- cycle ;
            	\path  [shading=_jepxc8gk1,_f6rgls948] (134.93,109.62) .. controls (134.93,102.43) and (140.76,96.6) .. (147.95,96.6) .. controls (155.15,96.6) and (160.97,102.43) .. (160.97,109.62) .. controls (160.97,116.81) and (155.15,122.64) .. (147.95,122.64) .. controls (140.76,122.64) and (134.93,116.81) .. (134.93,109.62) -- cycle ; 
            	\draw   (134.93,109.62) .. controls (134.93,102.43) and (140.76,96.6) .. (147.95,96.6) .. controls (155.15,96.6) and (160.97,102.43) .. (160.97,109.62) .. controls (160.97,116.81) and (155.15,122.64) .. (147.95,122.64) .. controls (140.76,122.64) and (134.93,116.81) .. (134.93,109.62) -- cycle ; 
            	\draw  [draw opacity=0] (137.2,110.14) .. controls (137.19,109.97) and (137.18,109.79) .. (137.18,109.62) .. controls (137.18,103.67) and (142.03,98.84) .. (148.02,98.84) -- (148.04,109.62) -- cycle ; \draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ] (137.2,110.14) .. controls (137.19,109.97) and (137.18,109.79) .. (137.18,109.62) .. controls (137.18,103.67) and (142.03,98.84) .. (148.02,98.84) ; 
            	\draw  [draw opacity=0][fill={rgb, 255:red, 186; green, 180; blue, 180 }  ,fill opacity=0.67 ] (166.95,120.55) .. controls (166.95,118.43) and (171.89,116.71) .. (177.98,116.71) .. controls (184.07,116.71) and (189.01,118.43) .. (189.01,120.55) .. controls (189.01,122.68) and (184.07,124.4) .. (177.98,124.4) .. controls (171.89,124.4) and (166.95,122.68) .. (166.95,120.55) -- cycle ;
            	\path  [shading=_zgolsul3s,_hvxgfmix6] (162.13,109.85) .. controls (162.13,102.86) and (167.8,97.2) .. (174.78,97.2) .. controls (181.77,97.2) and (187.43,102.86) .. (187.43,109.85) .. controls (187.43,116.83) and (181.77,122.5) .. (174.78,122.5) .. controls (167.8,122.5) and (162.13,116.83) .. (162.13,109.85) -- cycle ; 
            	\draw   (162.13,109.85) .. controls (162.13,102.86) and (167.8,97.2) .. (174.78,97.2) .. controls (181.77,97.2) and (187.43,102.86) .. (187.43,109.85) .. controls (187.43,116.83) and (181.77,122.5) .. (174.78,122.5) .. controls (167.8,122.5) and (162.13,116.83) .. (162.13,109.85) -- cycle ; 
            	\draw  [draw opacity=0] (164.33,110.35) .. controls (164.32,110.18) and (164.32,110.02) .. (164.32,109.85) .. controls (164.32,104.07) and (169.03,99.38) .. (174.85,99.37) -- (174.86,109.85) -- cycle ; \draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ] (164.33,110.35) .. controls (164.32,110.18) and (164.32,110.02) .. (164.32,109.85) .. controls (164.32,104.07) and (169.03,99.38) .. (174.85,99.37) ;  
            	\draw  [draw opacity=0][fill={rgb, 255:red, 186; green, 180; blue, 180 }  ,fill opacity=0.67 ] (194.09,120.84) .. controls (194.09,118.66) and (199.18,116.88) .. (205.45,116.88) .. controls (211.72,116.88) and (216.8,118.66) .. (216.8,120.84) .. controls (216.8,123.03) and (211.72,124.8) .. (205.45,124.8) .. controls (199.18,124.8) and (194.09,123.03) .. (194.09,120.84) -- cycle ;
            	\path  [shading=_z9l2hd6b8,_08f3gd1r9] (189.13,109.82) .. controls (189.13,102.63) and (194.96,96.8) .. (202.15,96.8) .. controls (209.35,96.8) and (215.17,102.63) .. (215.17,109.82) .. controls (215.17,117.01) and (209.35,122.84) .. (202.15,122.84) .. controls (194.96,122.84) and (189.13,117.01) .. (189.13,109.82) -- cycle ; 
            	\draw   (189.13,109.82) .. controls (189.13,102.63) and (194.96,96.8) .. (202.15,96.8) .. controls (209.35,96.8) and (215.17,102.63) .. (215.17,109.82) .. controls (215.17,117.01) and (209.35,122.84) .. (202.15,122.84) .. controls (194.96,122.84) and (189.13,117.01) .. (189.13,109.82) -- cycle ; 
            	\draw  [draw opacity=0] (191.4,110.34) .. controls (191.39,110.17) and (191.38,109.99) .. (191.38,109.82) .. controls (191.38,103.87) and (196.23,99.04) .. (202.22,99.04) -- (202.24,109.82) -- cycle ; \draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ] (191.4,110.34) .. controls (191.39,110.17) and (191.38,109.99) .. (191.38,109.82) .. controls (191.38,103.87) and (196.23,99.04) .. (202.22,99.04) ;  
            	\draw  [draw opacity=0][fill={rgb, 255:red, 186; green, 180; blue, 180 }  ,fill opacity=0.67 ] (221.29,122.44) .. controls (221.29,120.26) and (226.38,118.48) .. (232.65,118.48) .. controls (238.92,118.48) and (244,120.26) .. (244,122.44) .. controls (244,124.63) and (238.92,126.4) .. (232.65,126.4) .. controls (226.38,126.4) and (221.29,124.63) .. (221.29,122.44) -- cycle ;
            	\path  [shading=_c889qlf3z,_efbctp1mv] (216.33,111.42) .. controls (216.33,104.23) and (222.16,98.4) .. (229.35,98.4) .. controls (236.55,98.4) and (242.37,104.23) .. (242.37,111.42) .. controls (242.37,118.61) and (236.55,124.44) .. (229.35,124.44) .. controls (222.16,124.44) and (216.33,118.61) .. (216.33,111.42) -- cycle ; 
            	\draw   (216.33,111.42) .. controls (216.33,104.23) and (222.16,98.4) .. (229.35,98.4) .. controls (236.55,98.4) and (242.37,104.23) .. (242.37,111.42) .. controls (242.37,118.61) and (236.55,124.44) .. (229.35,124.44) .. controls (222.16,124.44) and (216.33,118.61) .. (216.33,111.42) -- cycle ; 
            	\draw  [draw opacity=0] (218.6,111.94) .. controls (218.59,111.77) and (218.58,111.59) .. (218.58,111.42) .. controls (218.58,105.47) and (223.43,100.64) .. (229.42,100.64) -- (229.44,111.42) -- cycle ; \draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ] (218.6,111.94) .. controls (218.59,111.77) and (218.58,111.59) .. (218.58,111.42) .. controls (218.58,105.47) and (223.43,100.64) .. (229.42,100.64) ;  
            	\draw  [draw opacity=0][fill={rgb, 255:red, 186; green, 180; blue, 180 }  ,fill opacity=0.67 ] (248.35,122.75) .. controls (248.35,120.63) and (253.29,118.91) .. (259.38,118.91) .. controls (265.47,118.91) and (270.41,120.63) .. (270.41,122.75) .. controls (270.41,124.88) and (265.47,126.6) .. (259.38,126.6) .. controls (253.29,126.6) and (248.35,124.88) .. (248.35,122.75) -- cycle ;
            	\path  [shading=_qpgi75qlm,_0s4gsuo1m] (243.53,112.05) .. controls (243.53,105.06) and (249.2,99.4) .. (256.18,99.4) .. controls (263.17,99.4) and (268.83,105.06) .. (268.83,112.05) .. controls (268.83,119.03) and (263.17,124.7) .. (256.18,124.7) .. controls (249.2,124.7) and (243.53,119.03) .. (243.53,112.05) -- cycle ; 
            	\draw   (243.53,112.05) .. controls (243.53,105.06) and (249.2,99.4) .. (256.18,99.4) .. controls (263.17,99.4) and (268.83,105.06) .. (268.83,112.05) .. controls (268.83,119.03) and (263.17,124.7) .. (256.18,124.7) .. controls (249.2,124.7) and (243.53,119.03) .. (243.53,112.05) -- cycle ;  
            	\draw  [draw opacity=0] (245.73,112.55) .. controls (245.72,112.38) and (245.72,112.22) .. (245.72,112.05) .. controls (245.72,106.27) and (250.43,101.58) .. (256.25,101.57) -- (256.26,112.05) -- cycle ; \draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ] (245.73,112.55) .. controls (245.72,112.38) and (245.72,112.22) .. (245.72,112.05) .. controls (245.72,106.27) and (250.43,101.58) .. (256.25,101.57) ;  
            	\draw  [draw opacity=0][fill={rgb, 255:red, 181; green, 208; blue, 240 }  ,fill opacity=0.44 ] (124,73.03) -- (272.6,73.03) -- (272.6,129.33) -- (124,129.33) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 163; green, 194; blue, 230 }  ,fill opacity=0.62 ] (296.68,48.88) -- (296.76,105.15) -- (272.6,129.33) -- (272.6,73.03) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.41 ] (219.18,72.8) -- (232.54,72.8) -- (207.66,129.14) -- (194.3,129.14) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.41 ] (244.77,73.67) -- (250.56,73.67) -- (225.58,130) -- (219.8,130) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.38 ] (187.47,73.33) -- (137.47,129.33) -- (179.47,130) -- (205.13,73.33) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.55 ] (160.13,73.33) -- (141.13,96.33) -- (146.13,73.33) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 186; green, 180; blue, 180 }  ,fill opacity=0.67 ] (151.62,139.89) .. controls (151.62,137.76) and (156.55,136.04) .. (162.65,136.04) .. controls (168.74,136.04) and (173.68,137.76) .. (173.68,139.89) .. controls (173.68,142.01) and (168.74,143.73) .. (162.65,143.73) .. controls (156.55,143.73) and (151.62,142.01) .. (151.62,139.89) -- cycle ;
            	\path  [shading=_2jaimmkfh,_wxk5uzbxt] (146.8,129.18) .. controls (146.8,122.2) and (152.46,116.53) .. (159.45,116.53) .. controls (166.43,116.53) and (172.1,122.2) .. (172.1,129.18) .. controls (172.1,136.17) and (166.43,141.83) .. (159.45,141.83) .. controls (152.46,141.83) and (146.8,136.17) .. (146.8,129.18) -- cycle ; 
            	\draw   (146.8,129.18) .. controls (146.8,122.2) and (152.46,116.53) .. (159.45,116.53) .. controls (166.43,116.53) and (172.1,122.2) .. (172.1,129.18) .. controls (172.1,136.17) and (166.43,141.83) .. (159.45,141.83) .. controls (152.46,141.83) and (146.8,136.17) .. (146.8,129.18) -- cycle ; 
            	\draw  [draw opacity=0] (149,129.68) .. controls (148.99,129.52) and (148.99,129.35) .. (148.99,129.18) .. controls (148.99,123.4) and (153.7,118.71) .. (159.51,118.71) -- (159.53,129.18) -- cycle ; \draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ] (149,129.68) .. controls (148.99,129.52) and (148.99,129.35) .. (148.99,129.18) .. controls (148.99,123.4) and (153.7,118.71) .. (159.51,118.71) ;  
            	\draw  [draw opacity=0][fill={rgb, 255:red, 186; green, 180; blue, 180 }  ,fill opacity=0.67 ] (135.62,150.55) .. controls (135.62,148.43) and (140.55,146.71) .. (146.65,146.71) .. controls (152.74,146.71) and (157.68,148.43) .. (157.68,150.55) .. controls (157.68,152.68) and (152.74,154.4) .. (146.65,154.4) .. controls (140.55,154.4) and (135.62,152.68) .. (135.62,150.55) -- cycle ;
            	\path  [shading=_qvdbejarw,_057kuimsq] (130.8,139.85) .. controls (130.8,132.86) and (136.46,127.2) .. (143.45,127.2) .. controls (150.43,127.2) and (156.1,132.86) .. (156.1,139.85) .. controls (156.1,146.83) and (150.43,152.5) .. (143.45,152.5) .. controls (136.46,152.5) and (130.8,146.83) .. (130.8,139.85) -- cycle ;  
            	\draw   (130.8,139.85) .. controls (130.8,132.86) and (136.46,127.2) .. (143.45,127.2) .. controls (150.43,127.2) and (156.1,132.86) .. (156.1,139.85) .. controls (156.1,146.83) and (150.43,152.5) .. (143.45,152.5) .. controls (136.46,152.5) and (130.8,146.83) .. (130.8,139.85) -- cycle ; 
            	\draw  [draw opacity=0] (133,140.35) .. controls (132.99,140.18) and (132.99,140.02) .. (132.99,139.85) .. controls (132.99,134.07) and (137.7,129.38) .. (143.51,129.37) -- (143.53,139.85) -- cycle ; \draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ] (133,140.35) .. controls (132.99,140.18) and (132.99,140.02) .. (132.99,139.85) .. controls (132.99,134.07) and (137.7,129.38) .. (143.51,129.37) ;  
            	\draw  [draw opacity=0][fill={rgb, 255:red, 186; green, 180; blue, 180 }  ,fill opacity=0.67 ] (167.89,152.31) .. controls (167.89,150.12) and (172.98,148.35) .. (179.25,148.35) .. controls (185.52,148.35) and (190.6,150.12) .. (190.6,152.31) .. controls (190.6,154.49) and (185.52,156.27) .. (179.25,156.27) .. controls (172.98,156.27) and (167.89,154.49) .. (167.89,152.31) -- cycle ;
            	\path  [shading=_3bkvylu9b,_7mikztv3r] (162.93,141.29) .. controls (162.93,134.1) and (168.76,128.27) .. (175.95,128.27) .. controls (183.15,128.27) and (188.97,134.1) .. (188.97,141.29) .. controls (188.97,148.48) and (183.15,154.31) .. (175.95,154.31) .. controls (168.76,154.31) and (162.93,148.48) .. (162.93,141.29) -- cycle ; 
            	\draw   (162.93,141.29) .. controls (162.93,134.1) and (168.76,128.27) .. (175.95,128.27) .. controls (183.15,128.27) and (188.97,134.1) .. (188.97,141.29) .. controls (188.97,148.48) and (183.15,154.31) .. (175.95,154.31) .. controls (168.76,154.31) and (162.93,148.48) .. (162.93,141.29) -- cycle ; 
            	\draw  [draw opacity=0] (165.2,141.8) .. controls (165.19,141.63) and (165.18,141.46) .. (165.18,141.29) .. controls (165.18,135.34) and (170.03,130.51) .. (176.02,130.5) -- (176.04,141.29) -- cycle ; \draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ] (165.2,141.8) .. controls (165.19,141.63) and (165.18,141.46) .. (165.18,141.29) .. controls (165.18,135.34) and (170.03,130.51) .. (176.02,130.5) ;  
            \end{tikzpicture} \end{center}'''

                # Câu hỏi
                noidungcauhoi = (r'''Một hộp chứa $%s$ viên bi xanh và $%s$ viên bi đỏ. Bạn Hòa lấy ngẫu nhiên $1$ viên bi từ hộp, xem màu, rồi bỏ ra ngoài.%s - Nếu viên bi Hòa lấy ra có màu xanh, bạn Bình sẽ lấy ra ngẫu nhiên $2$ viên bi từ hộp.\\- Nếu viên bi Hòa lấy ra có màu đỏ, bạn Bình sẽ lấy ra ngẫu nhiên $3$ viên bi từ hộp.\\ Xác suất để Hòa lấy được viên bi màu xanh, biết rằng tất cả các viên bi được hai bạn chọn ra đều có đủ cả hai màu bằng bao nhiêu? (làm tròn kết quả đến hàng phần trăm).'''
                                 % (xanh, do, hinhve))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Gọi $A$ là biến cố: "Hòa lấy được bi xanh" $\\Rightarrow \\overline{A}$ là biến cố: "Hòa lấy được bi màu đỏ" \\\\
            $B$ là biến cố: "tất cả các bi lấy ra đều có đủ hai màu" $\\Rightarrow \\overline{B}$ là biến cố: "tất cả các bi lấy ra cùng một màu" \\\\
            Ta có $P\\left(A\\right)=\\frac{%s}{%s}=%s; P\\left(\\overline{A}\\right)=1-%s=%s$. \\\\
            $P\\left(\\overline{B}|A\\right)=\\frac{C_{%s}^2}{C_{%s}^2}=%s \\Rightarrow P\\left(B|A\\right)=1-%s=%s$. \\\\
            $P\\left(\\overline{B}|\\overline{A}\\right)=\\frac{C_{%s}^3}{C_{%s}^3}=%s \\Rightarrow P\\left(B|\\overline{A}\\right)=1-%s=%s$. \\\\
            Yêu cầu bài toán tính $P\\left(A|B\\right)$. \\\\
            $P\\left(A|B\\right)=\\frac{P\\left(AB\\right)}{P\\left(B\\right)}$ \\\\
            $P\\left(AB\\right)=P\\left(B|A\\right)P\\left(A\\right)=%s \\cdot %s=%s$. \\\\
            $P\\left(B\\right)=P\\left(B|A\\right)P\\left(A\\right)+P\\left(B|\\overline{A}\\right)P\\left(\\overline{A}\\right)=%s \\cdot %s+%s \\cdot %s=%s$. \\\\
            Vậy $P\\left(A|B\\right)=%s \\approx %s$.''' 
                         % (xanh, tong, latex(P_A), latex(P_A), latex(P_A_bar),
                            xanh-1, tong-1, latex(P_B_bar_A), latex(P_B_bar_A), latex(P_B_A),
                            do-1, tong-1, latex(P_B_bar_A_bar), latex(P_B_bar_A_bar), latex(P_B_A_bar),
                            latex(P_B_A), latex(P_A), latex(P_AB),
                            latex(P_B_A), latex(P_A), latex(P_B_A_bar), latex(P_A_bar), latex(P_B),
                            latex(kq_frac), kq_dec))
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq_dec))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content

