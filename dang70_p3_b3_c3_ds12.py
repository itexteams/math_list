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


def bt_dang70_p3_b3_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            # Hàm phụ để hiển thị số dạng 1.5 -> 1,5 hoặc 2.0 -> 2
            def fmt(num):
                if num == int(num):
                    return str(int(num))
                return str(num).replace('.', ',')

            if dang=='1':
                # Random thông số a, b của elip và r của lỗ khoan
                a = random.choice([1.5,1.2,1.3,1.4])
                b = random.choice([1.0])
                r = random.choice([0.2, 0.3, 0.4, 0.5])

                # Ràng buộc lỗ khoan không được to hơn bán trục nhỏ của elip
                while r >= b:
                    r = random.choice([0.2, 0.3, 0.4, 0.5])

                # Khởi tạo các biến Sympy để biểu diễn nghiệm và công thức dưới dạng phân số đẹp mắt
                x_sym = sp.Symbol('x')
                a_sym = sp.Rational(str(a))
                b_sym = sp.Rational(str(b))
                r_sym = sp.Rational(str(r))

                # Tính cận giao điểm x0
                x0_sym = a_sym * sp.sqrt(1 - (r_sym/b_sym)**2)
                x0_latex = sp.latex(x0_sym).replace('.', ',')

                # Hàm số dưới dấu tích phân và nguyên hàm
                integrand = b_sym**2 - r_sym**2 - (b_sym**2 / a_sym**2) * x_sym**2
                integrand_latex = sp.latex(integrand).replace('.', ',')
                antideriv = sp.integrate(integrand, x_sym)
                antideriv_latex = sp.latex(antideriv).replace('.', ',')

                # Tính thể tích (Chính xác bằng biểu thức toán học và Làm tròn số thập phân)
                V_exact_sym = 2 * sp.pi * sp.integrate(integrand, (x_sym, 0, x0_sym))
                V_exact_latex = sp.latex(V_exact_sym).replace('.', ',')

                V_exact_val = float(V_exact_sym.evalf())
                V_rounded = round(V_exact_val, 2)

                # Kết quả chuỗi đổi dấu phẩy
                kq = str(V_rounded).replace('.', ',')

                # Các đáp án trắc nghiệm
                du = ['$%s$'%(kq)]
                da = random.choice(du)

                # Sinh các đáp án nhiễu (Dựa trên sai lầm thường gặp như quên nhân số Pi, quên nhân đôi do tính chẵn,...)
                v_wrong_1 = round(V_exact_val / math.pi, 2)
                v_wrong_2 = round(V_exact_val / 2, 2)
                v_wrong_3 = round(V_exact_val + 0.46, 2)
                v_wrong_4 = round(abs(V_exact_val - 0.27), 2)
                v_wrong_5 = round(V_exact_val * 2, 2)

                fake_pool = list(set([v_wrong_1, v_wrong_2, v_wrong_3, v_wrong_4, v_wrong_5]))
                if V_rounded in fake_pool: 
                    fake_pool.remove(V_rounded)

                s = ['$%s$' % str(f).replace('.', ',') for f in random.sample(fake_pool, 3)]

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]
                hinhve=r'''\begin{center}
            	\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            			\tikzset {_a6ksm3p3l/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{-90 }  \pgftransformscale{2 }  }}}
            		\pgfdeclarehorizontalshading{_w3irhzoe2}{150bp}{rgb(0bp)=(0.61,0.61,0.61);
            			rgb(37.5bp)=(0.61,0.61,0.61);
            			rgb(50bp)=(1,1,1);
            			rgb(62.5bp)=(0.58,0.73,0.91);
            			rgb(100bp)=(0.58,0.73,0.91)}
            		\tikzset {_r5ejtcpbu/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{-271 }  \pgftransformscale{2 }  }}}
            		\pgfdeclarehorizontalshading{_676ssom5j}{150bp}{rgb(0bp)=(0.49,0.83,0.13);
            			rgb(37.5bp)=(0.49,0.83,0.13);
            			rgb(62.5bp)=(0,0.5,0.5);
            			rgb(100bp)=(0,0.5,0.5)}
            		\tikzset {_u82jbcrhi/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{-90 }  \pgftransformscale{2 }  }}}
            		\pgfdeclarehorizontalshading{_xgai4fjm5}{150bp}{rgb(0bp)=(0.49,0.83,0.13);
            			rgb(37.5bp)=(0.49,0.83,0.13);
            			rgb(62.5bp)=(0,0.5,0.5);
            			rgb(100bp)=(0,0.5,0.5)}
            		\tikzset {_e3kcdkgxw/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{-271 }  \pgftransformscale{2 }  }}}
            		\pgfdeclarehorizontalshading{_amb8r5y2a}{150bp}{rgb(0bp)=(0.49,0.83,0.13);
            			rgb(37.5bp)=(0.49,0.83,0.13);
            			rgb(62.5bp)=(0,0.5,0.5);
            			rgb(100bp)=(0,0.5,0.5)}
            		\tikzset{every picture/.style={line width=0.75pt}} 	
            		\draw  [line width=1]  (75.84,112.52) .. controls (75.84,83.92) and (109.68,60.74) .. (151.42,60.74) .. controls (193.16,60.74) and (227,83.92) .. (227,112.52) .. controls (227,141.11) and (193.16,164.29) .. (151.42,164.29) .. controls (109.68,164.29) and (75.84,141.11) .. (75.84,112.52) -- cycle ;
            		\draw [line width=1]  [dash pattern={on 1.69pt off 2.76pt}]  (75.84,112.52) -- (227,112.52) ;
            		\draw [line width=1]  [dash pattern={on 1.69pt off 2.76pt}]  (77.5,123.04) -- (225.34,123.04) ;
            		\draw [line width=1]  [dash pattern={on 1.69pt off 2.76pt}]  (78.05,100.89) -- (225.34,100.89) ;
            		\draw [line width=1]  [dash pattern={on 1.69pt off 2.76pt}]  (272.41,112.52) -- (423.58,112.52) ;
            		\draw  [draw opacity=0][line width=1]  (152.88,164.14) .. controls (152.74,164.24) and (152.59,164.3) .. (152.44,164.3) .. controls (149.32,164.3) and (146.79,141.02) .. (146.79,112.3) .. controls (146.79,83.92) and (149.26,60.85) .. (152.33,60.31) -- (152.44,112.3) -- cycle ; \draw  [line width=1]  (152.88,164.14) .. controls (152.74,164.24) and (152.59,164.3) .. (152.44,164.3) .. controls (149.32,164.3) and (146.79,141.02) .. (146.79,112.3) .. controls (146.79,83.92) and (149.26,60.85) .. (152.33,60.31) ;  
            		\draw  [draw opacity=0][dash pattern={on 5.63pt off 4.5pt}][line width=1]  (151.78,164.04) .. controls (151.93,164.2) and (152.07,164.29) .. (152.22,164.29) .. controls (154.68,164.29) and (156.68,141.01) .. (156.68,112.29) .. controls (156.68,84) and (154.74,60.99) .. (152.33,60.31) -- (152.22,112.29) -- cycle ; \draw  [dash pattern={on 5.63pt off 4.5pt}][line width=1]  (151.78,164.04) .. controls (151.93,164.2) and (152.07,164.29) .. (152.22,164.29) .. controls (154.68,164.29) and (156.68,141.01) .. (156.68,112.29) .. controls (156.68,84) and (154.74,60.99) .. (152.33,60.31) ;  
            		\draw  [draw opacity=0][line width=1]  (103.14,150.88) .. controls (103.03,150.96) and (102.92,151) .. (102.81,151) .. controls (100.45,151) and (98.54,133.4) .. (98.54,111.69) .. controls (98.54,90.23) and (100.41,72.78) .. (102.73,72.38) -- (102.81,111.69) -- cycle ; \draw  [line width=1]  (103.14,150.88) .. controls (103.03,150.96) and (102.92,151) .. (102.81,151) .. controls (100.45,151) and (98.54,133.4) .. (98.54,111.69) .. controls (98.54,90.23) and (100.41,72.78) .. (102.73,72.38) ;  
            		\draw  [draw opacity=0][dash pattern={on 5.63pt off 4.5pt}][line width=1]  (101.95,150.81) .. controls (102.06,150.94) and (102.17,151) .. (102.29,151) .. controls (104.15,151) and (105.66,133.4) .. (105.66,111.69) .. controls (105.66,90.29) and (104.19,72.89) .. (102.37,72.38) -- (102.29,111.69) -- cycle ; \draw  [dash pattern={on 5.63pt off 4.5pt}][line width=1]  (101.95,150.81) .. controls (102.06,150.94) and (102.17,151) .. (102.29,151) .. controls (104.15,151) and (105.66,133.4) .. (105.66,111.69) .. controls (105.66,90.29) and (104.19,72.89) .. (102.37,72.38) ;  
            		\draw  [draw opacity=0][line width=1]  (200.05,152.54) .. controls (199.94,152.62) and (199.83,152.66) .. (199.71,152.66) .. controls (197.35,152.66) and (195.44,135.06) .. (195.44,113.35) .. controls (195.44,91.89) and (197.31,74.44) .. (199.63,74.04) -- (199.71,113.35) -- cycle ; \draw  [line width=1]  (200.05,152.54) .. controls (199.94,152.62) and (199.83,152.66) .. (199.71,152.66) .. controls (197.35,152.66) and (195.44,135.06) .. (195.44,113.35) .. controls (195.44,91.89) and (197.31,74.44) .. (199.63,74.04) ;  
            		\draw  [draw opacity=0][dash pattern={on 5.63pt off 4.5pt}][line width=1]  (198.85,152.47) .. controls (198.96,152.6) and (199.08,152.66) .. (199.19,152.66) .. controls (201.05,152.66) and (202.56,135.06) .. (202.56,113.35) .. controls (202.56,91.95) and (201.09,74.55) .. (199.27,74.04) -- (199.19,113.35) -- cycle ; \draw  [dash pattern={on 5.63pt off 4.5pt}][line width=1]  (198.85,152.47) .. controls (198.96,152.6) and (199.08,152.66) .. (199.19,152.66) .. controls (201.05,152.66) and (202.56,135.06) .. (202.56,113.35) .. controls (202.56,91.95) and (201.09,74.55) .. (199.27,74.04) ;  
            		\draw [line width=1]    (224.24,100.89) -- (224.24,123.04) ;
            		\draw [line width=1]    (227,112.52) -- (257.34,112.52) ;
            		\draw [shift={(261.34,112.52)}, rotate = 180] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (15.6,-3.9) -- (0,0) -- (15.6,3.9) -- cycle    ;
            		\draw [line width=1]    (152.33,60.31) -- (152.33,33.73) ;
            		\draw [shift={(152.33,29.73)}, rotate = 90] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (15.6,-3.9) -- (0,0) -- (15.6,3.9) -- cycle    ;
            		\draw [line width=1]    (75.84,112.52) -- (55.9,112.52) ;
            		\path  [shading=_w3irhzoe2,_a6ksm3p3l] (6.08,121.75) -- (6.08,101.75) -- (42.07,101.77) -- (50.38,111.77) -- (42.07,121.76) -- cycle ; 
            		\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.39 ][line width=1]  (6.08,121.75) -- (6.08,101.75) -- (42.07,101.77) -- (50.38,111.77) -- (42.07,121.76) -- cycle ; 
            		\path  [shading=_676ssom5j,_r5ejtcpbu] (273.14,101.89) .. controls (279.67,78.55) and (310.7,60.87) .. (347.99,60.87) .. controls (385.63,60.87) and (416.89,78.88) .. (423.03,102.53) -- cycle ; 
            		\draw  [line width=1]  (273.14,101.89) .. controls (279.67,78.55) and (310.7,60.87) .. (347.99,60.87) .. controls (385.63,60.87) and (416.89,78.88) .. (423.03,102.53) -- cycle ; 
            		\path  [shading=_xgai4fjm5,_u82jbcrhi] (423.44,122.81) .. controls (416.95,146.58) and (385.76,164.59) .. (348.27,164.59) .. controls (310.44,164.59) and (279.03,146.25) .. (272.93,122.17) -- cycle ; 
            		\draw  [line width=1]  (423.44,122.81) .. controls (416.95,146.58) and (385.76,164.59) .. (348.27,164.59) .. controls (310.44,164.59) and (279.03,146.25) .. (272.93,122.17) -- cycle ; 
            		\draw  [line width=1]  (271.86,112.38) .. controls (271.86,107.1) and (272.85,102.83) .. (274.07,102.83) .. controls (275.29,102.83) and (276.29,107.1) .. (276.29,112.38) .. controls (276.29,117.65) and (275.29,121.93) .. (274.07,121.93) .. controls (272.85,121.93) and (271.86,117.65) .. (271.86,112.38) -- cycle ;
            		\draw  [line width=1]  (420.8,112.44) .. controls (420.8,107.16) and (421.79,102.89) .. (423.01,102.89) .. controls (424.23,102.89) and (425.23,107.16) .. (425.23,112.44) .. controls (425.23,117.72) and (424.23,121.99) .. (423.01,121.99) .. controls (421.79,121.99) and (420.8,117.72) .. (420.8,112.44) -- cycle ;
            		\draw  [draw opacity=0][line width=1]  (348.91,164.69) .. controls (348.76,164.8) and (348.61,164.85) .. (348.46,164.85) .. controls (345.34,164.85) and (342.81,141.57) .. (342.81,112.85) .. controls (342.81,84.47) and (345.28,61.4) .. (348.35,60.87) -- (348.46,112.85) -- cycle ; \draw  [line width=1]  (348.91,164.69) .. controls (348.76,164.8) and (348.61,164.85) .. (348.46,164.85) .. controls (345.34,164.85) and (342.81,141.57) .. (342.81,112.85) .. controls (342.81,84.47) and (345.28,61.4) .. (348.35,60.87) ;  
            		\draw  [draw opacity=0][dash pattern={on 5.63pt off 4.5pt}][line width=1]  (347.8,164.59) .. controls (347.95,164.76) and (348.09,164.84) .. (348.24,164.84) .. controls (350.71,164.84) and (352.7,141.56) .. (352.7,112.85) .. controls (352.7,84.56) and (350.76,61.54) .. (348.35,60.87) -- (348.24,112.85) -- cycle ; \draw  [dash pattern={on 5.63pt off 4.5pt}][line width=1]  (347.8,164.59) .. controls (347.95,164.76) and (348.09,164.84) .. (348.24,164.84) .. controls (350.71,164.84) and (352.7,141.56) .. (352.7,112.85) .. controls (352.7,84.56) and (350.76,61.54) .. (348.35,60.87) ;  
            		\path  [shading=_amb8r5y2a,_e3kcdkgxw] (465.66,102.53) .. controls (472.2,79.19) and (503.23,61.51) .. (540.52,61.51) .. controls (577.67,61.51) and (608.6,79.05) .. (615.3,102.25) -- cycle ; 
            		\draw  [line width=1]  (465.66,102.53) .. controls (472.2,79.19) and (503.23,61.51) .. (540.52,61.51) .. controls (577.67,61.51) and (608.6,79.05) .. (615.3,102.25) -- cycle ;  
            		\draw [line width=1]    (442.41,102.53) -- (652.27,102.53) ;
            		\draw [line width=1]    (442.41,112.5) -- (648.27,112.5) ;
            		\draw [shift={(652.27,112.5)}, rotate = 180] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (15.6,-3.9) -- (0,0) -- (15.6,3.9) -- cycle    ;
            		\draw [line width=1]    (465.66,102.53) -- (465.66,111.69) ;
            		\draw [line width=1]    (615.3,102.25) -- (615.3,111.4) ;
            		\draw [line width=1]    (540.97,124.68) -- (540.97,33.73) ;
            		\draw [shift={(540.97,29.73)}, rotate = 90] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (15.6,-3.9) -- (0,0) -- (15.6,3.9) -- cycle    ;
            		\draw [line width=1]    (152.88,164.14) -- (152.88,178.13) ;
            		\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (152.33,60.31) -- (151.78,164.04) ;
            		\draw [line width=1]    (34.67,148.33) -- (62.06,117.15) ;
            		\draw [shift={(64.7,114.15)}, rotate = 131.3] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (15.6,-3.9) -- (0,0) -- (15.6,3.9) -- cycle    ;
            		\draw [line width=1]    (52.53,52.8) -- (87.87,102.15) ;
            		\draw [shift={(90.2,105.4)}, rotate = 234.39] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (15.6,-3.9) -- (0,0) -- (15.6,3.9) -- cycle    ;
            		\draw [line width=1]    (91.7,100.9) -- (91.45,112.4) ;
            		\draw (11.33,34.67) node [anchor=north west][inner sep=0.75pt]  [font=\scriptsize] [align=left] {Bán kính lỗ khoan};
            		\draw (4,148.67) node [anchor=north west][inner sep=0.75pt]  [font=\scriptsize] [align=left] {Trục xoay};
            		\draw (2.67,80.67) node [anchor=north west][inner sep=0.75pt]  [font=\scriptsize] [align=left] {Mũi khoan};
            		\draw (526.67,33) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$y$};
            		\draw (630,119) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$x$};
            		\draw (524.67,112.67) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$O$};
            		\draw (137.33,33) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$y$};
            		\draw (240.67,119) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$x$};
            		\draw (131.33,107.33) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$O$};
            	\end{tikzpicture}
            \end{center}'''
                # Câu hỏi
                noidungcauhoi = (r'''Để chế tác một hạt cườm, người ta lấy một khối vật thể có dạng một khối tròn xoay được tạo thành khi quay hình phẳng giới hạn bởi trục $Ox$ và nửa trên của elip $\frac{x^2}{%s^2} + \frac{y^2}{%s^2} = 1$ (một đơn vị dài trên mỗi trục tọa độ tương ứng với một xăng-ti-mét trong thực tế) quanh trục $Ox$; sau đó khoan dọc theo trục xoay. Lỗ khoan có dạng hình trụ với bán kính $%s$ cm và có trục nằm trên trục xoay. Phần còn lại sau khi khoan là hạt cườm, có dạng một khối tròn xoay. Thể tích của hạt cườm đó bằng bao nhiêu xăng-ti-mét khối (không làm tròn kết quả các phép tính trung gian, chỉ làm tròn kết quả cuối cùng đến hàng phần trăm)? %s'''
                                 % (fmt(a), fmt(b), fmt(r), hinhve))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Xử lý text để hiển thị "1" thay vì "1\sqrt{...}" ở lời giải
                b_str = '' if fmt(b) == '1' else fmt(b)

                # Nội dung lời giải (Chèn Sympy để render phân số, căn thức cho chuẩn đẹp)
                loigiai_raw = ('''Từ phương trình elip, ta có phương trình nửa trên của elip là $y = %s\\sqrt{1 - \\frac{x^2}{%s^2}}$.\\\\
            Lỗ khoan hình trụ có bán kính $r = %s$, cắt mặt ngoài của hạt cườm tại các điểm có tung độ $y = %s$.
            Hoành độ giao điểm là nghiệm của phương trình:
            $$ %s\\sqrt{1 - \\frac{x^2}{%s^2}} = %s \\Leftrightarrow 1 - \\frac{x^2}{%s^2} = \\left(\\frac{%s}{%s}\\right)^2 \\Leftrightarrow x = \\pm %s$$
            Thể tích khối hạt cườm là phần thể tích khối tròn xoay sinh ra bởi nửa elip khi quay quanh $Ox$ trừ đi thể tích khối trụ.
            $$V = \\pi \\int_{-%s}^{%s} \\left[ \\left(%s \\sqrt{1 - \\frac{x^2}{%s^2}}\\right)^2 - %s^2 \\right] \\mathrm{d}x$$
            Do tính chẵn của hàm số, ta có:
            $$V = 2\\pi \\int_{0}^{%s} \\left( %s \\right) \\mathrm{d}x = 2\\pi \\left[ %s \\right]_0^{%s} = %s \\approx %s \\text{ (cm}^3\\text{)}.$$'''
                           % (b_str, fmt(a),
                              fmt(r), fmt(r),
                              b_str, fmt(a), fmt(r), fmt(a), fmt(r), fmt(b), x0_latex,
                              x0_latex, x0_latex, b_str, fmt(a), fmt(r),
                              x0_latex, integrand_latex, antideriv_latex, x0_latex, V_exact_latex, kq))

                # Chuẩn hóa triệt để dấu + - theo yêu cầu
                loigiai = loigiai_raw.replace('+ -', '- ').replace('- -', '+ ')
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

