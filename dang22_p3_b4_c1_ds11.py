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


def bt_dang22_p3_b4_c1_ds11(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        # Biên độ dao động s0 = a*sqrt(2) hoặc random biên độ
        # omega và phi
        omega = random.randint(4, 9)
        # Thời gian khảo sát T_total (giây)
        T_total = random.choice([20, 25, 30, 35, 40])


        k_min = 0
        k_max = math.floor(omega * T_total - 1/6)

        if (1 + 6 * k_max) / (6 * omega) == T_total:
            so_lan = k_max  # loại mốc t = T_total nếu xét khoảng (0; T_total)
        else:
            so_lan = k_max - k_min + 1

        ans_correct = so_lan

        # Tạo các phương án nhiễu
        sai_1 = ans_correct + 1
        sai_2 = ans_correct - 1
        sai_3 = ans_correct - 2

        ds_dapan = [ans_correct, sai_1, sai_2, sai_3]
        # Gán nhãn trắc nghiệm A, B, C, D
        # Để tạo trắc nghiệm 4 phương án:
        dap_an_dung = ans_correct
        # Trộn phương án
        options = [ans_correct, sai_1, sai_2, sai_3]
        random.shuffle(options)

        labels = ['A', 'B', 'C', 'D']
        idx_correct = options.index(ans_correct)

        pa_str = []
        for i in range(4):
            if i == idx_correct:
                pa_str.append('\\True %s' % options[i])
            else:
                pa_str.append('%s' % options[i])

        # Hình vẽ TikZ con lắc đơn và đồng hồ bấm giờ (100% chi tiết, đường nét đen 1pt)
        tikz_hinh = ('''\\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
        	\\tikzset {_uxc998g3d/.code = {\\pgfsetadditionalshadetransform{ \\pgftransformshift{\\pgfpoint{0 bp } { 0 bp }  }  \\pgftransformrotate{-35 }  \\pgftransformscale{2 }  }}}
        	\\pgfdeclarehorizontalshading{_lvj13w3a6}{150bp}{rgb(0bp)=(0.36,0.4,0.45);
        		rgb(38.98102896554129bp)=(0.36,0.4,0.45);
        		rgb(44.67745644705636bp)=(1,1,1);
        		rgb(52.71317073277065bp)=(0.6,0.69,0.8);
        		rgb(61.74888610839844bp)=(0.27,0.32,0.38);
        		rgb(100bp)=(0.27,0.32,0.38)}
        	\\tikzset {_uzlxo3ruc/.code = {\\pgfsetadditionalshadetransform{ \\pgftransformshift{\\pgfpoint{0 bp } { 0 bp }  }  \\pgftransformrotate{-35 }  \\pgftransformscale{2 }  }}}
        	\\pgfdeclarehorizontalshading{_r0qr408ox}{150bp}{rgb(0bp)=(0.36,0.4,0.45);
        		rgb(38.98102896554129bp)=(0.36,0.4,0.45);
        		rgb(44.67745644705636bp)=(1,1,1);
        		rgb(52.71317073277065bp)=(0.6,0.69,0.8);
        		rgb(61.74888610839844bp)=(0.27,0.32,0.38);
        		rgb(100bp)=(0.27,0.32,0.38)}
        	\\tikzset {_9m7sgrc0p/.code = {\\pgfsetadditionalshadetransform{ \\pgftransformshift{\\pgfpoint{0 bp } { 0 bp }  }  \\pgftransformrotate{0 }  \\pgftransformscale{2 }  }}}
        	\\pgfdeclarehorizontalshading{_fmfheor7x}{150bp}{rgb(0bp)=(0.36,0.4,0.45);
        		rgb(38.98102896554129bp)=(0.36,0.4,0.45);
        		rgb(44.67745644705636bp)=(1,1,1);
        		rgb(52.71317073277065bp)=(0.6,0.69,0.8);
        		rgb(61.74888610839844bp)=(0.27,0.32,0.38);
        		rgb(100bp)=(0.27,0.32,0.38)}
        	\\tikzset {_08own38hd/.code = {\\pgfsetadditionalshadetransform{ \\pgftransformshift{\\pgfpoint{0 bp } { 0 bp }  }  \\pgftransformrotate{0 }  \\pgftransformscale{2 }  }}}
        	\\pgfdeclarehorizontalshading{_eopf9q2a1}{150bp}{rgb(0bp)=(0.36,0.4,0.45);
        		rgb(38.98102896554129bp)=(0.36,0.4,0.45);
        		rgb(44.67745644705636bp)=(1,1,1);
        		rgb(52.71317073277065bp)=(0.6,0.69,0.8);
        		rgb(61.74888610839844bp)=(0.27,0.32,0.38);
        		rgb(100bp)=(0.27,0.32,0.38)}
        	\\tikzset {_24ievj970/.code = {\\pgfsetadditionalshadetransform{ \\pgftransformshift{\\pgfpoint{0 bp } { 0 bp }  }  \\pgftransformrotate{-92 }  \\pgftransformscale{2 }  }}}
        	\\pgfdeclarehorizontalshading{_6wrgxew8n}{150bp}{rgb(0bp)=(0.27,0.36,0.47);
        		rgb(37.5bp)=(0.27,0.36,0.47);
        		rgb(42.98102787562779bp)=(0.27,0.36,0.47);
        		rgb(50bp)=(1,1,1);
        		rgb(56.12388065883091bp)=(0.27,0.36,0.47);
        		rgb(62.5bp)=(0.36,0.44,0.53);
        		rgb(100bp)=(0.36,0.44,0.53)}
        	\\tikzset {_cr0yrr77o/.code = {\\pgfsetadditionalshadetransform{ \\pgftransformshift{\\pgfpoint{0 bp } { 0 bp }  }  \\pgftransformrotate{-85 }  \\pgftransformscale{2 }  }}}
        	\\pgfdeclarehorizontalshading{_eh67k8otl}{150bp}{rgb(0bp)=(0.36,0.4,0.45);
        		rgb(38.98102896554129bp)=(0.36,0.4,0.45);
        		rgb(44.67745644705636bp)=(1,1,1);
        		rgb(52.71317073277065bp)=(0.6,0.69,0.8);
        		rgb(61.74888610839844bp)=(0.27,0.32,0.38);
        		rgb(100bp)=(0.27,0.32,0.38)}
        	\\tikzset {_m4l5gnp5h/.code = {\\pgfsetadditionalshadetransform{ \\pgftransformshift{\\pgfpoint{0 bp } { 0 bp }  }  \\pgftransformrotate{-85 }  \\pgftransformscale{2 }  }}}
        	\\pgfdeclarehorizontalshading{_511vh41xn}{150bp}{rgb(0bp)=(0.36,0.4,0.45);
        		rgb(38.98102896554129bp)=(0.36,0.4,0.45);
        		rgb(44.67745644705636bp)=(1,1,1);
        		rgb(52.71317073277065bp)=(0.6,0.69,0.8);
        		rgb(61.74888610839844bp)=(0.27,0.32,0.38);
        		rgb(100bp)=(0.27,0.32,0.38)}
        	\\tikzset {_580c3fu8b/.code = {\\pgfsetadditionalshadetransform{ \\pgftransformshift{\\pgfpoint{0 bp } { 0 bp }  }  \\pgftransformrotate{0 }  \\pgftransformscale{2 }  }}}
        	\\pgfdeclarehorizontalshading{_4by52mc4q}{150bp}{rgb(0bp)=(0.47,0.54,0.63);
        		rgb(39.892856052943635bp)=(0.47,0.54,0.63);
        		rgb(46.58928462437221bp)=(1,1,1);
        		rgb(61.05357033865793bp)=(0.38,0.46,0.55);
        		rgb(100bp)=(0.38,0.46,0.55)}
        	\\tikzset {_4jd6naxyb/.code = {\\pgfsetadditionalshadetransform{ \\pgftransformshift{\\pgfpoint{0 bp } { 0 bp }  }  \\pgftransformrotate{0 }  \\pgftransformscale{2 }  }}}
        	\\pgfdeclarehorizontalshading{_3qijztiqv}{150bp}{rgb(0bp)=(0.36,0.4,0.45);
        		rgb(38.98102896554129bp)=(0.36,0.4,0.45);
        		rgb(44.67745644705636bp)=(1,1,1);
        		rgb(52.71317073277065bp)=(0.6,0.69,0.8);
        		rgb(61.74888610839844bp)=(0.27,0.32,0.38);
        		rgb(100bp)=(0.27,0.32,0.38)}
        	\\tikzset {_pmlghip12/.code = {\\pgfsetadditionalshadetransform{ \\pgftransformshift{\\pgfpoint{89.1 bp } { -108.9 bp }  }  \\pgftransformscale{1.32 }  }}}
        	\\pgfdeclareradialshading{_gige4sx33}{\\pgfpoint{-72bp}{88bp}}{rgb(0bp)=(1,1,1);
        		rgb(0bp)=(1,1,1);
        		rgb(13.999998910086495bp)=(0.27,0.35,0.46);
        		rgb(24.427457536969865bp)=(0,0,0);
        		rgb(400bp)=(0,0,0)}
        	\\tikzset {_1mkzw1zyt/.code = {\\pgfsetadditionalshadetransform{ \\pgftransformshift{\\pgfpoint{0 bp } { 0 bp }  }  \\pgftransformrotate{-92 }  \\pgftransformscale{2 }  }}}
        	\\pgfdeclarehorizontalshading{_ivrvuvixy}{150bp}{rgb(0bp)=(0.27,0.36,0.47);
        		rgb(37.5bp)=(0.27,0.36,0.47);
        		rgb(42.98102787562779bp)=(0.27,0.36,0.47);
        		rgb(50bp)=(1,1,1);
        		rgb(56.12388065883091bp)=(0.27,0.36,0.47);
        		rgb(62.5bp)=(0.36,0.44,0.53);
        		rgb(100bp)=(0.36,0.44,0.53)}
        	\\tikzset {_o6cb0k3p6/.code = {\\pgfsetadditionalshadetransform{ \\pgftransformshift{\\pgfpoint{89.1 bp } { -108.9 bp }  }  \\pgftransformscale{1.32 }  }}}
        	\\pgfdeclareradialshading{_3iytni3ru}{\\pgfpoint{-72bp}{88bp}}{rgb(0bp)=(1,1,1);
        		rgb(0bp)=(1,1,1);
        		rgb(16.857141767229354bp)=(0.27,0.35,0.46);
        		rgb(24.803570338657924bp)=(0,0,0);
        		rgb(400bp)=(0,0,0)}
        	\\tikzset {_gnyntclcl/.code = {\\pgfsetadditionalshadetransform{ \\pgftransformshift{\\pgfpoint{0 bp } { 0 bp }  }  \\pgftransformrotate{0 }  \\pgftransformscale{2 }  }}}
        	\\pgfdeclarehorizontalshading{_sx1ipk9ri}{150bp}{rgb(0bp)=(0.38,0.49,0.62);
        		rgb(37.5bp)=(0.38,0.49,0.62);
        		rgb(50bp)=(1,1,1);
        		rgb(62.5bp)=(0.57,0.64,0.73);
        		rgb(100bp)=(0.57,0.64,0.73)}
        	\\tikzset{every picture/.style={line width=0.75pt}} 
        	\\path  [shading=_lvj13w3a6,_uxc998g3d] (291.27,67.21) -- (296.16,61.44) .. controls (296.61,60.91) and (298.73,61.97) .. (300.91,63.81) .. controls (303.08,65.65) and (304.48,67.58) .. (304.03,68.11) -- (299.14,73.87) .. controls (298.69,74.41) and (296.56,73.34) .. (294.39,71.5) .. controls (292.22,69.66) and (290.82,67.74) .. (291.27,67.21) .. controls (291.72,66.68) and (293.85,67.74) .. (296.02,69.58) .. controls (298.19,71.42) and (299.59,73.34) .. (299.14,73.87) ; 
        	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.31 ] (291.27,67.21) -- (296.16,61.44) .. controls (296.61,60.91) and (298.73,61.97) .. (300.91,63.81) .. controls (303.08,65.65) and (304.48,67.58) .. (304.03,68.11) -- (299.14,73.87) .. controls (298.69,74.41) and (296.56,73.34) .. (294.39,71.5) .. controls (292.22,69.66) and (290.82,67.74) .. (291.27,67.21) .. controls (291.72,66.68) and (293.85,67.74) .. (296.02,69.58) .. controls (298.19,71.42) and (299.59,73.34) .. (299.14,73.87) ; 
        	\\path  [shading=_r0qr408ox,_uzlxo3ruc] (286.68,74.53) -- (291.51,68.83) .. controls (292.37,67.82) and (294.41,68.14) .. (296.06,69.54) .. controls (297.71,70.94) and (298.35,72.89) .. (297.5,73.9) -- (292.66,79.6) .. controls (291.81,80.62) and (289.77,80.3) .. (288.12,78.9) .. controls (286.47,77.5) and (285.82,75.55) .. (286.68,74.53) .. controls (287.54,73.52) and (289.57,73.84) .. (291.23,75.24) .. controls (292.88,76.64) and (293.52,78.59) .. (292.66,79.6) ; 
        	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.31 ] (286.68,74.53) -- (291.51,68.83) .. controls (292.37,67.82) and (294.41,68.14) .. (296.06,69.54) .. controls (297.71,70.94) and (298.35,72.89) .. (297.5,73.9) -- (292.66,79.6) .. controls (291.81,80.62) and (289.77,80.3) .. (288.12,78.9) .. controls (286.47,77.5) and (285.82,75.55) .. (286.68,74.53) .. controls (287.54,73.52) and (289.57,73.84) .. (291.23,75.24) .. controls (292.88,76.64) and (293.52,78.59) .. (292.66,79.6) ; 
        	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.47 ][fill={rgb, 255:red, 141; green, 159; blue, 181 }  ,fill opacity=1 ,even odd rule] (247.32,42.11) .. controls (247.32,36.38) and (251.94,31.72) .. (257.63,31.72) .. controls (263.33,31.72) and (267.95,36.38) .. (267.95,42.11) .. controls (267.95,47.85) and (263.33,52.51) .. (257.63,52.51) .. controls (251.94,52.51) and (247.32,47.85) .. (247.32,42.11)(244.95,42.11) .. controls (244.95,35.07) and (250.63,29.36) .. (257.63,29.36) .. controls (264.64,29.36) and (270.32,35.07) .. (270.32,42.11) .. controls (270.32,49.16) and (264.64,54.87) .. (257.63,54.87) .. controls (250.63,54.87) and (244.95,49.16) .. (244.95,42.11) ;
        	\\path  [shading=_fmfheor7x,_9m7sgrc0p] (251.42,60.73) -- (251.3,50.23) .. controls (251.29,49.01) and (254.05,47.98) .. (257.47,47.95) .. controls (260.88,47.91) and (263.66,48.87) .. (263.68,50.09) -- (263.8,60.59) .. controls (263.81,61.81) and (261.05,62.84) .. (257.63,62.87) .. controls (254.22,62.91) and (251.43,61.95) .. (251.42,60.73) .. controls (251.41,59.51) and (254.17,58.48) .. (257.58,58.44) .. controls (261,58.41) and (263.78,59.37) .. (263.8,60.59) ; 
        	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.31 ] (251.42,60.73) -- (251.3,50.23) .. controls (251.29,49.01) and (254.05,47.98) .. (257.47,47.95) .. controls (260.88,47.91) and (263.66,48.87) .. (263.68,50.09) -- (263.8,60.59) .. controls (263.81,61.81) and (261.05,62.84) .. (257.63,62.87) .. controls (254.22,62.91) and (251.43,61.95) .. (251.42,60.73) .. controls (251.41,59.51) and (254.17,58.48) .. (257.58,58.44) .. controls (261,58.41) and (263.78,59.37) .. (263.8,60.59) ; 
        	\\path  [shading=_eopf9q2a1,_08own38hd] (250.08,67.22) -- (249.97,57.63) .. controls (249.95,56.15) and (253.38,54.92) .. (257.63,54.87) .. controls (261.88,54.83) and (265.34,55.98) .. (265.36,57.46) -- (265.46,67.04) .. controls (265.48,68.52) and (262.05,69.75) .. (257.8,69.8) .. controls (253.55,69.85) and (250.09,68.69) .. (250.08,67.22) .. controls (250.06,65.74) and (253.49,64.51) .. (257.74,64.46) .. controls (261.99,64.41) and (265.45,65.57) .. (265.46,67.04) ; 
        	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.31 ] (250.08,67.22) -- (249.97,57.63) .. controls (249.95,56.15) and (253.38,54.92) .. (257.63,54.87) .. controls (261.88,54.83) and (265.34,55.98) .. (265.36,57.46) -- (265.46,67.04) .. controls (265.48,68.52) and (262.05,69.75) .. (257.8,69.8) .. controls (253.55,69.85) and (250.09,68.69) .. (250.08,67.22) .. controls (250.06,65.74) and (253.49,64.51) .. (257.74,64.46) .. controls (261.99,64.41) and (265.45,65.57) .. (265.46,67.04) ; 
        	\\path  [shading=_6wrgxew8n,_24ievj970] (183.39,43.2) -- (186.55,43.13) .. controls (187.13,43.12) and (187.64,45.12) .. (187.69,47.61) .. controls (187.74,50.09) and (187.31,52.11) .. (186.74,52.12) -- (183.57,52.19) .. controls (183,52.2) and (182.49,50.2) .. (182.44,47.71) .. controls (182.38,45.23) and (182.81,43.21) .. (183.39,43.2) .. controls (183.97,43.19) and (184.48,45.19) .. (184.53,47.67) .. controls (184.58,50.15) and (184.15,52.18) .. (183.57,52.19) ; 
        	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.55 ] (183.39,43.2) -- (186.55,43.13) .. controls (187.13,43.12) and (187.64,45.12) .. (187.69,47.61) .. controls (187.74,50.09) and (187.31,52.11) .. (186.74,52.12) -- (183.57,52.19) .. controls (183,52.2) and (182.49,50.2) .. (182.44,47.71) .. controls (182.38,45.23) and (182.81,43.21) .. (183.39,43.2) .. controls (183.97,43.19) and (184.48,45.19) .. (184.53,47.67) .. controls (184.58,50.15) and (184.15,52.18) .. (183.57,52.19) ;  
        	\\path  [shading=_eh67k8otl,_cr0yrr77o] (177.95,44.86) -- (183.62,44.84) .. controls (184.12,44.84) and (184.52,46.01) .. (184.53,47.45) .. controls (184.53,48.9) and (184.13,50.07) .. (183.63,50.07) -- (177.96,50.09) .. controls (177.46,50.09) and (177.06,48.92) .. (177.06,47.47) .. controls (177.05,46.03) and (177.45,44.86) .. (177.95,44.86) .. controls (178.44,44.85) and (178.85,46.02) .. (178.85,47.47) .. controls (178.86,48.91) and (178.46,50.09) .. (177.96,50.09) ; 
        	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.55 ] (177.95,44.86) -- (183.62,44.84) .. controls (184.12,44.84) and (184.52,46.01) .. (184.53,47.45) .. controls (184.53,48.9) and (184.13,50.07) .. (183.63,50.07) -- (177.96,50.09) .. controls (177.46,50.09) and (177.06,48.92) .. (177.06,47.47) .. controls (177.05,46.03) and (177.45,44.86) .. (177.95,44.86) .. controls (178.44,44.85) and (178.85,46.02) .. (178.85,47.47) .. controls (178.86,48.91) and (178.46,50.09) .. (177.96,50.09) ; 
        	\\draw    (118.72,55.28) -- (118.72,168.73) ;
        	\\draw    (118.72,55.28) -- (166.55,146.45) ;
        	\\path  [shading=_511vh41xn,_m4l5gnp5h] (77.27,43.84) -- (178.47,43.57) .. controls (179.78,43.57) and (180.85,45.32) .. (180.85,47.47) .. controls (180.86,49.63) and (179.8,51.38) .. (178.49,51.38) -- (77.29,51.65) .. controls (75.97,51.65) and (74.91,49.91) .. (74.9,47.75) .. controls (74.89,45.59) and (75.95,43.84) .. (77.27,43.84) .. controls (78.58,43.84) and (79.65,45.58) .. (79.65,47.74) .. controls (79.66,49.89) and (78.6,51.65) .. (77.29,51.65) ; 
        	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.55 ] (77.27,43.84) -- (178.47,43.57) .. controls (179.78,43.57) and (180.85,45.32) .. (180.85,47.47) .. controls (180.86,49.63) and (179.8,51.38) .. (178.49,51.38) -- (77.29,51.65) .. controls (75.97,51.65) and (74.91,49.91) .. (74.9,47.75) .. controls (74.89,45.59) and (75.95,43.84) .. (77.27,43.84) .. controls (78.58,43.84) and (79.65,45.58) .. (79.65,47.74) .. controls (79.66,49.89) and (78.6,51.65) .. (77.29,51.65) ; 
        	\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.22 ] (205.2,208.6) -- (219,208.5) -- (204.7,224.1) -- (194.7,225.6) -- cycle ;
        	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.22 ][fill={rgb, 255:red, 154; green, 176; blue, 203 }  ,fill opacity=1 ] (142.7,195.1) -- (209,196) -- (194.7,211.6) -- (129.2,211.1) -- cycle ;
        	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ][fill={rgb, 255:red, 136; green, 153; blue, 174 }  ,fill opacity=1 ] (129.2,211.1) -- (194.7,211.6) -- (195.2,225.1) -- (129.2,225.1) -- cycle ;
        	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ][fill={rgb, 255:red, 97; green, 109; blue, 123 }  ,fill opacity=1 ] (194.7,211.6) -- (209,196) -- (208.2,211.1) -- (194.7,225.6) -- cycle ;
        	\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (129.2,211.1) -- (194.7,211.6) ;
        	\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.22 ]   (130.2,211.1) -- (130.2,225.1) ;
        	\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.22 ]   (143.7,195.1) -- (131.2,211.1) ;
        	\\path  [shading=_4by52mc4q,_580c3fu8b] (157.78,203.05) .. controls (157.78,200.58) and (162.39,198.57) .. (168.09,198.57) .. controls (173.78,198.57) and (178.4,200.58) .. (178.4,203.05) .. controls (178.4,205.52) and (173.78,207.52) .. (168.09,207.52) .. controls (162.39,207.52) and (157.78,205.52) .. (157.78,203.05) -- cycle ; 
        	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.55 ] (157.78,203.05) .. controls (157.78,200.58) and (162.39,198.57) .. (168.09,198.57) .. controls (173.78,198.57) and (178.4,200.58) .. (178.4,203.05) .. controls (178.4,205.52) and (173.78,207.52) .. (168.09,207.52) .. controls (162.39,207.52) and (157.78,205.52) .. (157.78,203.05) -- cycle ; 
        	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.55 ][fill={rgb, 255:red, 154; green, 176; blue, 203 }  ,fill opacity=1 ] (157.84,201.7) .. controls (157.84,199.22) and (162.39,197.22) .. (168.01,197.22) .. controls (173.63,197.22) and (178.18,199.22) .. (178.18,201.7) .. controls (178.18,204.17) and (173.63,206.17) .. (168.01,206.17) .. controls (162.39,206.17) and (157.84,204.17) .. (157.84,201.7) -- cycle ;
        	\\path  [shading=_3qijztiqv,_4jd6naxyb] (172.01,46.12) -- (172.01,201.75) .. controls (172.01,202.52) and (170.26,203.15) .. (168.1,203.15) .. controls (165.94,203.15) and (164.19,202.52) .. (164.19,201.75) -- (164.19,46.12) .. controls (164.19,45.35) and (165.94,44.72) .. (168.1,44.72) .. controls (170.26,44.72) and (172.01,45.35) .. (172.01,46.12) .. controls (172.01,46.89) and (170.26,47.52) .. (168.1,47.52) .. controls (165.94,47.52) and (164.19,46.89) .. (164.19,46.12) ; 
        	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.55 ] (172.01,46.12) -- (172.01,201.75) .. controls (172.01,202.52) and (170.26,203.15) .. (168.1,203.15) .. controls (165.94,203.15) and (164.19,202.52) .. (164.19,201.75) -- (164.19,46.12) .. controls (164.19,45.35) and (165.94,44.72) .. (168.1,44.72) .. controls (170.26,44.72) and (172.01,45.35) .. (172.01,46.12) .. controls (172.01,46.89) and (170.26,47.52) .. (168.1,47.52) .. controls (165.94,47.52) and (164.19,46.89) .. (164.19,46.12) ; 
        	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.43 ][fill={rgb, 255:red, 81; green, 92; blue, 106 }  ,fill opacity=1 ] (158.2,40.8) .. controls (158.2,39.58) and (159.19,38.6) .. (160.4,38.6) -- (175.8,38.6) .. controls (177.01,38.6) and (178,39.58) .. (178,40.8) -- (178,54.24) .. controls (178,55.46) and (177.01,56.44) .. (175.8,56.44) -- (160.4,56.44) .. controls (159.19,56.44) and (158.2,55.46) .. (158.2,54.24) -- cycle ;
        	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.43 ][fill={rgb, 255:red, 154; green, 176; blue, 203 }  ,fill opacity=1 ] (159.75,40.02) .. controls (159.75,38.92) and (160.65,38.02) .. (161.75,38.02) -- (174.5,38.02) .. controls (175.6,38.02) and (176.5,38.92) .. (176.5,40.02) -- (176.5,52.27) .. controls (176.5,53.38) and (175.6,54.27) .. (174.5,54.27) -- (161.75,54.27) .. controls (160.65,54.27) and (159.75,53.38) .. (159.75,52.27) -- cycle ;
        	\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.66 ]   (160.4,39.6) -- (160.75,52.27) ;
        	\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.66 ]   (161.75,39.02) -- (174.5,39.02) ;
        	\\path  [shading=_gige4sx33,_pmlghip12] (114.27,55.28) .. controls (114.27,52.83) and (116.26,50.83) .. (118.72,50.83) .. controls (121.17,50.83) and (123.17,52.83) .. (123.17,55.28) .. controls (123.17,57.74) and (121.17,59.73) .. (118.72,59.73) .. controls (116.26,59.73) and (114.27,57.74) .. (114.27,55.28) -- cycle ; 
        	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ] (114.27,55.28) .. controls (114.27,52.83) and (116.26,50.83) .. (118.72,50.83) .. controls (121.17,50.83) and (123.17,52.83) .. (123.17,55.28) .. controls (123.17,57.74) and (121.17,59.73) .. (118.72,59.73) .. controls (116.26,59.73) and (114.27,57.74) .. (114.27,55.28) -- cycle ; 
        	\\path  [shading=_ivrvuvixy,_1mkzw1zyt] (74.57,42.98) -- (78.85,42.89) .. controls (80.03,42.87) and (81.04,44.98) .. (81.09,47.6) .. controls (81.14,50.23) and (80.23,52.38) .. (79.04,52.4) -- (74.76,52.49) .. controls (73.58,52.51) and (72.58,50.4) .. (72.52,47.78) .. controls (72.47,45.15) and (73.38,43) .. (74.57,42.98) .. controls (75.75,42.95) and (76.75,45.06) .. (76.81,47.69) .. controls (76.86,50.32) and (75.94,52.46) .. (74.76,52.49) ; 
        	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.55 ] (74.57,42.98) -- (78.85,42.89) .. controls (80.03,42.87) and (81.04,44.98) .. (81.09,47.6) .. controls (81.14,50.23) and (80.23,52.38) .. (79.04,52.4) -- (74.76,52.49) .. controls (73.58,52.51) and (72.58,50.4) .. (72.52,47.78) .. controls (72.47,45.15) and (73.38,43) .. (74.57,42.98) .. controls (75.75,42.95) and (76.75,45.06) .. (76.81,47.69) .. controls (76.86,50.32) and (75.94,52.46) .. (74.76,52.49) ; 
        	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.55 ][fill={rgb, 255:red, 207; green, 221; blue, 240 }  ,fill opacity=1 ] (68.67,150.65) .. controls (101.67,171.15) and (137.17,166.65) .. (168.17,155.65) .. controls (171.9,164.15) and (171.9,162.82) .. (173.17,167.15) .. controls (156.67,181.15) and (101.67,190.65) .. (62.17,165.15) .. controls (65.23,158.15) and (64.57,159.48) .. (68.67,150.65) -- cycle ;
        	\\path  [shading=_3iytni3ru,_o6cb0k3p6] (153.1,146.45) .. controls (153.1,139.02) and (159.12,133) .. (166.55,133) .. controls (173.98,133) and (180,139.02) .. (180,146.45) .. controls (180,153.88) and (173.98,159.9) .. (166.55,159.9) .. controls (159.12,159.9) and (153.1,153.88) .. (153.1,146.45) -- cycle ;  
        	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ] (153.1,146.45) .. controls (153.1,139.02) and (159.12,133) .. (166.55,133) .. controls (173.98,133) and (180,139.02) .. (180,146.45) .. controls (180,153.88) and (173.98,159.9) .. (166.55,159.9) .. controls (159.12,159.9) and (153.1,153.88) .. (153.1,146.45) -- cycle ; 
        	\\draw    (118.2,174.4) -- (118.2,181.4) ;
        	\\draw    (145.2,171.4) -- (146.95,178.4) ;
        	\\draw    (90.7,170.15) -- (88.7,176.9) ;
        	\\draw    (131.95,174.15) -- (132.7,180.4) ;
        	\\draw    (157.95,167.9) -- (159.95,174.9) ;
        	\\draw    (104.2,173.15) -- (103.2,179.65) ;
        	\\draw    (76.7,165.4) -- (74.2,171.4) ;
        	\\draw    (110.99,60.4) -- (110.51,158.3) ;
        	\\draw [shift={(110.5,161.3)}, rotate = 270.28] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (5.36,-2.57) -- (0,0) -- (5.36,2.57) -- (3.56,0) -- cycle    ;
        	\\draw [shift={(111,57.4)}, rotate = 90.28] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (5.36,-2.57) -- (0,0) -- (5.36,2.57) -- (3.56,0) -- cycle    ;
        	\\draw [color={rgb, 255:red, 74; green, 144; blue, 226 }  ,draw opacity=1 ]   (123.65,135.62) .. controls (134.11,135.88) and (146.64,131.81) .. (151.3,123.91) ;
        	\\draw [shift={(152.5,121.3)}, rotate = 108.43] [fill={rgb, 255:red, 74; green, 144; blue, 226 }  ,fill opacity=1 ][line width=0.08]  [draw opacity=0] (5.36,-2.57) -- (0,0) -- (5.36,2.57) -- (3.56,0) -- cycle    ;
        	\\draw [shift={(120.5,135.4)}, rotate = 6.65] [fill={rgb, 255:red, 74; green, 144; blue, 226 }  ,fill opacity=1 ][line width=0.08]  [draw opacity=0] (5.36,-2.57) -- (0,0) -- (5.36,2.57) -- (3.56,0) -- cycle    ;
        	\\path  [shading=_sx1ipk9ri,_gnyntclcl] (206.3,112.3) .. controls (206.3,83.86) and (229.36,60.8) .. (257.8,60.8) .. controls (286.24,60.8) and (309.3,83.86) .. (309.3,112.3) .. controls (309.3,140.74) and (286.24,163.8) .. (257.8,163.8) .. controls (229.36,163.8) and (206.3,140.74) .. (206.3,112.3) -- cycle ; 
        	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ] (206.3,112.3) .. controls (206.3,83.86) and (229.36,60.8) .. (257.8,60.8) .. controls (286.24,60.8) and (309.3,83.86) .. (309.3,112.3) .. controls (309.3,140.74) and (286.24,163.8) .. (257.8,163.8) .. controls (229.36,163.8) and (206.3,140.74) .. (206.3,112.3) -- cycle ; 
        	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ][fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (214.3,112.3) .. controls (214.3,88.28) and (233.78,68.8) .. (257.8,68.8) .. controls (281.82,68.8) and (301.3,88.28) .. (301.3,112.3) .. controls (301.3,136.32) and (281.82,155.8) .. (257.8,155.8) .. controls (233.78,155.8) and (214.3,136.32) .. (214.3,112.3) -- cycle ;
        	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ][fill={rgb, 255:red, 240; green, 236; blue, 236 }  ,fill opacity=1 ] (215.3,112.3) .. controls (215.3,88.83) and (234.33,69.8) .. (257.8,69.8) .. controls (281.27,69.8) and (300.3,88.83) .. (300.3,112.3) .. controls (300.3,135.77) and (281.27,154.8) .. (257.8,154.8) .. controls (234.33,154.8) and (215.3,135.77) .. (215.3,112.3) -- cycle ;
        	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ] (218.3,112.3) .. controls (218.3,90.48) and (235.98,72.8) .. (257.8,72.8) .. controls (279.62,72.8) and (297.3,90.48) .. (297.3,112.3) .. controls (297.3,134.12) and (279.62,151.8) .. (257.8,151.8) .. controls (235.98,151.8) and (218.3,134.12) .. (218.3,112.3) -- cycle ;
        	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ][fill={rgb, 255:red, 80; green, 100; blue, 123 }  ,fill opacity=1 ] (255.7,112.3) .. controls (255.7,111.14) and (256.64,110.2) .. (257.8,110.2) .. controls (258.96,110.2) and (259.9,111.14) .. (259.9,112.3) .. controls (259.9,113.46) and (258.96,114.4) .. (257.8,114.4) .. controls (256.64,114.4) and (255.7,113.46) .. (255.7,112.3) -- cycle ;
        	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.22 ][fill={rgb, 255:red, 71; green, 90; blue, 111 }  ,fill opacity=1 ] (257.75,111.4) -- (284.64,86.8) -- (258.9,112.3) -- cycle ;
        	\\draw    (257.8,72.8) -- (257.7,78.4) ;
        	\\draw    (257.9,146.2) -- (257.8,151.8) ;
        	\\draw    (218.3,112.3) -- (224.25,112.4) ;
        	\\draw    (291.35,112.2) -- (297.3,112.3) ;
        	\\draw    (236.3,79.3) -- (239.35,83.65) ;
        	\\draw    (222.8,94.55) -- (228.6,97.4) ;
        	\\draw    (286.05,128.05) -- (291.85,130.9) ;
        	\\draw    (274.05,141.8) -- (277.1,146.15) ;
        	\\draw    (276.05,77.55) -- (273.6,82.15) ;
        	\\draw    (290.55,90.05) -- (286.6,92.9) ;
        	\\draw    (227.35,128.9) -- (223.6,131.15) ;
        	\\draw    (238.85,140.15) -- (235.85,144.4) ;
        	\\draw (113.5,166.7) node [anchor=north west][inner sep=0.75pt]  [font=\\tiny]  {$0$};
        	\\draw (124.21,166.49) node [anchor=north west][inner sep=0.75pt]  [font=\\tiny,rotate=-354.5]  {$10$};
        	\\draw (136.97,164.9) node [anchor=north west][inner sep=0.75pt]  [font=\\tiny,rotate=-348.59]  {$20$};
        	\\draw (149.17,162.59) node [anchor=north west][inner sep=0.75pt]  [font=\\tiny,rotate=-344.28]  {$30$};
        	\\draw (98.76,164.8) node [anchor=north west][inner sep=0.75pt]  [font=\\tiny,rotate=-8.81]  {$10$};
        	\\draw (86.97,160.47) node [anchor=north west][inner sep=0.75pt]  [font=\\tiny,rotate=-16.06]  {$20$};
        	\\draw (73.08,156) node [anchor=north west][inner sep=0.75pt]  [font=\\tiny,rotate=-23.63]  {$30$};
        	\\draw (130,116.9) node [anchor=north west][inner sep=0.75pt]  [font=\\scriptsize,color={rgb, 255:red, 24; green, 85; blue, 155 }  ,opacity=1 ]  {$\\theta $};
        	\\draw (91,95.4) node [anchor=north west][inner sep=0.75pt]  [font=\\footnotesize]  {$L$};
        	\\draw (158.5,137.4) node [anchor=north west][inner sep=0.75pt]  [font=\\scriptsize]  {$m$};
        	\\draw (266.75,80.45) node [anchor=north west][inner sep=0.75pt]  [font=\\tiny]  {$5$};
        	\\draw (275,91.45) node [anchor=north west][inner sep=0.75pt]  [font=\\tiny]  {$10$};
        	\\draw (281.25,107.2) node [anchor=north west][inner sep=0.75pt]  [font=\\tiny]  {$15$};
        	\\draw (276.5,119.45) node [anchor=north west][inner sep=0.75pt]  [font=\\tiny]  {$20$};
        	\\draw (266.25,133.2) node [anchor=north west][inner sep=0.75pt]  [font=\\tiny]  {$25$};
        	\\draw (250.75,138.2) node [anchor=north west][inner sep=0.75pt]  [font=\\tiny]  {$30$};
        	\\draw (233.5,131.7) node [anchor=north west][inner sep=0.75pt]  [font=\\tiny]  {$35$};
        	\\draw (224.25,119.7) node [anchor=north west][inner sep=0.75pt]  [font=\\tiny]  {$40$};
        	\\draw (222,106.45) node [anchor=north west][inner sep=0.75pt]  [font=\\tiny]  {$45$};
        	\\draw (226.5,94.45) node [anchor=north west][inner sep=0.75pt]  [font=\\tiny]  {$50$};
        	\\draw (236.5,81.7) node [anchor=north west][inner sep=0.75pt]  [font=\\tiny]  {$55$};
        	\\draw (250.5,76.95) node [anchor=north west][inner sep=0.75pt]  [font=\\tiny]  {$60$};
        \\end{tikzpicture}''')

        # Nội dung câu hỏi
        noidungcauhoi = ('''\\immini{Học sinh An tiến hành làm một thí nghiệm trên một con lắc đơn. Tại vị trí cân bằng, An tác động một lực lên con lắc theo phương ngang. Từ các kết quả thí nghiệm, An tính được con lắc dao động điều hòa quanh vị trí cân bằng theo phương trình $s=2\\sqrt{2}\\cos\\left(%st+\\frac{\\pi}{3}\\right)$ với $s$ (cm) là độ dài cung quét của con lắc từ một vị trí bất kì tại thời điểm $t$ (giây) đến vị trí cân bằng. Con lắc đi qua vị trí cân bằng bao nhiêu lần trong khoảng thời gian từ $0$ đến $%s$ giây?}
    {%s}'''
                         % (omega, T_total, tikz_hinh))

        # Nội dung lời giải
        loigiai = ('''Vị trí cân bằng của con lắc ứng với $s=0$.\\\\
    Ta có phương trình:\\\\
    $2\\sqrt{2}\\cos\\left(%st+\\frac{\\pi}{3}\\right)=0 \\Leftrightarrow \\cos\\left(%st+\\frac{\\pi}{3}\\right)=0$\\\\
    $\\Leftrightarrow %st+\\frac{\\pi}{3}=\\frac{\\pi}{2}+k\\pi \\quad (k \\in \\mathbb{Z})$\\\\
    $\\Leftrightarrow %st=\\frac{\\pi}{6}+k\\pi \\Leftrightarrow t=\\frac{1}{%s}+\\frac{k}{%s} \\quad (k \\in \\mathbb{Z})$.\\\\
    Theo giả thiết, xét khoảng thời gian từ $0$ đến $%s$ giây nên:\\\\
    $0 < \\frac{1}{%s}+\\frac{k}{%s} < %s$\\\\
    $\\Leftrightarrow -\\frac{1}{6} < k < %s - \\frac{1}{6} \\Leftrightarrow -\\frac{1}{6} < k < %s$.\\\\
    Vì $k \\in \\mathbb{Z}$ nên $k \\in \\{%s; %s; \\ldots; %s\\}$.\\\\
    Số giá trị nguyên của $k$ là: $%s - %s + 1 = %s$.\\\\
    Vậy trong khoảng thời gian từ $0$ đến $%s$ giây, con lắc đi qua vị trí cân bằng $%s$ lần.'''
                   % (omega, omega,
                      omega,
                      omega, 6 * omega, omega,
                      T_total,
                      6 * omega, omega, T_total,
                      omega * T_total, Rational(6 * omega * T_total - 1, 6),
                      k_min, k_min + 1, k_max,
                      k_max, k_min, ans_correct,
                      T_total, ans_correct))

        # Đáp án
        dapan='\\shortans[0]{$%s$}\n'%(ans_correct)

    # Xuất câu hỏi với đáp án và lời giải đã được định dạng
    content = ('\\begin{minipage}{\\textwidth}\n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\\loigiai{\n' +
               str(loigiai) + '\n}\n' +
               '\\end{ex}\n' +
               '\\end{minipage}\n\n')
    return content

