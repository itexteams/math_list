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


def bt_dang44_p2_b2_c4_ds12(self):
            # Khai báo biến
            # Khai báo biến và random thông số
            nA = randint(45, 65) # Số học sinh trường A
            nB = randint(20, 35) # Số học sinh trường B
            total = nA + nB

            # Xác suất giành huy chương vàng (tử số của phần trăm)
            pA_num = randint(5, 12) 
            pB_num = randint(4, 9)
            while pA_num == pB_num:
                pB_num = randint(4, 9)

            # Chuỗi hiển thị số thập phân dùng dấu phẩy (vd: 0,08)
            str_pA = "0,%02d" % pA_num
            str_pB = "0,%02d" % pB_num

            # Tính toán các giá trị chính xác bằng Rational
            P_A = Rational(nA, total)
            P_B = Rational(nB, total)
            P_C_given_A = Rational(pA_num, 100)
            P_C_given_B = Rational(pB_num, 100)

            P_notC_given_B_val = 100 - pB_num
            str_P_notC_given_B = "0,%02d" % P_notC_given_B_val

            # Tính xác suất toàn phần và Bayes
            P_C = P_A * P_C_given_A + P_B * P_C_given_B
            P_A_given_C = (P_A * P_C_given_A) / P_C

            # Các giá trị sai (để tạo đáp án nhiễu)
            fake_P_notC_given_B = "0,%02d" % (100 - pA_num)
            fake_P_C = P_C + Rational(randint(1, 3), P_C.q)
            fake_P_A_given_C = P_A_given_C + Rational(1, P_A_given_C.q + randint(3, 7))

            hinhve=r'''\tikzset {_b9tanbmuy/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{-126 }  \pgftransformscale{2 }  }}}
            \pgfdeclarehorizontalshading{_xfa6zduvg}{150bp}{rgb(0bp)=(0.86,0.67,0.09);
            	rgb(37.5bp)=(0.86,0.67,0.09);
            	rgb(50bp)=(0.95,0.95,0.47);
            	rgb(62.5bp)=(0.86,0.67,0.09);
            	rgb(100bp)=(0.86,0.67,0.09)}
            \tikzset {_muh8k0x8m/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{-128 }  \pgftransformscale{2 }  }}}
            \pgfdeclarehorizontalshading{_y8uzwf67u}{150bp}{rgb(0bp)=(0.86,0.67,0.09);
            	rgb(42.30357033865792bp)=(0.86,0.67,0.09);
            	rgb(50bp)=(0.97,0.91,0.11);
            	rgb(53.9999989100865bp)=(0.86,0.67,0.09);
            	rgb(100bp)=(0.86,0.67,0.09)}
            \tikzset {_e28llpw6b/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{0 }  \pgftransformscale{2 }  }}}
            \pgfdeclarehorizontalshading{_kq15g8jq6}{150bp}{rgb(0bp)=(0.86,0.67,0.09);
            	rgb(37.5bp)=(0.86,0.67,0.09);
            	rgb(50bp)=(0.94,0.94,0.21);
            	rgb(62.5bp)=(0.86,0.67,0.09);
            	rgb(100bp)=(0.86,0.67,0.09)}
            \tikzset {_6w708odgi/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{-131 }  \pgftransformscale{2 }  }}}
            \pgfdeclarehorizontalshading{_cgkxd35jo}{150bp}{rgb(0bp)=(0.96,0.76,0.14);
            	rgb(43.10714176722935bp)=(0.96,0.76,0.14);
            	rgb(50bp)=(1,1,0);
            	rgb(55.8749989100865bp)=(0.96,0.76,0.14);
            	rgb(100bp)=(0.96,0.76,0.14)}
            \tikzset{every picture/.style={line width=0.75pt}} 
            \begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-0.7,xscale=0.7]
            	\draw  [draw opacity=0][fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (203.24,20.04) -- (213.46,20.04) -- (258.71,114.68) -- (248.49,114.68) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (213.47,20.04) -- (223.68,20.04) -- (268.93,114.68) -- (258.71,114.68) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 74; green, 74; blue, 226 }  ,fill opacity=1 ] (220.94,19.64) -- (231.16,19.64) -- (276.41,114.28) -- (266.19,114.28) -- cycle ;
            	\draw  [color={rgb, 255:red, 220; green, 171; blue, 22 }  ,draw opacity=1 ][line width=2.25]  (245.35,118.21) .. controls (245.35,115.82) and (247.29,113.89) .. (249.68,113.89) -- (275.35,113.89) .. controls (277.74,113.89) and (279.68,115.82) .. (279.68,118.21) -- (279.68,151.12) .. controls (279.68,153.51) and (277.74,155.45) .. (275.35,155.45) -- (249.68,155.45) .. controls (247.29,155.45) and (245.35,153.51) .. (245.35,151.12) -- cycle ;
            	\path  [shading=_xfa6zduvg,_b9tanbmuy] (208.32,175.76) .. controls (208.32,146.02) and (232.42,121.92) .. (262.16,121.92) .. controls (291.9,121.92) and (316,146.02) .. (316,175.76) .. controls (316,205.5) and (291.9,229.6) .. (262.16,229.6) .. controls (232.42,229.6) and (208.32,205.5) .. (208.32,175.76) -- cycle ; 
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.19 ] (208.32,175.76) .. controls (208.32,146.02) and (232.42,121.92) .. (262.16,121.92) .. controls (291.9,121.92) and (316,146.02) .. (316,175.76) .. controls (316,205.5) and (291.9,229.6) .. (262.16,229.6) .. controls (232.42,229.6) and (208.32,205.5) .. (208.32,175.76) -- cycle ;  
            	\path  [shading=_y8uzwf67u,_muh8k0x8m] (212.32,175.76) .. controls (212.32,148.23) and (234.63,125.92) .. (262.16,125.92) .. controls (289.69,125.92) and (312,148.23) .. (312,175.76) .. controls (312,203.29) and (289.69,225.6) .. (262.16,225.6) .. controls (234.63,225.6) and (212.32,203.29) .. (212.32,175.76) -- cycle ; 
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.19 ] (212.32,175.76) .. controls (212.32,148.23) and (234.63,125.92) .. (262.16,125.92) .. controls (289.69,125.92) and (312,148.23) .. (312,175.76) .. controls (312,203.29) and (289.69,225.6) .. (262.16,225.6) .. controls (234.63,225.6) and (212.32,203.29) .. (212.32,175.76) -- cycle ;
            	\path  [shading=_kq15g8jq6,_e28llpw6b] (225.12,175.76) .. controls (225.12,155.3) and (241.7,138.72) .. (262.16,138.72) .. controls (282.62,138.72) and (299.2,155.3) .. (299.2,175.76) .. controls (299.2,196.22) and (282.62,212.8) .. (262.16,212.8) .. controls (241.7,212.8) and (225.12,196.22) .. (225.12,175.76) -- cycle ;  
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.19 ] (225.12,175.76) .. controls (225.12,155.3) and (241.7,138.72) .. (262.16,138.72) .. controls (282.62,138.72) and (299.2,155.3) .. (299.2,175.76) .. controls (299.2,196.22) and (282.62,212.8) .. (262.16,212.8) .. controls (241.7,212.8) and (225.12,196.22) .. (225.12,175.76) -- cycle ; 
            	\path  [shading=_cgkxd35jo,_6w708odgi] (228.32,175.76) .. controls (228.32,157.07) and (243.47,141.92) .. (262.16,141.92) .. controls (280.85,141.92) and (296,157.07) .. (296,175.76) .. controls (296,194.45) and (280.85,209.6) .. (262.16,209.6) .. controls (243.47,209.6) and (228.32,194.45) .. (228.32,175.76) -- cycle ; 
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.19 ] (228.32,175.76) .. controls (228.32,157.07) and (243.47,141.92) .. (262.16,141.92) .. controls (280.85,141.92) and (296,157.07) .. (296,175.76) .. controls (296,194.45) and (280.85,209.6) .. (262.16,209.6) .. controls (243.47,209.6) and (228.32,194.45) .. (228.32,175.76) -- cycle ; 
            	\draw  [draw opacity=0] (251.33,202.09) .. controls (241.59,197.36) and (234.87,187.38) .. (234.87,175.82) .. controls (234.87,165.8) and (239.92,156.96) .. (247.62,151.7) -- (264.05,175.82) -- cycle ; \draw  [color={rgb, 255:red, 220; green, 171; blue, 22 }  ,draw opacity=1 ] (251.33,202.09) .. controls (241.59,197.36) and (234.87,187.38) .. (234.87,175.82) .. controls (234.87,165.8) and (239.92,156.96) .. (247.62,151.7) ;  
            	\draw  [draw opacity=0][fill={rgb, 255:red, 220; green, 171; blue, 22 }  ,fill opacity=1 ] (247.68,196.19) -- (249.67,198.33) -- (249.51,201.25) -- (247.52,199.11) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 220; green, 171; blue, 22 }  ,fill opacity=1 ] (245.95,201.96) -- (248.67,200.89) -- (251.33,202.09) -- (248.61,203.17) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 220; green, 171; blue, 22 }  ,fill opacity=1 ] (244.35,192.84) -- (245.93,195.3) -- (245.26,198.15) -- (243.68,195.69) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 220; green, 171; blue, 22 }  ,fill opacity=1 ] (241.44,199.26) -- (244.15,198.18) -- (246.82,199.39) -- (244.1,200.46) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 220; green, 171; blue, 22 }  ,fill opacity=1 ] (238.35,196.6) -- (241.07,195.52) -- (243.74,196.72) -- (241.02,197.8) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 220; green, 171; blue, 22 }  ,fill opacity=1 ] (241.55,189.76) -- (243.13,192.22) -- (242.46,195.06) -- (240.88,192.6) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 220; green, 171; blue, 22 }  ,fill opacity=1 ] (235.59,192.8) -- (238.45,192.17) -- (240.89,193.79) -- (238.03,194.42) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 220; green, 171; blue, 22 }  ,fill opacity=1 ] (240.88,185.85) -- (241.44,188.72) -- (239.77,191.12) -- (239.21,188.25) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 220; green, 171; blue, 22 }  ,fill opacity=1 ] (233.12,188.37) -- (236.02,187.99) -- (238.31,189.81) -- (235.41,190.19) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 220; green, 171; blue, 22 }  ,fill opacity=1 ] (238.92,182.77) -- (239.48,185.64) -- (237.81,188.04) -- (237.25,185.17) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 220; green, 171; blue, 22 }  ,fill opacity=1 ] (231.3,184.59) -- (234.2,184.21) -- (236.49,186.03) -- (233.59,186.41) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 220; green, 171; blue, 22 }  ,fill opacity=1 ] (238.14,178.29) -- (238.15,181.22) -- (236.06,183.26) -- (236.05,180.34) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 220; green, 171; blue, 22 }  ,fill opacity=1 ] (230.52,179.86) -- (233.44,180.09) -- (235.31,182.34) -- (232.39,182.12) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 220; green, 171; blue, 22 }  ,fill opacity=1 ] (237.83,173.98) -- (237.34,176.49) -- (235.2,177.89) -- (235.69,175.37) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 220; green, 171; blue, 22 }  ,fill opacity=1 ] (230.76,175.53) -- (233.52,176.17) -- (234.97,178.59) -- (232.22,177.95) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 220; green, 171; blue, 22 }  ,fill opacity=1 ] (238.76,169.25) -- (237.77,171.77) -- (235.28,172.81) -- (236.27,170.29) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 220; green, 171; blue, 22 }  ,fill opacity=1 ] (239.85,165.57) -- (238.48,168.1) -- (235.7,168.87) -- (237.08,166.34) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 220; green, 171; blue, 22 }  ,fill opacity=1 ] (241.78,161.9) -- (240.03,163.97) -- (237.34,164.15) -- (239.08,162.09) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 220; green, 171; blue, 22 }  ,fill opacity=1 ] (244.55,158.18) -- (242.44,160.11) -- (239.59,160.26) -- (241.7,158.33) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 220; green, 171; blue, 22 }  ,fill opacity=1 ] (247.25,154.93) -- (245.16,156.57) -- (242.52,156.22) -- (244.61,154.57) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 220; green, 171; blue, 22 }  ,fill opacity=1 ] (250.44,151.54) -- (248.81,153.13) -- (246.54,152.91) -- (248.17,151.32) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 220; green, 171; blue, 22 }  ,fill opacity=1 ] (231.01,171.5) -- (233.55,172.09) -- (234.89,174.31) -- (232.35,173.73) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 220; green, 171; blue, 22 }  ,fill opacity=1 ] (232.2,166.97) -- (234.43,168.34) -- (234.99,170.89) -- (232.77,169.52) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 220; green, 171; blue, 22 }  ,fill opacity=1 ] (233.78,162.48) -- (235.77,164.05) -- (236.02,166.57) -- (234.04,165) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 220; green, 171; blue, 22 }  ,fill opacity=1 ] (236.09,158.79) -- (237.59,160.95) -- (237.08,163.53) -- (235.58,161.37) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 220; green, 171; blue, 22 }  ,fill opacity=1 ] (238.62,154.94) -- (240.19,157.2) -- (239.66,159.89) -- (238.09,157.64) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 220; green, 171; blue, 22 }  ,fill opacity=1 ] (241.8,151.94) -- (242.74,154.3) -- (241.69,156.61) -- (240.76,154.25) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 220; green, 171; blue, 22 }  ,fill opacity=1 ] (245.52,149.66) -- (245.83,152.08) -- (244.31,153.98) -- (244,151.57) -- cycle ;
            	\draw  [draw opacity=0] (269.75,202.55) .. controls (280.37,197.94) and (287.74,187.8) .. (287.74,176.02) .. controls (287.74,165.73) and (282.11,156.69) .. (273.62,151.49) -- (256.91,176.02) -- cycle ; \draw  [color={rgb, 255:red, 220; green, 171; blue, 22 }  ,draw opacity=1 ] (269.75,202.55) .. controls (280.37,197.94) and (287.74,187.8) .. (287.74,176.02) .. controls (287.74,165.73) and (282.11,156.69) .. (273.62,151.49) ;  
            	\draw  [draw opacity=0][fill={rgb, 255:red, 220; green, 171; blue, 22 }  ,fill opacity=1 ] (274.2,196.39) -- (272.1,198.53) -- (272.27,201.45) -- (274.37,199.31) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 220; green, 171; blue, 22 }  ,fill opacity=1 ] (276.03,202.16) -- (273.16,201.09) -- (270.34,202.29) -- (273.22,203.37) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 220; green, 171; blue, 22 }  ,fill opacity=1 ] (277.71,193.04) -- (276.05,195.5) -- (276.75,198.35) -- (278.42,195.89) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 220; green, 171; blue, 22 }  ,fill opacity=1 ] (280.8,199.46) -- (277.92,198.38) -- (275.11,199.59) -- (277.98,200.66) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 220; green, 171; blue, 22 }  ,fill opacity=1 ] (284.06,196.8) -- (281.18,195.72) -- (278.37,196.92) -- (281.24,198) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 220; green, 171; blue, 22 }  ,fill opacity=1 ] (280.68,189.96) -- (279.01,192.42) -- (279.71,195.26) -- (281.38,192.8) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 220; green, 171; blue, 22 }  ,fill opacity=1 ] (286.97,193) -- (283.95,192.37) -- (281.38,193.99) -- (284.39,194.62) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 220; green, 171; blue, 22 }  ,fill opacity=1 ] (281.39,186.05) -- (280.79,188.92) -- (282.56,191.32) -- (283.15,188.45) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 220; green, 171; blue, 22 }  ,fill opacity=1 ] (289.58,188.57) -- (286.52,188.19) -- (284.1,190.01) -- (287.16,190.39) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 220; green, 171; blue, 22 }  ,fill opacity=1 ] (283.46,182.97) -- (282.87,185.84) -- (284.63,188.24) -- (285.22,185.37) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 220; green, 171; blue, 22 }  ,fill opacity=1 ] (291.5,184.79) -- (288.44,184.41) -- (286.02,186.23) -- (289.08,186.61) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 220; green, 171; blue, 22 }  ,fill opacity=1 ] (284.28,178.49) -- (284.27,181.42) -- (286.47,183.46) -- (286.49,180.54) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 220; green, 171; blue, 22 }  ,fill opacity=1 ] (292.32,180.06) -- (289.24,180.29) -- (287.27,182.54) -- (290.35,182.32) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 220; green, 171; blue, 22 }  ,fill opacity=1 ] (284.61,174.18) -- (285.12,176.69) -- (287.39,178.09) -- (286.87,175.57) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 220; green, 171; blue, 22 }  ,fill opacity=1 ] (292.08,175.73) -- (289.16,176.37) -- (287.62,178.79) -- (290.54,178.15) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 220; green, 171; blue, 22 }  ,fill opacity=1 ] (283.62,169.45) -- (284.67,171.97) -- (287.3,173.01) -- (286.26,170.49) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 220; green, 171; blue, 22 }  ,fill opacity=1 ] (282.47,165.77) -- (283.92,168.3) -- (286.85,169.07) -- (285.4,166.54) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 220; green, 171; blue, 22 }  ,fill opacity=1 ] (280.44,162.1) -- (282.28,164.17) -- (285.13,164.35) -- (283.28,162.29) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 220; green, 171; blue, 22 }  ,fill opacity=1 ] (277.51,158.38) -- (279.74,160.31) -- (282.75,160.46) -- (280.52,158.53) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 220; green, 171; blue, 22 }  ,fill opacity=1 ] (274.66,155.13) -- (276.87,156.77) -- (279.65,156.42) -- (277.44,154.77) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 220; green, 171; blue, 22 }  ,fill opacity=1 ] (271.29,151.74) -- (273.01,153.33) -- (275.41,153.11) -- (273.68,151.52) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 220; green, 171; blue, 22 }  ,fill opacity=1 ] (291.81,171.7) -- (289.13,172.29) -- (287.72,174.51) -- (290.39,173.93) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 220; green, 171; blue, 22 }  ,fill opacity=1 ] (290.55,167.17) -- (288.2,168.54) -- (287.6,171.09) -- (289.96,169.72) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 220; green, 171; blue, 22 }  ,fill opacity=1 ] (288.88,162.68) -- (286.78,164.25) -- (286.52,166.77) -- (288.62,165.2) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 220; green, 171; blue, 22 }  ,fill opacity=1 ] (286.44,158.99) -- (284.86,161.15) -- (285.4,163.73) -- (286.98,161.57) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 220; green, 171; blue, 22 }  ,fill opacity=1 ] (283.77,155.14) -- (282.11,157.4) -- (282.68,160.09) -- (284.33,157.84) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 220; green, 171; blue, 22 }  ,fill opacity=1 ] (280.41,152.14) -- (279.42,154.5) -- (280.52,156.81) -- (281.51,154.45) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 220; green, 171; blue, 22 }  ,fill opacity=1 ] (276.49,149.86) -- (276.15,152.28) -- (277.76,154.18) -- (278.09,151.77) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (286.1,22.24) -- (296.31,22.24) -- (259.11,116.88) -- (248.89,116.88) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (296.32,22.24) -- (306.54,22.24) -- (269.33,116.88) -- (259.11,116.88) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 74; green, 74; blue, 226 }  ,fill opacity=1 ] (304.14,21.84) -- (314.36,21.84) -- (277.16,116.48) -- (266.94,116.48) -- cycle ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.5 ]   (248.89,116.88) -- (277.16,116.48) ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.14 ][fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (258.96,160.3) -- (254.08,160.14) -- (254.08,156.44) -- (257.78,155.6) -- (261.14,152.57) -- (265.68,152.57) -- (265.68,183.67) -- (259.12,183.84) -- cycle ;
            	\draw (243,184.4) node [anchor=north west][inner sep=0.75pt][font=\fontsize{6pt}{6pt}\selectfont,color={rgb,255:red,191; green,128; blue,16},opacity=0.52] {$iTeX$};
            \end{tikzpicture}'''

            # Nội dung câu hỏi
            noidungcauhoi = ('''\\immini{Trong một cuộc thi Olympic môn Toán dành cho học sinh THPT, trường THPT A có %s học sinh và trường THPT B có %s học sinh tham dự. Giả sử xác suất giành huy chương vàng của mỗi học sinh của trường A và B lần lượt là %s và %s. Chọn ngẫu nhiên một học sinh trong số các học sinh tham dự.}{%s}'''                 
                             %(nA, nB, str_pA, str_pB, hinhve))

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Xác suất để học sinh được chọn thuộc trường A là $\\frac{%s}{%s}$' %(P_A.p, P_A.q)
            nb_da_1_s = 'Xác suất để học sinh được chọn thuộc trường A là $\\frac{%s}{%s}$' %(P_B.p, P_B.q)
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Gọi $A$ là biến cố: "Học sinh được chọn thuộc trường A" $\\Rightarrow n\\left(A\\right)=%s$.\\\\
            Gọi $B$ là biến cố: "Học sinh được chọn thuộc trường B" $\\Rightarrow n\\left(B\\right)=%s$.\\\\
            Tổng số học sinh là %s + %s = %s.\\\\
            Xác suất để học sinh được chọn thuộc trường A là $P\\left(A\\right) = \\frac{%s}{%s} = \\frac{%s}{%s}$.'''
                        %(nA, nB, nA, nB, total, nA, total, P_A.p, P_A.q))

            # Đưa các lời giải vào danh sách lời giải
            list_nb_2 = [loigiai_nb_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_nb = list(zip(list_nb_1, list_nb_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_nb)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ######################################################################## Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = '\\True Biết rằng học sinh được chọn thuộc trường B, xác suất để học sinh đó không giành được huy chương vàng là %s' %(str_P_notC_given_B)  
            th_da_1_s = 'Biết rằng học sinh được chọn thuộc trường B, xác suất để học sinh đó không giành được huy chương vàng là %s' %(fake_P_notC_given_B)   
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)


            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Gọi $C$ là biến cố: "Học sinh được chọn giành huy chương vàng".\\\\
            Gọi $\\overline{C}$ là biến cố: "Học sinh được chọn không giành huy chương vàng".\\\\
            Xác suất để học sinh đó không giành huy chương vàng biết rằng học sinh đó thuộc trường B là $P\\left(\\overline{C}|B\\right) = 1 - %s = %s$.'''       
                       %(str_pB, str_P_notC_given_B))

            # Đưa các lời giải vào danh sách lời giải
            list_th_2 = [loigiai_th_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_th = list(zip(list_th_1, list_th_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_th)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## Vận dụng ############################################
            # Các đáp án
            vd_da_1_d = '\\True Xác suất để học sinh được chọn giành huy chương vàng là $\\frac{%s}{%s}$' %(P_C.p, P_C.q)  
            vd_da_1_s = 'Xác suất để học sinh được chọn giành huy chương vàng là $\\frac{%s}{%s}$' %(fake_P_C.p, fake_P_C.q)  
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Theo công thức xác suất toàn phần, xác suất để học sinh được chọn giành huy chương vàng là:\\\\
            $P\\left(C\\right) = P\\left(A\\right) \\cdot P\\left(C|A\\right) + P\\left(B\\right) \\cdot P\\left(C|B\\right) = \\frac{%s}{%s} \\cdot %s + \\frac{%s}{%s} \\cdot %s = \\frac{%s}{%s}$.'''  
                       %(P_A.p, P_A.q, str_pA, P_B.p, P_B.q, str_pB, P_C.p, P_C.q))

            # Đưa các lời giải vào danh sách lời giải
            list_vd_2 = [loigiai_vd_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vd = list(zip(list_vd_1, list_vd_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vd)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## Vận dụng cao ############################################
            # Các đáp án
            vdc_da_1_d = '\\True Biết rằng học sinh được chọn giành huy chương vàng, xác suất để học sinh đó thuộc trường A là $\\frac{%s}{%s}$' %(P_A_given_C.p, P_A_given_C.q) 
            vdc_da_1_s = 'Biết rằng học sinh được chọn giành huy chương vàng, xác suất để học sinh đó thuộc trường A là $\\frac{%s}{%s}$' %(fake_P_A_given_C.p, fake_P_A_given_C.q) 
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Theo công thức Bayes, xác suất học sinh đó thuộc trường A biết rằng học sinh đó giành huy chương vàng là:\\\\
            $P\\left(A|C\\right) = \\frac{P\\left(A \\cap C\\right)}{P\\left(C\\right)} = \\frac{P\\left(A\\right) \\cdot P\\left(C|A\\right)}{P\\left(C\\right)} = \\frac{\\frac{%s}{%s} \\cdot %s}{\\frac{%s}{%s}} = \\frac{%s}{%s}$.'''
                       %(P_A.p, P_A.q, str_pA, P_C.p, P_C.q, P_A_given_C.p, P_A_given_C.q))

            # Đưa các lời giải vào danh sách lời giải
            list_vdc_2 = [loigiai_vdc_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vdc)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi đáp án có từ 1 đến 3 đúng
            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

            # Gán lại vào list
            list_nb_1 = [nb_da_1]
            list_th_1 = [th_da_1]
            list_vd_1 = [vd_da_1]
            list_vdc_1 = [vdc_da_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            combined_th = list(zip(list_th_1, list_th_2))
            combined_vd = list(zip(list_vd_1, list_vd_2))
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            random.shuffle(combined_nb)
            random.shuffle(combined_th)
            random.shuffle(combined_vd)
            random.shuffle(combined_vdc)

            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
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
                '\\end{ex}\n'
                '\\end{minipage}\n\n')
            return content

