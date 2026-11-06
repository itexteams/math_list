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


def bt_dang7_p2_b2_c2_ds11(self):
            # Khai báo biến
            # Random các giá trị cơ bản
            u1 = random.randint(200, 250)  # Chiều dài bậc đầu tiên (cm)
            d_nghich = random.randint(5, 12)  # Công sai âm (giảm dần d cm mỗi bậc)
            n_bac = random.randint(15, 25)  # Tổng số bậc
            chieu_rong = random.choice([25, 30, 35])  # Chiều rộng mỗi bậc (cm)
            gia_tien = random.choice([250000, 300000, 350000])  # Giá tiền mỗi m2 (đồng)

            # Tính toán các thông số phụ thuộc
            un = u1 - (n_bac - 1) * d_nghich  # Chiều dài bậc cuối
            u5 = u1 - 4 * d_nghich  # Chiều dài bậc thứ 5
            tong_chieu_dai_cm = (n_bac * (u1 + un)) / 2
            dien_tich_m2 = (tong_chieu_dai_cm / 100) * (chieu_rong / 100)
            tong_tien = int(dien_tich_m2 * gia_tien)
            nguong_tien = (tong_tien // 1000000 + 1) * 1000000 # Ngưỡng để so sánh ở câu d

            # Định dạng số tiền có dấu phân cách (nếu cần) hoặc viết liền
            gia_tien_str = "{:,}".format(gia_tien).replace(',', ' ')
            nguong_tien_str = str(nguong_tien // 1000000)
            hinhve=r'''\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            	\tikzset {_neimis5kq/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{-265 }  \pgftransformscale{2 }  }}}
            	\pgfdeclarehorizontalshading{_pio6qh4a2}{150bp}{rgb(0bp)=(1,1,1);
            		rgb(37.5bp)=(1,1,1);
            		rgb(62.5bp)=(0.04,0.6,0.99);
            		rgb(100bp)=(0.04,0.6,0.99)}
            	\tikzset {_bwcadnbk9/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{-87 }  \pgftransformscale{2 }  }}}
            	\pgfdeclarehorizontalshading{_imri99ddn}{150bp}{rgb(0bp)=(1,1,1);
            		rgb(43.196427481515066bp)=(1,1,1);
            		rgb(62.5bp)=(0.31,0.76,0.92);
            		rgb(100bp)=(0.31,0.76,0.92)}
            	\tikzset {_2f0dm07mf/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{-87 }  \pgftransformscale{2 }  }}}
            	\pgfdeclarehorizontalshading{_nbd3h8p93}{150bp}{rgb(0bp)=(1,1,1);
            		rgb(43.196427481515066bp)=(1,1,1);
            		rgb(62.5bp)=(0.31,0.76,0.92);
            		rgb(100bp)=(0.31,0.76,0.92)}
            	\tikzset {_det4z0jls/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{-87 }  \pgftransformscale{2 }  }}}
            	\pgfdeclarehorizontalshading{_82j0ktubf}{150bp}{rgb(0bp)=(1,1,1);
            		rgb(43.196427481515066bp)=(1,1,1);
            		rgb(62.5bp)=(0.31,0.76,0.92);
            		rgb(100bp)=(0.31,0.76,0.92)}
            	\tikzset {_nwpjv0dvu/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{-87 }  \pgftransformscale{2 }  }}}
            	\pgfdeclarehorizontalshading{_7dayyo5zd}{150bp}{rgb(0bp)=(1,1,1);
            		rgb(43.196427481515066bp)=(1,1,1);
            		rgb(62.5bp)=(0.31,0.76,0.92);
            		rgb(100bp)=(0.31,0.76,0.92)}
            	\tikzset {_4dmtepl1y/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{-87 }  \pgftransformscale{2 }  }}}
            	\pgfdeclarehorizontalshading{_1rrsfv0jo}{150bp}{rgb(0bp)=(1,1,1);
            		rgb(43.196427481515066bp)=(1,1,1);
            		rgb(62.5bp)=(0.31,0.76,0.92);
            		rgb(100bp)=(0.31,0.76,0.92)}
            	\tikzset {_jyxtyvaje/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{-87 }  \pgftransformscale{2 }  }}}
            	\pgfdeclarehorizontalshading{_gcil2fgkp}{150bp}{rgb(0bp)=(1,1,1);
            		rgb(43.196427481515066bp)=(1,1,1);
            		rgb(62.5bp)=(0.31,0.76,0.92);
            		rgb(100bp)=(0.31,0.76,0.92)}
            	\tikzset {_x4izcsmj8/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{-87 }  \pgftransformscale{2 }  }}}
            	\pgfdeclarehorizontalshading{_519gua95k}{150bp}{rgb(0bp)=(1,1,1);
            		rgb(43.196427481515066bp)=(1,1,1);
            		rgb(62.5bp)=(0.31,0.76,0.92);
            		rgb(100bp)=(0.31,0.76,0.92)}
            	\tikzset {_di0ea9fx0/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{-87 }  \pgftransformscale{2 }  }}}
            	\pgfdeclarehorizontalshading{_3yuhs11i4}{150bp}{rgb(0bp)=(1,1,1);
            		rgb(43.196427481515066bp)=(1,1,1);
            		rgb(62.5bp)=(0.31,0.76,0.92);
            		rgb(100bp)=(0.31,0.76,0.92)}
            	\tikzset {_9z8i7c06k/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{-87 }  \pgftransformscale{2 }  }}}
            	\pgfdeclarehorizontalshading{_qwzmkle9p}{150bp}{rgb(0bp)=(1,1,1);
            		rgb(43.196427481515066bp)=(1,1,1);
            		rgb(62.5bp)=(0.31,0.76,0.92);
            		rgb(100bp)=(0.31,0.76,0.92)}
            	\tikzset{every picture/.style={line width=0.75pt}} 
            	\draw  [draw opacity=0][shading=_pio6qh4a2,_neimis5kq] (83.3,2.35) -- (278.3,2.35) -- (278.3,237.55) -- (83.3,237.55) -- cycle ;
            	\draw  [draw opacity=0][shading=_imri99ddn,_bwcadnbk9] (124.27,32.3) .. controls (129.28,32.3) and (133.53,35.54) .. (135.06,40.03) .. controls (136.31,39.18) and (137.82,38.67) .. (139.46,38.67) .. controls (143.67,38.67) and (147.1,42.01) .. (147.26,46.19) -- (147.99,46.19) .. controls (153.02,46.19) and (157.1,50.26) .. (157.1,55.29) .. controls (157.1,60.32) and (153.02,64.4) .. (147.99,64.4) -- (110.38,64.4) .. controls (104.1,64.4) and (99,59.3) .. (99,53.02) .. controls (99,46.73) and (104.1,41.63) .. (110.38,41.63) .. controls (111.29,41.63) and (112.17,41.74) .. (113.02,41.94) .. controls (113.86,36.48) and (118.58,32.3) .. (124.27,32.3) -- cycle ;
            	\draw  [draw opacity=0][shading=_nbd3h8p93,_2f0dm07mf] (108.47,46.66) .. controls (111.88,46.66) and (114.78,48.86) .. (115.82,51.93) .. controls (116.67,51.34) and (117.7,51) .. (118.82,51) .. controls (121.69,51) and (124.03,53.27) .. (124.13,56.12) -- (124.63,56.12) .. controls (128.06,56.12) and (130.84,58.9) .. (130.84,62.33) .. controls (130.84,65.76) and (128.06,68.53) .. (124.63,68.53) -- (99,68.53) .. controls (94.72,68.53) and (91.24,65.06) .. (91.24,60.78) .. controls (91.24,56.49) and (94.72,53.02) .. (99,53.02) .. controls (99.62,53.02) and (100.22,53.09) .. (100.8,53.23) .. controls (101.37,49.51) and (104.58,46.66) .. (108.47,46.66) -- cycle ;
            	\draw  [draw opacity=0][shading=_82j0ktubf,_det4z0jls] (237.52,12.8) .. controls (231.66,12.8) and (226.68,16.04) .. (224.9,20.53) .. controls (223.43,19.68) and (221.66,19.17) .. (219.75,19.17) .. controls (214.82,19.17) and (210.8,22.51) .. (210.62,26.69) -- (209.76,26.69) .. controls (203.87,26.69) and (199.1,30.76) .. (199.1,35.79) .. controls (199.1,40.82) and (203.87,44.9) .. (209.76,44.9) -- (253.78,44.9) .. controls (261.14,44.9) and (267.1,39.8) .. (267.1,33.52) .. controls (267.1,27.23) and (261.14,22.13) .. (253.78,22.13) .. controls (252.71,22.13) and (251.68,22.24) .. (250.69,22.44) .. controls (249.71,16.98) and (244.19,12.8) .. (237.52,12.8) -- cycle ;
            	\draw  [draw opacity=0][shading=_7dayyo5zd,_nwpjv0dvu] (253.36,27.8) .. controls (249.97,27.8) and (247.08,29.68) .. (246.05,32.28) .. controls (245.2,31.78) and (244.17,31.49) .. (243.07,31.49) .. controls (240.21,31.49) and (237.88,33.43) .. (237.77,35.85) -- (237.28,35.85) .. controls (233.87,35.85) and (231.1,38.21) .. (231.1,41.12) .. controls (231.1,44.04) and (233.87,46.4) .. (237.28,46.4) -- (262.78,46.4) .. controls (267.05,46.4) and (270.5,43.45) .. (270.5,39.8) .. controls (270.5,36.16) and (267.05,33.21) .. (262.78,33.21) .. controls (262.17,33.21) and (261.57,33.27) .. (260.99,33.39) .. controls (260.43,30.22) and (257.23,27.8) .. (253.36,27.8) -- cycle ;
            	\draw  [draw opacity=0][shading=_1rrsfv0jo,_4dmtepl1y] (107.92,82.29) .. controls (111.33,82.29) and (114.23,84.5) .. (115.27,87.56) .. controls (116.12,86.98) and (117.16,86.64) .. (118.27,86.64) .. controls (121.14,86.64) and (123.48,88.91) .. (123.59,91.76) -- (124.09,91.76) .. controls (127.52,91.76) and (130.29,94.54) .. (130.29,97.96) .. controls (130.29,101.39) and (127.52,104.17) .. (124.09,104.17) -- (98.45,104.17) .. controls (94.17,104.17) and (90.69,100.7) .. (90.69,96.41) .. controls (90.69,92.13) and (94.17,88.65) .. (98.45,88.65) .. controls (99.07,88.65) and (99.67,88.73) .. (100.25,88.86) .. controls (100.82,85.14) and (104.04,82.29) .. (107.92,82.29) -- cycle ;
            	\draw  [draw opacity=0][shading=_gcil2fgkp,_jyxtyvaje] (125.29,94.37) .. controls (127.61,94.37) and (129.59,95.88) .. (130.29,97.96) .. controls (130.88,97.57) and (131.58,97.33) .. (132.34,97.33) .. controls (134.29,97.33) and (135.89,98.88) .. (135.96,100.82) -- (136.3,100.82) .. controls (138.64,100.82) and (140.53,102.71) .. (140.53,105.05) .. controls (140.53,107.38) and (138.64,109.28) .. (136.3,109.28) -- (118.84,109.28) .. controls (115.92,109.28) and (113.55,106.91) .. (113.55,103.99) .. controls (113.55,101.07) and (115.92,98.71) .. (118.84,98.71) .. controls (119.26,98.71) and (119.67,98.76) .. (120.06,98.85) .. controls (120.45,96.31) and (122.64,94.37) .. (125.29,94.37) -- cycle ;
            	\draw  [draw opacity=0][shading=_519gua95k,_x4izcsmj8] (240.36,101.8) .. controls (236.97,101.8) and (234.08,103.68) .. (233.05,106.28) .. controls (232.2,105.78) and (231.17,105.49) .. (230.07,105.49) .. controls (227.21,105.49) and (224.88,107.43) .. (224.77,109.85) -- (224.28,109.85) .. controls (220.87,109.85) and (218.1,112.21) .. (218.1,115.12) .. controls (218.1,118.04) and (220.87,120.4) .. (224.28,120.4) -- (249.78,120.4) .. controls (254.05,120.4) and (257.5,117.45) .. (257.5,113.8) .. controls (257.5,110.16) and (254.05,107.21) .. (249.78,107.21) .. controls (249.17,107.21) and (248.57,107.27) .. (247.99,107.39) .. controls (247.43,104.22) and (244.23,101.8) .. (240.36,101.8) -- cycle ;
            	\draw  [draw opacity=0][shading=_3yuhs11i4,_di0ea9fx0] (259.03,125.02) .. controls (257.13,125.02) and (255.52,126.06) .. (254.95,127.52) .. controls (254.47,127.24) and (253.9,127.08) .. (253.28,127.08) .. controls (251.69,127.08) and (250.39,128.16) .. (250.33,129.51) -- (250.05,129.51) .. controls (248.14,129.51) and (246.6,130.83) .. (246.6,132.45) .. controls (246.6,134.08) and (248.14,135.4) .. (250.05,135.4) -- (264.29,135.4) .. controls (266.67,135.4) and (268.6,133.75) .. (268.6,131.72) .. controls (268.6,129.68) and (266.67,128.04) .. (264.29,128.04) .. controls (263.95,128.04) and (263.61,128.07) .. (263.29,128.13) .. controls (262.97,126.37) and (261.19,125.02) .. (259.03,125.02) -- cycle ;
            	\draw  [draw opacity=0][shading=_qwzmkle9p,_9z8i7c06k] (135.29,141.37) .. controls (137.61,141.37) and (139.59,142.88) .. (140.29,144.96) .. controls (140.88,144.57) and (141.58,144.33) .. (142.34,144.33) .. controls (144.29,144.33) and (145.89,145.88) .. (145.96,147.82) -- (146.3,147.82) .. controls (148.64,147.82) and (150.53,149.71) .. (150.53,152.05) .. controls (150.53,154.38) and (148.64,156.28) .. (146.3,156.28) -- (128.84,156.28) .. controls (125.92,156.28) and (123.55,153.91) .. (123.55,150.99) .. controls (123.55,148.07) and (125.92,145.71) .. (128.84,145.71) .. controls (129.26,145.71) and (129.67,145.76) .. (130.06,145.85) .. controls (130.45,143.31) and (132.64,141.37) .. (135.29,141.37) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.23 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (178.17,21.12) -- (185.43,21.12) -- (185.43,30.9) -- (178.17,30.9) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.23 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (178,18.8) -- (185.6,18.8) -- (185.6,21.12) -- (178,21.12) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.23 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (175.77,26.83) -- (187.83,26.83) -- (187.83,35.4) -- (175.77,35.4) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.23 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (175.5,24.8) -- (188.1,24.8) -- (188.1,26.83) -- (175.5,26.83) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.23 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (173.88,35.12) -- (190.72,35.12) -- (190.72,47) -- (173.88,47) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.23 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (173.5,32.3) -- (191.1,32.3) -- (191.1,35.12) -- (173.5,35.12) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.23 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (170.51,44.69) -- (193.09,44.69) -- (193.09,59) -- (170.51,59) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.23 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (170,41.3) -- (193.6,41.3) -- (193.6,44.69) -- (170,44.69) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.23 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (167.67,54.98) -- (196.93,54.98) -- (196.93,70.5) -- (167.67,70.5) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.23 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (167,51.3) -- (197.6,51.3) -- (197.6,54.98) -- (167,54.98) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.23 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (164.32,67.27) -- (200.28,67.27) -- (200.28,84) -- (164.32,84) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.23 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (163.5,63.3) -- (201.1,63.3) -- (201.1,67.27) -- (163.5,67.27) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.23 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (161.95,80.55) -- (203.65,80.55) -- (203.65,98.5) -- (161.95,98.5) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.23 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (161,76.3) -- (204.6,76.3) -- (204.6,80.55) -- (161,80.55) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.23 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (157.63,94.03) -- (206.97,94.03) -- (206.97,114) -- (157.63,114) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.23 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (156.5,89.3) -- (208.1,89.3) -- (208.1,94.03) -- (156.5,94.03) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.23 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (153.84,107.4) -- (212.76,107.4) -- (212.76,128.5) -- (153.84,128.5) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.23 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (152.5,102.4) -- (214.1,102.4) -- (214.1,107.4) -- (152.5,107.4) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.23 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (149.04,123.9) -- (216.56,123.9) -- (216.56,145) -- (149.04,145) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.23 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (147.5,118.9) -- (218.1,118.9) -- (218.1,123.9) -- (147.5,123.9) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.23 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (145.24,140.4) -- (221.36,140.4) -- (221.36,161.5) -- (145.24,161.5) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.23 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (143.5,135.4) -- (223.1,135.4) -- (223.1,140.4) -- (143.5,140.4) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.23 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (140.02,157.4) -- (228.58,157.4) -- (228.58,178.5) -- (140.02,178.5) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.23 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (138,152.4) -- (230.6,152.4) -- (230.6,157.4) -- (138,157.4) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.23 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (135.67,176.4) -- (230.93,176.4) -- (230.93,197.5) -- (135.67,197.5) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.23 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (133.5,171.4) -- (233.1,171.4) -- (233.1,176.4) -- (133.5,176.4) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.23 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (129.93,193.4) -- (236.67,193.4) -- (236.67,214.5) -- (129.93,214.5) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.23 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (127.5,188.4) -- (239.1,188.4) -- (239.1,193.4) -- (127.5,193.4) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.23 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (125.13,211.9) -- (240.47,211.9) -- (240.47,233) -- (125.13,233) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.23 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (122.5,206.9) -- (243.1,206.9) -- (243.1,211.9) -- (122.5,211.9) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.23 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (119.6,227.8) -- (247.6,227.8) -- (247.6,233) -- (119.6,233) -- cycle ;
            \end{tikzpicture}'''
            # Nội dung câu hỏi
            noidungcauhoi = (r'''\immini{Một cầu thang đường lên cổng trời của công viên được hàn bằng sắt. Các mặt bậc thang làm bằng gỗ đều là hình chữ nhật với cùng chiều rộng là $%s cm$ và chiều dài của nó theo thứ tự mỗi bậc đều giảm dần đi $%s cm$. Biết rằng bậc đầu tiên của cầu thang là hình chữ nhật có chiều dài $%s cm$ và bậc cuối cùng cầu thang là hình chữ nhật có chiều dài $%s cm$. Phần bề mặt bậc cầu thang sử dụng vật liệu gỗ công nghiệp có giá thành $%s$ đồng trên một mét vuông.}{%s}''' 
                             %(latex(chieu_rong), latex(d_nghich), latex(u1), latex(un), gia_tien_str,hinhve))

            ########################################################################
            # Nhận biết ############################################
            nb_da_1_d = '\\True Chiều dài các bậc cầu thang từ dưới lên trên theo thứ tự lập thành một cấp số cộng với công sai $d=-%s cm$' %(latex(d_nghich))
            nb_da_1_s = 'Chiều dài các bậc cầu thang từ dưới lên trên theo thứ tự lập thành một cấp số cộng với công sai $d=%s cm$' %(latex(d_nghich))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = ('''Do chiều dài bậc cầu thang theo thứ tự mỗi bậc giảm dần $%s cm$ nên chúng lập thành cấp số cộng có số hạng đầu $u_1=%s$, công sai $d=-%s$.'''
                            %(latex(d_nghich), latex(u1), latex(d_nghich)))

            ########################################################################
            # Thông hiểu ############################################
            check_chia_het = "chia hết" if u5 % 5 == 0 else "không chia hết"
            sai_chia_het = "không chia hết" if u5 % 5 == 0 else "chia hết"

            th_da_1_d = '\\True Chiều dài của bậc thang thứ 5 là một số %s cho 5' %(check_chia_het)
            th_da_1_s = 'Chiều dài của bậc thang thứ 5 là một số %s cho 5' %(sai_chia_het)
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = ('''Theo công thức số hạng tổng quát của cấp số cộng $u_n=u_1+\\left(n-1\\right)d$ ta có: \\\\
            Chiều dài bậc thang thứ 5 bằng: $u_5=%s+\\left(5-1\\right).\\left(-%s\\right)=%s$. \\\\
            Số $%s$ %s cho 5.''' 
                            %(latex(u1), latex(d_nghich), latex(u5), latex(u5), check_chia_het))

            ########################################################################
            # Vận dụng ############################################
            vd_da_1_d = '\\True Cầu thang có tất cả %s bậc' %(latex(n_bac))
            vd_da_1_s = 'Cầu thang có tất cả %s bậc' %(latex(n_bac + 2))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1 = ('''Vì chiều dài bậc thang cuối cùng là $%s cm$ nên: \\\\
            $u_n=%s \\Leftrightarrow %s+\\left(n-1\\right).\\left(-%s\\right)=%s \\Leftrightarrow n=%s$. \\\\
            Vậy cầu thang có tất cả %s bậc.''' 
                            %(latex(un), latex(un), latex(u1), latex(d_nghich), latex(un), latex(n_bac), latex(n_bac)))

            ########################################################################
            # Vận dụng cao ############################################
            vdc_da_1_d = '\\True Số tiền phần vật liệu gỗ dùng để làm bề mặt bậc cầu thang dưới %s triệu đồng' %(nguong_tien_str)
            vdc_da_1_s = 'Số tiền phần vật liệu gỗ dùng để làm bề mặt bậc cầu thang trên %s triệu đồng' %(nguong_tien_str)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            # Xử lý dấu phẩy thập phân cho diện tích
            dt_str = str(round(dien_tich_m2, 2)).replace('.', ',')
            tong_tien_str = "{:,}".format(tong_tien).replace(',', '.')

            loigiai_vdc_1 = ('''Tổng chiều dài của %s bậc thang đó là: \\\\
            $S_{%s}=%s. \\frac{%s+%s}{2}=%s cm$. \\\\
            Đổi $%s cm = %s m$. \\\\
            Diện tích bề mặt các bậc thang là: $S = %s \\cdot %s = %s m^2$. \\\\
            Số tiền vật liệu là: $%s \\cdot %s = %s$ đồng. \\\\
            Vậy số tiền dưới %s triệu đồng.''' 
                             %(latex(n_bac), latex(n_bac), latex(n_bac), latex(u1), latex(un), latex(int(tong_chieu_dai_cm)), 
                               latex(int(tong_chieu_dai_cm)), str(tong_chieu_dai_cm/100).replace('.', ','), 
                               str(tong_chieu_dai_cm/100).replace('.', ','), str(chieu_rong/100).replace('.', ','), dt_str,
                               dt_str, gia_tien_str, tong_tien_str, nguong_tien_str))

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)
                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                if 1 <= count_true_answers(answers) <= 3:
                    break

            list_nb_1, list_th_1, list_vd_1, list_vdc_1 = [nb_da_1], [th_da_1], [vd_da_1], [vdc_da_1]
            list_nb_2, list_th_2, list_vd_2, list_vdc_2 = [loigiai_nb_1], [loigiai_th_1], [loigiai_vd_1], [loigiai_vdc_1]

            shuffled_answers_nb, shuffled_solutions_nb = zip(*list(zip(list_nb_1, list_nb_2)))
            shuffled_answers_th, shuffled_solutions_th = zip(*list(zip(list_th_1, list_th_2)))
            shuffled_answers_vd, shuffled_solutions_vd = zip(*list(zip(list_vd_1, list_vd_2)))
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*list(zip(list_vdc_1, list_vdc_2)))

            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
                str(noidungcauhoi)+ 
                '\n\\choiceTFn \n'
                '{'+str(shuffled_answers_nb[0])+'}\n'
                '{'+str(shuffled_answers_th[0])+'}\n'
                '{'+str(shuffled_answers_vd[0])+'}\n'
                '{'+str(shuffled_answers_vdc[0])+'}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(shuffled_solutions_nb[0])+'\n'
                '\\item '+str(shuffled_solutions_th[0])+'\n'
                '\\item '+str(shuffled_solutions_vd[0])+'\n'
                '\\item '+str(shuffled_solutions_vdc[0])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

