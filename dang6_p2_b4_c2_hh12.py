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


def bt_dang6_p2_b4_c2_hh12(self):
            # Khai báo biến
            # Khai báo biến
            x0 = randint(-3, 3)
            y0 = randint(-3, 3)
            z0 = randint(-3, 3)
            R = randint(4, 6)

            # Random khoảng cách h1, h2 đảm bảo h1, h2 < R và h1 khác h2
            h1 = randint(1, R-1)
            h2 = randint(0, R-1)
            while h1 == h2:
                h2 = randint(0, R-1)

            # Tính hệ số D cho mặt phẳng (P) và (Q)
            sign1 = random.choice([1, -1])
            D1 = sign1 * 3 * h1 - 2*x0 + 2*y0 - z0

            sign2 = random.choice([1, -1])
            D2 = sign2 * 3 * h2 - 2*x0 + 2*y0 - z0

            # Hàm hỗ trợ định dạng phương trình
            def format_eq(D):
                if D > 0: return "+ %s" % D
                elif D < 0: return "- %s" % (-D)
                else: return ""

            def format_term(var, val):
                if val > 0: return "\\left(%s-%s\\right)^2" % (var, val)
                elif val < 0: return "\\left(%s+%s\\right)^2" % (var, -val)
                else: return "%s^2" % var

            term_x = format_term('x', x0)
            term_y = format_term('y', y0)
            term_z = format_term('z', z0)

            term_x_f = format_term('x', -x0)
            term_y_f = format_term('y', -y0)
            term_z_f = format_term('z', -z0)

            eq_true = "%s + %s + %s = %s" % (term_x, term_y, term_z, R**2)
            eq_false = "%s + %s + %s = %s" % (term_x_f, term_y_f, term_z_f, R**2)

            P_eq = "2x - 2y + z %s = 0" % format_eq(D1)
            Q_eq = "2x - 2y + z %s = 0" % format_eq(D2)

            # Các giá trị tính toán
            num1 = 2*x0 - 2*y0 + z0 + D1
            num2 = 2*x0 - 2*y0 + z0 + D2
            r1_2 = R**2 - h1**2
            r2_2 = R**2 - h2**2

            ratio_true = sp.Rational(r1_2, r2_2)
            ratio_false = sp.Rational(r2_2, r1_2)
            if ratio_true == ratio_false:
                ratio_false = sp.Rational(1, 2)
            hinhve=r'''\tikzset {_vnss14lpr/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 21 bp }  }  \pgftransformscale{1 }  }}}
            \pgfdeclareradialshading{_tnud3kc2e}{\pgfpoint{0bp}{0bp}}{rgb(0bp)=(1,1,1);
            	rgb(0bp)=(1,1,1);
            	rgb(25bp)=(0.49,0.69,0.91);
            	rgb(400bp)=(0.49,0.69,0.91)}
            \tikzset {_sjslwfpm3/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformscale{1 }  }}}
            \pgfdeclareradialshading{_5kjekkiwm}{\pgfpoint{0bp}{0bp}}{rgb(0bp)=(1,1,1);
            	rgb(4.803564889090402bp)=(1,1,1);
            	rgb(25bp)=(0.6,0.74,0.91);
            	rgb(400bp)=(0.6,0.74,0.91)}
            \tikzset {_fzv8sfcrl/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{0 }  \pgftransformscale{2 }  }}}
            \pgfdeclarehorizontalshading{_lp4sra7xv}{150bp}{rgb(0bp)=(0.52,0.71,0.93);
            	rgb(40.071427481515066bp)=(0.52,0.71,0.93);
            	rgb(43.9999989100865bp)=(1,1,1);
            	rgb(62.5bp)=(0.29,0.56,0.89);
            	rgb(100bp)=(0.29,0.56,0.89)}
            \tikzset {_st9ibrrwx/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformscale{1 }  }}}
            \pgfdeclareradialshading{_705j6i8zc}{\pgfpoint{0bp}{0bp}}{rgb(0bp)=(1,1,1);
            	rgb(0bp)=(1,1,1);
            	rgb(25bp)=(0.83,0.87,0.93);
            	rgb(400bp)=(0.83,0.87,0.93)}
            \tikzset {_pmicj8w75/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{-112 }  \pgftransformscale{2 }  }}}
            \pgfdeclarehorizontalshading{_oa3e4jlmv}{150bp}{rgb(0bp)=(0.5,0.5,0.5);
            	rgb(37.5bp)=(0.5,0.5,0.5);
            	rgb(50bp)=(0.8,0.76,0.76);
            	rgb(62.5bp)=(0.5,0.5,0.5);
            	rgb(100bp)=(0.5,0.5,0.5)}
            \tikzset{every picture/.style={line width=0.75pt}} \scalebox{0.6}{ 
            \begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.27 ] (379.8,271.75) .. controls (379.8,261.78) and (405.63,253.7) .. (437.5,253.7) .. controls (469.37,253.7) and (495.2,261.78) .. (495.2,271.75) .. controls (495.2,281.72) and (469.37,289.8) .. (437.5,289.8) .. controls (405.63,289.8) and (379.8,281.72) .. (379.8,271.75) -- cycle ;
            	\draw  [draw opacity=0][shading=_tnud3kc2e,_vnss14lpr] (536.29,181.84) .. controls (535.49,235.31) and (491.81,278.4) .. (438.05,278.4) .. controls (383.94,278.4) and (340.04,234.74) .. (339.8,180.8) -- cycle ;
            	\draw  [draw opacity=0][shading=_5kjekkiwm,_sjslwfpm3] (340.2,180.8) .. controls (340.2,166.22) and (384.19,154.4) .. (438.44,154.4) .. controls (492.7,154.4) and (536.69,166.22) .. (536.69,180.8) .. controls (536.69,195.37) and (492.7,207.19) .. (438.44,207.19) .. controls (384.19,207.19) and (340.2,195.37) .. (340.2,180.8) -- cycle ;
            	\draw   (339.8,180.8) .. controls (339.8,126.67) and (383.68,82.79) .. (437.81,82.79) .. controls (491.93,82.79) and (535.81,126.67) .. (535.81,180.8) .. controls (535.81,234.92) and (491.93,278.8) .. (437.81,278.8) .. controls (383.68,278.8) and (339.8,234.92) .. (339.8,180.8) -- cycle ;
            	\path  [shading=_lp4sra7xv,_fzv8sfcrl] (478.7,95.6) -- (478.7,171) .. controls (478.7,173.1) and (475.51,174.8) .. (471.57,174.8) .. controls (467.64,174.8) and (464.45,173.1) .. (464.45,171) -- (464.45,95.6) .. controls (464.45,93.5) and (467.64,91.8) .. (471.57,91.8) .. controls (475.51,91.8) and (478.7,93.5) .. (478.7,95.6) .. controls (478.7,97.7) and (475.51,99.4) .. (471.57,99.4) .. controls (467.64,99.4) and (464.45,97.7) .. (464.45,95.6) ; 
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.48 ] (478.7,95.6) -- (478.7,171) .. controls (478.7,173.1) and (475.51,174.8) .. (471.57,174.8) .. controls (467.64,174.8) and (464.45,173.1) .. (464.45,171) -- (464.45,95.6) .. controls (464.45,93.5) and (467.64,91.8) .. (471.57,91.8) .. controls (475.51,91.8) and (478.7,93.5) .. (478.7,95.6) .. controls (478.7,97.7) and (475.51,99.4) .. (471.57,99.4) .. controls (467.64,99.4) and (464.45,97.7) .. (464.45,95.6) ;
            	\draw  [draw opacity=0] (535.95,181.59) .. controls (531.8,195.93) and (489.59,207.19) .. (438.12,207.19) .. controls (383.9,207.19) and (339.95,194.69) .. (339.95,179.27) .. controls (339.95,179.2) and (339.95,179.13) .. (339.95,179.07) -- (438.12,179.27) -- cycle ; \draw   (535.95,181.59) .. controls (531.8,195.93) and (489.59,207.19) .. (438.12,207.19) .. controls (383.9,207.19) and (339.95,194.69) .. (339.95,179.27) .. controls (339.95,179.2) and (339.95,179.13) .. (339.95,179.07) ;  
            	\draw  [draw opacity=0] (468.78,180.23) .. controls (455.72,179.66) and (445.84,176.93) .. (445.84,173.65) .. controls (445.84,170.81) and (453.29,168.38) .. (463.79,167.41) -- (473.94,173.65) -- cycle ; \draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ] (468.78,180.23) .. controls (455.72,179.66) and (445.84,176.93) .. (445.84,173.65) .. controls (445.84,170.81) and (453.29,168.38) .. (463.79,167.41) ;  
            	\draw  [draw opacity=0] (459.74,180.28) .. controls (441.49,179.83) and (427.44,177.03) .. (427.44,173.65) .. controls (427.44,170.6) and (438.86,168.03) .. (454.49,167.22) -- (464.94,173.65) -- cycle ; \draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ] (459.74,180.28) .. controls (441.49,179.83) and (427.44,177.03) .. (427.44,173.65) .. controls (427.44,170.6) and (438.86,168.03) .. (454.49,167.22) ;  
            	\draw  [draw opacity=0] (447.52,184.81) .. controls (427.7,184.02) and (412.64,180.09) .. (412.64,175.36) .. controls (412.64,171.23) and (424.15,167.7) .. (440.3,166.35) -- (454.94,175.36) -- cycle ; \draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.48 ] (447.52,184.81) .. controls (427.7,184.02) and (412.64,180.09) .. (412.64,175.36) .. controls (412.64,171.23) and (424.15,167.7) .. (440.3,166.35) ;  
            	\draw  [draw opacity=0] (472.78,180.63) .. controls (459.72,180.06) and (449.84,177.33) .. (449.84,174.05) .. controls (449.84,171.47) and (455.99,169.23) .. (465,168.11) -- (477.94,174.05) -- cycle ; \draw  [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=0.15 ] (472.78,180.63) .. controls (459.72,180.06) and (449.84,177.33) .. (449.84,174.05) .. controls (449.84,171.47) and (455.99,169.23) .. (465,168.11) ;  
            	\draw  [draw opacity=0] (461.14,183.2) .. controls (447.39,182.48) and (437.04,179.34) .. (437.04,175.56) .. controls (437.04,172.33) and (444.63,169.55) .. (455.45,168.37) -- (467.14,175.56) -- cycle ; \draw  [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=0.22 ] (461.14,183.2) .. controls (447.39,182.48) and (437.04,179.34) .. (437.04,175.56) .. controls (437.04,172.33) and (444.63,169.55) .. (455.45,168.37) ;  
            	\draw  [draw opacity=0] (432.96,188.72) .. controls (414.04,187.63) and (399.84,183.09) .. (399.84,177.66) .. controls (399.84,173.03) and (410.11,169.06) .. (424.81,167.3) -- (441.64,177.66) -- cycle ; \draw  [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=0.17 ] (432.96,188.72) .. controls (414.04,187.63) and (399.84,183.09) .. (399.84,177.66) .. controls (399.84,173.03) and (410.11,169.06) .. (424.81,167.3) ;  
            	\draw  [draw opacity=0] (474.19,179.91) .. controls (482.42,179.14) and (488.48,176.54) .. (488.48,173.45) .. controls (488.48,171.27) and (485.45,169.33) .. (480.76,168.11) -- (469.11,173.45) -- cycle ; \draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.31 ] (474.19,179.91) .. controls (482.42,179.14) and (488.48,176.54) .. (488.48,173.45) .. controls (488.48,171.27) and (485.45,169.33) .. (480.76,168.11) ;  
            	\draw  [draw opacity=0] (482.43,182.44) .. controls (491.03,181.49) and (497.3,178.5) .. (497.3,174.96) .. controls (497.3,172.14) and (493.33,169.68) .. (487.38,168.3) -- (476.55,174.96) -- cycle ; \draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.36 ] (482.43,182.44) .. controls (491.03,181.49) and (497.3,178.5) .. (497.3,174.96) .. controls (497.3,172.14) and (493.33,169.68) .. (487.38,168.3) ;  
            	\draw  [draw opacity=0] (491.12,187.36) .. controls (502.89,185.94) and (511.44,181.64) .. (511.44,176.56) .. controls (511.44,172.55) and (506.13,169.03) .. (498.13,167.02) -- (482.63,176.56) -- cycle ; \draw  [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=0.22 ] (491.12,187.36) .. controls (502.89,185.94) and (511.44,181.64) .. (511.44,176.56) .. controls (511.44,172.55) and (506.13,169.03) .. (498.13,167.02) ;  
            	\draw  [draw opacity=0][fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=0.07 ] (536.02,183.68) .. controls (535.53,236.71) and (491.24,279.29) .. (437.1,278.79) .. controls (382.95,278.29) and (339.46,234.9) .. (339.95,181.87) .. controls (345.81,229.15) and (386.96,265.94) .. (437.21,266.41) .. controls (487.46,266.87) and (529.29,230.85) .. (536.02,183.68) -- cycle ;
            	\draw  [draw opacity=0][shading=_705j6i8zc,_st9ibrrwx] (462.24,172.76) .. controls (462.06,172.31) and (462.65,171.85) .. (463.77,171.6) .. controls (464.88,171.34) and (466.32,171.33) .. (467.48,171.56) .. controls (467.89,171.3) and (468.64,171.11) .. (469.5,171.07) .. controls (470.37,171.02) and (471.24,171.12) .. (471.86,171.33) .. controls (472.21,171.09) and (472.9,170.93) .. (473.67,170.9) .. controls (474.45,170.88) and (475.21,170.99) .. (475.69,171.21) .. controls (476.32,170.95) and (477.32,170.84) .. (478.26,170.93) .. controls (479.2,171.02) and (479.91,171.28) .. (480.09,171.61) .. controls (480.86,171.68) and (481.5,171.87) .. (481.85,172.12) .. controls (482.2,172.36) and (482.22,172.65) .. (481.9,172.9) .. controls (482.66,173.24) and (482.84,173.7) .. (482.37,174.09) .. controls (481.9,174.49) and (480.85,174.77) .. (479.61,174.83) .. controls (479.6,175.21) and (479.01,175.55) .. (478.06,175.73) .. controls (477.11,175.91) and (475.95,175.9) .. (475.02,175.7) .. controls (474.63,176.15) and (473.53,176.47) .. (472.19,176.54) .. controls (470.85,176.61) and (469.52,176.41) .. (468.76,176.02) .. controls (467.84,176.21) and (466.73,176.27) .. (465.69,176.17) .. controls (464.65,176.08) and (463.76,175.85) .. (463.23,175.52) .. controls (462.29,175.56) and (461.37,175.39) .. (460.95,175.1) .. controls (460.52,174.81) and (460.67,174.46) .. (461.31,174.22) .. controls (460.47,174.05) and (460.04,173.72) .. (460.25,173.39) .. controls (460.46,173.06) and (461.25,172.81) .. (462.22,172.78) ; \draw  [draw opacity=0] (461.31,174.22) .. controls (461.71,174.31) and (462.17,174.34) .. (462.63,174.33)(463.23,175.52) .. controls (463.43,175.52) and (463.62,175.5) .. (463.8,175.47)(468.76,176.02) .. controls (468.62,175.95) and (468.51,175.87) .. (468.42,175.79)(475.02,175.7) .. controls (475.1,175.62) and (475.14,175.53) .. (475.16,175.45)(479.61,174.83) .. controls (479.62,174.44) and (478.97,174.07) .. (477.93,173.9)(481.9,172.9) .. controls (481.73,173.04) and (481.48,173.16) .. (481.15,173.25)(480.09,171.61) .. controls (480.11,171.67) and (480.13,171.72) .. (480.13,171.78)(475.69,171.21) .. controls (475.53,171.27) and (475.4,171.34) .. (475.3,171.42)(471.86,171.33) .. controls (471.78,171.39) and (471.72,171.45) .. (471.68,171.51)(467.48,171.56) .. controls (467.72,171.61) and (467.95,171.67) .. (468.15,171.74)(462.24,172.76) .. controls (462.27,172.82) and (462.3,172.89) .. (462.36,172.95) ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.56 ][fill={rgb, 255:red, 148; green, 188; blue, 235 }  ,fill opacity=1 ,even odd rule] (468,96.72) .. controls (468,96.72) and (469.6,96.72) .. (471.57,96.72) .. controls (473.55,96.72) and (475.15,96.72) .. (475.15,96.72) .. controls (475.15,96.72) and (473.55,96.72) .. (471.57,96.72) .. controls (469.6,96.72) and (468,96.72) .. (468,96.72)(463.07,96.72) .. controls (463.07,94) and (466.88,91.8) .. (471.57,91.8) .. controls (476.27,91.8) and (480.07,94) .. (480.07,96.72) .. controls (480.07,99.45) and (476.27,101.65) .. (471.57,101.65) .. controls (466.88,101.65) and (463.07,99.45) .. (463.07,96.72) ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.51 ][fill={rgb, 255:red, 142; green, 184; blue, 235 }  ,fill opacity=1 ] (467.06,62.96) -- (476.08,62.96) -- (476.08,96.56) -- (467.06,96.56) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.51 ][fill={rgb, 255:red, 142; green, 184; blue, 235 }  ,fill opacity=1 ] (485.04,45.4) -- (531.61,45.4) -- (531.61,54.15) -- (485.04,54.15) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 142; green, 184; blue, 235 }  ,fill opacity=1 ] (467.06,63.75) .. controls (467.1,53.66) and (475.38,45.5) .. (485.58,45.5) .. controls (485.68,45.5) and (485.78,45.5) .. (485.88,45.5) -- (485.58,63.82) -- cycle ; \draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.51 ] (467.06,63.75) .. controls (467.1,53.66) and (475.38,45.5) .. (485.58,45.5) .. controls (485.68,45.5) and (485.78,45.5) .. (485.88,45.5) ;  
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (476.13,63.91) .. controls (476.15,58.57) and (480.73,54.24) .. (486.37,54.24) .. controls (486.42,54.24) and (486.47,54.24) .. (486.52,54.24) -- (486.37,63.95) -- cycle ; \draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.51 ] (476.13,63.91) .. controls (476.15,58.57) and (480.73,54.24) .. (486.37,54.24) .. controls (486.42,54.24) and (486.47,54.24) .. (486.52,54.24) ;  
            	\draw  [draw opacity=0][fill={rgb, 255:red, 135; green, 179; blue, 230 }  ,fill opacity=1 ] (476.1,95.55) .. controls (476.08,97.26) and (474.07,98.65) .. (471.58,98.65) .. controls (469.1,98.65) and (467.08,97.26) .. (467.06,95.55) -- (471.58,95.52) -- cycle ; \draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.52 ] (476.1,95.55) .. controls (476.08,97.26) and (474.07,98.65) .. (471.58,98.65) .. controls (469.1,98.65) and (467.08,97.26) .. (467.06,95.55) ;  
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.86 ][line width=2.25]    (469.7,97.4) .. controls (468.95,43.4) and (462.2,47.4) .. (531.47,47.4) ;
            	\draw  [fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (529.24,66.4) -- (538.24,55.16) -- (547.04,55.16) -- (556.04,66.4) -- cycle ;
            	\path  [shading=_oa3e4jlmv,_pmicj8w75] (531.84,51.59) .. controls (531.84,51.59) and (531.84,51.59) .. (531.84,51.59) .. controls (531.84,57.22) and (536.68,61.78) .. (542.64,61.78) .. controls (548.6,61.78) and (553.44,57.22) .. (553.44,51.59) .. controls (553.44,45.96) and (548.6,41.4) .. (542.64,41.4) .. controls (535.44,41.4) and (531.84,41.4) .. (531.84,41.4) .. controls (531.84,41.4) and (531.84,44.8) .. (531.84,51.59) -- cycle ; 
            	\draw   (531.84,51.59) .. controls (531.84,51.59) and (531.84,51.59) .. (531.84,51.59) .. controls (531.84,57.22) and (536.68,61.78) .. (542.64,61.78) .. controls (548.6,61.78) and (553.44,57.22) .. (553.44,51.59) .. controls (553.44,45.96) and (548.6,41.4) .. (542.64,41.4) .. controls (535.44,41.4) and (531.84,41.4) .. (531.84,41.4) .. controls (531.84,41.4) and (531.84,44.8) .. (531.84,51.59) -- cycle ; 
            \end{tikzpicture} }'''
            # Nội dung câu hỏi
            noidungcauhoi = (r'''\immini{Một bể chứa nước trong nhà máy có dạng hình cầu. Trong không gian với hệ trục $Oxyz$ (đơn vị trên các trục là mét), một mặt cầu được mô phỏng hình dáng của bể có tâm $I\left(%s;%s;%s\right)$ và bán kính bằng $%s$. Tại một thời điểm quan sát, mặt nước trong bể nằm trên mặt phẳng có phương trình $(P): %s$.}{%s}'''              
                             %(x0, y0, z0, R, P_eq,hinhve))

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Phương trình mặt cầu của bể nước là $%s$' % eq_true
            nb_da_1_s = 'Phương trình mặt cầu của bể nước là $%s$' % eq_false
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Mặt cầu có tâm $I\\left(%s;%s;%s\\right)$ và bán kính $R=%s$ có phương trình là \\\\ $%s$.'''
                            %(x0, y0, z0, R, eq_true))

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
            th_da_1_d = '\\True $\\text{d}\\left(I;(P)\\right)=%s$ (m)' % h1  
            th_da_1_s = '$\\text{d}\\left(I;(P)\\right)=%s$ (dm)' % (h1)   
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)


            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Khoảng cách từ tâm $I$ đến mặt phẳng $(P)$ là: \\\\
                            $\\text{d}\\left(I;(P)\\right) = \\frac{\\left| 2\\cdot\\left(%s\\right) - 2\\cdot\\left(%s\\right) + 1\\cdot\\left(%s\\right) %s \\right|}{\\sqrt{2^2 + \\left(-2\\right)^2 + 1^2}} = \\frac{\\left| %s \\right|}{3} = %s$ (m).'''       
                       %(x0, y0, z0, format_eq(D1), num1, h1))

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
            vd_da_1_d = '\\True Tại thời điểm quan sát, diện tích mặt thoáng của nước trong bể bằng $%s\\pi$ (m$^2$)' % r1_2  
            vd_da_1_s = 'Tại thời điểm quan sát, diện tích mặt thoáng của nước trong bể bằng $%s$ (m$^2$)' % r1_2  
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Bán kính mặt thoáng của nước trong bể là: \\\\
                            $r_1 = \\sqrt{R^2 - d^2\\left(I;(P)\\right)} = \\sqrt{%s^2 - %s^2} = \\sqrt{%s}$ (m). \\\\
                            Diện tích mặt thoáng của nước là $S_1 = \\pi r_1^2 = %s\\pi$ (m$^2$).'''  
                       %(R, h1, r1_2, r1_2))

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
            vdc_da_1_d = '\\True Giả sử nước được bơm thêm vào bể với lưu lượng không đổi. Khi mặt nước dâng lên và nằm trên mặt phẳng $(Q): %s$, tốc độ dâng của mực nước bằng $%s$ tốc độ dâng tại thời điểm quan sát ban đầu' % (Q_eq, latex(ratio_true)) 
            vdc_da_1_s = 'Giả sử nước được bơm thêm vào bể với lưu lượng không đổi. Khi mặt nước dâng lên và nằm trên mặt phẳng $(Q): %s$, tốc độ dâng của mực nước bằng $%s$ tốc độ dâng tại thời điểm quan sát ban đầu' % (Q_eq, latex(ratio_false)) 
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Gọi $V$ là thể tích nước, $h$ là chiều cao mực nước. \\\\ Vì lưu lượng bơm không đổi nên $\\frac{dV}{dt} = C$ (hằng số). \\\\
                            Ta có $\\frac{dV}{dt} = S\\left(h\\right) \\cdot \\frac{dh}{dt} \\Rightarrow v = \\frac{dh}{dt} = \\frac{C}{S\\left(h\\right)}$, với $S\\left(h\\right)$ là diện tích mặt thoáng. \\\\
                            Tại mặt phẳng $(P)$, diện tích mặt thoáng là $S_1 = %s\\pi$. \\\\
                            Khoảng cách từ tâm $I$ đến mặt phẳng $(Q)$ là \\\\ $d_2 = \\text{d}\\left(I;(Q)\\right) = \\frac{\\left| 2\\cdot\\left(%s\\right) - 2\\cdot\\left(%s\\right) + 1\\cdot\\left(%s\\right) %s \\right|}{3} = \\frac{\\left| %s \\right|}{3} = %s$ (m). \\\\
                            Bán kính mặt thoáng tại $(Q)$ là $r_2 = \\sqrt{R^2 - d_2^2} = \\sqrt{%s^2 - %s^2} = \\sqrt{%s}$ (m). \\\\
                            Diện tích mặt thoáng tại $(Q)$ là $S_2 = \\pi r_2^2 = %s\\pi$ (m$^2$). \\\\
                            Tốc độ dâng tại $(Q)$ so với tại $(P)$ là $\\frac{v_2}{v_1} = \\frac{S_1}{S_2} = \\frac{%s\\pi}{%s\\pi} = %s$.'''
                       %(r1_2, x0, y0, z0, format_eq(D2), num2, h2, R, h2, r2_2, r2_2, r1_2, r2_2, latex(ratio_true)))

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
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

