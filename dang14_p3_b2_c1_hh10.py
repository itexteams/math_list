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


def bt_dang14_p3_b2_c1_hh10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Chiều cao tháp BC (chọn các số chẵn để kết quả chia 2 ra số nguyên đẹp)
                list_h = [40,42,44,46,48,52,54,56,58,62,64,66,68,70,72,74,76,78,82,84,86,88,92,94,96,98,102,104,106,108,112,114,116,118,122,124,126,128,130,132,134,136,138, 50, 60, 80, 90, 100, 110, 120, 140, 150, 160, 180, 200]
                h_thap = random.choice(list_h)

                # Tính toán kết quả AH = BC * sin(30) = BC / 2
                kq_num = int(h_thap / 2) if h_thap % 2 == 0 else h_thap / 2
                kq = str(kq_num).replace('.', ',')

                # Các đáp án trắc nghiệm
                du = ['$%s$' % (kq)]
                da = random.choice(du)

                # Tạo các đáp án sai (nhiễu)
                s = [
                    '$%s$' % (str(kq_num + 10).replace('.', ',')),
                    '$%s$' % (str(kq_num - 10).replace('.', ',')),
                    '$%s$' % (str(kq_num + 20).replace('.', ',')),
                    '$%s$' % (str(kq_num - 20).replace('.', ',')),
                    '$%s$' % (str(h_thap).replace('.', ',')),
                    '$%s$' % (str(int(h_thap * math.sqrt(3) / 2)).replace('.', ',')), # Bẫy tính nhầm cos(30)
                ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                hinhve=r'''\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-0.6,xscale=0.6]
            	\tikzset {_e5t15dpdb/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{-125 }  \pgftransformscale{2 }  }}}
            	\pgfdeclarehorizontalshading{_t1sqsuky1}{150bp}{rgb(0bp)=(0.55,0.34,0.16);
            		rgb(37.5bp)=(0.55,0.34,0.16);
            		rgb(50bp)=(0.93,0.93,0.74);
            		rgb(62.5bp)=(0.55,0.34,0.16);
            		rgb(100bp)=(0.55,0.34,0.16)}
            	\tikzset {_4sinojcrv/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{-125 }  \pgftransformscale{2 }  }}}
            	\pgfdeclarehorizontalshading{_3hhbu85jg}{150bp}{rgb(0bp)=(0.55,0.34,0.16);
            		rgb(37.5bp)=(0.55,0.34,0.16);
            		rgb(50bp)=(0.91,0.79,0.6);
            		rgb(62.5bp)=(0.55,0.34,0.16);
            		rgb(100bp)=(0.55,0.34,0.16)}
            	\tikzset {_dzhenvw4e/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{-114 }  \pgftransformscale{2 }  }}}
            	\pgfdeclarehorizontalshading{_iuck92yfx}{150bp}{rgb(0bp)=(0.29,0.56,0.89);
            		rgb(37.5bp)=(0.29,0.56,0.89);
            		rgb(50bp)=(0.83,0.89,0.93);
            		rgb(62.5bp)=(0.29,0.56,0.89);
            		rgb(100bp)=(0.29,0.56,0.89)}
            	\tikzset {_hu754y4dd/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{-125 }  \pgftransformscale{2 }  }}}
            	\pgfdeclarehorizontalshading{_5z89gg6q0}{150bp}{rgb(0bp)=(1,0,0);
            		rgb(37.5bp)=(1,0,0);
            		rgb(50bp)=(1,1,0);
            		rgb(62.5bp)=(1,0,0);
            		rgb(100bp)=(1,0,0)}
            	\tikzset{every picture/.style={line width=0.75pt}} 
            	\draw  [draw opacity=0][fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (261.48,206.03) -- (253.19,218.13) -- (249.14,204.04) -- (254.25,211.58) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (258.33,204.39) -- (249.66,216.43) -- (245.23,202.27) -- (250.72,209.88) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (265.53,206.66) -- (256.86,218.69) -- (252.43,204.54) -- (257.92,212.14) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (329.21,246.44) -- (324.02,254.21) -- (321.58,245.22) -- (324.71,250.02) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (327.26,245.4) -- (321.84,253.14) -- (319.17,244.11) -- (322.53,248.95) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (331.71,246.81) -- (326.29,254.55) -- (323.61,245.52) -- (326.97,250.36) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (301.98,227.03) -- (293.69,239.13) -- (289.64,225.04) -- (294.75,232.58) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (298.83,225.39) -- (290.16,237.43) -- (285.73,223.27) -- (291.22,230.88) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (306.03,227.66) -- (297.36,239.69) -- (292.93,225.54) -- (298.42,233.14) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (87.48,142.53) -- (79.19,154.63) -- (75.14,140.54) -- (80.25,148.08) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (84.33,140.89) -- (75.66,152.93) -- (71.23,138.77) -- (76.72,146.38) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (91.53,143.16) -- (82.86,155.19) -- (78.43,141.04) -- (83.92,148.64) -- cycle ;
            	\draw  [fill={rgb, 255:red, 193; green, 213; blue, 234 }  ,fill opacity=1 ] (154.33,184.73) -- (205.07,184.73) -- (205.07,188.73) -- (154.33,188.73) -- cycle ;
            	\path  [shading=_t1sqsuky1,_e5t15dpdb] (70.3,149.6) .. controls (77.3,149.6) and (84.53,154.67) .. (95.8,159.5) .. controls (104.11,163.06) and (116.14,164.02) .. (123.8,168) .. controls (137.59,175.16) and (145.87,185.82) .. (154.33,188.73) .. controls (170.96,188.66) and (189.17,188.35) .. (205.84,189.23) .. controls (214.95,189.72) and (218.61,188.46) .. (226.3,189.9) .. controls (243.3,197.8) and (238.09,197.44) .. (247.8,212) .. controls (252.35,218.83) and (275.8,217.5) .. (275.8,231.5) .. controls (286.3,237.5) and (338.3,265.6) .. (365.62,270.56) .. controls (291.8,270.5) and (105.3,271) .. (70.4,270.56) .. controls (70.3,234) and (70.3,195.6) .. (70.3,149.6) -- cycle ; 
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.3 ] (70.3,149.6) .. controls (77.3,149.6) and (84.53,154.67) .. (95.8,159.5) .. controls (104.11,163.06) and (116.14,164.02) .. (123.8,168) .. controls (137.59,175.16) and (145.87,185.82) .. (154.33,188.73) .. controls (170.96,188.66) and (189.17,188.35) .. (205.84,189.23) .. controls (214.95,189.72) and (218.61,188.46) .. (226.3,189.9) .. controls (243.3,197.8) and (238.09,197.44) .. (247.8,212) .. controls (252.35,218.83) and (275.8,217.5) .. (275.8,231.5) .. controls (286.3,237.5) and (338.3,265.6) .. (365.62,270.56) .. controls (291.8,270.5) and (105.3,271) .. (70.4,270.56) .. controls (70.3,234) and (70.3,195.6) .. (70.3,149.6) -- cycle ; 
            	\path  [shading=_3hhbu85jg,_4sinojcrv] (70.3,163.6) .. controls (77.8,165.6) and (86.53,172.77) .. (97.8,177.6) .. controls (106.11,181.16) and (114.64,191.12) .. (122.3,195.1) .. controls (136.09,202.26) and (143.84,203.18) .. (152.3,206.1) .. controls (170.8,202.4) and (167.3,190.4) .. (181.28,184.44) .. controls (197.3,196.9) and (215.3,198.1) .. (228.3,210.6) .. controls (247.8,224.1) and (244.09,209.04) .. (253.8,223.6) .. controls (258.35,230.43) and (272.3,222.1) .. (279.3,234.6) .. controls (298.3,230.1) and (324.3,259.6) .. (365.62,270.56) .. controls (291.8,270.5) and (105.3,271) .. (70.4,270.56) .. controls (70.3,234) and (70.8,209.6) .. (70.3,163.6) -- cycle ; % for fading 
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.3 ] (70.3,163.6) .. controls (77.8,165.6) and (86.53,172.77) .. (97.8,177.6) .. controls (106.11,181.16) and (114.64,191.12) .. (122.3,195.1) .. controls (136.09,202.26) and (143.84,203.18) .. (152.3,206.1) .. controls (170.8,202.4) and (167.3,190.4) .. (181.28,184.44) .. controls (197.3,196.9) and (215.3,198.1) .. (228.3,210.6) .. controls (247.8,224.1) and (244.09,209.04) .. (253.8,223.6) .. controls (258.35,230.43) and (272.3,222.1) .. (279.3,234.6) .. controls (298.3,230.1) and (324.3,259.6) .. (365.62,270.56) .. controls (291.8,270.5) and (105.3,271) .. (70.4,270.56) .. controls (70.3,234) and (70.8,209.6) .. (70.3,163.6) -- cycle ; 
            	\path  [shading=_iuck92yfx,_dzhenvw4e] (70.8,186) .. controls (78.3,188) and (91.03,197.17) .. (102.3,202) .. controls (110.61,205.56) and (124.64,211.52) .. (132.3,215.5) .. controls (146.09,222.66) and (147.34,225.58) .. (155.8,228.5) .. controls (172.43,228.42) and (168.13,229.61) .. (184.8,230.5) .. controls (193.91,230.99) and (207.3,205) .. (220.3,217.5) .. controls (239.8,231) and (241.09,213.94) .. (250.8,228.5) .. controls (255.35,235.33) and (283.8,235) .. (290.8,247.5) .. controls (309.8,243) and (324.58,259.04) .. (365.9,270) .. controls (292.08,269.94) and (105.58,270.44) .. (70.68,270) .. controls (70.58,233.44) and (69.3,229.5) .. (70.8,186) -- cycle ; % for fading 
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.3 ] (70.8,186) .. controls (78.3,188) and (91.03,197.17) .. (102.3,202) .. controls (110.61,205.56) and (124.64,211.52) .. (132.3,215.5) .. controls (146.09,222.66) and (147.34,225.58) .. (155.8,228.5) .. controls (172.43,228.42) and (168.13,229.61) .. (184.8,230.5) .. controls (193.91,230.99) and (207.3,205) .. (220.3,217.5) .. controls (239.8,231) and (241.09,213.94) .. (250.8,228.5) .. controls (255.35,235.33) and (283.8,235) .. (290.8,247.5) .. controls (309.8,243) and (324.58,259.04) .. (365.9,270) .. controls (292.08,269.94) and (105.58,270.44) .. (70.68,270) .. controls (70.58,233.44) and (69.3,229.5) .. (70.8,186) -- cycle ; 
            	\path  [shading=_5z89gg6q0,_hu754y4dd] (71.08,203.84) .. controls (78.58,205.84) and (98.81,225) .. (110.08,229.84) .. controls (118.39,233.4) and (124.14,230.92) .. (131.8,234.9) .. controls (145.59,242.06) and (156.34,215.98) .. (164.8,218.9) .. controls (181.43,218.82) and (174.13,239.51) .. (190.8,240.4) .. controls (199.91,240.89) and (207.8,225.9) .. (220.8,238.4) .. controls (240.3,251.9) and (247.59,234.84) .. (257.3,249.4) .. controls (261.85,256.23) and (274.8,241.9) .. (281.8,254.4) .. controls (300.8,249.9) and (324.58,259.04) .. (365.9,270) .. controls (292.08,269.94) and (105.58,270.44) .. (70.68,270) .. controls (70.58,233.44) and (69.58,247.34) .. (71.08,203.84) -- cycle ; 
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.3 ] (71.08,203.84) .. controls (78.58,205.84) and (98.81,225) .. (110.08,229.84) .. controls (118.39,233.4) and (124.14,230.92) .. (131.8,234.9) .. controls (145.59,242.06) and (156.34,215.98) .. (164.8,218.9) .. controls (181.43,218.82) and (174.13,239.51) .. (190.8,240.4) .. controls (199.91,240.89) and (207.8,225.9) .. (220.8,238.4) .. controls (240.3,251.9) and (247.59,234.84) .. (257.3,249.4) .. controls (261.85,256.23) and (274.8,241.9) .. (281.8,254.4) .. controls (300.8,249.9) and (324.58,259.04) .. (365.9,270) .. controls (292.08,269.94) and (105.58,270.44) .. (70.68,270) .. controls (70.58,233.44) and (69.58,247.34) .. (71.08,203.84) -- cycle ; 
            	\draw [fill={rgb, 255:red, 193; green, 213; blue, 234 }  ,fill opacity=1 ]   (181.07,50.67) -- (181.73,188) ;
            	\draw  [fill={rgb, 255:red, 193; green, 213; blue, 234 }  ,fill opacity=1 ] (162.04,182.42) -- (197.16,172.61) -- (197.73,174.67) -- (162.61,184.48) -- cycle ;
            	\draw  [fill={rgb, 255:red, 193; green, 213; blue, 234 }  ,fill opacity=1 ] (163.4,164.51) -- (195.07,155.67) -- (195.62,157.63) -- (163.95,166.48) -- cycle ;
            	\draw  [fill={rgb, 255:red, 193; green, 213; blue, 234 }  ,fill opacity=1 ] (166.43,148.63) -- (193.73,141) -- (194.25,142.85) -- (166.95,150.48) -- cycle ;
            	\draw  [fill={rgb, 255:red, 193; green, 213; blue, 234 }  ,fill opacity=1 ] (168.75,132.24) -- (191.07,126) -- (191.6,127.91) -- (169.28,134.15) -- cycle ;
            	\draw  [fill={rgb, 255:red, 193; green, 213; blue, 234 }  ,fill opacity=1 ] (171.75,115.93) -- (189.4,111) -- (189.93,112.88) -- (172.28,117.81) -- cycle ;
            	\draw  [fill={rgb, 255:red, 193; green, 213; blue, 234 }  ,fill opacity=1 ] (174.71,101.12) -- (187.07,97.67) -- (187.63,99.69) -- (175.28,103.15) -- cycle ;
            	\draw  [fill={rgb, 255:red, 193; green, 213; blue, 234 }  ,fill opacity=1 ] (176.51,88.58) -- (185.73,86) -- (186.17,87.57) -- (176.95,90.15) -- cycle ;
            	\draw  [fill={rgb, 255:red, 193; green, 213; blue, 234 }  ,fill opacity=1 ] (178.57,78.44) -- (183.73,77) -- (184.12,78.37) -- (178.95,79.81) -- cycle ;
            	\draw  [fill={rgb, 255:red, 193; green, 213; blue, 234 }  ,fill opacity=1 ] (163.12,166.95) -- (197.71,170.21) -- (197.52,172.16) -- (162.94,168.91) -- cycle ;
            	\draw  [fill={rgb, 255:red, 193; green, 213; blue, 234 }  ,fill opacity=1 ] (166.6,150.54) -- (195.29,153.25) -- (195.07,155.67) -- (166.37,152.96) -- cycle ;
            	\draw  [fill={rgb, 255:red, 193; green, 213; blue, 234 }  ,fill opacity=1 ] (169.19,135.09) -- (194.07,137.43) -- (193.85,139.81) -- (168.97,137.46) -- cycle ;
            	\draw  [fill={rgb, 255:red, 193; green, 213; blue, 234 }  ,fill opacity=1 ] (171.95,119.45) -- (191.54,123.94) -- (191.07,126) -- (171.48,121.51) -- cycle ;
            	\draw  [fill={rgb, 255:red, 193; green, 213; blue, 234 }  ,fill opacity=1 ] (174.28,107.54) -- (189.4,111) -- (189.93,108.67) -- (174.81,105.21) -- cycle ;
            	\draw  [fill={rgb, 255:red, 193; green, 213; blue, 234 }  ,fill opacity=1 ] (176.13,93.51) -- (186.25,99.06) -- (187.19,97.34) -- (177.07,91.79) -- cycle ;
            	\draw  [fill={rgb, 255:red, 193; green, 213; blue, 234 }  ,fill opacity=1 ] (178.01,81.53) -- (185.5,85.64) -- (186.4,84) -- (178.9,79.89) -- cycle ;
            	\draw  [fill={rgb, 255:red, 193; green, 213; blue, 234 }  ,fill opacity=1 ] (181.07,50.67) -- (181.07,62) -- (162.61,184.48) -- (159.07,185) -- cycle ;
            	\draw  [fill={rgb, 255:red, 193; green, 213; blue, 234 }  ,fill opacity=1 ] (181.07,62) -- (181.07,50.67) -- (201.73,184.33) -- (198.19,184.85) -- cycle ;
            	\draw [fill={rgb, 255:red, 193; green, 213; blue, 234 }  ,fill opacity=1 ]   (180.23,170.53) -- (164.07,181.33) ;
            	\draw [fill={rgb, 255:red, 193; green, 213; blue, 234 }  ,fill opacity=1 ]   (193.4,158.67) -- (182.07,169) ;
            	\draw [fill={rgb, 255:red, 193; green, 213; blue, 234 }  ,fill opacity=1 ]   (181.73,176.33) -- (165.73,169) ;
            	\draw [fill={rgb, 255:red, 193; green, 213; blue, 234 }  ,fill opacity=1 ]   (196.07,169) -- (182.4,162.33) ;
            	\draw [fill={rgb, 255:red, 193; green, 213; blue, 234 }  ,fill opacity=1 ]   (198.19,184.85) -- (183.73,179) ;
            	\draw [fill={rgb, 255:red, 193; green, 213; blue, 234 }  ,fill opacity=1 ]   (197.73,174.67) -- (181.28,184.44) ;
            	\draw [fill={rgb, 255:red, 193; green, 213; blue, 234 }  ,fill opacity=1 ]   (181.4,158.67) -- (168.4,153.67) ;
            	\draw [fill={rgb, 255:red, 193; green, 213; blue, 234 }  ,fill opacity=1 ]   (180.72,154.32) -- (167.07,164) ;
            	\draw [fill={rgb, 255:red, 193; green, 213; blue, 234 }  ,fill opacity=1 ]   (192.23,143.53) -- (180.95,151.89) ;
            	\draw [fill={rgb, 255:red, 193; green, 213; blue, 234 }  ,fill opacity=1 ]   (193.56,152.53) -- (180.6,146.66) ;
            	\draw [fill={rgb, 255:red, 193; green, 213; blue, 234 }  ,fill opacity=1 ]   (181.41,138.64) -- (169.4,147.67) ;
            	\draw [fill={rgb, 255:red, 193; green, 213; blue, 234 }  ,fill opacity=1 ]   (170.9,137.87) -- (181.73,144) ;
            	\draw [fill={rgb, 255:red, 193; green, 213; blue, 234 }  ,fill opacity=1 ]   (189.56,128.2) -- (181.63,136.26) ;
            	\draw [fill={rgb, 255:red, 193; green, 213; blue, 234 }  ,fill opacity=1 ]   (191.56,137.2) -- (180.44,131.03) ;
            	\draw [fill={rgb, 255:red, 193; green, 213; blue, 234 }  ,fill opacity=1 ]   (181.27,123.76) -- (171.07,131.67) ;
            	\draw [fill={rgb, 255:red, 193; green, 213; blue, 234 }  ,fill opacity=1 ]   (171.48,121.51) -- (182.73,129.33) ;
            	\draw [fill={rgb, 255:red, 193; green, 213; blue, 234 }  ,fill opacity=1 ]   (187.56,114.53) -- (181.75,121.7) ;
            	\draw [fill={rgb, 255:red, 193; green, 213; blue, 234 }  ,fill opacity=1 ]   (181.1,115.35) -- (189.63,123.43) ;
            	\draw [fill={rgb, 255:red, 193; green, 213; blue, 234 }  ,fill opacity=1 ]   (174.28,107.54) -- (180.58,113.46) ;
            	\draw [fill={rgb, 255:red, 193; green, 213; blue, 234 }  ,fill opacity=1 ]   (181.84,109.27) -- (174.1,115.15) ;
            	\draw [fill={rgb, 255:red, 193; green, 213; blue, 234 }  ,fill opacity=1 ]   (181.46,101.42) -- (187.85,107.9) ;
            	\draw [fill={rgb, 255:red, 193; green, 213; blue, 234 }  ,fill opacity=1 ]   (185.6,100.4) -- (182.1,105.4) ;
            	\draw [fill={rgb, 255:red, 193; green, 213; blue, 234 }  ,fill opacity=1 ]   (181.19,96.28) -- (176.35,100.4) ;
            	\draw [fill={rgb, 255:red, 193; green, 213; blue, 234 }  ,fill opacity=1 ]   (181.56,88.86) -- (185.85,96.15) ;
            	\draw [fill={rgb, 255:red, 193; green, 213; blue, 234 }  ,fill opacity=1 ]   (181.75,83.58) -- (177.6,87.9) ;
            	\draw [color={rgb, 255:red, 54; green, 101; blue, 156 }  ,draw opacity=1 ]   (181.28,184.44) -- (365.9,185) ;
            	\draw [color={rgb, 255:red, 54; green, 101; blue, 156 }  ,draw opacity=1 ]   (181.07,50.67) -- (365.9,270) ;
            	\draw [color={rgb, 255:red, 54; green, 101; blue, 156 }  ,draw opacity=1 ]   (365.9,270) -- (365.9,185) ;
            	\draw [color={rgb, 255:red, 54; green, 101; blue, 156 }  ,draw opacity=1 ]   (70.4,270.56) -- (365.62,270.56) ;
            	\draw [color={rgb, 255:red, 61; green, 102; blue, 151 }  ,draw opacity=1 ]   (181.28,184.44) -- (365.9,270) ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.29 ][fill={rgb, 255:red, 239; green, 216; blue, 179 }  ,fill opacity=1 ] (86.67,152.91) .. controls (89.1,152.92) and (92.57,153.56) .. (96.38,156.42) .. controls (100.19,159.28) and (96.19,160.22) .. (94.72,161.03) .. controls (93.24,161.83) and (86.41,159.98) .. (85.08,156.89) .. controls (83.76,153.81) and (84.23,152.9) .. (86.67,152.91) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.29 ][fill={rgb, 255:red, 239; green, 216; blue, 179 }  ,fill opacity=1 ] (94.72,161.03) .. controls (96.4,161.03) and (98.79,161.47) .. (101.42,163.44) .. controls (104.04,165.41) and (101.29,166.07) .. (100.27,166.62) .. controls (99.25,167.18) and (94.54,165.9) .. (93.63,163.77) .. controls (92.71,161.65) and (93.04,161.02) .. (94.72,161.03) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.29 ][fill={rgb, 255:red, 239; green, 216; blue, 179 }  ,fill opacity=1 ] (85.82,158.06) .. controls (87.41,157.76) and (89.6,157.93) .. (91.74,160.19) .. controls (93.87,162.46) and (91.13,163.87) .. (90.06,164.83) .. controls (89,165.79) and (84.76,164.87) .. (84.28,162.08) .. controls (83.81,159.29) and (84.23,158.36) .. (85.82,158.06) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.29 ][fill={rgb, 255:red, 239; green, 216; blue, 179 }  ,fill opacity=1 ] (76.47,154.84) .. controls (77.67,154.75) and (79.34,154.98) .. (81.1,156.51) .. controls (82.86,158.03) and (80.85,158.75) .. (80.1,159.28) .. controls (79.34,159.81) and (76.07,159) .. (75.54,157.24) .. controls (75.01,155.48) and (75.28,154.93) .. (76.47,154.84) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.29 ][fill={rgb, 255:red, 239; green, 216; blue, 179 }  ,fill opacity=1 ] (105.33,173.65) .. controls (106.51,173.38) and (108.11,173.46) .. (109.62,175.2) .. controls (111.12,176.94) and (109.08,178.13) .. (108.27,178.92) .. controls (107.47,179.71) and (104.38,179.09) .. (104.1,176.89) .. controls (103.82,174.68) and (104.16,173.93) .. (105.33,173.65) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.29 ][fill={rgb, 255:red, 239; green, 216; blue, 179 }  ,fill opacity=1 ] (117.33,171.15) .. controls (118.51,170.88) and (120.11,170.96) .. (121.62,172.7) .. controls (123.12,174.44) and (121.08,175.63) .. (120.27,176.42) .. controls (119.47,177.21) and (116.38,176.59) .. (116.1,174.39) .. controls (115.82,172.18) and (116.16,171.43) .. (117.33,171.15) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.29 ][fill={rgb, 255:red, 239; green, 216; blue, 179 }  ,fill opacity=1 ] (135.33,182.65) .. controls (136.51,182.38) and (138.11,182.46) .. (139.62,184.2) .. controls (141.12,185.94) and (139.08,187.13) .. (138.27,187.92) .. controls (137.47,188.71) and (134.38,188.09) .. (134.1,185.89) .. controls (133.82,183.68) and (134.16,182.93) .. (135.33,182.65) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.29 ][fill={rgb, 255:red, 239; green, 216; blue, 179 }  ,fill opacity=1 ] (122.83,183.65) .. controls (124.01,183.38) and (125.61,183.46) .. (127.12,185.2) .. controls (128.62,186.94) and (126.58,188.13) .. (125.77,188.92) .. controls (124.97,189.71) and (121.88,189.09) .. (121.6,186.89) .. controls (121.32,184.68) and (121.66,183.93) .. (122.83,183.65) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.29 ][fill={rgb, 255:red, 239; green, 216; blue, 179 }  ,fill opacity=1 ] (146.83,195.65) .. controls (148.01,195.38) and (149.61,195.46) .. (151.12,197.2) .. controls (152.62,198.94) and (150.58,200.13) .. (149.77,200.92) .. controls (148.97,201.71) and (145.88,201.09) .. (145.6,198.89) .. controls (145.32,196.68) and (145.66,195.93) .. (146.83,195.65) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.29 ][fill={rgb, 255:red, 239; green, 216; blue, 179 }  ,fill opacity=1 ] (214.83,190.65) .. controls (216.01,190.38) and (217.61,190.46) .. (219.12,192.2) .. controls (220.62,193.94) and (218.58,195.13) .. (217.77,195.92) .. controls (216.97,196.71) and (213.88,196.09) .. (213.6,193.89) .. controls (213.32,191.68) and (213.66,190.93) .. (214.83,190.65) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.29 ][fill={rgb, 255:red, 239; green, 216; blue, 179 }  ,fill opacity=1 ] (226.29,194.98) .. controls (227.72,194.91) and (229.73,195.21) .. (231.87,196.99) .. controls (234.01,198.76) and (231.63,199.52) .. (230.74,200.11) .. controls (229.85,200.69) and (225.91,199.68) .. (225.23,197.67) .. controls (224.56,195.67) and (224.86,195.05) .. (226.29,194.98) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.29 ][fill={rgb, 255:red, 239; green, 216; blue, 179 }  ,fill opacity=1 ] (265.33,215.65) .. controls (266.51,215.38) and (268.11,215.46) .. (269.62,217.2) .. controls (271.12,218.94) and (269.08,220.13) .. (268.27,220.92) .. controls (267.47,221.71) and (264.38,221.09) .. (264.1,218.89) .. controls (263.82,216.68) and (264.16,215.93) .. (265.33,215.65) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.29 ][fill={rgb, 255:red, 239; green, 216; blue, 179 }  ,fill opacity=1 ] (260.7,214.55) .. controls (261.69,214.36) and (263.04,214.45) .. (264.34,215.87) .. controls (265.65,217.28) and (263.95,218.18) .. (263.29,218.79) .. controls (262.62,219.4) and (260.01,218.85) .. (259.73,217.09) .. controls (259.45,215.34) and (259.72,214.75) .. (260.7,214.55) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (137.65,164.62) -- (130.86,176.51) -- (128.47,163.29) -- (131.96,170.23) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (135.36,163.2) -- (128.29,175.05) -- (125.62,161.79) -- (129.39,168.77) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (140.66,165.02) -- (133.59,176.87) -- (130.92,163.61) -- (134.69,170.59) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 235; green, 222; blue, 201 }  ,fill opacity=1 ] (179.17,188) -- (184.3,188) -- (184.3,270.4) -- (179.17,270.4) -- cycle ;
            	\draw [color={rgb, 255:red, 54; green, 101; blue, 156 }  ,draw opacity=1 ] [dash pattern={on 0.84pt off 2.51pt}]  (182.1,188.2) -- (181.37,270.2) ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.29 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (92.54,170.05) .. controls (91.45,170.38) and (89.99,170.37) .. (88.68,168.66) .. controls (87.37,166.95) and (89.29,165.66) .. (90.06,164.83) .. controls (90.83,163.99) and (93.63,164.5) .. (93.8,166.72) .. controls (93.96,168.95) and (93.63,169.72) .. (92.54,170.05) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.29 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (112.04,169.55) .. controls (110.95,169.88) and (109.49,169.87) .. (108.18,168.16) .. controls (106.87,166.45) and (108.79,165.16) .. (109.56,164.33) .. controls (110.33,163.49) and (113.13,164) .. (113.3,166.22) .. controls (113.46,168.45) and (113.13,169.22) .. (112.04,169.55) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.29 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (117.54,185.05) .. controls (116.45,185.38) and (114.99,185.37) .. (113.68,183.66) .. controls (112.37,181.95) and (114.29,180.66) .. (115.06,179.83) .. controls (115.83,178.99) and (118.63,179.5) .. (118.8,181.72) .. controls (118.96,183.95) and (118.63,184.72) .. (117.54,185.05) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.29 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (142.54,196.55) .. controls (141.45,196.88) and (139.99,196.87) .. (138.68,195.16) .. controls (137.37,193.45) and (139.29,192.16) .. (140.06,191.33) .. controls (140.83,190.49) and (143.63,191) .. (143.8,193.22) .. controls (143.96,195.45) and (143.63,196.22) .. (142.54,196.55) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.29 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (166.54,194.05) .. controls (165.45,194.38) and (163.99,194.37) .. (162.68,192.66) .. controls (161.37,190.95) and (163.29,189.66) .. (164.06,188.83) .. controls (164.83,187.99) and (167.63,188.5) .. (167.8,190.72) .. controls (167.96,192.95) and (167.63,193.72) .. (166.54,194.05) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.29 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (237.04,206.05) .. controls (235.95,206.38) and (234.49,206.37) .. (233.18,204.66) .. controls (231.87,202.95) and (233.79,201.66) .. (234.56,200.83) .. controls (235.33,199.99) and (238.13,200.5) .. (238.3,202.72) .. controls (238.46,204.95) and (238.13,205.72) .. (237.04,206.05) -- cycle ;
            	\draw (203.5,161) node [anchor=north west][inner sep=0.75pt]    {$C$};
            	\draw (172,270.5) node [anchor=north west][inner sep=0.75pt]    {$D$};
            	\draw (365.5,267.5) node [anchor=north west][inner sep=0.75pt]    {$A$};
            	\draw (363,164.5) node [anchor=north west][inner sep=0.75pt]    {$H$};
            	\draw (174,28) node [anchor=north west][inner sep=0.75pt]    {$B$};
            	\draw (368,216) node [anchor=north west][inner sep=0.75pt]    {$h$};
            \end{tikzpicture}'''
                # Câu hỏi
                noidungcauhoi = (r'''\immini{Trên ngọn đồi có một cái tháp cao $%s$m. Đỉnh tháp $B$ và chân tháp $C$ lần lượt nhìn điểm $A$ ở chân đồi dưới các góc tương ứng bằng $30^\circ$ và $60^\circ$ so với phương thẳng đứng. Chiều cao $AH$ của ngọn đồi bằng bao nhiêu mét?}{%s}'''
                                 % (h_thap, hinhve))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Ta có $\\widehat{ACB} = 180^\\circ - 60^\\circ = 120^\\circ$; $\\widehat{ABC} = 30^\\circ \\Rightarrow \\widehat{BAC} = 180^\\circ - (120^\\circ + 30^\\circ) = 30^\\circ$. \\\\ 
                             Nên $\\Delta ABC$ cân tại $C \\Rightarrow AC = BC = %s$. \\\\ 
                             Trong tam giác vuông $AHC$, ta có góc hợp bởi $AC$ và phương ngang là $\\widehat{ACH} = 90^\\circ - 60^\\circ = 30^\\circ$. \\\\ 
                             Do đó: $\\sin \\widehat{ACH} = \\frac{AH}{AC} \\Leftrightarrow AH = AC \\cdot \\sin 30^\\circ = %s \\cdot \\frac{1}{2} = %s$m.'''
                           % (h_thap, h_thap, kq))
                dapan='\\shortans[0]{$%s$}\n'%(kq)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content

