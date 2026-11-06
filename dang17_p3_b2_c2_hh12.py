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


def bt_dang17_p3_b2_c2_hh12(self):
            # Khai báo biến
            # Danh sách các bộ số (h, R, D) thỏa mãn điều kiện và HM_min < h*sqrt(3) để tồn tại M_max
            lis_params = [
                (4, 3, 6),   # D-R=3, h=4 => m_min=5. M_max=8. Tổng=13. (Đề gốc)
                (12, 5, 10), # D-R=5, h=12 => m_min=13. M_max=24. Tổng=37.
                (8, 2, 8),   # D-R=6, h=8 => m_min=10. M_max=16. Tổng=26.
                (3, 1, 5),   # D-R=4, h=3 => m_min=5. M_max=6. Tổng=11.
                (15, 7, 15)  # D-R=8, h=15 => m_min=17. M_max=30. Tổng=47.
            ]

            h, R, D = random.choice(lis_params)

            # Tạo phương trình đường thẳng d: ax + by - D*sqrt(a^2+b^2) = 0
            # Chọn (a,b) là (3,4) hoặc (5,12) hoặc (8,15)
            ab_triples = [(3, 4, 5), (5, 12, 13), (8, 15, 17)]
            a, b, c_sqrt = random.choice(ab_triples)

            # Tính các hệ số cho phương trình tham số của d
            # ax + by = D * c_sqrt
            # Ví dụ: 3x + 4y = 30 => x = 10 - 4/3 y. Đặt y = -3t => x = 10 + 4t.
            val_c = D * c_sqrt
            x0 = Rational(val_c, a)
            y_coeff = -b
            x_coeff = a # Để đơn giản hóa phương trình tham số

            # --- Tính toán kết quả ---
            m_min = int(sqrt((D - R)**2 + h**2))
            M_max = 2 * h
            kq_val = M_max + m_min

            # --- B4: Điều chỉnh phương án sai ---
            da = str(kq_val).replace('.', ',')
            s = [
                str(kq_val + random.randint(1, 5)).replace('.', ','),
                str(kq_val - random.randint(1, 3)).replace('.', ','),
                str(kq_val + random.randint(6, 10)).replace('.', ','),
                str(abs(kq_val - 5)).replace('.', ',')
            ]
            # Đảm bảo không trùng đáp án đúng
            s = [x for x in s if x != da]
            random.shuffle(s)

            das1, das2, das3 = s[0], s[1], s[2]

            hinhve=r'''\tikzset {_vx5qbryac/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{89.1 bp } { -108.9 bp }  }  \pgftransformscale{1.32 }  }}}
            \pgfdeclareradialshading{_4v4ti390t}{\pgfpoint{-72bp}{88bp}}{rgb(0bp)=(1,1,1);
            	rgb(0bp)=(1,1,1);
            	rgb(10.761909527438029bp)=(0.97,0.85,0.02);
            	rgb(21.773065882069723bp)=(0.19,0.17,0.08);
            	rgb(400bp)=(0.19,0.17,0.08)}
            \tikzset {_3b7bfa658/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{0 }  \pgftransformscale{2 }  }}}
            \pgfdeclarehorizontalshading{_qgeabi1q9}{150bp}{rgb(0bp)=(0,0,0);
            	rgb(38.886904077870504bp)=(0,0,0);
            	rgb(45.85118979215622bp)=(1,1,1);
            	rgb(53.351195241723744bp)=(0,0,0);
            	rgb(100bp)=(0,0,0)}
            \tikzset {_wbrk004nl/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{0 }  \pgftransformscale{2 }  }}}
            \pgfdeclarehorizontalshading{_s5dawim2z}{150bp}{rgb(0bp)=(0.97,0.91,0.11);
            	rgb(40.273813562733785bp)=(0.97,0.91,0.11);
            	rgb(44.60714616945812bp)=(1,1,1);
            	rgb(49.78571759802955bp)=(0.97,0.91,0.11);
            	rgb(62.13095532996314bp)=(0.29,0.29,0.29);
            	rgb(100bp)=(0.29,0.29,0.29)}
            \tikzset {_dvd0ne71f/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{0 }  \pgftransformscale{2 }  }}}
            \pgfdeclarehorizontalshading{_6qk4pwpou}{150bp}{rgb(0bp)=(0.97,0.91,0.11);
            	rgb(40.273813562733785bp)=(0.97,0.91,0.11);
            	rgb(44.60714616945812bp)=(1,1,1);
            	rgb(49.78571759802955bp)=(0.97,0.91,0.11);
            	rgb(62.13095532996314bp)=(0.29,0.29,0.29);
            	rgb(100bp)=(0.29,0.29,0.29)}
            \tikzset{every picture/.style={line width=0.75pt}}     
            \begin{center} \begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-0.8,xscale=0.8]
            	\draw  [draw opacity=0][fill={rgb, 255:red, 193; green, 190; blue, 190 }  ,fill opacity=1 ] (230.72,141.87) -- (277.59,142.88) -- (276.74,151.2) -- (228.61,162.68) -- cycle ;
            	\draw    (225.97,152.46) -- (403.23,198.18) ;
            	\draw [shift={(406.13,198.93)}, rotate = 194.46] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (10.72,-5.15) -- (0,0) -- (10.72,5.15) -- (7.12,0) -- cycle    ;
            	\draw    (225.97,152.46) -- (58.39,190.27) ;
            	\draw [shift={(55.47,190.93)}, rotate = 347.28] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (10.72,-5.15) -- (0,0) -- (10.72,5.15) -- (7.12,0) -- cycle    ;
            	\draw    (225.97,152.46) -- (226.13,28.6) ;
            	\draw [shift={(226.13,25.6)}, rotate = 90.08] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (10.72,-5.15) -- (0,0) -- (10.72,5.15) -- (7.12,0) -- cycle    ;
            	\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (403.39,181.14) -- (404.79,182.02) -- (405.4,184.67) -- (62.82,263.51) -- (61.43,262.63) -- (60.82,259.98) -- cycle ; \draw   (405.4,184.67) -- (404,183.79) -- (403.39,181.14) ; \draw   (404,183.79) -- (61.43,262.63) ;
            	\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (397.79,174.47) -- (399.01,175.24) -- (399.53,177.55) -- (58.67,254.62) -- (57.45,253.85) -- (56.93,251.53) -- cycle ; \draw   (399.53,177.55) -- (398.31,176.79) -- (397.79,174.47) ; \draw   (398.31,176.79) -- (57.45,253.85) ;
            	\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (70.69,262.79) -- (69.95,264.39) -- (67.11,265.32) -- (60.48,249.05) -- (61.21,247.46) -- (64.05,246.52) -- cycle ; \draw   (67.11,265.32) -- (67.84,263.73) -- (70.69,262.79) ; \draw   (67.84,263.73) -- (61.21,247.46) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.5 ]   (62.21,247.46) -- (68.84,263.73) ;
            	\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (85.94,259.54) -- (85.2,261.14) -- (82.36,262.07) -- (75.73,245.8) -- (76.46,244.21) -- (79.3,243.27) -- cycle ; \draw   (82.36,262.07) -- (83.09,260.48) -- (85.94,259.54) ; \draw   (83.09,260.48) -- (76.46,244.21) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.5 ]   (77.46,244.21) -- (84.09,260.48) ;
            	\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (101.78,254.77) -- (101.13,256.4) -- (98.34,257.48) -- (90.88,241.58) -- (91.53,239.95) -- (94.32,238.86) -- cycle ; \draw   (98.34,257.48) -- (98.99,255.85) -- (101.78,254.77) ; \draw   (98.99,255.85) -- (91.53,239.95) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.5 ]   (92.53,239.9) -- (99.99,255.8) ;
            	\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (116.15,251.68) -- (115.53,253.31) -- (112.76,254.45) -- (105.02,238.67) -- (105.64,237.03) -- (108.41,235.9) -- cycle ; \draw   (112.76,254.45) -- (113.38,252.81) -- (116.15,251.68) ; \draw   (113.38,252.81) -- (105.64,237.03) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.5 ]   (106.64,236.96) -- (114.38,252.74) ;
            	\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (130.51,248.08) -- (129.91,249.73) -- (127.16,250.91) -- (119.16,235.27) -- (119.75,233.62) -- (122.51,232.44) -- cycle ; \draw   (127.16,250.91) -- (127.75,249.26) -- (130.51,248.08) ; \draw   (127.75,249.26) -- (119.75,233.62) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.5 ]   (120.75,233.53) -- (128.75,249.17) ;
            	\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (144.29,244.82) -- (143.77,246.49) -- (141.08,247.79) -- (132.38,232.53) -- (132.89,230.85) -- (135.59,229.55) -- cycle ; \draw   (141.08,247.79) -- (141.59,246.12) -- (144.29,244.82) ; \draw   (141.59,246.12) -- (132.89,230.85) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.5 ]   (133.89,230.72) -- (142.59,245.99) ;
            	\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (158.45,241.16) -- (157.98,242.84) -- (155.32,244.22) -- (146.21,229.19) -- (146.69,227.5) -- (149.34,226.13) -- cycle ; \draw   (155.32,244.22) -- (155.79,242.53) -- (158.45,241.16) ; \draw   (155.79,242.53) -- (146.69,227.5) ; 
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.5 ]   (147.67,227.35) -- (156.78,242.37) ;
            	\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (171.95,238.41) -- (171.48,240.09) -- (168.82,241.47) -- (159.71,226.44) -- (160.19,224.75) -- (162.84,223.38) -- cycle ; \draw   (168.82,241.47) -- (169.29,239.78) -- (171.95,238.41) ; \draw   (169.29,239.78) -- (160.19,224.75) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.5 ]   (161.17,224.6) -- (170.28,239.62) ;
            	\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (184.45,235.41) -- (183.98,237.09) -- (181.32,238.47) -- (172.21,223.44) -- (172.69,221.75) -- (175.34,220.38) -- cycle ; \draw   (181.32,238.47) -- (181.79,236.78) -- (184.45,235.41) ; \draw   (181.79,236.78) -- (172.69,221.75) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.5 ]   (173.67,221.6) -- (182.78,236.62) ;
            	\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (197.24,232.1) -- (196.85,233.81) -- (194.26,235.31) -- (184.42,220.75) -- (184.81,219.04) -- (187.4,217.54) -- cycle ; \draw   (194.26,235.31) -- (194.65,233.6) -- (197.24,232.1) ; \draw   (194.65,233.6) -- (184.81,219.04) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.5 ]   (185.79,218.84) -- (195.63,233.39) ;
            	\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (210.74,229.35) -- (210.35,231.06) -- (207.76,232.56) -- (197.92,218) -- (198.31,216.29) -- (200.9,214.79) -- cycle ; \draw   (207.76,232.56) -- (208.15,230.85) -- (210.74,229.35) ; \draw   (208.15,230.85) -- (198.31,216.29) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.5 ]   (199.29,216.09) -- (209.13,230.64) ;
            	\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (223.24,226.1) -- (222.85,227.81) -- (220.26,229.31) -- (210.42,214.75) -- (210.81,213.04) -- (213.4,211.54) -- cycle ; \draw   (220.26,229.31) -- (220.65,227.6) -- (223.24,226.1) ; \draw   (220.65,227.6) -- (210.81,213.04) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.5 ]   (211.79,212.84) -- (221.63,227.39) ;
            	\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (235.59,223.23) -- (235.23,224.95) -- (232.67,226.5) -- (222.58,212.11) -- (222.94,210.4) -- (225.5,208.85) -- cycle ; \draw   (232.67,226.5) -- (233.03,224.78) -- (235.59,223.23) ; \draw   (233.03,224.78) -- (222.94,210.4) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.5 ]   (223.91,210.17) -- (234,224.56) ;
            	\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (248.09,220.73) -- (247.73,222.45) -- (245.17,224) -- (235.08,209.61) -- (235.44,207.9) -- (238,206.35) -- cycle ; \draw   (245.17,224) -- (245.53,222.28) -- (248.09,220.73) ; \draw   (245.53,222.28) -- (235.44,207.9) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.5 ]   (236.41,207.67) -- (246.5,222.06) ;
            	\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (260.09,217.98) -- (259.73,219.7) -- (257.17,221.25) -- (247.08,206.86) -- (247.44,205.15) -- (250,203.6) -- cycle ; \draw   (257.17,221.25) -- (257.53,219.53) -- (260.09,217.98) ; \draw   (257.53,219.53) -- (247.44,205.15) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.5 ]   (248.41,204.92) -- (258.5,219.31) ;
            	\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (273.03,215.26) -- (272.73,216.98) -- (270.22,218.62) -- (259.64,204.59) -- (259.94,202.86) -- (262.45,201.23) -- cycle ; \draw   (270.22,218.62) -- (270.52,216.89) -- (273.03,215.26) ; \draw   (270.52,216.89) -- (259.94,202.86) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.5 ]   (260.91,202.61) -- (271.49,216.64) ;
            	\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (284.78,212.01) -- (284.48,213.73) -- (281.97,215.37) -- (271.39,201.34) -- (271.69,199.61) -- (274.2,197.98) -- cycle ; \draw   (281.97,215.37) -- (282.27,213.64) -- (284.78,212.01) ; \draw   (282.27,213.64) -- (271.69,199.61) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.5 ]   (272.66,199.36) -- (283.24,213.39) ;
            	\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (297.47,209.01) -- (297.23,210.74) -- (294.79,212.47) -- (283.7,198.84) -- (283.93,197.1) -- (286.38,195.38) -- cycle ; \draw   (294.79,212.47) -- (295.02,210.73) -- (297.47,209.01) ; \draw   (295.02,210.73) -- (283.93,197.1) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.5 ]   (284.89,196.81) -- (295.98,210.44) ;
            	\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (309.28,205.42) -- (309.07,207.16) -- (306.65,208.91) -- (295.38,195.43) -- (295.6,193.69) -- (298.02,191.93) -- cycle ; \draw   (306.65,208.91) -- (306.86,207.17) -- (309.28,205.42) ; \draw   (306.86,207.17) -- (295.6,193.69) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.5 ]   (296.55,193.39) -- (307.81,206.87) ;
            	\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (321.53,203.42) -- (321.32,205.16) -- (318.9,206.91) -- (307.63,193.43) -- (307.85,191.69) -- (310.27,189.93) -- cycle ; \draw   (318.9,206.91) -- (319.11,205.17) -- (321.53,203.42) ; \draw   (319.11,205.17) -- (307.85,191.69) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.5 ]   (308.8,191.39) -- (320.06,204.87) ;
            	\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (333.03,200.67) -- (332.82,202.41) -- (330.4,204.16) -- (319.13,190.68) -- (319.35,188.94) -- (321.77,187.18) -- cycle ; \draw   (330.4,204.16) -- (330.61,202.42) -- (333.03,200.67) ; \draw   (330.61,202.42) -- (319.35,188.94) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.5 ]   (320.3,188.64) -- (331.56,202.12) ;
            	\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (344.69,197.94) -- (344.54,199.68) -- (342.17,201.52) -- (330.47,188.41) -- (330.63,186.66) -- (333,184.83) -- cycle ; \draw   (342.17,201.52) -- (342.33,199.77) -- (344.69,197.94) ; \draw   (342.33,199.77) -- (330.63,186.66) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.5 ]   (331.57,186.33) -- (343.27,199.44) ;
            	\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (356.67,195.08) -- (356.6,196.83) -- (354.33,198.78) -- (342,186.27) -- (342.07,184.51) -- (344.34,182.56) -- cycle ; \draw   (354.33,198.78) -- (354.4,197.03) -- (356.67,195.08) ; \draw   (354.4,197.03) -- (342.07,184.51) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.5 ]   (342.99,184.13) -- (355.32,196.65) ;
            	\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (368.17,192.33) -- (368.1,194.08) -- (365.83,196.03) -- (353.5,183.52) -- (353.57,181.76) -- (355.84,179.81) -- cycle ; \draw   (365.83,196.03) -- (365.9,194.28) -- (368.17,192.33) ; \draw   (365.9,194.28) -- (353.57,181.76) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.5 ]   (354.49,181.38) -- (366.82,193.9) ;
            	\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (378.67,189.33) -- (378.6,191.08) -- (376.33,193.03) -- (364,180.52) -- (364.07,178.76) -- (366.34,176.81) -- cycle ; \draw   (376.33,193.03) -- (376.4,191.28) -- (378.67,189.33) ; \draw   (376.4,191.28) -- (364.07,178.76) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.5 ]   (364.99,178.38) -- (377.32,190.9) ;
            	\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (390.67,186.83) -- (390.6,188.58) -- (388.33,190.53) -- (376,178.02) -- (376.07,176.26) -- (378.34,174.31) -- cycle ; \draw   (388.33,190.53) -- (388.4,188.78) -- (390.67,186.83) ; \draw   (388.4,188.78) -- (376.07,176.26) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.5 ]   (376.99,175.88) -- (389.32,188.4) ;
            	\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (402.42,184.08) -- (402.35,185.83) -- (400.08,187.78) -- (387.75,175.27) -- (387.82,173.51) -- (390.09,171.56) -- cycle ; \draw   (400.08,187.78) -- (400.15,186.03) -- (402.42,184.08) ; \draw   (400.15,186.03) -- (387.82,173.51) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.5 ]   (388.74,173.13) -- (401.07,185.65) ;
            	\path  [shading=_4v4ti390t,_vx5qbryac] (134.27,225.97) .. controls (134.27,221.82) and (137.62,218.47) .. (141.77,218.47) .. controls (145.91,218.47) and (149.27,221.82) .. (149.27,225.97) .. controls (149.27,230.11) and (145.91,233.47) .. (141.77,233.47) .. controls (137.62,233.47) and (134.27,230.11) .. (134.27,225.97) -- cycle ; 
            	\draw   (134.27,225.97) .. controls (134.27,221.82) and (137.62,218.47) .. (141.77,218.47) .. controls (145.91,218.47) and (149.27,221.82) .. (149.27,225.97) .. controls (149.27,230.11) and (145.91,233.47) .. (141.77,233.47) .. controls (137.62,233.47) and (134.27,230.11) .. (134.27,225.97) -- cycle ; 
            	\path  [shading=_qgeabi1q9,_3b7bfa658] (241.22,148.02) -- (241.22,156.9) .. controls (241.22,159.35) and (234.39,161.33) .. (225.97,161.33) .. controls (217.54,161.33) and (210.72,159.35) .. (210.72,156.9) -- (210.72,148.02) .. controls (210.72,145.57) and (217.54,143.58) .. (225.97,143.58) .. controls (234.39,143.58) and (241.22,145.57) .. (241.22,148.02) .. controls (241.22,150.47) and (234.39,152.46) .. (225.97,152.46) .. controls (217.54,152.46) and (210.72,150.47) .. (210.72,148.02) ; 
            	\draw   (241.22,148.02) -- (241.22,156.9) .. controls (241.22,159.35) and (234.39,161.33) .. (225.97,161.33) .. controls (217.54,161.33) and (210.72,159.35) .. (210.72,156.9) -- (210.72,148.02) .. controls (210.72,145.57) and (217.54,143.58) .. (225.97,143.58) .. controls (234.39,143.58) and (241.22,145.57) .. (241.22,148.02) .. controls (241.22,150.47) and (234.39,152.46) .. (225.97,152.46) .. controls (217.54,152.46) and (210.72,150.47) .. (210.72,148.02) ; 
            	\path  [shading=_s5dawim2z,_wbrk004nl] (231.72,87.14) -- (231.72,147.87) .. controls (231.72,148.84) and (229.03,149.63) .. (225.72,149.63) .. controls (222.4,149.63) and (219.72,148.84) .. (219.72,147.87) -- (219.72,87.14) .. controls (219.72,86.17) and (222.4,85.38) .. (225.72,85.38) .. controls (229.03,85.38) and (231.72,86.17) .. (231.72,87.14) .. controls (231.72,88.12) and (229.03,88.91) .. (225.72,88.91) .. controls (222.4,88.91) and (219.72,88.12) .. (219.72,87.14) ; 
            	\draw   (231.72,87.14) -- (231.72,147.87) .. controls (231.72,148.84) and (229.03,149.63) .. (225.72,149.63) .. controls (222.4,149.63) and (219.72,148.84) .. (219.72,147.87) -- (219.72,87.14) .. controls (219.72,86.17) and (222.4,85.38) .. (225.72,85.38) .. controls (229.03,85.38) and (231.72,86.17) .. (231.72,87.14) .. controls (231.72,88.12) and (229.03,88.91) .. (225.72,88.91) .. controls (222.4,88.91) and (219.72,88.12) .. (219.72,87.14) ; 
            	\path  [shading=_6qk4pwpou,_dvd0ne71f] (233.62,76.8) -- (233.62,86.82) .. controls (233.62,87.97) and (230.14,88.91) .. (225.84,88.91) .. controls (221.54,88.91) and (218.05,87.97) .. (218.05,86.82) -- (218.05,76.8) .. controls (218.05,75.65) and (221.54,74.72) .. (225.84,74.72) .. controls (230.14,74.72) and (233.62,75.65) .. (233.62,76.8) .. controls (233.62,77.95) and (230.14,78.88) .. (225.84,78.88) .. controls (221.54,78.88) and (218.05,77.95) .. (218.05,76.8) ; 
            	\draw   (233.62,76.8) -- (233.62,86.82) .. controls (233.62,87.97) and (230.14,88.91) .. (225.84,88.91) .. controls (221.54,88.91) and (218.05,87.97) .. (218.05,86.82) -- (218.05,76.8) .. controls (218.05,75.65) and (221.54,74.72) .. (225.84,74.72) .. controls (230.14,74.72) and (233.62,75.65) .. (233.62,76.8) .. controls (233.62,77.95) and (230.14,78.88) .. (225.84,78.88) .. controls (221.54,78.88) and (218.05,77.95) .. (218.05,76.8) ; 
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (245.41,78) -- (240.59,74.37) -- (239.21,64.52) -- (251.42,62.8) -- (256.24,66.43) -- (257.62,76.29) -- cycle ; \draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ] (239.21,64.52) -- (244.03,68.15) -- (245.41,78) ; \draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ] (244.03,68.15) -- (256.24,66.43) ;
            	\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (167.22,87.18) -- (163.63,84.48) -- (162.6,77.13) -- (240.17,66.24) -- (243.76,68.95) -- (244.79,76.3) -- cycle ; \draw   (162.6,77.13) -- (166.19,79.84) -- (167.22,87.18) ; \draw   (166.19,79.84) -- (243.76,68.95) ;
            	\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (226.6,53.5) -- (226.13,67.8) -- (228.6,67.8) -- (228.14,53.5) -- cycle ;
            	\draw    (228.14,53.5) .. controls (232.85,56.75) and (231.85,64.5) .. (239.21,64.52) ;
            	\draw    (211.85,61.92) .. controls (206.25,70.75) and (188.25,68.25) .. (167.5,77.75) ;
            	\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (208.51,91.79) -- (209.53,87.31) -- (212.95,87.31) -- (213.97,91.79) -- (212.95,96.27) -- (209.53,96.27) -- cycle ;
            	\draw    (209.53,87.31) -- (209.57,81.57) ;
            	\draw    (212.95,87.31) -- (212.77,80.37) ;
            	\draw  [fill={rgb, 255:red, 140; green, 131; blue, 22 }  ,fill opacity=1 ] (166.19,79.84) -- (243.76,68.95) -- (244.79,76.3) -- (167.22,87.18) -- cycle ;
            	\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (211.85,61.92) -- (224.35,60.17) -- (228.6,69.42) -- (228.85,79.83) -- (214.85,81.83) -- (214.6,71.42) -- (211.85,69.92) -- cycle ;
            	\draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (174.07,84.32) .. controls (174.07,83.35) and (173.18,82.57) .. (172.08,82.57) .. controls (170.99,82.57) and (170.1,83.35) .. (170.1,84.32) .. controls (170.1,85.28) and (170.99,86.07) .. (172.08,86.07) .. controls (173.18,86.07) and (174.07,85.28) .. (174.07,84.32) -- cycle ;
            	\draw    (172.08,84.32) -- (141.77,218.47) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (243.03,67.15) -- (255.24,65.43) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (217.33,70.77) -- (214.53,63.57) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (218.05,76.8) -- (217.33,70.77) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (212.73,72.17) -- (167.19,78.84) ;
            	\draw  [dash pattern={on 0.84pt off 2.51pt}] (144.8,76.56) .. controls (144.8,59.05) and (181.08,44.85) .. (225.84,44.85) .. controls (270.59,44.85) and (306.87,59.05) .. (306.87,76.56) .. controls (306.87,94.07) and (270.59,108.27) .. (225.84,108.27) .. controls (181.08,108.27) and (144.8,94.07) .. (144.8,76.56) -- cycle ;
            	\draw (393.33,211) node [anchor=north west][inner sep=0.75pt]    {$x$};
            	\draw (64,199) node [anchor=north west][inner sep=0.75pt]    {$y$};
            	\draw (233.33,17.33) node [anchor=north west][inner sep=0.75pt]    {$z$};
            	\draw (210.72,166) node [anchor=north west][inner sep=0.75pt]    {$O$};
            	\draw (110.67,211) node [anchor=north west][inner sep=0.75pt]    {$M$};
            	\draw (152,53.67) node [anchor=north west][inner sep=0.75pt]    {$A$};
            	\draw (217.53,108.23) node [anchor=north west][inner sep=0.75pt]  [rotate=-178.81] [align=left] {?};
            \end{tikzpicture} \end{center}'''

            # Nội dung câu hỏi
            noidungcauhoi = (
                'Tại một cảng biển, hoạt động của một cần cẩu tháp được mô hình hóa trong không gian với hệ tọa độ $Oxyz$ (đơn vị trên các trục là mét). '
                'Cần cẩu có trụ đứng trùng với trục $Oz$ và tay cần nằm trong mặt phẳng nằm ngang $(P): z = ' + str(h) + '$. '
                'Trong quá trình vận hành, tay cần có thể quay tự do quanh trục $Oz$ sao cho đầu tay cần (điểm $A$) luôn cách trục $Oz$ một khoảng bằng ' + str(R) + ' mét. '
                'Một sợi dây cáp tải hàng được nối từ điểm $A$ đến móc cẩu $M$. Biết rằng điểm $M$ di chuyển trên một thanh ray thẳng nằm trên mặt đất (mặt phẳng $Oxy$) có phương trình tham số là đường thẳng '
                '$d: \\left\\{ \\begin{array}{l} x = ' + latex(x0) + ' + ' + latex(b) + 't \\\\ y = -' + latex(a) + 't \\\\ z = 0 \\end{array} \\right. (t \\in \\mathbb{R})$. '+str(hinhve)+
                'Để đảm bảo an toàn kỹ thuật và tránh đứt cáp do lực căng ngang, góc tạo bởi sợi dây cáp $AM$ và phương thẳng đứng được quy định không vượt quá $60^\\circ$. '
                'Trong điều kiện vận hành an toàn đó, gọi $M_{\\max}$ và $m_{\\min}$ lần lượt là chiều dài lớn nhất và chiều dài nhỏ nhất của sợi dây cáp $AM$. '
                'Giá trị của $M_{\\max} + m_{\\min}$ bằng bao nhiêu mét?'
            )

            # Nội dung lời giải chi tiết
            loigiai = (
                'Điểm $A$ nằm trên mặt phẳng $z = ' + str(h) + '$ và cách trục $Oz$ một khoảng $R = ' + str(R) + '$, '
                'nên tập hợp các điểm $A$ là đường tròn nằm trên mặt phẳng $z = ' + str(h) + '$ có tâm là $(0; 0; ' + str(h) + ')$ và bán kính $R = ' + str(R) + '$.\\\\ '
                'Gọi $H$ là hình chiếu của $A$ lên mặt phẳng $(Oxy)$, suy ra $H$ thuộc đường tròn $(C)$ tâm $O(0; 0; 0)$ bán kính $R = ' + str(R) + '$ nằm trên mặt phẳng $Oxy$.\\\\ '
                'Điểm $M$ thuộc đường thẳng $d$ trên mặt phẳng $Oxy$. Từ phương trình tham số của $d$, ta có phương trình tổng quát của $d$ là: '
                '$' + str(a) + 'x + ' + str(b) + 'y - ' + str(val_c) + ' = 0$.\\\\ '
                'Khoảng cách từ tâm $O$ đến đường thẳng $d$ là: $d(O, d) = \\frac{|' + str(a) + ' \\cdot 0 + ' + str(b) + ' \\cdot 0 - ' + str(val_c) + '|}{\\sqrt{' + str(a) + '^2 + ' + str(b) + '^2}} = ' + str(D) + '$.\\\\ '
                'Độ dài sợi dây cáp là $AM = \\sqrt{HM^2 + h^2} = \\sqrt{HM^2 + ' + str(h**2) + '}$.\\\\ '
                'Sợi dây cáp $AM$ có độ dài nhỏ nhất khi $HM$ nhỏ nhất. Khoảng cách $HM$ nhỏ nhất khi $M$ là hình chiếu của $H$ lên $d$ và $H$ nằm giữa $O$ và $M$. '
                'Khi đó $HM_{\\min} = d(O, d) - R = ' + str(D) + ' - ' + str(R) + ' = ' + str(D-R) + '$.\\\\ '
                'Suy ra $m_{\\min} = \\sqrt{' + str(D-R) + '^2 + ' + str(h) + '^2} = ' + str(m_min) + '$.\\\\ '
                'Gọi $\\alpha$ là góc giữa $AM$ và phương thẳng đứng $Oz$. Ta có $\\cos \\alpha = \\frac{h}{AM} = \\frac{' + str(h) + '}{AM}$.\\\\ '
                'Theo quy định an toàn: $\\alpha \\le 60^\\circ \\implies \\cos \\alpha \\ge \\cos 60^\\circ = \\frac{1}{2}$.\\\\ '
                'Suy ra $\\frac{' + str(h) + '}{AM} \\ge \\frac{1}{2} \\implies AM \\le ' + str(2*h) + '$.\\\\ '
                'Vậy chiều dài lớn nhất cho phép của sợi dây cáp là $M_{\\max} = ' + str(M_max) + '$.\\\\ '
                'Giá trị cần tìm là $M_{\\max} + m_{\\min} = ' + str(M_max) + ' + ' + str(m_min) + ' = ' + str(kq_val) + '$.'
            )
            dapan='\\shortans[0]{$%s$}\n'%(str(kq_val))
            # --- Xuất kết quả ---
            da_d = ('\\True $' + str(da) + '$')
            list_1 = [da_d, '$' + das1 + '$', '$' + das2 + '$', '$' + das3 + '$']
            random.shuffle(list_1)

            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content  

